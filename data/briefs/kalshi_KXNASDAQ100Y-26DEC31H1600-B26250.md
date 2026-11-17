# Research Brief: Will the Nasdaq-100 close between 26,000 and 26,499.99 on Dec 31, 2026?

## 1. Resolution mechanics
- **YES condition:** the Nasdaq-100 (NDX) value "on Dec 31, 2026 at 4pm EST" must be **≥26,000.00 and ≤26,499.99**. Anything else resolves NO. In practice this is the official closing value for Thursday, Dec 31, 2026. That is a normal full trading day for US stocks; the market is closed on New Year's Day, Friday Jan 1, 2027.
- **Timing:** the market closes Dec 31, 2026. It expires at the first release of the data, or one week after Dec 31 if the data is not released.
- **Who decides:** Kalshi, using the index value from its designated source. The rules say the Exchange has modified the "Source Agency and Underlying" for index markets. Forecasters should assume the official Nasdaq Global Indexes NDX close is the reference, but the exact source was not checked in the rulebook.
- **Edge cases:**
  - A market closure on Dec 31 (an unscheduled holiday or outage) could raise questions about which value counts.
  - A late print or closing-cross revision could matter if the close lands near 26,000 or 26,499.99.
  - "4pm EST" should mean the regular closing value, not an after-hours indicative value.
- **What the band means:** from the latest confirmed close (~27,197 on Nov 16), the band requires the index to finish between **−2.6% and −4.4%**. That range sits just below the November closing low of 26,629.81 (Nov 5). In practice, YES means a modest new low for the correction at year-end, about 15–17% below the Oct 6 record close of 31,224.47.

## 2. Reference classes and base rates
**A. Unconditional log-normal / volatility model (the main anchor).** There are about 31 trading days from Nov 17 to Dec 31 (9 left in November plus 22 in December). The band is ~1.9% wide in log terms, centred ~3.5% below spot.

| Annualized vol | σ over 31 days | Assumed drift | P(in band) |
|---|---|---|---|
| 25% | ~8.8% | ~+0.5% | ~7.8% |
| 30% | ~10.5% | ~+0.5% | ~6.7% |
| 35% | ~12.3% | ~+0.5% | ~5.8% |

These are my own calculations (normal approximation of band width × density). Fat tails in a high-volatility regime slightly lower the chance of landing in a narrow band near the centre. Recent daily moves of −6.36%, +3.4% and −2.7% suggest realized volatility well above 30%. No current VXN reading was found; the latest one located was 30.82 on Jun 26, 2026 (Yahoo Finance ^VXN).

**B. Historical NDX ~6-week returns.** NDX's long-run annualized volatility is roughly 22–25%, so σ over 31 days is ~7.5%. Late November through year-end has historically had a positive seasonal drift; my rough estimate is +1–1.5% average, with about 60–70% of years up. That estimate comes from general market-history knowledge and was not re-verified here. Under those assumptions, P(−4.5% < r < −2.6%) ≈ 8%.

**C. Post-correction behaviour.** This is NDX's third correction of 2026; the earlier ones were in late March and late July (Coinpaper / tradingandinvestmentnews, Nov 2026). On Nov 3, 24/7 Wall St. said the index needed a close above 28,437.17 to confirm a rebound, and that a close below 26,989.99 would signal only a relief bounce. Earlier 2026 corrections apparently recovered to new highs by October (record on Oct 6), which suggests mean reversion. On the other hand, corrections driven by Fed rate hikes (2022 is the analogue) often made lower lows. No clean frequency could be computed.

**Rough range across these classes: ~5–9%** for any single 500-point band this close to spot.

