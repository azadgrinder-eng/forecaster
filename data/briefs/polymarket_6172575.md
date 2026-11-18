# Research Brief: Will SPY trade at or above $790 during regular hours in November 2026?

## 1. Resolution mechanics
- **What counts as YES:** Any 1-minute candle on the Pyth SPY/USD chart has a High of $790.00 or more. The candle must fall during regular trading hours (9:30 AM–4:00 PM ET), after the market was created, and on or before November 30, 2026. Pre-market and after-hours prices don't count. Pyth prices are used exactly as published, with no rounding.
- **Close:** The market closes 2026-12-01 04:59:59 UTC, which is 11:59 PM ET on November 30. As of today (Wed Nov 18) about **8 trading sessions are left**: Nov 18, 19, 20, 23, 24, 25, 27 (closes early at 1:00 PM ET) and 30. Markets are shut on Thanksgiving, Nov 26 (Admiral Markets calendar).
- **Who decides:** Pyth data on pythdata.app. If Pyth is down or its data fails, the primary exchange's official daily high is used instead.
- **Edge cases:**
  - Pyth is an aggregated oracle feed, so a brief outlier in a 1-minute high could in theory print above the consolidated tape. This only matters if SPY ends up within a few cents of $790.
  - Splits are not relevant to SPY.
  - SPY pays its quarterly dividend in December, not November, so no ex-dividend drop is expected inside the window.
  - Only reaching the price matters. SPY does not need to close above $790.

## 2. Reference classes and base rates
**Distance to target.**
- SPY closed at **$732.44 on Nov 17**. That day's range was $727.00–$739.76 (Gotrade quote data, Nov 17).
- $790 is **+7.9% from that close**. If the ~+0.8% overnight futures gain carries into the open (about $738), the gap is about +7.0%.
- $790 is also **above SPY's all-time intraday high of about $781.62**, set Oct 6, 2026. The record close that day was $779.09 (TradingNews; Macrotrends). So YES needs a new record high, about 1.1% above the old one.
- SPY tracks the S&P 500 at roughly 0.0998×, so $790 SPY ≈ **S&P 500 7,915–7,920**. The index record is 7,844.52 intraday and 7,818.93 at the close, both Oct 6 (Wikipedia closing milestones; Yahoo history).

**Reference class A: volatility model (barrier-hit probability).**
- I used the reflection-principle approximation: P(max ≥ target) ≈ 2·(1−Φ(x/σ√T)), with T ≈ 8 sessions. These are my own estimates.
- VIX closed around 25.5–26 on Nov 17, with an intraday high of 27.73 (Yahoo; Weekend Spread, Nov 17). That implies about 1.6% daily vol.

| Starting price | Daily vol 1.6% (VIX-implied) | Daily vol 1.3% (realized usually below VIX) |
|---|---|---|
| $732 (Nov 17 close, +7.9% needed) | ~8–9% | ~3% |
| ~$738 (after futures gain, +7.0% needed) | ~12–13% | ~5–6% |

- Caveats:
  - These numbers ignore drift and the overhead resistance at the old record.
  - The approximation overstates the chance a little because trading is in discrete minutes and the window ends with a half day.
  - It understates fat-tailed short-squeeze outcomes.

**Reference class B: historical frequency of 8-session gains of 8% or more.**
- Since 1950, a high in the next 8 sessions at least 8% above a starting close has happened in only about 1–2% of windows. This is my rough estimate from known episodes: 1974, 1982, 1987, 2008–09, March–April 2020, Nov 2022, April 2025.
- Almost all of these came when VIX was above 30 and the index was deep in a bear market (down 15% or more), not about 6% off its high.
- With VIX in the mid-20s, a rough base rate of **2–5%** seems reasonable.

**Reference class C: V-shaped recoveries to new highs.**
- Going from about 6–7% below the record to a new record within about 2 weeks is rare.
- One close analogue is April 2025. After the tariff pause, SPY rose about 10% in one day, but it still took months to reach new highs.
- After the late-2023 and Dec 2018 lows, recovering a 6–10% drawdown typically took several weeks to months.

## 3. Current state of the world (most recent first)
- **Nov 18 (today), scheduled:**
  - FOMC minutes from the Oct 27–28 meeting at 2:00 PM ET.
  - Housing starts.
  - Anthropic IPO pricing may come after the close, with first trade possibly Thu Nov 19 on Nasdaq. The date is unconfirmed and sources conflict (Hyperstocks/Helious calendars; TradingView/Stocktwits, Nov 17).
- **Nov 17, after hours: Nvidia's fiscal Q3 report beat expectations.**
  - Adjusted EPS $2.68 vs $2.48 expected; revenue $115.84B vs $109.1B (CNBC, Nov 17).
  - Q4 revenue guide $130B ±3% vs about $125.3B expected. FY28 growth outlook raised to 75% from 70%.
  - NVDA rose about 2–4.8% after hours.
  - S&P 500 futures rose about 0.7–0.8% and Nasdaq-100 futures about 1.4%. By early Wednesday in Tokyo, S&P futures had pared the gain to about +0.4% (swissinfo/Bloomberg wrap; Investing.com, Nov 17–18).
