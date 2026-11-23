# Research Brief: Will Nvidia's market cap be between $4.00T and $4.50T at the close on Dec 31, 2026?

**Bottom line:** At the Nov 20, 2026 close Nvidia was worth about **$3.04–3.05T**. To land in this bracket it must rise **about 31–48% in roughly 26 trading days**. The crash that got it here came from a CEO resignation, a reported SEC accounting probe, a delayed 10-Q, and a market-wide AI selloff.

*Caveat on sources:* WebFetch was blocked by the network proxy for every page I tried. All facts below come from search-result summaries of the cited articles, not from reading the primary documents directly. Figures that differ between sources are flagged.

---

## 1. Resolution mechanics

- **What counts:** Nvidia's official Nasdaq regular-session closing price on the last trading day of 2026, multiplied by total shares outstanding taken from official filings. Nvidia has one share class, so no conversion questions arise.
- **Date:** Thursday, Dec 31, 2026 should be a normal full trading day (Jan 1, 2027 is the holiday). After-hours prices don't count.
- **YES range:** $4.00T ≤ market cap < $4.50T. A value of exactly $4.00T counts as YES. A value of exactly $4.50T goes to the next bracket up and counts as NO.
- **Price needed:**
  - At 24.3B shares (10-Q cover, Nov 14, 2025): about **$164.6 to $185.2**.
  - At 24.1B shares (an aggregator's figure for Nov 4, 2026, not verified against a filing): about **$166.0 to $186.7**.
  - The Q1 FY2027 10-Q gave 24.2B shares as of May 15, 2026, which implies about $165.3–$186.0.
  - So the YES price window is roughly **$165–$186**.
- **Share-count edge case:** The Q3 FY2027 10-Q, which would carry the newest cover-page share count, **had not been filed** as of Nov 18. If it is still missing at year end, whoever resolves the market may use the Q2 10-Q count or an aggregator. The choice of count moves the price window by about $1.5–2. That only matters if the close lands right at a boundary.
- **Who decides:** The market operator, using exchange data and SEC filings. The rules don't name a specific data vendor, so there is some ambiguity in which number gets used.

## 2. Reference classes and base rates

**A. Nvidia's own ~5-week returns.** The question needs a gain of +31% to +48% from $125.53.
- From memory of Nvidia's monthly return history since about 2010, roughly 4–6% of calendar months gained more than 30%. Examples include about +34% in Jan 2023 and about +36% in May 2023, plus several in 2016. I estimate only about 3–5% of months landed in the narrower +31% to +48% band. These are approximate counts from memory, not verified this session.

**B. Volatility model (lognormal, no drift, 26 trading days).**

| Annualized volatility | P(+31% to +48%) | P(above +48%) |
|---|---|---|
| 50% | ~4% | ~1% |
| 60% | ~6% | ~2% |
| 75% (plausible after the crash) | ~8% | ~5% |
| 90% | ~10% | ~8% |

**C. Rebounds after megacap crashes caused by scandal or panic.**
- **Rebounds that happened:**
  - Nvidia's COVID drop in March 2020 recovered about 45–50% from the low within about 5–6 weeks, helped by a market-wide rebound and Fed support.
  - After DeepSeek (Jan 27, 2025, −17% in one day), Nvidia won back much of the loss within about 3 weeks, but full recovery took months.
- **Rebounds that didn't happen:**
  - Super Micro (2024, auditor resignation and filing delay) did not get back to its pre-scandal level within weeks. The stock recovered partly only once the filings were cured.
  - Nvidia's 2018 crypto/inventory crash (about −56%) took more than a year to recover.
  - 24/7 Wall St notes that the last time the SEC examined Nvidia's accounting (the 2008 era), the stock fell 81% in a year (24/7 Wall St, Nov 20, 2026).
- **Takeaway:** A 30%+ recovery inside 5 weeks has usually needed a macro relief rally plus a quick resolution of the specific fear.

## 3. Current state of the world (most recent first)

- **Nov 23, 2026 (pre-market):** Nasdaq/S&P/Dow futures were up about 2% after the previous week's selloff (TradingView/Stocktwits, Nov 23). I found no regular-session Nvidia quote for today.
- **Nov 20–21:**
  - Nvidia closed at **$125.53**, down 14.0% on the day (prior close $145.98) and down about 23% on the week. That was its worst week since Oct 2008 and its seventh straight weekly decline.
  - It lost about $900B in value that week, a record one-week loss for any company per Dow Jones Market Data. The previous week's loss was about $573B.
  - The stock is about 48% below its **Oct 6, 2026 record of $243.37**, which was roughly $5.9T in market cap. Its 52-week low is about $124.50.
  - After hours it traded around $130–132 (Investing.com; Motley Fool, Nov 21; Yahoo Finance).
  - Market cap is reported at about $3.03–3.14T depending on the source.
- **Nov 20 (Reuters):** SEC enforcement staff are reportedly examining possible accounting problems at Nvidia. The scope and start date are unknown.
  - The probe follows questions about Nvidia's 2025 change to how it reports revenue by geography, made while Singapore sales neared about half of revenue (per the FT).
  - It also connects to Megaspeed, a Singapore customer. Huang reportedly had a relationship with someone tied to that company.
  - Nvidia denies wrongdoing (Stocktwits).
  - One Yahoo report says California AG Rob Bonta subpoenaed Nvidia over whether its chips reached China and whether investors were misled. A second search could not confirm this.
- **Nov 20 (market):** The Nasdaq Composite fell about 5.1–5.3% that day and about 10% for the week, wiping out its 2026 gains. The Nasdaq-100 is close to a bear market. Causes cited:
  - doubts about how the AI buildout is being financed
  - Anthropic shares falling after its Nasdaq IPO
  - futures pricing a near-certain **25bp Fed rate hike at the Dec 9 meeting**, with Governor Waller floating 50bp (Invezz, Nov 20; HNGN, Nov 20; Schwab)
- **Nov 18:** On the earnings call, Nvidia said it would **delay its Q3 10-Q** and file "in the coming weeks." Management connected the delay to the ongoing investigation and possible new risk factors.
  - Nvidia has filed the Q3 10-Q between Nov 14 and Nov 22 every year since 2013.
  - The 40-day deadline is about **Dec 4, 2026**; an NT 10-Q extension would add 5 days.
  - Michael Burry compared the situation to Super Micro's (TechCrunch, Nov 18; The Inference).
- **Nov 18 (stock reaction):** An after-hours gain of about 4% faded. The stock closed about −2.9% (reports put the close near $151, versus $155.46 on Nov 17; sources conflict).
- **Nov 17 (Q3 FY2027 results):**
  - Revenue $115.8B, up 103% from a year earlier (guidance was $108B ±2%; consensus about $109B).
  - Data Center revenue $107.6B, up 110%.
  - GAAP gross margin 74.8%; non-GAAP EPS $2.68 versus about $2.47 expected.
  - Q4 guidance $130B ±3%, which assumes no China data-center revenue and includes an extra week.
  - Q4 gross margin guided down to 71–72% (Nvidia press release via StockTitan/Panabee, Nov 17).
  - So the fundamentals are very strong, and the selloff is about governance, accounting, and macro.
- **Nov 12–13 (leadership):**
  - **Jensen Huang resigned** as CEO, president, and director, effective immediately. Reports cite affair allegations and espionage-related allegations; CNBC sources say the board pushed him out.
  - **CFO Colette Kress is interim CEO** and remains CFO. Harvey Jones became board chair.
  - The board says it won't reinstate Huang. On Nov 13 it had not yet picked a search firm.
  - Names mentioned: Rene Haas (Arm; the FT says he was approached, while the board says no one has been formally engaged), Jay Puri (internal), Nikesh Arora, Thomas Kurian, and Tim Cook (suggested by Trump).
  - Huang has been summoned to testify before Congress (CNN, Nov 11; CNBC, Nov 12–13; Al Jazeera, Nov 12; SEC 8-K).
- **Analysts:** Phillip Securities cut its target to $225 from $300 and kept Buy. Sell-side targets still sit well above the YES window.

**Scheduled or expected before Dec 31:**
- the Q3 10-Q filing (around Dec 4, or later with an NT 10-Q)
- FOMC decision on Dec 9
- possible news on the CEO search
- possible congressional testimony by Huang
- any SEC or state follow-ups
- monthly CPI and jobs data
- year-end rebalancing and tax-loss selling (tax-loss selling could weigh on a stock down about 48% from its peak)

## 4. Drivers and scenarios

**YES (close roughly $165–186):** needs a recovery to about where the stock traded on Nov 17–19 ($151–155) plus another 7–20%. Plausible ways that happens:
- The 10-Q is filed cleanly and on time, with no restatement and only limited new risk-factor language.
- Reporting suggests the SEC probe is narrow, about disclosure only.
- The board names a credible permanent CEO quickly, such as Haas or a strong internal pick.
- The macro picture turns: the Fed hikes less than feared or signals a pause, and AI stocks rally broadly into year end.
- A large buyback is announced or accelerated.
- The valuation argument (Q4 run-rate revenue of about $130B a quarter) brings dip buyers back.

**NO, below $4.0T (the most likely NO path):**
- A partial recovery that stalls below about $165.
- The 10-Q slips past the deadline, an NT 10-Q is filed, or the auditor raises issues.
- The SEC probe widens, or a restatement or China export-diversion findings emerge.
- The CEO search drags on.
- The Fed hikes and the Nasdaq-100 enters a bear market.
- Tax-loss selling into year end.

**NO, at or above $4.5T (close ≥ about $185–187):** needs a very fast V-shaped recovery of about 48% or more, essentially every overhang resolving plus a strong market rally. This is unlikely, but not much less likely than YES given how volatile the stock is.

## 5. Signposts

- **10-Q filed by about Dec 4 with no restatement and a clean auditor opinion:** strong move up. An NT 10-Q, a restatement, or an auditor change would be a strong move down (the Super Micro pattern).
- **Details on the SEC probe** (scope, any Wells notice, or reporting that it is routine): large effect in either direction.
- **Permanent CEO announced:** a credible external or well-regarded internal pick is a moderate-to-strong positive. A prolonged search or board turmoil is negative.
- **The Dec 9 FOMC decision and Nasdaq-100 direction:** a 25bp hike is already priced in. 50bp or hawkish guidance would hurt; a pause would help.
- **Nvidia's price by mid-December:** if it is still under about $140 by Dec 15, YES becomes remote. A move back above about $155 makes YES a live possibility.
- **More fallout:** Huang's testimony, the California AG probe, China-diversion stories, customer reactions (hyperscalers' capex comments), and any Anthropic or OpenAI financing worries.

