# TSLA close above $390 on the last trading day of November 2026: research brief

## 1. Resolution mechanics
- **What counts as YES:** the Pyth "Close" of TSLA/USD for the final 1-minute candle of regular trading on the last trading day of November 2026 must be **strictly above $390.00**. Exactly $390.00 resolves NO. No rounding is applied.
- **Which day:** Monday, November 30, 2026 is a normal full session, so the deciding candle is the one ending at 4:00 pm ET (21:00 UTC, which matches the market's close time). Thanksgiving (Thursday, Nov 26) is a holiday and Friday, Nov 27 is a half day. Neither is the final trading day, so the shortened-session rule should not apply.
- **Who decides:** Pyth data at pythdata.app (Equity.US.TSLA/USD). If there is no valid 1-minute close, the last valid Pyth price from regular hours is used. If Pyth has no data at all, the official exchange close is used. If TSLA does not trade at all that session, the market resolves 50-50.
- **Edge cases:**
  - The Pyth last-minute candle close is not necessarily the same as Nasdaq's official closing-auction price. They can differ by cents to tens of cents, which only matters if the stock finishes within about $0.50 of $390.
  - If there is a split, the target is adjusted. No split has been announced as far as I found.
  - Data vendors already disagree on recent closes (see section 3). Only Pyth's number counts.

## 2. Reference classes and base rates
**What has to happen:** the latest widely reported close is **$374.41 (Nov 19)**. From there, YES needs a gain of about **+4.2% (log return ≈ 0.041)** over 6 trading sessions: Nov 20, 23, 24, 25, 27 (half day) and 30. That is roughly 5.5 days' worth of trading variance. The Nov 20 close was not available when I checked.

**A. Option-implied lognormal model.**
- TSLA 30-day implied volatility (IV) was **42.3% as of Nov 11** (OptionCharts, Nov 11 2026). An undated report gives about 43.8% (iTiger, undated).
- The market has become more stressed since then (VIX ~28 on Nov 19), so current IV is plausibly 45–55%.
- Expected move over 6 sessions at different IV levels, with the implied chance of finishing above $390:

| IV | 1σ move over 6 sessions | z-score needed | P(close > $390) |
|---|---|---|---|
| 42% | ≈ 6.5% | 0.63 | ≈ 26% |
| 50% | ≈ 7.7% | 0.53 | ≈ 30% |
| 55% | ≈ 8.5% | 0.48 | ≈ 32% |

- Two adjustments: a drift term would cut these by about 1 point. If Friday closed lower (futures pointed weaker), every $5 of decline subtracts roughly 6–8 points.

**B. Historical TSLA 6-day returns.**
- TSLA's long-run realized volatility is about 55–60% a year, with fat tails.
- Over 2015–2025, a 6-trading-day gain of more than 4% happened roughly **30–33%** of the time. This is my own estimate from TSLA's daily-return distribution (daily standard deviation ~3.5%, small positive mean), not a counted dataset.
- In the 2025–26 regime, with somewhat lower volatility, the figure is closer to 27–30%.

**C. Recent path dependence.**
- TSLA closed **above $390 as recently as Nov 13 ($390.22)** and traded intraday up to about $391–393 on Nov 19 before reversing (Benzinga, Nov 19 2026; Heygotrade, Nov 2026).
- The level is clearly reachable, but each test this past week has failed while the broader tech selloff continued.

## 3. Current state of the world (most recent first)
- **Nov 20 (Fri):** I found no Tesla print for the day. As of the Australian session, U.S. futures were pointing weaker after Thursday's reversal (ABC News live markets, Nov 20 2026).
- **Nov 19 (Thu), Tesla:**
  - TSLA closed about **$374.41, down 2.43%** from $383.72 (Global Banking & Finance, Nov 19 2026; TradingView). Other vendors show $376.33 (Yahoo history) and $378.64 (Investing.com), so treat the exact close as uncertain within $374–379.
  - Intraday, the stock rallied to about $391 on reports of Shanghai production plans and pre-Anthropic-IPO tech euphoria, then reversed (Benzinga, Nov 19 2026).
  - Musk said Tesla and SpaceX would "probably" be better together (24/7 Wall St., Nov 19 2026).
- **Nov 19 (Thu), market:**
  - Nasdaq −2.25% to 23,879 and S&P 500 −2.0% to about 7,176.
  - Nvidia fell for a sixth straight day (−3.3%) after the resignation of CEO Jensen Huang.
  - The Anthropic IPO failed to revive the AI trade, and the VIX was about 28.
  - The S&P and Nasdaq were heading for their largest one-week drawdowns in more than a year, each down about 5% (Motley Fool, Nov 19 2026; CNBC, Nov 18–19 2026; Yahoo Finance, Nov 2026).
- **Nov 18:** TSLA +0.95% to $383.72 (24/7 Wall St. via search summary).
- **Nov 17:** TSLA +0.1% to $380.11. Stifel raised its target to $508 from $483 (Buy) (Heygotrade, Nov 18 2026; Stifel coverage, Nov 17 2026).
- **Nov 16:** TSLA −2.69% to about $379.7 (Global Banking & Finance, Nov 16 2026). Reuters reported a Berlin-area expansion plan.
- **Nov 14–15:** Musk said Cybercab "will be available nationwide, as we receive regulatory approval." Customer Cybercab sales opened, with first Austin deliveries expected in December (Yahoo/JPMorgan, Nov 2026). One outlet's claim that nationwide approval has already been granted is unverified (24/7 Wall St. card, Nov 14 2026).
- **Nov 13:** TSLA −1.8% to $390.22 in a broad tech selloff (Heygotrade, Nov 2026).
- **Context:**
  - 52-week range about $297–$499.
  - Down about 15% year to date and about 3% over the past month.
  - All-time closing high of about $489 in December 2025 (Nasdaq, Dec 2025).
- **Oct 21:** Q3 2026 results showed adjusted EPS of $0.48 against about $0.45 expected and revenue of about $28.05B. Capex guidance was cut to about $20B. Robotaxi and Optimus timelines slipped, and the stock fell about 3–5% afterward (SiliconANGLE; TIKR, Oct 2026).
- **Oct 20:** Musk said SpaceX and Tesla had formed special committees to explore a merger. It is not certain and would need approval from 50% of all Tesla shareholders (Bloomberg Government, Oct 20 2026). Earlier merger buzz sent TSLA −5% premarket (Asianet Newsable, 2026).
- **Analysts:**
  - Barclays: Overweight, $450 target (late October).
  - Consensus target about $411 (TIKR, late Oct 2026).
- **Scheduled before close:** Thanksgiving holiday Nov 26 and half day Nov 27, which usually bring low volume. I did not verify any Tesla-specific scheduled event before Nov 30. November China sales data and Cybercab deliveries come in December, after resolution. The usual late-month U.S. macro releases (e.g., PCE) were not verified.

## 4. Drivers and scenarios
**Paths to YES (needs about +4% or more from $374):**
- **Relief rally in tech/AI.** After a ~5% weekly Nasdaq drawdown and VIX near 28, a mean-reverting bounce into the Thanksgiving week, which historically leans positive, could lift a high-beta stock like TSLA 5–10%. This depends on the Nvidia leadership news settling and the Anthropic IPO trading stabilizing.
- **Tesla-specific good news:**
  - Confirmation of Cybercab regulatory approval or delivery milestones.
  - China or EU FSD approval.
  - Shanghai expansion.
  - A merger structure seen as favorable to TSLA holders.

**Paths to NO:**
- **Selloff continues.** It is broad (AI/tech bear-market talk, 20 large tech names down 25–76% from highs), and TSLA has been drifting lower in step with it.
- **Merger fears.** Dilution and governance worries over a SpaceX deal have hurt TSLA before, and Musk's Nov 19 remarks keep the topic live.
- **Thin trading.** Low holiday-week liquidity and the lack of scheduled Tesla catalysts favor staying near current levels, which are below the strike.

## 5. Signposts
- **Nov 20 close (most important):** a close at or above $385 would push P(YES) toward 40% or more. A close at $365 or below would push it toward 15% or less.
- **Nasdaq/VIX direction Nov 23–25:** a VIX drop under 22 together with a Nasdaq rebound favors YES.
- **Any SpaceX–Tesla merger announcement or terms:** the direction is ambiguous, but historically this has been negative for TSLA in the short run.
- **Cybercab/FSD regulatory confirmations:** positive. Fresh NHTSA actions or delays: negative.
- **Nvidia/AI-complex stabilization:** TSLA has been trading with AI sentiment.
- **Close to the line on Nov 30:** if TSLA trades within about $1 of $390 late in the session, the gap between the Pyth candle and the official close becomes relevant.

## 6. Uncertainties
- I could not confirm the exact Nov 19 close ($374.41 vs. $376.33 vs. $378.64 across vendors), and I found no Nov 20 data. All page fetches were blocked, so I relied on search snippets only.
- I could not get current (post–Nov 19) TSLA implied volatility. The 42% figure is from Nov 11 and is likely stale on the low side given the VIX spike.
- I could not verify whether Cybercab nationwide approval has actually been granted.
- I could not confirm the timing of any merger committee announcement or of U.S. macro releases before Nov 30.
- The historical base rates in section 2B are model-based estimates, not counted frequencies.

## Sources
- [Tesla falls 2.43% in Thursday's session (Global Banking & Finance)](https://www.globalbankingandfinance.com/tesla-tsla-falls-2026-11-19/)
- [Tesla falls 2.69% in Monday's session (Global Banking & Finance)](https://www.globalbankingandfinance.com/tesla-tsla-falls-2026-11-16/)
- [Tesla Stock (TSLA) Falls 1.8% to $390.22 (Nov 13) — Heygotrade](https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-16-2026/)
- [Tesla Stock (TSLA) Rises 0.1% to $380.11 (Nov 17) — Heygotrade](https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-18-2026/)
- [What's Going On With Tesla Stock Thursday? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/63427524/whats-going-on-with-tesla-stock-thursday-2)
- [Elon Musk Says Tesla and SpaceX Would "Probably" Be Better Together — 24/7 Wall St.](https://247wallst.com/investing/2026/11/19/elon-musk-says-tesla-and-spacex-would-probably-be-better-together)
- [Yahoo Finance TSLA historical prices](https://finance.yahoo.com/quote/TSLA/history/)
- [Investing.com TSLA historical data](https://www.investing.com/equities/tesla-motors-historical-data)
- [TradingView NASDAQ:TSLA](https://www.tradingview.com/symbols/NASDAQ-TSLA/)
- [Stock Market Today, Nov. 19: Nvidia Slides as Investors Weigh CEO Transition Fallout — Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/11/19/stock-market-today-nov-19-nvidia-slides-as-investors-weigh-ceo-transition-fallout-despite-strong-q3-results/)
- [Dow closes below 50,000; Nasdaq falls 2% as Anthropic IPO fails to resuscitate AI trade — CNBC](https://www.cnbc.com/2026/11/18/stock-market-today-live-updates.html)
- [Is Tech in a Bear Market? 20 Tech Stocks Fall Up to 76% From Highs — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/tech-bear-market-20-tech-224039016.html)
- [Markets live Nov 20 — ABC News](https://www.abc.net.au/news/2026-11-20/asx-markets-business-live-news-nov-20/107403768)
- [TSLA Option Probability — OptionCharts](https://optioncharts.io/options/TSLA/probability-distribution)
- [iTiger TSLA IV note](https://www.itiger.com/news/1107472277)
- [Stifel Turns More Bullish on Tesla — Yahoo Finance](https://finance.yahoo.com/news/stifel-turns-more-bullish-tesla-142217068.html)
- [Barclays sees 20% upside in TSLA — Stocktwits](https://stocktwits.com/news-articles/markets/equity/tesla-robotaxi-push-gets-wall-street-cheer-barclays-sees-20-upside-tsla-stock/cNbasV0R9Wg)
- [Tesla Stock Slides Despite Q3 Earnings And Revenue Beat — TIKR](https://www.tikr.com/blog/tesla-stock-slides-after-hours-q3-earnings-revenue-beat)
- [Musk Says SpaceX and Tesla Have Begun Exploring a Merger — Bloomberg Government](https://news.bgov.com/antitrust/musk-says-spacex-tesla-have-formed-committees-to-explore-merger)
- [TSLA stock down, SPCX up premarket as merger buzz grows — Asianet Newsable](https://newsable.asianetnews.com/markets/tsla-stock-down-spcx-stock-up-premarket-as-merger-buzz-grows-analyst-raises-deal-odds-to-90-articleshow-ow3vcwt)
- [Tesla's Cybercab sales to the public are 'early validation' — Yahoo Finance/JPMorgan](https://finance.yahoo.com/markets/stocks/article/teslas-cybercab-sales-to-the-public-are-early-validation-of-robotaxi-push-jpmorgan-says-192145629.html)
- [Tesla Cybercab Clears Nationwide Regulatory Approval — 24/7 Wall St. card](https://247wallst.com/cards/tsla-xpost-01m7decw90bz2588segfrmvny2)
- [Stock Market Today, Dec. 22: Tesla shares jump after court reinstates Musk pay deal — Nasdaq](https://www.nasdaq.com/articles/stock-market-today-dec-22-tesla-shares-jump-after-court-reinstates-elon-musk-pay-deal)