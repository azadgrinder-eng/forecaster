# Research brief: Will Micron (MU) trade at or above $1,020 during November 2026?

## 1. Resolution mechanics
- **What counts as YES:** any 1-minute candle on Pyth's MU/USD feed with a High of **$1,020 or more**, after the market was created and before the end of November 2026 (close is 2026-12-01 04:59:59 UTC, which is 11:59 PM ET on Nov 30). Only regular trading hours count (9:30 AM–4:00 PM ET). Pre-market and after-hours prints do not count. Pyth prices are used as published, with no rounding.
- **Trading days left (counted from Nov 12):** Nov 12, 13, 16–20, 23–25, 27 and 30. That is about 12 sessions. Markets are closed Nov 26 for Thanksgiving, and Nov 27 is a half day ending at 1 PM ET.
- **Fallback source:** if Pyth data is unavailable, the primary exchange's (Nasdaq) official daily high is used instead.
- **Edge cases:**
  - Pyth is an aggregated price feed, so a brief Pyth wick could differ slightly from the Nasdaq consolidated high. This only matters if the price comes within a few cents of $1,020.
  - The target adjusts for stock splits. No split has been announced as far as I found. A split is plausible for a stock above $1,000 but unlikely to be announced and take effect within November.
  - The question says "after market creation". I don't know the creation date, but MU has been below $1,020 since mid-October, so earlier prints don't matter.

## 2. Reference classes and base rates
**A. Volatility-based barrier-touch math (driftless lognormal model).** The model gives the chance of touching $1,020 at least once within about 12 sessions (T ≈ 0.048 years).

| Starting price | Gain needed |
|---|---|
| $811 (Nov 11 close) | +25.7% (ln = 0.229) |
| $796 (after-hours price) | +28% |

| Annualized vol (σ) | Chance of touch from $811 |
|---|---|
| 60% | ≈7% |
| 80% | ≈19% |
| 100% | ≈29% |

- The latest clearly dated 30-day implied vol was **60.5% on Nov 4** (OptionCharts, Nov 4 2026). Its one-year range was 45% (Oct 6) to 107.7% (Jun 15). Implied vol almost certainly rose after the Nov 5 crash.
- Realized vol right now is extreme: −17.5% on Nov 5, +6% on Nov 9, +11.9% on Nov 11. A fair working range is about 75–95%, which gives roughly **12–25%**.
- Model limits: barrier models assume no drift and no fat tails. MU's recent history shows both fat tails and momentum regimes.

**B. MU's own recent 12-session rallies of 25% or more.** In 2026 this has happened several times:
- About +23.6% in 4 sessions from the Nov 5 close ($656.39) to the Nov 11 close ($811.30).
- A +19.3% single day to $895.88 on May 26.
- A climb from about $896 (May 26) to a $1,255 intraday high on Jun 25, about +40% in a month.

My rough guess is that a forward 12-day window with a +25% max gain occurred maybe 10–20% of the time in MU's 2026 trading. These figures are estimated from scattered reports, not a full price series.

**C. Large-cap tech after a sharp drawdown.** It is rare for a stock worth more than $800B to regain about 25% within 3 weeks. It happens mostly in V-shaped recoveries after a market-wide panic (for example, April 2025 after the "Liberation Day" tariff shock, when many chip stocks rose 25–40% within a few weeks). The Nov 5, 2026 selloff was the S&P 500's worst day since April 2025, so that analogy is apt. Still, most such recoveries take longer than 3 weeks to reach prior resistance.

## 3. Current state of the world (most recent first)
- **Nov 11 after hours / Nov 12:**
  - Reports said Nvidia's board might meet to replace CEO Jensen Huang. NVDA fell about 8% after hours and Nasdaq-100 futures about 1% (ABC News live blog, Nov 12 2026).
  - MU traded at **$796 after hours** (Google Finance snapshot, Nov 11).
  - I could not find Nov 12 session data.
- **Nov 11:**
  - MU closed at **$811.30, up 11.89%**. The intraday range was $763.05–$827.58 (Google Finance / Robinhood, Nov 11). Gurufocus reported $823.86, so sources differ.
  - The driver was CoreWeave's Q3 beat (CRWV +24.7%).
  - The semiconductor index (SOX) rose 5.7%, the Nasdaq 1.6% and the S&P 500 1.31% to 7,619 (HDFC Sky, Nov 12 2026).
  - Anthropic's IPO prospectus showed Micron among seven tech companies agreeing to buy $26B of its stock (Gotrade, Nov 12 2026).
  - Morgan Stanley said the valuation pullback improves the risk-reward for memory stocks (TradingKey, Nov 11).