## 6. Uncertainties

- I could not get a regular-session quote for Nov 23, 2026. Pre-market futures were up about 2%, and Nvidia's after-hours price on Nov 20 was about $130.
- The exact current share count is unverified (24.1B from an aggregator versus 24.2–24.3B in filings), and it's unclear which count the resolver would use if the Q3 10-Q is late.
- The scope of the SEC probe and the California AG subpoena are not confirmed; the AG subpoena appeared in only one source.
- Current implied volatility on Nvidia options could not be checked. The volatility table assumes 50–90%.
- Some search summaries conflicted on exact figures: the Nov 18 close, the size of the Nasdaq drop, and the total wealth lost ($2.5T versus $2.7T "rout").
- The base-rate frequencies in reference class A are from memory, not computed from data this session.

## Sources
- [NVIDIA Announces Financial Results for Third Quarter Fiscal 2027 (StockTitan)](https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-third-quarter-fiscal-fpx9dw5egxqa.html)
- [NVIDIA Announces Financial Results for Third Quarter Fiscal 2027 (Nvidia IR)](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2027/)
- [Nvidia (NVDA) Q3 2027 Earnings: Revenue Grows 103% (Panabee)](https://www.panabee.com/news/nvidia-earnings-q3-2027)
- [Nvidia Q3 Revenue Surges 103%... (TradingKey)](https://www.tradingkey.com/analysis/stocks/us-stocks/262309793-nvidia-earnings-report-q3-rubin-ramp-data-center-growth-revenue-guidance-gross-margin-tradingkey)
- [NVIDIA (NVDA) Market capitalization (CompaniesMarketCap)](https://companiesmarketcap.com/nvidia/marketcap/)
- [After Its Worst Week in 18 Years, Nvidia Now Faces an SEC Investigation (Motley Fool, Nov 21, 2026)](https://www.fool.com/investing/2026/11/21/after-its-worst-week-in-18-years-nvidia-now-faces-an-sec-investigation-what-it-means-for-investors/)
- [Nvidia suffers worst week since 2008, as SEC probe report fuels post-Huang turmoil (Investing.com)](https://www.investing.com/news/stock-market-news/nvidia-shares-fall-10-as-report-of-sec-accounting-probe-adds-to-pressure-5042464)
- [Nvidia's accounting is a focus of US SEC investigation, sources say (Reuters via Investing.com)](https://www.investing.com/news/economy-news/exclusiveus-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-5042460)
- [Wall Street Regulator Probes Nvidia Accounting, Reuters Says (Bloomberg, Nov 20, 2026)](https://www.bloomberg.com/news/articles/2026-11-20/wall-street-regulator-probing-nvidia-s-accounting-reuters-says)
- [Nvidia stock extends $2.7 trillion rout as SEC probe reportedly investigates its accounting (Yahoo Finance)](https://finance.yahoo.com/markets/article/nvidia-stock-extends-25-trillion-rout-as-sec-probe-reportedly-investigates-its-accounting-194945274.html)
- [Nvidia Stock Just Lost $900 Billion in Its Worst Week Since 2008 (24/7 Wall St, Nov 20, 2026)](https://247wallst.com/investing/2026/11/20/nvidia-stock-just-lost-900-billion-in-its-worst-week-since-2008-the-last-time-the-sec-examined-nvidias-accounting-the-stock-fell-81-in-a-year/)
- [NVDA Stock Clocks Worst Week In 18 Years (Stocktwits/TradingView)](https://www.tradingview.com/news/stocktwits:bc8433c56094b:0-nvda-stock-clocks-worst-week-in-18-years-as-sec-reportedly-probes-its-accounting-practices/)
- [Nvidia CEO Jensen Huang resigns: Live updates (CNBC, Nov 12, 2026)](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- [Nvidia CEO: Search firm not yet selected for Huang replacement (CNBC, Nov 13, 2026)](https://www.cnbc.com/2026/11/13/nvidia-huang-ceo-replacement-search.html)
- [Why did Nvidia CEO Jensen Huang resign, and who is Colette Kress? (Al Jazeera, Nov 12, 2026)](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress)
- [NVIDIA Form 8-K – CEO transition (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm)
- [Jensen Huang summoned to testify before Congress (CNN, Nov 11, 2026)](https://www.cnn.com/2026/11/11/business/live-news/nvidia-jensen-huang-investigation-fallout)
- [Nvidia earnings live updates: Board has no plans to reinstate Jensen Huang (NBC News)](https://www.nbcnews.com/business/business-news/live-blog/nvidia-stock-earnings-report-jensen-huang-rcna609804)
- [Nvidia's new CEO search is on (Yahoo Finance UK)](https://uk.finance.yahoo.com/news/nvidias-ceo-search-top-candidates-163713679.html)
- [Nvidia created a weird bit of intrigue by not filing a routine SEC report (TechCrunch, Nov 18, 2026)](https://techcrunch.com/2026/11/18/nvidia-created-a-weird-bit-of-intrigue-by-not-filing-a-routine-sec-report/)
- [Michael Burry compares Nvidia's unfiled 10-Q to Super Micro's auditor-scandal delay (The Inference)](https://theinference.org/article/michael-burry-compares-nvidia-s-unfiled-10-q-to-super-micro-s-auditor-scandal-delay)
- [NVIDIA Form 10-Q, quarter ended Apr 26, 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000052/nvda-20260426.htm)
- [NVIDIA Form 10-Q, quarter ended Jul 26, 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm)
- [NVDA shares outstanding (Arincen)](https://en.arincen.com/instruments/NVDA/shares-outstanding)
- [Nasdaq, Dow, S&P 500 Futures Jump Nearly 2% After Brutal Tech Selloff (Stocktwits/TradingView, Nov 23, 2026)](https://www.tradingview.com/news/stocktwits:516edb8ad094b:0-nasdaq-dow-s-p-500-futures-jump-nearly-2-after-brutal-tech-selloff-last-week-gme-jnj-alny-gap-in-focus/)
- [Nasdaq falls as Anthropic slides, dragging AI stocks into weekly selloff (Invezz, Nov 20, 2026)](https://invezz.com/news/2026/11/20/nasdaq-falls-as-anthropic-slides-dragging-ai-stocks-into-weekly-selloff/)
- [Wall Street Plunges Into Correction as AI Selloff Erases Nasdaq's 2026 Gains (HNGN, Nov 20, 2026)](https://www.hngn.com/articles/273903/20261120/wall-street-plunges-correction-ai-selloff-erases-nasdaqs-2026-gains.htm)
- [Dip buyers hesitate to step in as Nasdaq 100 nears a bear market (The Edge Singapore)](https://www.theedgesingapore.com/news/highlight/dip-buyers-hesitate-step-nasdaq-100-nears-bear-market)
- [Markets' November Nightmare Keeps Getting Worse (Schwab)](https://www.schwab.com/learn/story/market-volatility)
- [Nvidia Stock Analysis Nov 2026 (Vantage Markets)](https://www.vantagemarkets.com/market-analysis/nvda-stock-monthly-outlook-analysis-nvidia/)