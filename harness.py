#!/usr/bin/env python3
"""Measurement harness for the forecaster: collect markets, forecast them, resolve, score.

Everything lives in an append-only log under data/ so results can't be tuned in hindsight:
  data/questions.jsonl   one line per collected market (price snapshot at collection)
  data/forecasts.jsonl   one line per forecast (version, samples, as-of date)
  data/resolutions.jsonl one line per resolved market
  data/briefs/<qid>.md   the research brief each forecast was based on

Commands:
  python harness.py daily                  collect + forecast + resolve + score (what the scheduler runs)
  python harness.py collect [-n 15]        pick today's markets
  python harness.py forecast               forecast every collected market that has no v0 forecast yet
  python harness.py resolve                check for resolved markets
  python harness.py score                  write reports/scorecard.md
  python harness.py variant NAME [opts]    rerun only the forecast step on saved briefs (A/B tests)
  python harness.py add --question ...     add a hand-written question (also handy for testing)
  python harness.py settle QID yes|no|void settle a hand-written question
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

import forecast as fc

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
BRIEFS = DATA / "briefs"
QUESTIONS = DATA / "questions.jsonl"
FORECASTS = DATA / "forecasts.jsonl"
RESOLUTIONS = DATA / "resolutions.jsonl"
REPORTS = ROOT / "reports"

BASE_VERSION = "v0"
# Skip near-certain markets (they cost plan usage and mostly measure nothing) and
# high-frequency noise the research step can't add anything to.
MIN_PRICE, MAX_PRICE = 0.03, 0.97
EXCLUDE_WORDS = ["up or down", "o/u", "over/under", "spread", "points scored", "total goals",
                 "price of bitcoin", "price of ethereum", "highest temperature", "tweets"]
# Volume above which a market counts as "liquid" (each site uses its own units).
LIQUID = {"Manifold": 50, "Polymarket": 100_000, "Kalshi": 20_000}  # bettors / USD volume / contracts


def now() -> datetime:
    return datetime.now(timezone.utc)


def iso(d: datetime) -> str:
    return d.isoformat(timespec="seconds")


# --------------------------------------------------------------------------- log helpers


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"warning: skipping a corrupt line in {path.name}", file=sys.stderr)
    return out


def append_jsonl(path: Path, rec: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def safe_id(qid: str) -> str:
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in qid)


# --------------------------------------------------------------------------- collect


def _days(lo: int, hi: int) -> tuple[datetime, datetime]:
    t = now()
    return t + timedelta(days=lo), t + timedelta(days=hi)


def candidates_manifold(lo: int, hi: int) -> list[dict]:
    start, end = _days(lo, hi)
    # Sorted by soonest close, so page until we pass the end of the window.
    rows: list[dict] = []
    for offset in range(0, 10_000, 1000):
        page = fc._get("https://api.manifold.markets/v0/search-markets", term="", filter="open",
                       contractType="BINARY", sort="close-date", limit=1000, offset=offset)
        rows += page
        last = page[-1].get("closeTime") if page else None
        if len(page) < 1000 or (last and last / 1000 > end.timestamp()):
            break
    out = []
    for m in rows:
        close = m.get("closeTime")
        if not close or m.get("isResolved") or m.get("outcomeType") != "BINARY":
            continue
        ct = datetime.fromtimestamp(close / 1000, timezone.utc)
        if not (start <= ct <= end) or m.get("probability") is None:
            continue
        out.append({
            "qid": f"manifold:{m['id']}", "source": "Manifold", "source_id": m["id"],
            "question": m["question"], "url": m.get("url", ""), "close_time": iso(ct),
            "market_prob": float(m["probability"]), "volume": m.get("uniqueBettorCount") or 0,
            "group": m["id"],
        })
    return out


def candidates_polymarket(lo: int, hi: int) -> list[dict]:
    start, end = _days(lo, hi)
    # The gamma API caps pages at 100 and refuses deep offsets, so walk the keyset endpoint.
    # The volume floor drops tens of thousands of untraded auto-generated markets.
    out, cursor = [], None
    for _ in range(100):
        params = dict(active="true", closed="false", end_date_min=iso(start), end_date_max=iso(end),
                      volume_num_min=100, limit=100)
        if cursor:
            params["after_cursor"] = cursor
        data = fc._get("https://gamma-api.polymarket.com/markets/keyset", **params)
        rows = data.get("markets") or []
        for m in rows:
            events = m.get("events") or [{}]
            ev = events[0].get("slug")
            link = (f"https://polymarket.com/event/{ev}/{m.get('slug', '')}" if ev
                    else f"https://polymarket.com/market/{m.get('slug', '')}")
            mk = fc._poly_market(m, link)
            if mk.market_prob is None or not m.get("endDate"):
                continue
            out.append({
                "qid": f"polymarket:{m['id']}", "source": "Polymarket", "source_id": str(m["id"]),
                "question": mk.question, "criteria": mk.criteria, "url": mk.url, "close_time": m["endDate"],
                "market_prob": mk.market_prob, "volume": float(m.get("volumeNum") or m.get("volume") or 0),
                "group": ev or m["id"],
            })
        cursor = data.get("next_cursor")
        if not cursor or not rows:
            break
    return out


def candidates_kalshi(lo: int, hi: int) -> list[dict]:
    start, end = _days(lo, hi)
    out, cursor = [], None
    for _ in range(50):
        # mve_filter drops the multi-leg parlays, which otherwise make up most of the listing
        params = dict(status="open", mve_filter="exclude", min_close_ts=int(start.timestamp()),
                      max_close_ts=int(end.timestamp()), limit=1000)
        if cursor:
            params["cursor"] = cursor
        data = fc._get(f"{fc.KALSHI}/markets", **params)
        for m in data.get("markets", []):
            if m.get("ticker", "").startswith("KXMVE") or m.get("market_type", "binary") != "binary":
                continue  # multi-leg parlays
            mk = fc._kalshi_market(m, f"https://kalshi.com/markets/{m.get('event_ticker', '')}")
            if mk.market_prob is None:
                continue
            vol = float(m.get("volume_fp") or m.get("volume") or 0)
            if vol <= 0:
                continue  # never traded: the quote isn't a crowd price
            out.append({
                "qid": f"kalshi:{m['ticker']}", "source": "Kalshi", "source_id": m["ticker"],
                "question": mk.question, "criteria": mk.criteria, "url": mk.url, "close_time": m.get("close_time", ""),
                "market_prob": mk.market_prob, "volume": float(vol),
                "group": m.get("event_ticker") or m["ticker"],
            })
        cursor = data.get("cursor")
        if not cursor:
            break
    return out


SOURCES = {"Manifold": candidates_manifold, "Polymarket": candidates_polymarket, "Kalshi": candidates_kalshi}


def tier(c: dict) -> str:
    return "liquid" if c["volume"] >= LIQUID.get(c["source"], math.inf) else "thin"


def eligible(c: dict) -> bool:
    q = c["question"].lower()
    return MIN_PRICE <= c["market_prob"] <= MAX_PRICE and not any(w in q for w in EXCLUDE_WORDS)


def select(cands: list[dict], n: int, seen_groups: set[str], seed: int) -> list[dict]:
    """Random pick, spread evenly over sources and liquid/thin, at most one market per event
    (sub-markets of one event move together and would overcount the evidence)."""
    rng = random.Random(seed)
    buckets: dict[tuple[str, str], list[dict]] = {}
    for c in cands:
        buckets.setdefault((c["source"], tier(c)), []).append(c)
    for b in buckets.values():
        rng.shuffle(b)
    keys = sorted(buckets)
    rng.shuffle(keys)
    picked, groups = [], set(seen_groups)
    while len(picked) < n and any(buckets.values()):
        for k in keys:
            while buckets[k]:
                c = buckets[k].pop()
                g = f"{c['source']}:{c['group']}"
                if g not in groups:
                    picked.append(c)
                    groups.add(g)
                    break
            if len(picked) >= n:
                break
    return picked


def fill_criteria(c: dict) -> None:
    if c.get("criteria"):
        return
    if c["source"] == "Manifold":
        try:
            m = fc._get(f"https://api.manifold.markets/v0/market/{c['source_id']}")
            c["criteria"] = m.get("textDescription") or ""
        except Exception as e:
            print(f"  couldn't fetch description for {c['qid']}: {e}", file=sys.stderr)


def cmd_collect(args) -> list[dict]:
    existing = read_jsonl(QUESTIONS)
    have = {q["qid"] for q in existing}
    open_groups = {f"{q['source']}:{q.get('group')}" for q in existing
                   if q["qid"] not in {r["qid"] for r in read_jsonl(RESOLUTIONS)}}
    cands = []
    for name, fn in SOURCES.items():
        try:
            got = [c for c in fn(args.min_days, args.max_days) if eligible(c) and c["qid"] not in have]
            print(f"  {name}: {len(got)} eligible markets")
            cands += got
        except Exception as e:
            print(f"  {name}: failed ({e}); skipping it today", file=sys.stderr)
    seed = int(now().strftime("%Y%m%d"))
    picked = select(cands, args.n, open_groups, seed)
    for c in picked:
        fill_criteria(c)
        c.update(collected_at=iso(now()), tier=tier(c))
        append_jsonl(QUESTIONS, c)
    print(f"Collected {len(picked)} new questions "
          f"({sum(c['tier'] == 'liquid' for c in picked)} liquid, {sum(c['tier'] == 'thin' for c in picked)} thin).")
    return picked


def cmd_add(args) -> None:
    qid = f"manual:{uuid.uuid4().hex[:8]}"
    rec = {"qid": qid, "source": "manual", "source_id": qid, "question": args.question, "criteria": args.criteria or "",
           "url": "", "close_time": args.close or "", "market_prob": args.price, "volume": 0, "group": qid,
           "collected_at": iso(now()), "tier": "manual"}
    append_jsonl(QUESTIONS, rec)
    print(f"Added {qid}")


# --------------------------------------------------------------------------- forecast


def to_market(q: dict) -> fc.Market:
    return fc.Market(q["source"], q["question"], q.get("criteria", ""), q.get("close_time", ""), None, q.get("url", ""))


def resolved_ids() -> set[str]:
    return {r["qid"] for r in read_jsonl(RESOLUTIONS)}


def forecast_one(q: dict, version: str, model: str, effort: str, samples: int, searches: int) -> dict | None:
    mk = to_market(q)  # market price deliberately left out
    as_of = now().strftime("%Y-%m-%d")
    try:
        brief, _ = fc.research(mk, searches, model, effort)
    except Exception as e:
        print(f"  research failed for {q['qid']}: {e}", file=sys.stderr)
        return None
    BRIEFS.mkdir(parents=True, exist_ok=True)
    (BRIEFS / f"{safe_id(q['qid'])}.md").write_text(brief, encoding="utf-8")
    framings = [fc.FRAMINGS[i % len(fc.FRAMINGS)] for i in range(samples)]
    outs = [r for r in (fc._safe(fc.one_forecast, mk, brief, f, model, effort, as_of) for f in framings) if r]
    if not outs:
        return None
    rec = {"qid": q["qid"], "version": version, "forecast_at": iso(now()), "as_of": as_of,
           "model": model, "effort": effort, "samples": [o["probability"] for o in outs],
           "prob": fc.aggregate([o["probability"] for o in outs]),
           "rationale": min(outs, key=lambda o: abs(o["probability"] - fc.aggregate([x["probability"] for x in outs])))["rationale"]}
    append_jsonl(FORECASTS, rec)
    print(f"  {q['qid']}: {fc.pct(rec['prob'])} (market at collection {fc.pct(q['market_prob'])})")
    return rec


def cmd_forecast(args) -> None:
    done = {(f["qid"], f["version"]) for f in read_jsonl(FORECASTS)}
    res = resolved_ids()
    todo = [q for q in read_jsonl(QUESTIONS) if (q["qid"], BASE_VERSION) not in done and q["qid"] not in res]
    if args.limit:
        todo = todo[: args.limit]
    print(f"Forecasting {len(todo)} questions with {args.model} ({args.samples} samples each)…")
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        list(pool.map(lambda q: forecast_one(q, BASE_VERSION, args.model, args.effort, args.samples, args.max_searches), todo))
    print(f"Plan usage this run: {fc.USAGE['calls']} Claude calls (≈${fc.USAGE['cost_usd']:.2f} at API prices, not billed on a plan)")


def cmd_variant(args) -> None:
    """Rerun only the forecast step on the saved v0 briefs, with the same as-of date.
    The forecast step has no tools, so rerunning after a question resolves can't leak the answer
    (beyond what the model already knew at its training cutoff)."""
    qs = {q["qid"]: q for q in read_jsonl(QUESTIONS)}
    fs = read_jsonl(FORECASTS)
    base = {f["qid"]: f for f in fs if f["version"] == BASE_VERSION}
    done = {f["qid"] for f in fs if f["version"] == args.name}
    todo = [qid for qid in base if qid not in done and (BRIEFS / f"{safe_id(qid)}.md").exists()]
    if args.limit:
        todo = todo[: args.limit]
    print(f"Variant {args.name}: {len(todo)} questions, model={args.model}, effort={args.effort}, samples={args.samples}")

    def run(qid: str) -> None:
        q, b = qs[qid], base[qid]
        brief = (BRIEFS / f"{safe_id(qid)}.md").read_text(encoding="utf-8")
        framings = [fc.FRAMINGS[i % len(fc.FRAMINGS)] for i in range(args.samples)]
        outs = [r for r in (fc._safe(fc.one_forecast, to_market(q), brief, f, args.model, args.effort, b["as_of"]) for f in framings) if r]
        if outs:
            ps = [o["probability"] for o in outs]
            append_jsonl(FORECASTS, {"qid": qid, "version": args.name, "forecast_at": iso(now()), "as_of": b["as_of"],
                                     "model": args.model, "effort": args.effort, "samples": ps, "prob": fc.aggregate(ps),
                                     "rerun_of": BASE_VERSION})
            print(f"  {qid}: {fc.pct(fc.aggregate(ps))} (v0 {fc.pct(b['prob'])})")

    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        list(pool.map(run, todo))


# --------------------------------------------------------------------------- resolve


def check_resolution(q: dict) -> str | None:
    """Return 'yes', 'no', 'void' or None (still open)."""
    src, sid = q["source"], q["source_id"]
    if src == "Manifold":
        m = fc._get(f"https://api.manifold.markets/v0/market/{sid}")
        if not m.get("isResolved"):
            return None
        return {"YES": "yes", "NO": "no"}.get(m.get("resolution"), "void")
    if src == "Polymarket":
        m = fc._get(f"https://gamma-api.polymarket.com/markets/{sid}")
        if not m.get("closed"):
            return None
        status = m.get("umaResolutionStatus")
        if status and status != "resolved":
            return None  # outcome proposed or disputed, not final yet
        outcomes, prices = fc._poly_outcomes(m)
        if not prices or len(prices) != len(outcomes):
            return None
        yes = prices[outcomes.index("Yes") if "Yes" in outcomes else 0]
        if yes >= 0.99:
            return "yes"
        if yes <= 0.01:
            return "no"
        if status == "resolved" and abs(yes - 0.5) < 0.01:
            return "void"  # resolved 50-50 (cancelled / unknowable)
        return None  # closed but not settled yet
    if src == "Kalshi":
        m = fc._get(f"{fc.KALSHI}/markets/{sid}")["market"]
        result = (m.get("result") or "").lower()
        if result in ("yes", "no"):
            return result
        if m.get("status") in ("finalized", "settled") and result:
            return "void"
        return None
    return None  # manual questions are settled by hand


def cmd_resolve(args) -> None:
    res = resolved_ids()
    pending = [q for q in read_jsonl(QUESTIONS) if q["qid"] not in res and q["source"] != "manual"]
    n = 0
    for q in pending:
        try:
            out = check_resolution(q)
        except Exception as e:
            print(f"  {q['qid']}: check failed ({e})", file=sys.stderr)
            continue
        if out:
            append_jsonl(RESOLUTIONS, {"qid": q["qid"], "outcome": out, "resolved_seen_at": iso(now())})
            n += 1
    print(f"Resolved {n} of {len(pending)} open questions.")


def cmd_settle(args) -> None:
    if args.qid in resolved_ids():
        sys.exit(f"{args.qid} is already resolved")
    append_jsonl(RESOLUTIONS, {"qid": args.qid, "outcome": args.outcome, "resolved_seen_at": iso(now()), "manual": True})
    print(f"Settled {args.qid} as {args.outcome}")


# --------------------------------------------------------------------------- score


def brier(p: float, y: int) -> float:
    return (p - y) ** 2


def logloss(p: float, y: int) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return -math.log(p if y else 1 - p)


def logit(p: float) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return math.log(p / (1 - p))


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def fit_platt(ps: list[float], ys: list[int]) -> tuple[float, float]:
    """Fit y ~ sigmoid(a*logit(p) + b) by Newton's method (light L2 pull toward a=1, b=0)."""
    a, b, lam = 1.0, 0.0, 1.0
    xs = [logit(p) for p in ps]
    for _ in range(50):
        ga, gb = lam * (a - 1), lam * b
        haa, hab, hbb = lam, 0.0, lam
        for x, y in zip(xs, ys):
            q = sigmoid(a * x + b)
            w = q * (1 - q)
            ga += (q - y) * x
            gb += q - y
            haa += w * x * x
            hab += w * x
            hbb += w
        det = haa * hbb - hab * hab
        if abs(det) < 1e-12:
            break
        da = (hbb * ga - hab * gb) / det
        db = (haa * gb - hab * ga) / det
        a, b = a - da, b - db
        if abs(da) + abs(db) < 1e-8:
            break
    return a, b


