# Baseline forecaster

Gives a baseline "fair price" for a prediction market you don't know much about, the way a careful forecaster would: research first, then several independent estimates combined.

It runs Claude through Claude Code on your Claude plan, so there's no API key and no per-call bill. Each question uses some of your plan's usage limit.

## Setup (Windows, PowerShell)

```powershell
# 1. Install Claude Code once, then run `claude` and log in with your Claude account
irm https://claude.ai/install.ps1 | iex
claude

# 2. Set up the forecaster
cd path\to\forecaster
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Use

```powershell
python forecast.py https://manifold.markets/someone/will-x-happen
python forecast.py https://polymarket.com/event/some-event            # lists the sub-markets if there are several
python forecast.py https://polymarket.com/event/some-event --pick 2   # or --pick "some text"
python forecast.py https://kalshi.com/markets/kxfed/fed-decision/KXFED-26DEC
python forecast.py --question "Will X happen by 2027-01-01?" --criteria "Resolves YES if ..." --price 0.35
```

It prints the fair probability, the market price and the difference, and saves a full report (rationale, research brief, sources) as Markdown and JSON in `reports/`.

Options: `-n` number of forecasts to combine (default 5), `--model opus|sonnet|haiku` (default opus), `--effort low..max` (default high), `--workers` forecasts at once (default 3), `--max-searches` web search cap (default 12), `--price` to override the market price, `-q` quiet.

A run with the defaults takes about 2 to 4 minutes. At the end it prints how much plan usage it took, shown as the equivalent API price. Use `--model sonnet` or `-n 3` to stretch your limits.

## Measuring it: the harness

`harness.py` builds a scored track record so changes can be judged on evidence (see the plan doc). Each day it:

1. checks which earlier questions have resolved,
2. picks about 15 open markets closing in 7 to 45 days. The pick is random, spread across the three sites and across liquid and thin markets, with at most one market per event. It skips near-certain prices (under 3% or over 97%) and high-frequency noise like daily crypto prices.
3. forecasts them with the current version (`v0`) and saves each research brief,
4. writes `reports/scorecard.md`: Brier and log loss against the market price, liquid vs thin, a calibration table, and confidence intervals.

```powershell
python harness.py daily                 # what the scheduler runs (about 30 to 60 minutes)
powershell -ExecutionPolicy Bypass -File setup_schedule.ps1 -At 09:00   # run it every day
python harness.py score                 # rebuild the scorecard any time
```

**Testing a change cheaply.** `variant` reruns only the forecast step on the saved briefs, using the original date. Both versions then see identical evidence. The forecast step has no web access, so this is fair even after questions resolve.

```powershell
python harness.py variant sonnet-high --model sonnet
python harness.py variant opus-xhigh-n7 --effort xhigh -n 7
```

The scorecard then shows each variant against v0 on the same questions, with a verdict: better, worse, or not distinguishable yet. Aggregation choices (median, mean of log-odds, caps) and Platt calibration are scored from saved samples, at no cost. Platt calibration needs 40 or more resolved questions.

Data is append-only in `data/` (questions, forecasts, resolutions, briefs). Don't edit these files by hand. Back the folder up now and then.

## How it works

1. **Market data** from the public Manifold, Polymarket (gamma API) and Kalshi APIs: question, resolution rules, close date, current price.
2. **Research**: Claude (via `claude -p`) with web search and page fetching writes a brief covering resolution mechanics, base rates, latest dated news, scenarios and signposts. It's told not to look up market or betting odds, page fetches from those sites are blocked, and the price is never shown to the model, so the baseline is independent of the crowd.
3. **Forecasts**: 5 separate calls read the brief, each starting from a different angle (outside view, inside view, both sides, status quo, pre-mortem), and return a probability with structured output.
4. **Combine**: the median of the samples. The spread between samples is a rough signal of how uncertain the question is.

## Caveats

- Not yet scored. Run the harness for a few weeks before trusting it for money.
- The model's knowledge and search results can lag; read the dated news in the brief.
- Multi-outcome markets are forecast one outcome at a time (use `--pick`).