## 3. Current state of the world (most recent first)
- **Nov 17, 2026 (today):** Nvidia reports fiscal Q3 FY2027 results **after the close**. It is the company's first report since Jensen Huang resigned as CEO "last Thursday" (Nov 12) (Kiplinger live blog, Nov 2026; Yahoo/24-7 Wall St., Nov 16). Today's NDX close was not found. On Nov 16, NVDA fell 4.1% to $156.10, its lowest close since June 2025.
- **Nov 18–19:** the Anthropic IPO is reportedly set to price on Nov 18 and start trading on Nasdaq as "ANT" on Nov 19. The offer is 825M shares at an estimated $70–78, roughly $1.4T valuation, raising up to ~$64B (fourweekmba; letsdatascience; The Next Web, Nov 2026). This is a large supply and liquidity event for AI equities. Inclusion in NDX would not happen before Dec 31 under normal seasoning rules; not verified.
- **Nov 18:** minutes of the October FOMC meeting are released (TheStreet / Motley Fool, Nov 16).
- **Nov 16 (Mon):** NDX fell about 2.7%, its third straight loss. Close figures conflict:

  | Source | NDX close (Nov 16) |
  |---|---|
  | Cappnotes closing summary | 27,197.15 (−2.67%) |
  | Bloomberg | about −2.7% (level not given) |
  | Yahoo Finance quote page (internally inconsistent) | 27,310.40 |

  Other Nov 16 data (STL.News/Reuters):
  - Nasdaq Composite: 24,509.76 (−2.49%)
  - S&P 500: 7,416.59 (−1.92%)
  - VIX: up ~19%

  Drivers: chip and AI-infrastructure selling before Nvidia earnings; Amazon fell on a new AI chip export rule and a Leo satellite launch failure; Fed Chair Kevin Warsh warned that AI disappointment could cause a stock bust and a slowdown (Axios, CNBC, Nov 16).
- **Fed backdrop (Nov 16):** the Fed is in a **hiking** posture. At the October meeting the vote was 10–2 to hold, with two dissents in favour of a 25 bp hike. A strong October jobs report pushed market pricing toward a hike at the **Dec 8–9 FOMC**; one headline calls it a "100% chance" (Motley Fool, Nov 16; TheStreet). In October, Warsh declined to give forward guidance (CNBC, Oct 28).
- **Nov 11:** "AI stocks rebound and carry the Nasdaq 100 to a one-week high" (FXStreet, Nov 11).
- **Nov 9:** NDX rose ~3.4–3.5% to 27,907.63, its best day since Mar 31. That close was 10.62% below the record and implies a prior close of ~26,990 on Nov 6 (24/7 Wall St., Nov 10).
- **Nov 5:** NDX fell **6.36% to 26,629.81**, its worst day since Mar 16, 2020. The Philadelphia Semiconductor Index fell ~12%, Micron −17.5%, and NDX lost about $2.3T in value. The trigger was a Democratic midterm sweep raising fears for the pace of the AI data-center buildout (investinglive; 24/7 Wall St., Nov 6; IBTimes). **This is the lowest close of the correction so far, ~130 points above the top of the band.**
- **Nov 4:** NDX closed at 28,437.17 after a post-midterm rally.
- **Nov 2:** NDX closed at 27,989.82, 10.4% below the record, entering a correction (Bloomberg, Nov 2; 24/7 Wall St., Nov 3).
- **Oct 6:** record close of **31,224.47**.
- **Earlier 2026:** published year-end targets included Oppenheimer at 27,500 and StoneX at 26,500 (BingX, Apr 2026; stale). Through Aug 28, NDX was up ~16.6% year-to-date on a price basis (ChartRow).

**Scheduled before Dec 31:**
- Nvidia earnings (Nov 17, after the close)
- Anthropic IPO (Nov 18–19)
- FOMC minutes (Nov 18)
- Thanksgiving (Nov 26 closed; Nov 27 half-day)
- November jobs report (early December, presumably Dec 4)
- November CPI (mid-December)
- **FOMC decision (Dec 9)**
- Annual NDX reconstitution (announced in early/mid December, effective before the open on the Monday after the third Friday of December, ~Dec 21)
- Triple witching (Dec 18)
- Holiday-thin trading in the final week

## 4. Drivers and scenarios
- **Path to YES (−2.6% to −4.4%):**
  - A mild continuation of the correction: Nvidia's results or guidance disappoint, or a leadership-transition discount persists.
  - The Anthropic IPO drains capital from other AI names.
  - A hawkish Dec 9 hike with guidance for more hikes.
  - The index retests and slightly undercuts the Nov 5 low (26,630), then holds there into year-end.

  YES needs the move to be *moderate*. A deeper slide (below 26,000, i.e. more than −4.4%) or any recovery fails.