- **Nov 17 session:**
  - S&P 500 fell 1.03% to 7,340.53, its lowest close since late July. The S&P 500 and Nasdaq each had their first 4-session losing streak since September.
  - The Dow fell 1.64% to 50,759.
  - Causes cited: AI capex and valuation worries, rate warnings, tech outages, and Salesforce down about 9.4% (CNBC; HNGN; Yahoo/Reuters, Nov 17).
- **Nov 16:** S&P 500 fell 1.92% (−145 points) to 7,416.59, and the Dow dropped more than 800 points (CNBC, Nov 16).
- **Nvidia leadership turmoil:**
  - Reuters and AP report that Jensen Huang resigned as CEO amid a scandal over his personal conduct and alleged ties to a Chinese spy.
  - NVDA has lost about $735B in market value. It is down about 24% in November and about 35% from its Oct 6 record. Colette Kress is interim CEO, and the board says Huang will not return (Yahoo/AP/Reuters, Schwab, Nov 16–17).
  - Treat the specific details with some caution. They come through search summaries and I could not open the original pages.
- **Nov 13:** The Nasdaq-100 was about 10.5% below its October high, while the S&P 500 was only about 3% off its high (Motley Fool, Nov 17).
- **Nov 11:** S&P 500 rose 1.31% to 7,619. **Nov 4:** the index reached about 7,688 (CNBC). The November high so far is therefore about SPY $767. **$790 has not been touched this month.**
- **Oct 6:** Record S&P 500 close of 7,818.93 and intraday high of 7,844.52. SPY's record close was $779.09 and its intraday high about $781.62.
- **Rest of the window:**
  - Nov 19: jobless claims.
  - Nov 20: final UMich sentiment.
  - Nov 25: PCE, second estimate of Q3 GDP, and the Beige Book.
  - Nov 26: market holiday.
  - Nov 27: half-day session.
  - The next FOMC meeting is Dec 8–9, after the window closes (Admiral Markets; LiteFinance calendars).

## 4. Drivers and scenarios
**Paths to YES (all require about +7–8% in 8 sessions plus a new all-time high):**
1. **Relief rally led by Nvidia and AI.** NVDA's strong guidance flips the "AI unwind" narrative, and the beaten-down megacaps short-squeeze (NVDA is about 35% off its peak). A successful Anthropic IPO adds to AI enthusiasm. This depends on the strength holding for several sessions, not just a one-day pop.
2. **Macro shock to the upside.** Examples: a dovish surprise in the FOMC minutes, soft PCE on Nov 25 that raises odds of a December cut, or a sudden policy or geopolitical positive. A big one-day move needs a surprise of 2025-tariff-pause size, and nothing like that is scheduled.
3. **Seasonality.** The Thanksgiving week is historically mildly positive, worth roughly +0.5–1%. That is not enough on its own.

**Paths to NO:**
1. **Normal mean reversion.** SPY bounces 2–4% but stops below the October high ($780–782). Even a strong recovery would usually stall at or below the old record within 8 days.
2. **Continued AI de-rating.** The Nvidia governance scandal, capex doubts and rate concerns keep pressing on the index, and the Nvidia pop fades as it did in early Asian trading.
3. **Holiday liquidity.** Thin trading on Nov 25 and the Nov 27 half day reduces the chance of a breakout late in the window.

## 5. Signposts
- **Nov 18 regular session (biggest single update):**
  - Upward: SPY closes at $745 or higher (about +1.7%) with NVDA up strongly and broad participation.
  - Downward: the futures gain fades and SPY closes at $735 or lower.
- **SPY at $760 or higher by Nov 20–23:** the target would then be about 4% away with about 5 sessions left, which raises the probability materially.
- **VIX:**
  - A drop below 20 in a quiet, grinding rally means lower vol, which works against reaching a far target quickly.
  - A violent upside squeeze while VIX stays above 22 is the only realistic YES profile.
- **Scheduled events:** FOMC minutes tone (Nov 18), PCE and GDP (Nov 25), and Anthropic's IPO reception (Nov 18–19).
- **Nvidia news:** Any further revelations or legal action tied to Nvidia's leadership scandal would push the probability down.
- **Near the end:** If SPY gets within about 1% of $781.62 (the old intraday record), watch for breakout momentum.

## 6. Uncertainties
- I could not get actual Nov 18 intraday or opening prices. The direct page fetches were blocked, so the numbers here come from search-result summaries.
- Sources differ on details:
  - VIX close: 23.5 to 26.1.
  - An Investing.com figure of about 7,288 for Nov 17 is probably the intraday low or stale data.
  - SPY's exact intraday all-time high: about $781.62, taken from one TradingNews article whose date I couldn't confirm.