def platt_cv(ps: list[float], ys: list[int], k: int = 5) -> list[float]:
    """Out-of-fold calibrated probabilities, so the calibration gain isn't measured on its own training data."""
    n = len(ps)
    out = [0.0] * n
    idx = list(range(n))
    for fold in range(k):
        test = [i for i in idx if i % k == fold]
        train = [i for i in idx if i % k != fold]
        a, b = fit_platt([ps[i] for i in train], [ys[i] for i in train]) if len(train) >= 20 else (1.0, 0.0)
        for i in test:
            out[i] = sigmoid(a * logit(ps[i]) + b)
    return out


def bootstrap_ci(diffs: list[float], reps: int = 4000, seed: int = 0) -> tuple[float, float]:
    rng = random.Random(seed)
    n = len(diffs)
    means = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(reps))
    return means[int(0.05 * reps)], means[int(0.95 * reps) - 1]


def agg_logodds(samples: list[float]) -> float:
    return sigmoid(statistics.fmean(logit(p) for p in samples))


def cmd_score(args) -> str:
    qs = {q["qid"]: q for q in read_jsonl(QUESTIONS)}
    res = {r["qid"]: r["outcome"] for r in read_jsonl(RESOLUTIONS)}
    fs = read_jsonl(FORECASTS)
    by_version: dict[str, dict[str, dict]] = {}
    for f in fs:
        by_version.setdefault(f["version"], {})[f["qid"]] = f  # last forecast per (version, question) wins

    lines = ["# Forecaster scorecard", "", f"Generated {iso(now())}. Lower Brier and log loss are better.", "",
             f"Questions collected: {len(qs)}. Resolved yes/no: {sum(v in ('yes', 'no') for v in res.values())}. "
             f"Voided: {sum(v == 'void' for v in res.values())}.", ""]

    # agreement check: how far v0 sits from the market price at collection, on all forecast questions
    v0 = by_version.get(BASE_VERSION, {})
    liquid = [(f["prob"], qs[q]["market_prob"]) for q, f in v0.items() if q in qs and qs[q].get("tier") == "liquid"
              and qs[q].get("market_prob") is not None]
    if liquid:
        mad = statistics.fmean(abs(a - b) for a, b in liquid)
        lines += ["## Agreement check (no waiting needed)", "",
                  f"On {len(liquid)} liquid markets, v0 sits on average **{mad * 100:.1f} points** from the market price "
                  "recorded at collection. This catches broken changes; it is not a reason to ship one.", ""]

    def table(rows: list[tuple[str, list[float], list[int]]], market: list[float]) -> list[str]:
        out = ["| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |", "| --- | --- | --- | --- | --- |"]
        if market:
            out.append(f"| Market price at collection | {len(market)} | {statistics.fmean(brier(p, y) for p, y in zip(market, rows[0][2])):.4f} "
                       f"| {statistics.fmean(logloss(p, y) for p, y in zip(market, rows[0][2])):.3f} | |")
        for name, ps, ys in rows:
            b = statistics.fmean(brier(p, y) for p, y in zip(ps, ys))
            ll = statistics.fmean(logloss(p, y) for p, y in zip(ps, ys))
            if market:
                d = [brier(p, y) - brier(m, y) for p, m, y in zip(ps, market, ys)]
                lo, hi = bootstrap_ci(d)
                cmp = f"{statistics.fmean(d):+.4f} ({lo:+.4f} to {hi:+.4f})"
            else:
                cmp = ""
            out.append(f"| {name} | {len(ps)} | {b:.4f} | {ll:.3f} | {cmp} |")
        return out

    order = sorted(by_version, key=lambda v: (v != BASE_VERSION, v))
    for version in order:
        fmap = by_version[version]
        keys = [q for q in fmap if res.get(q) in ("yes", "no") and q in qs]
        if not keys:
            continue
        ys = [1 if res[q] == "yes" else 0 for q in keys]
        ps = [fmap[q]["prob"] for q in keys]
        market = [qs[q]["market_prob"] for q in keys] if all(qs[q].get("market_prob") is not None for q in keys) else []
        rows = [(f"{version} (median)", ps, ys),
                (f"{version}, mean of log-odds", [agg_logodds(fmap[q]["samples"]) for q in keys], ys),
                (f"{version}, capped 2-98%", [min(max(p, 0.02), 0.98) for p in ps], ys)]
        if len(keys) >= 40:
            rows.append((f"{version} + Platt scaling (5-fold CV)", platt_cv(ps, ys), ys))
        lines += [f"## {version}: all resolved questions", ""] + table(rows, market) + [""]
        for t in ("liquid", "thin"):
            tk = [i for i, q in enumerate(keys) if qs[q].get("tier") == t]
            if len(tk) >= 5 and market:
                lines += [f"### {version}: {t} markets", ""] + table(
                    [(version, [ps[i] for i in tk], [ys[i] for i in tk])], [market[i] for i in tk]) + [""]

        # calibration table
        bins = [(0, .1), (.1, .3), (.3, .5), (.5, .7), (.7, .9), (.9, 1.01)]
        lines += [f"### {version}: calibration", "", "| Forecast range | n | Avg forecast | Actually happened |", "| --- | --- | --- | --- |"]
        for lo, hi in bins:
            sel = [(p, y) for p, y in zip(ps, ys) if lo <= p < hi]
            if sel:
                lines.append(f"| {lo * 100:.0f}-{min(hi, 1) * 100:.0f}% | {len(sel)} | {statistics.fmean(p for p, _ in sel) * 100:.0f}% "
                             f"| {statistics.fmean(y for _, y in sel) * 100:.0f}% |")
        lines.append("")

    # paired version-vs-v0 comparisons
    base = by_version.get(BASE_VERSION, {})
    for version, fmap in sorted(by_version.items()):
        if version == BASE_VERSION:
            continue
        keys = [q for q in fmap if q in base and res.get(q) in ("yes", "no")]
        if len(keys) >= 5:
            ys = [1 if res[q] == "yes" else 0 for q in keys]
            d = [brier(fmap[q]["prob"], y) - brier(base[q]["prob"], y) for q, y in zip(keys, ys)]
            lo, hi = bootstrap_ci(d)
            verdict = "better" if hi < 0 else "worse" if lo > 0 else "not distinguishable yet"
            lines += [f"**{version} vs v0** on {len(keys)} shared questions: Brier difference {statistics.fmean(d):+.4f} "
                      f"(90% CI {lo:+.4f} to {hi:+.4f}), {verdict}.", ""]

    if len(lines) < 10:
        lines += ["No resolved questions yet. Scores appear once markets start resolving (the first within about a week)."]
    text = "\n".join(lines)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "scorecard.md").write_text(text, encoding="utf-8")
    print(text)
    return text


