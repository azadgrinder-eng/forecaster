#!/usr/bin/env python3
"""Baseline "fair price" forecaster for prediction markets.

Give it a Manifold, Polymarket or Kalshi link (or a plain question) and it:
  1. pulls the question and resolution rules from the market's public API,
  2. has Claude research it on the web (base rates, latest news, key drivers),
     with the market sites themselves blocked so it can't see the current price,
  3. runs several independent forecasts from that research and takes the median,
  4. compares the result with the market price.

Needs Claude Code installed and logged in with your Claude plan (no API key).

Usage:
  python forecast.py https://manifold.markets/someone/will-x-happen
  python forecast.py https://polymarket.com/event/some-event --pick 2
  python forecast.py https://kalshi.com/markets/kxfoo/some-title/KXFOO-26DEC31
  python forecast.py --question "Will X happen by 2027-01-01?" --criteria "Resolves YES if ..."
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import statistics
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

# Runs through the Claude Code CLI ("claude -p"), so it uses your Claude plan, not an API key.
MODEL = "opus"  # Claude Code model alias: opus / sonnet / haiku
EFFORT = "high"
MARKET_DOMAINS = [
    "polymarket.com",
    "kalshi.com",
    "manifold.markets",
    "metaculus.com",
    "predictit.org",
    "oddschecker.com",
]
HTTP = requests.Session()
HTTP.headers["User-Agent"] = "baseline-forecaster/0.1"


# --------------------------------------------------------------------------- markets


@dataclass
class Market:
    source: str
    question: str
    criteria: str = ""
    close_time: str = ""
    market_prob: float | None = None
    url: str = ""
    options: list[str] = field(default_factory=list)  # filled when an event has several markets


def _get(url: str, **params) -> dict | list:
    r = HTTP.get(url, params=params or None, timeout=20)
    r.raise_for_status()
    return r.json()


def fetch_manifold(url: str) -> Market:
    slug = urlparse(url).path.rstrip("/").split("/")[-1]
    m = _get(f"https://api.manifold.markets/v0/slug/{slug}")
    if m.get("outcomeType") != "BINARY":
        print(f"note: this is a {m.get('outcomeType')} market; forecasting P(YES) for the question as written.")
    close = m.get("closeTime")
    return Market(
        source="Manifold",
        question=m["question"],
        criteria=m.get("textDescription") or "",
        close_time=datetime.fromtimestamp(close / 1000, timezone.utc).isoformat() if close else "",
        market_prob=m.get("probability"),
        url=m.get("url", url),
    )


def _poly_market(m: dict, url: str) -> Market:
    prob = None
    try:
        outcomes = json.loads(m.get("outcomes") or "[]")
        prices = [float(p) for p in json.loads(m.get("outcomePrices") or "[]")]
        idx = outcomes.index("Yes") if "Yes" in outcomes else 0
        prob = prices[idx]
    except (ValueError, IndexError, TypeError):
        pass
    return Market(
        source="Polymarket",
        question=m["question"],
        criteria=m.get("description") or "",
        close_time=m.get("endDate") or "",
        market_prob=prob,
        url=url,
    )


def fetch_polymarket(url: str, pick: str | None) -> Market:
    parts = [p for p in urlparse(url).path.split("/") if p]
    # polymarket.com/event/<event-slug>[/<market-slug>]  or  polymarket.com/market/<market-slug>
    if len(parts) >= 3 or (parts and parts[0] == "market"):
        res = _get("https://gamma-api.polymarket.com/markets", slug=parts[-1])
        if res:
            return _poly_market(res[0], url)
    events = _get("https://gamma-api.polymarket.com/events", slug=parts[1] if len(parts) > 1 else parts[-1])
    if not events:
        sys.exit(f"Couldn't find a Polymarket event for {url}")
    markets = [m for m in events[0].get("markets", []) if not m.get("closed")] or events[0].get("markets", [])
    if len(markets) == 1:
        return _poly_market(markets[0], url)
    chosen = _choose([m["question"] for m in markets], pick)
    if chosen is None:
        mk = Market(source="Polymarket", question=events[0].get("title", ""), url=url)
        mk.options = [m["question"] for m in markets]
        return mk
    return _poly_market(markets[chosen], url)


KALSHI = "https://api.elections.kalshi.com/trade-api/v2"


def _kalshi_market(m: dict, url: str, event: dict | None = None) -> Market:
    def price(key: str) -> float | None:
        if m.get(f"{key}_dollars") not in (None, ""):
            return float(m[f"{key}_dollars"])
        if m.get(key) not in (None, ""):
            return float(m[key]) / 100
        return None

    bid, ask, last = price("yes_bid"), price("yes_ask"), price("last_price")
    prob = (bid + ask) / 2 if bid and ask else last
    title = m.get("title") or (event or {}).get("title", "")
    sub = m.get("yes_sub_title") or m.get("subtitle") or ""
    question = f"{title} — {sub}" if sub and sub not in title else title
    criteria = "\n\n".join(x for x in (m.get("rules_primary"), m.get("rules_secondary")) if x)
    return Market("Kalshi", question, criteria, m.get("close_time", ""), prob, url)


def fetch_kalshi(url: str, pick: str | None) -> Market:
    ticker = urlparse(url).path.rstrip("/").split("/")[-1].upper()
    try:
        return _kalshi_market(_get(f"{KALSHI}/markets/{ticker}")["market"], url)
    except requests.HTTPError:
        pass
    data = _get(f"{KALSHI}/events/{ticker}", with_nested_markets="true")
    event = data.get("event", {})
    markets = data.get("markets") or event.get("markets") or []
    markets = [m for m in markets if m.get("status") in (None, "active", "open")] or markets
    if not markets:
        sys.exit(f"Couldn't find a Kalshi market for {url}")
    if len(markets) == 1:
        return _kalshi_market(markets[0], url, event)
    labels = [m.get("yes_sub_title") or m.get("subtitle") or m.get("ticker") for m in markets]
    chosen = _choose(labels, pick)
    if chosen is None:
        mk = Market(source="Kalshi", question=event.get("title", ticker), url=url)
        mk.options = labels
        return mk
    return _kalshi_market(markets[chosen], url, event)


def _choose(labels: list[str], pick: str | None) -> int | None:
    if pick is None:
        return None
    if pick.isdigit() and 1 <= int(pick) <= len(labels):
        return int(pick) - 1
    hits = [i for i, l in enumerate(labels) if pick.lower() in (l or "").lower()]
    return hits[0] if len(hits) == 1 else None


def load_market(args) -> Market:
    if args.question:
        return Market("manual", args.question, args.criteria or "", args.close or "", args.price)
    host = urlparse(args.url).netloc.lower()
    if "manifold" in host:
        mk = fetch_manifold(args.url)
    elif "polymarket" in host:
        mk = fetch_polymarket(args.url, args.pick)
    elif "kalshi" in host:
        mk = fetch_kalshi(args.url, args.pick)
    else:
        sys.exit("Unrecognised link. Use a Manifold/Polymarket/Kalshi URL, or --question.")
    if args.price is not None:
        mk.market_prob = args.price
    return mk


# --------------------------------------------------------------------------- model calls


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _question_block(mk: Market, as_of: str | None = None) -> str:
    return (
        f"<question>{mk.question}</question>\n"
        f"<resolution_criteria>{mk.criteria or '(none given: use the plain meaning of the question)'}</resolution_criteria>\n"
        f"<close_date>{mk.close_time or 'unknown'}</close_date>\n"
        f"<today>{as_of or _today()}</today>"
    )


RESEARCH_SYSTEM = """You are the research analyst for a team of superforecasters. Your job is to gather the evidence a forecaster needs to put a well-calibrated probability on a prediction-market question. You do not give the final probability yourself.