- **Paths to NO, higher (most probability mass):**
  - Nvidia beats and relief follows.
  - A strong Anthropic debut revives AI sentiment.
  - The hike is already priced ("sell the rumor, buy the news").
  - Seasonal Santa-rally strength and dip-buying, as after the March and July corrections.

  Any year-end close above 26,500 resolves NO. Spot (~27,200) is already above the band.
- **Path to NO, lower:**
  - The AI-capex unwind deepens: the post-midterm data-center policy fears, Warsh's warning about an AI bust, and further export curbs.
  - A credit or liquidity event.
  - NDX falls below 26,000; that is roughly −17% from the peak, approaching bear-market territory.
- **Key dependency:** the very high realized volatility spreads probability widely and *lowers* the chance for any single 500-point band.

## 5. Signposts
- **Nov 17 close and the Nov 18 reaction to Nvidia results:**
  - A move of ±5–10% in NDX-heavy names would shift spot by roughly ±2–3%.
  - A drop toward ~26,500–26,800 would put the band near the centre of the distribution and raise the probability to perhaps 8–10%.
  - A rally back above 28,000 would cut it to ~3–5%.
- **Anthropic IPO pricing and day-one trading (Nov 18–19):** a weak debut is bearish for AI names; a hot debut is bullish.
- **Dec 9 FOMC:** a hike with a hawkish dot plot is bearish; a hike paired with dovish guidance, or a hold, is bullish.
- **Whether the 26,630 low (Nov 5) holds:** a close below it signals a trend toward or through the band.
- **Implied volatility (VXN):** a falling VXN concentrates probability near spot, which is above the band. A rising VXN flattens the distribution.
- **In late December:** distance from the band edges matters most; each 1% of distance changes the probability substantially.

## 6. Uncertainties
- The exact Nov 16 close is unconfirmed (27,197 vs 27,310), and the Nov 17 close and Nvidia's results were not available.
- No current VXN, VIX or options-implied distribution for December was found, so the volatility assumption (25–35%) is an estimate.
- Kalshi's modified "Source Agency/Underlying" for index markets was not checked in the rulebook.
- Some secondary sources give slightly inconsistent numbers (for example, the Nov 9 gain is cited as 3.40% and 3.54%). Exchange data was not available because the page fetches were blocked.
- No current (November 2026) strategist year-end targets were found.
- The size and timing of Anthropic IPO effects on index constituents are unclear.