# --------------------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser(description="Measurement harness for the forecaster.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def fc_opts(p, samples=5):
        p.add_argument("--model", default=fc.MODEL)
        p.add_argument("--effort", default=fc.EFFORT)
        p.add_argument("-n", "--samples", type=int, default=samples)
        p.add_argument("--parallel", type=int, default=2, help="Questions (or variant reruns) at once")
        p.add_argument("--limit", type=int, help="Only do this many")

    p = sub.add_parser("collect")
    p.add_argument("-n", type=int, default=15)
    p.add_argument("--min-days", type=int, default=7)
    p.add_argument("--max-days", type=int, default=45)

    p = sub.add_parser("forecast")
    fc_opts(p)
    p.add_argument("--max-searches", type=int, default=12)

    p = sub.add_parser("daily")
    fc_opts(p)
    p.add_argument("-q", "--questions", dest="n", type=int, default=15)
    p.add_argument("--max-searches", type=int, default=12)
    p.add_argument("--min-days", type=int, default=7)
    p.add_argument("--max-days", type=int, default=45)

    sub.add_parser("resolve")
    sub.add_parser("score")

    p = sub.add_parser("variant")
    p.add_argument("name", help="Label for this variant, e.g. sonnet-high or opus-xhigh-n7")
    fc_opts(p)

    p = sub.add_parser("add")
    p.add_argument("--question", required=True)
    p.add_argument("--criteria")
    p.add_argument("--close")
    p.add_argument("--price", type=float)

    p = sub.add_parser("settle")
    p.add_argument("qid")
    p.add_argument("outcome", choices=["yes", "no", "void"])

    args = ap.parse_args()
    if args.cmd == "daily":
        print(f"== {iso(now())} daily run")
        print("Resolving…"); cmd_resolve(args)
        print("Collecting…"); cmd_collect(args)
        cmd_forecast(args)
        cmd_score(args)
    else:
        {"collect": cmd_collect, "forecast": cmd_forecast, "resolve": cmd_resolve, "score": cmd_score,
         "variant": cmd_variant, "add": cmd_add, "settle": cmd_settle}[args.cmd](args)


if __name__ == "__main__":
    main()