Search the web thoroughly. Prefer primary and recent sources, and note the date of every fact that could have changed. Do not look up or report prediction-market or betting prices for this question; the forecasters must reason independently of the crowd.

Write a research brief with these sections:
1. Resolution mechanics: exactly what must happen for YES, by when, who decides, and any edge cases or ambiguities in the rules.
2. Reference classes and base rates: two or three reasonable reference classes, with concrete historical frequencies and how you got them (e.g. "incumbents in X won 14 of 20 times since 1980").
3. Current state of the world: the latest relevant facts and news, dated, most recent first. Include scheduled events before the close date.
4. Drivers and scenarios: the main paths to YES and to NO, and what each depends on.
5. Signposts: what new information would move the probability most, and in which direction.
6. Uncertainties: important things you could not establish.

Be concrete and quantitative. Cite sources inline as (Source title, date)."""


FORECAST_SYSTEM = """You are an experienced superforecaster with an excellent calibration record. You give a probability that a prediction-market question resolves YES, based on a research brief and your own knowledge.

Principles:
- Read the resolution criteria literally. Markets resolve on the rules, not on the spirit of the question.
- Account for time left until close: with little time left, the status quo is usually heavily favoured.
- Avoid both overconfidence and timid hedging toward 50%. If the evidence is strong, say 3% or 97%.
- Note how much you trust each piece of evidence, and that the brief may be incomplete."""

FRAMINGS = [
    "Start from the outside view: pick the best reference class and its base rate, then adjust for the specifics of this case.",
    "Start from the inside view: lay out the concrete scenarios that lead to YES and NO, estimate each, then sanity-check against base rates.",
    "First write the strongest case for YES and the strongest case for NO, then weigh them and decide.",
    "Focus on the status quo and the time remaining: what is the probability that things simply stay as they are through the close date, and what would have to change?",
    "Imagine it is after the close date and the question resolved unexpectedly. What most likely happened? Use that to check your estimate.",
]

class ClaudeError(RuntimeError):
    pass


USAGE = {"calls": 0, "cost_usd": 0.0}  # API-equivalent cost Claude Code reports; on a plan this is usage, not a bill


def run_claude(prompt: str, *, tools: list[str], model: str, effort: str, timeout: int = 1800) -> str:
    """Run one headless Claude Code turn and return its final text. The prompt goes in on stdin,
    which avoids Windows command-line length limits."""
    exe = shutil.which("claude")
    if not exe:
        sys.exit("Couldn't find the 'claude' command. Install Claude Code and run 'claude' once to log in with your plan.")
    cmd = [
        exe, "-p",
        "--output-format", "json",
        "--model", model,
        "--effort", effort,
        "--no-session-persistence",
        "--strict-mcp-config",
        "--system-prompt", "You are a careful forecasting assistant. Follow the user's instructions exactly.",
        "--tools", ",".join(tools) if tools else "",
    ]
    if tools:
        cmd += ["--allowedTools", *tools]
        cmd += ["--disallowedTools", *[f"WebFetch(domain:{d})" for d in MARKET_DOMAINS]]
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        raise ClaudeError(f"claude exited {proc.returncode}: {(proc.stderr or proc.stdout).strip()[:500]}")
    if out.get("is_error") or proc.returncode != 0:
        raise ClaudeError(f"claude reported an error: {str(out.get('result') or out)[:500]}")
    USAGE["calls"] += 1
    USAGE["cost_usd"] += float(out.get("total_cost_usd") or 0)
    return (out.get("result") or "").strip()


def research(mk: Market, max_searches: int, model: str, effort: str) -> tuple[str, list[dict]]:
    prompt = (
        f"{RESEARCH_SYSTEM}\n\n"
        f"Use the WebSearch tool (at most {max_searches} searches) and WebFetch to read the most useful pages. "
        "Do not search for prediction-market or betting odds on this question.\n\n"
        f"{_question_block(mk)}\n\n"
        "Write the brief now. End it with a section '## Sources' listing each source you relied on as "
        "'- [title](url)'. Output only the brief."
    )
    brief = run_claude(prompt, tools=["WebSearch", "WebFetch"], model=model, effort=effort)
    sources = [{"title": t, "url": u} for t, u in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", brief)]
    return brief, sources


def _extract_json(text: str) -> dict:
    """Pull the last JSON object with a 'probability' key out of the model's reply."""
    fenced = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidates = fenced[::-1] + [m.group(0) for m in re.finditer(r"\{[^{}]*\"probability\"[^{}]*(?:\[[^\]]*\][^{}]*)*\}", text, re.S)][::-1]
    for c in candidates:
        try:
            obj = json.loads(c)
            if "probability" in obj:
                return obj
        except json.JSONDecodeError:
            continue
    raise ClaudeError(f"no forecast JSON in reply: {text[-300:]}")