## Sources
- [The Nasdaq 100 Is Now Officially in a Correction – 24/7 Wall St. (Nov 3, 2026)](https://247wallst.com/investing/2026/11/03/the-nasdaq-100-is-now-officially-in-a-correction/)
- [The Nasdaq-100 Just Had Its Best Day Since March Without Nvidia's Help – 24/7 Wall St. (Nov 10, 2026)](https://247wallst.com/investing/2026/11/10/the-nasdaq-100-just-had-its-best-day-since-march-without-nvidias-help/)
- [Big Tech Selloff Pushes Nasdaq 100 Into Correction – Bloomberg (Nov 2, 2026)](https://www.bloomberg.com/news/articles/2026-11-02/nasdaq-100-enters-correction-as-megacap-results-amplify-ai-fears)
- [Nasdaq 100 suffers worst day since 2020 – investinglive (Nov 5, 2026)](https://investinglive.com/stocks/nasdaq-100-suffers-worst-day-since-2020/)
- [Tech Stocks Just Had Their Worst Day Since 2020 – 24/7 Wall St. (Nov 6, 2026)](https://247wallst.com/investing/2026/11/06/tech-stocks-just-had-their-worst-day-since-2020/)
- [Nvidia, Qualcomm shares / Nasdaq AI selloff – IBTimes](https://www.ibtimes.co.uk/nvidia-qualcomm-shares-nasdaq-ai-selloff-1830635)
- [Nasdaq 100 Crashes Into Third Correction of 2026 – Coinpaper](https://coinpaper.com/38282/nasdaq-100-enters-10-correction-as-ai-stock-selloff-wipes-out-trillions)
- [AI stocks rebound and carry the Nasdaq 100 to a one-week high – FXStreet (Nov 11, 2026)](https://www.fxstreet.com/news/ai-stocks-rebound-and-carry-the-nasdaq-100-to-a-one-week-high-202611112158)
- [Nasdaq 100 Tumbles for Third Day With Nvidia Earnings on Horizon – Bloomberg (Nov 16, 2026)](https://www.bloomberg.com/news/articles/2026-11-16/nasdaq-100-plunges-as-nvidia-earnings-anthropic-ipo-on-horizon)
- [Closing Look — Monday, November 16, 2026 – Cappnotes](https://cappnotes.substack.com/p/closing-look-monday-november-16-2026)
- [NASDAQ-100 (^NDX) – Yahoo Finance](https://finance.yahoo.com/quote/%5ENDX/)
- [U.S. Stock Market Today: November 16, 2026 – STL.News](https://www.stl.news/u-s-stock-market-today-november-16-2026/)
- [Stocks slide to kick off major week for Wall Street – CNN (Nov 16, 2026)](https://cnn.com/2026/11/16/business/stocks-nvidia-ai-anthropic)
- [Stock Market Today: Nasdaq-100 Sinks 1% as Nvidia Faces Its First Earnings Without Jensen Huang – 24/7 Wall St. (Nov 16, 2026)](https://247wallst.com/investing/2026/11/16/stock-market-today-nasdaq-100-sinks-1-as-nvidia-faces-its-first-earnings-without-jensen-huang/)
- [Nvidia Earnings: Live Updates November 2026 – Kiplinger](https://www.kiplinger.com/news/live/nvidia-earnings-live-updates-and-commentary-november-2026)
- [S&P 500, Dow, Nasdaq End Lower Ahead Of Nvidia Earnings, Anthropic IPO – Stocktwits (Nov 16, 2026)](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-end-lower-as-investors-hold-back-ahead-of-nvidia-earnings-anthropic-ipo/cNbaf4PR9gk)
- [Federal Reserve chairman Warsh sees risk of stock bust if AI boom disappoints – Axios (Nov 16, 2026)](https://axios.com/2026/11/16/fed-warsh-ai-boom-stocks)
- [Fed Chairman Kevin Warsh stresses importance of AI to economy – CNBC (Nov 16, 2026)](https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html)
- [There's Now a 100% Chance of a Fed Rate Hike in December – Motley Fool (Nov 16, 2026)](https://www.fool.com/investing/2026/11/16/theres-now-100-chance-fed-rate-hike-in-december-thats-not-worst-news-for-wall-street/)
- [Fed rate call leaves stock investors watching December closely – TheStreet](https://www.thestreet.com/fed/fed-rate-call-stock-investors-watching-for-december-hike)
- [Fed Chairman Warsh on a December hike – CNBC (Oct 28, 2026)](https://www.cnbc.com/video/2026/10/28/fed-chairman-warsh-on-a-december-hike-i-dont-believe-in-forward-guidance-absent-a-crisis.html)
- [Anthropic's IPO Day by Day: Pricing 18 Nov, Trading 19 Nov – FourWeekMBA](https://fourweekmba.com/ai-anthropics-ipo-day-by-day-pricing-18-nov-trading-19-nov/)
- [Anthropic Sets IPO Range and Adds $26 Billion Private Placement – letsdatascience](https://letsdatascience.com/news/anthropic-sets-ipo-range-and-adds-26-billion-private-placeme-f6c67619)
- [Anthropic's IPO seeks up to $64.4B at a $1.4 trillion valuation – The Next Web](https://thenextweb.com/news/anthropic-ipo-terms-1-4-trillion-valuation)
- [Nasdaq 100 (NAS100) Forecast 2026 – BingX (Apr 2026)](https://bingx.com/en/learn/article/nasdaq-100-nas100-outlook-and-price-prediction-is-nas100-a-good-investment)
- [Nasdaq-100 stock performance (2026) – ChartRow](https://chartrow.com/nasdaq-100/stock-performance)
- [CBOE Nasdaq-100 Volatility (^VXN) – Yahoo Finance](https://finance.yahoo.com/quote/%5EVXN/)