- **Nov 10:** MU closed about $724.86 (Kraken previous close).
- **Nov 9:** MU rose about 6.3% to about $733 (Gurufocus / MarketBeat, Nov 9).
- **Nov 5 (Thursday):**
  - AI-led crash: S&P 500 −4.4% (about $2.9T lost, the largest one-day dollar loss on record), Nasdaq about −5.5%, SOX −12.3%, NVDA −9.3%.
  - The crash was attributed to Democratic midterm wins raising fears of curbs on data-center buildout (AP via KPTV, Nov 5 2026).
  - MU fell 17.5% to **$656.39** (Trefis, Nov 6 2026).
  - Bloomberg also reported that Micron had all but halted construction of its Taoyuan Fab 11E (about $3–4.5B) over a labor dispute. Taiwan makes about 60% of Micron's DRAM (Taipei Times / DCD, Nov 5–6 2026).
- **Nov 4:** 30-day implied vol was 60.5%. The options-implied 1-week move was ±8.8%, which puts the close at about $793 (OptionCharts).
- **Oct 29:** MU fell to about $900–930 after Big Tech capex disappointed (FX Leaders, Oct 29).
- **Oct 13:** MU closed at $989.04, its first close below $1,000 since Sep 17. Concerns cited were CXMT competition, Microsoft's custom chips and a Netlist patent dispute (Tokenpost / FX Leaders, Oct 12–13).
- **Jun 25:** all-time high of $1,255 intraday ($1,213.56 close). MU is now down about 29% over the past month and in a descending channel (Trefis; Gotrade).
- **Fundamentals:** guidance for fiscal Q1 2027 (given Sep 30) is revenue of $61.5B ± $1.5B and non-GAAP EPS of $38.15 ± $1. That implies a very low forward P/E near $800, which supports the dip-buying case. A UBS $1,625 target and a "Strong Buy" consensus (49 analysts) were reported, but the UBS target's date is unclear.
- **Scheduled before Nov 30:**
  - **Nvidia FQ3 earnings, Tue Nov 17, after the close** (NVIDIA IR, Oct 28 2026). This is the single biggest catalyst.
  - Fallout from the Nvidia CEO story.
  - Thanksgiving-shortened week.
  - Micron's own FQ1 earnings are expected around mid-to-late December, outside the window. A Dec 9 capital-return step-up was mentioned.

## 4. Drivers and scenarios
**Paths to YES** (about a 26–28% further gain from $796–811):
1. A strong Nvidia report on Nov 17 plus a resolution of the CEO uncertainty reignites the AI trade, extending the V-recovery from the Nov 5 crash. MU's high beta (+12% on a CoreWeave print) makes $1,000+ reachable within 2–3 strong sessions.
2. Supply-tightness stories (the Taiwan fab pause, DRAM shortages) plus a memory price-hike announcement or major HBM contract news.
3. Political or regulatory fears around the midterms ease, for example clarity that data-center policy won't tighten.

**Paths to NO:**
1. The Nvidia governance turmoil and the Nov 5 regulatory fears keep AI stocks rangebound or falling.
2. Resistance levels hold: the descending channel, plus $900–930 (late-October level) and $989–1,000 (mid-October breakdown). TradingShot targets about $650 by Nov 20.
3. Simply running out of time: only about 12 sessions, including a holiday half day.

## 5. Signposts
- **Nov 12–13 price action:** whether MU holds $800 after the Nvidia CEO news. A drop toward $720 makes YES much less likely, since it would then need +40%. A move to $870+ would raise the odds substantially.
- **The Nvidia CEO story:** confirmation or denial, and how NVDA trades.
- **Nvidia's Nov 17 results and guidance**, especially data-center demand and HBM commentary. A move of ±10% or more in NVDA would likely produce ±10–15% in MU.
- **Whether MU reclaims $900 and then $1,000** (prior support turned resistance).
- **Memory-sector news:** DRAM/HBM contract prices, SK Hynix and Samsung commentary, the Micron Taiwan labor dispute, CXMT news.
- **Market-wide sentiment:** VIX, the SOX index, and any further policy headlines from the midterm results.

## 6. Uncertainties
- I could not find the Nov 12 open or close. Starting levels from $780 to $820 shift the probability noticeably.
- No current implied vol after Nov 5 was found. Using 60% versus 90% roughly triples the probability.
- Price sources differ for Nov 11 ($811.30 vs $823.86 vs $821.88). Treat Google's $811.30 as the official close.
- Whether the Nvidia CEO report is accurate.
- The market's creation date (low relevance).
- Whether Pyth's MU feed wicks match Nasdaq prints.