def one_forecast(mk: Market, brief: str, framing: str, model: str, effort: str, as_of: str | None = None) -> dict:
    prompt = (
        f"{FORECAST_SYSTEM}\n\n"
        f"{_question_block(mk, as_of)}\n\n<research_brief>\n{brief}\n</research_brief>\n\n"
        f"{framing}\n\n"
        "Think it through, then end your reply with a single JSON code block with exactly these keys:\n"
        "```json\n"
        '{"probability": <P(YES) between 0 and 1>, "base_rate": "<reference class and base rate you anchored on>", '
        '"rationale": "<3-6 sentences>", "key_factors": ["<factor>", "..."]}\n'
        "```"
    )
    out = _extract_json(run_claude(prompt, tools=[], model=model, effort=effort))
    out["probability"] = min(max(float(out["probability"]), 0.001), 0.999)
    out.setdefault("base_rate", "")
    out.setdefault("rationale", "")
    out.setdefault("key_factors", [])
    out["framing"] = framing
    return out


def aggregate(probs: list[float]) -> float:
    """Median of the samples. Robust to one odd sample; fine for a baseline."""
    return statistics.median(probs)


# --------------------------------------------------------------------------- output


def pct(p: float | None) -> str:
    return "n/a" if p is None else f"{p * 100:.1f}%"