- Details of the Nvidia CEO scandal and the Anthropic IPO date come from secondary summaries and need checking.
- I could not check how closely Pyth's SPY 1-minute highs track the consolidated tape, including whether outlier prints happen.
- The historical frequency of 8%+ gains within 8 sessions is my approximation, not a calculation I ran.

## Sources
- [S&P 500 ETF (SPY) Stock Price – Gotrade](https://www.heygotrade.com/en/us-stock/spy/)
- [The Close: Tuesday, November 17, 2026 – Weekend Spread](https://theweekendspread.substack.com/p/the-close-tuesday-november-17-2026)
- [Dow drops more than 800 points, S&P 500 posts lowest close since July – CNBC](https://www.cnbc.com/2026/11/16/stock-market-today-live-updates.html)
- [Stock futures rise as Nvidia gains on earnings beat and solid outlook – CNBC](https://www.cnbc.com/2026/11/17/stock-market-today-live-updates.html)
- [US Stock Futures Jump After Nvidia Earnings: Markets Wrap – swissinfo](https://www.swissinfo.ch/eng/us-stock-futures-jump-after-nvidia-earnings:-markets-wrap/92397458)
- [S&P 500, Dow, Nasdaq Futures Power Ahead On Nvidia Outlook Beat – TradingView/Stocktwits](https://www.tradingview.com/news/stocktwits:9ee541a45094b:0-s-p-500-dow-nasdaq-futures-power-ahead-on-nvidia-outlook-beat-nvda-tsla-ant-in-focus/)
- [U.S. stock futures jump as Nvidia earnings revive AI optimism – Investing.com](https://ca.investing.com/news/stock-market-news/us-stock-futures-jump-as-nvidia-earnings-revive-ai-optimism-4965395)
- [Wall Street ends sharply lower on AI jitters ahead of Nvidia results, Anthropic IPO – Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/p-500-nasdaq-futures-slide-104351968.html)
- [Stocks tumble on Wall Street as Nvidia leads another sell-off – Yahoo/AP](https://finance.yahoo.com/markets/stocks/articles/stocks-decline-asia-investor-concerns-045636045.html)
- [S&P 500 Hits Lowest Close Since July as Tech Selloff Deepens – HNGN](https://www.hngn.com/articles/273858/20261117/dow-sinks-848-points-tech-selloff-deepens-before-nvidia.htm)
- [Countdown to Nvidia: Stocks Mixed Before Earnings – Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [The Nasdaq-100 Is Down More Than 10% From Its High… – Motley Fool, Nov 17 2026](https://fool.com/investing/2026/11/17/the-nasdaq-100-is-down-more-than-10-from-its-high-but-the-broad-market-is-down-far-less-here-s-how-gaps-like-this-have-ended-since-1986)
- [Stock market news for Nov. 4, 2026 – CNBC](https://www.cnbc.com/2026/11/03/stock-market-today-live-updates.html)
- [Stock market news for Nov. 11, 2026 – CNBC](https://www.cnbc.com/2026/11/10/stock-market-today-live-updates.html)
- [Closing milestones of the S&P 500 – Wikipedia](https://en.wikipedia.org/wiki/Closing_milestones_of_the_S&P_500)
- [S&P 500 (^GSPC) Historical Data – Yahoo Finance](https://finance.yahoo.com/quote/%5EGSPC/history/)
- [SPY 15 Year Stock Price History – Macrotrends](https://www.macrotrends.net/stocks/charts/SPY/state-street-spdr-s-p-500-etf-trust/stock-price-history)
- [SPY ETF Slips 1.2% Below Its $779.09 Record… – TradingNews](https://www.tradingnews.com/news/spy-etf-slips-1-percent-below-its-799-usd-record-as-hot-cpi)
- [CBOE Volatility Index (^VIX) – Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
- [VIX Volatility Index – Macrotrends](https://www.macrotrends.net/2603/vix-volatility-index-historical-chart)
- [Volatility jumps at the front before Nvidia – Saxo Options Brief, 17 Nov 2026](https://www.home.saxo/content/articles/options/volatility-jumps-at-the-front-before-nvidia---options-brief---17-november-2026-17112026)
- [Market Calendar 2026: Fed Meetings, Holidays and Key Events – Admiral Markets](https://admiralmarkets.com/education/articles/general-trading/market-calendar-2026)
- [Economic Calendar Next Week: Nov 23 – Hyperstocks](https://terminal.hyperstocks.io/economic-calendar/next-week)
- [US Economic Calendar November 2026 – Helious](https://helious.io/calendar/2026-11)
- [Weekly Economic Calendar 23.11.2026–29.11.2026 – LiteFinance](https://www.litefinance.org/blog/analysts-opinions/weekly-economic-calendar-for-23112026-29112026/)