## Sources
- [Micron Stock (MU) Rises 11.9% After CoreWeave Results (Nov 11) – Gotrade](https://www.heygotrade.com/en/news/micron-mu-stock-news-november-12-2026/)
- [Micron Technology (MU) Shares Surge 13% … November 11, 2026 – GuruFocus](https://www.gurufocus.com/news/9193176/micron-technology-mu-shares-surge-13-amid-tech-sector-rally-on-november-11-2026)
- [Micron Technology (MU) Shares Surge Over 6% … November 9, 2026 – GuruFocus](https://www.gurufocus.com/news/9186350/micron-technology-mu-shares-surge-over-6-amid-tech-rally-on-november-9-2026)
- [Micron Technology Shares Climb 6.3% – MarketBeat](https://www.marketbeat.com/instant-alerts/price-micron-technology-nasdaq-mu-shares-climb-63-heres-what-happened-2026-11-09/)
- [What Sent Micron Stock Lower? – Trefis, Nov 6 2026](https://www.trefis.com/stock/mu/articles/623345/what-sent-micron-stock-lower/2026-11-06)
- [MU Stock Climbs Above $800 From Support – FX Leaders, Nov 11 2026](https://www.fxleaders.com/news/2026/11/11/mu-stock-climbs-above-800-from-support-as-analysts-and-memory-demand-return-for-micron/)
- [Trading expert sets Micron stock price for November 20, 2026 – Finbold](https://finbold.com/trading-expert-sets-micron-stock-price-for-november-20-2026/)
- [Micron Technology Inc (MU) – Google Finance](https://www.google.com/finance/quote/MU:NASDAQ)
- [Micron Technology (MU) – Robinhood](https://robinhood.com/us/en/stocks/MU/)
- [Micron Technology (MU) – Kraken](https://www.kraken.com/stocks/mu)
- [Micron Technology (MU) – StockAnalysis](https://stockanalysis.com/stocks/mu/)
- [Memory Stocks Surge, Micron Jumps 11% as Morgan Stanley… – TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262300967-memory-stocks-morgan-stanley-micron-sandisk-ai-demand-buying-opportunity-tradingkey)
- [A brutal sell-off for AI stocks sends Wall Street reeling – KPTV/AP, Nov 5 2026](https://www.kptv.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs/?outputType=apps)
- [S&P 500 loses about $2.9T in market value – StockAnalysis](https://stockanalysis.com/news/sp-500-record-one-day-market-value-loss/)
- [Micron Shares Fall Below $1,000 for First Time Since Sept. 17 – Tokenpost](https://www.tokenpost.com/news/investing/30955)
- [MU Stock Falls Below $1,000 as Microsoft Chips and CXMT Raise Competition Risks – FX Leaders, Oct 12 2026](https://www.fxleaders.com/news/2026/10/12/mu-stock-falls-below-1000-as-microsoft-chips-and-cxmt-raise-competition-risks-for-micron/)
- [Micron MU Stock Falls to $900 as Big Tech Spending Misses Expectations – FX Leaders, Oct 29 2026](https://www.fxleaders.com/news/2026/10/29/micron-mu-stock-falls-to-900-as-big-tech-spending-misses-expectations/)
- [NVIDIA Sets Conference Call for Third Quarter Financial Results – NVIDIA IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/)
- [MU Option Overview – OptionCharts](https://optioncharts.io/options/MU)
- [The Options Market Says Micron Stock Can Halve Or Double – Trefis, Aug 26 2026](https://www.trefis.com/stock/mu/articles/613009/the-options-market-says-micron-stock-can-halve-or-double-from-here/2026-08-26)
- [Micron Taiwan plant pause – Taipei Times, Nov 6 2026](https://taipeitimes.com/News/biz/archives/2026/11/06/2003867231)
- [Labor dispute sees Micron pause construction at Taoyuan fab – DatacenterDynamics](https://www.datacenterdynamics.com/en/news/ongoing-labor-dispute-sees-micron-pause-construction-at-its-45bn-memory-fab-in-taoyuan-taiwan-report/)
- [Micron Q4 earnings call highlights – MarketBeat, Sep 30 2026](https://www.marketbeat.com/instant-alerts/transcript-micron-technology-q4-earnings-call-highlights-2026-09-30/)
- [Micron forecasts first-quarter revenue above expectations – Finviz](https://finviz.com/news/397483/micron-forecasts-first-quarter-revenue-above-expectations-on-ai-demand)
- [Nasdaq Jumps 1.60% as CoreWeave Fuels AI Rebound – HDFC Sky, Nov 12 2026](https://hdfcsky.com/news/nasdaq-jumps-1-6percent-as-coreweave-fuels-ai-rebound-lifting-stocks-november-12-2026)
- [Markets live: Nvidia board reportedly meeting to oust CEO Jensen Huang – ABC News, Nov 12 2026](https://www.abc.net.au/news/2026-11-12/asx-markets-business-news-live-updates-thursday-12-november/107374826)
- [Micron Technology stock tops $1,000, exceeds $1T – NewsBytes](https://www.newsbytesapp.com/news/business/micron-technology-stock-tops-1000-exceeds-1t-on-hbm-demand/tldr)
- [Micron stock hits record $742.15 – NewsBytes](https://www.newsbytesapp.com/news/business/micron-stock-hits-record-74215-per-share-amid-memory-demand/tldr)