def render(mk: Market, fair: float, samples: list[dict], brief: str, sources: list[dict], model: str = MODEL) -> str:
    probs = sorted(s["probability"] for s in samples)
    lines = [
        f"# {mk.question}",
        "",
        f"- **Fair probability (model): {pct(fair)}**  (samples: {', '.join(pct(p) for p in probs)})",
        f"- Market price: {pct(mk.market_prob)}" + (f" on {mk.source}" if mk.source != "manual" else ""),
    ]
    if mk.market_prob is not None:
        edge = fair - mk.market_prob
        side = "YES looks cheap" if edge > 0 else "NO looks cheap"
        lines.append(f"- Difference: {edge * 100:+.1f} points ({side} if you trust the model)")
    lines += [f"- Closes: {mk.close_time or 'unknown'}", f"- Generated: {_today()} with Claude ({model}) via Claude Code", ""]
    best = min(samples, key=lambda s: abs(s["probability"] - fair))
    lines += ["## Why", "", best["rationale"], "", "**Base rate:** " + best["base_rate"], "", "**Key factors:**"]
    lines += [f"- {k}" for k in best["key_factors"]]
    lines += ["", "## Research brief", "", brief]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Baseline fair price for a prediction market question.")
    ap.add_argument("url", nargs="?", help="Manifold / Polymarket / Kalshi market link")
    ap.add_argument("--question", help="Forecast a question typed by hand instead of a link")
    ap.add_argument("--criteria", help="Resolution criteria (with --question)")
    ap.add_argument("--close", help="Close date (with --question)")
    ap.add_argument("--price", type=float, help="Market price to compare against, 0-1 (overrides the fetched one)")
    ap.add_argument("--pick", help="For events with several markets: number or text of the one to forecast")
    ap.add_argument("-n", "--samples", type=int, default=5, help="Independent forecasts to combine (default 5)")
    ap.add_argument("--max-searches", type=int, default=12, help="Web search cap for the research step")
    ap.add_argument("--model", default=MODEL, help="Claude Code model alias: opus, sonnet or haiku (default opus)")
    ap.add_argument("--effort", default=EFFORT, help="low / medium / high / xhigh / max (default high)")
    ap.add_argument("--workers", type=int, default=3, help="Forecasts run at the same time (default 3)")
    ap.add_argument("--out", default="reports", help="Folder for the markdown + JSON report")
    ap.add_argument("-q", "--quiet", action="store_true")
    args = ap.parse_args()
    if not args.url and not args.question:
        ap.error("give a market URL or --question")

    mk = load_market(args)
    if mk.options:
        print(f"'{mk.question}' has several markets. Re-run with --pick <number or text>:")
        for i, o in enumerate(mk.options, 1):
            print(f"  {i}. {o}")
        sys.exit(2)

    verbose = not args.quiet
    if verbose:
        print(f"Question: {mk.question}\nCloses: {mk.close_time or 'unknown'}\n\nResearching (this can take a few minutes)…", flush=True)

    brief, sources = research(mk, args.max_searches, args.model, args.effort)
    if verbose:
        print(f"Research done ({len(sources)} sources). Running {args.samples} forecasts…", flush=True)

    framings = [FRAMINGS[i % len(FRAMINGS)] for i in range(args.samples)]
    with ThreadPoolExecutor(max_workers=max(1, min(args.samples, args.workers))) as pool:
        results = list(pool.map(lambda f: _safe(one_forecast, mk, brief, f, args.model, args.effort), framings))
    samples = [r for r in results if r]
    if not samples:
        sys.exit("All forecast calls failed.")
    fair = aggregate([s["probability"] for s in samples])

    report = render(mk, fair, samples, brief, sources, args.model)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    stem = f"{_today()}-{re.sub(r'[^a-z0-9]+', '-', mk.question.lower())[:60].strip('-')}"
    (out / f"{stem}.md").write_text(report, encoding="utf-8")
    (out / f"{stem}.json").write_text(
        json.dumps({"market": asdict(mk), "fair_probability": fair, "samples": samples,
                    "brief": brief, "sources": sources, "model": args.model}, indent=2),
        encoding="utf-8",
    )

    print()
    print(f"Fair probability: {pct(fair)}   Market: {pct(mk.market_prob)}")
    if mk.market_prob is not None:
        print(f"Difference: {(fair - mk.market_prob) * 100:+.1f} points")
    print(f"Spread across samples: {pct(min(s['probability'] for s in samples))} to {pct(max(s['probability'] for s in samples))}")
    print(f"Plan usage: {USAGE['calls']} Claude calls, about ${USAGE['cost_usd']:.2f} at API prices (not billed on a plan)")
    print(f"Report: {out / (stem + '.md')}")


def _safe(fn, *a):
    try:
        return fn(*a)
    except Exception as e:  # one bad sample shouldn't sink the run
        print(f"  a forecast sample failed: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    main()
