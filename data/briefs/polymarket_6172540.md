# Research brief: Will SpaceX (SPCX) trade at or below $115 on Pyth during regular hours by Nov 30, 2026?

## 1. Resolution mechanics
- **What counts as YES:** SPCX has to print a 1-minute candle with a Pyth "Low" at or below $115.00 (no rounding) during regular Nasdaq hours (9:30–16:00 ET). The print has to come after the market was created and within November 2026. Pre-market and after-hours prints don't count.
- **Deadline:** The question closes Dec 1, 2026 04:59:59 UTC, which is the end of Nov 30 ET. From today (Thu Nov 19) that leaves about 6.5 regular sessions:
  - Nov 19 (already partly traded)
  - Nov 20, 23, 24, 25
  - Nov 27 (half day, closes about 1:00 PM ET)
  - Nov 30
  - Thanksgiving, Nov 26, is a market holiday.
- **Who decides:** Pyth's SPCX/USD 1-minute candles. If Pyth data is unavailable, the fallback is the primary exchange's official daily low.
- **Edge cases:**
  - **Market creation date is unknown.** The Nov 5 intraday low of $120.39 didn't reach $115 anyway, so nothing has resolved this yet.
  - **Pyth vs. exchange prints.** Pyth aggregates publisher prices, so a 1-minute Pyth low can differ slightly from the Nasdaq tape. That gives a small extra chance of YES from a brief outlier print.
  - **Splits.** The target adjusts for splits. No split has been announced.
- **Distance to the target:** The last confirmed close was $143.50 on Nov 18 (Gotrade, Nov 18; Google Finance). Midday Nov 19 Yahoo showed about $144.19 with a day range of $141.22–$146.30. Hitting $115 needs a drop of about 20% from $143.50 (ln ratio −0.22).

## 2. Reference classes and base rates
1. **Option-implied barrier probability.**
   - Reported at-the-money implied volatility has come down from 111% at the June IPO to about 54–62% in autumn readings. These include Marketchameleon's Oct-23-expiry snapshot at 62.4% and Tiger notes at 54–57%, with an IV percentile of about 75% (OptionStrat; Marketchameleon; itiger, dates unclear).
   - I approximated the touch probability as twice the chance of finishing below $115, using about 6.5 sessions.
   - At σ = 60%: z ≈ 2.3, giving about 2%.
   - At σ = 80%: z ≈ 1.7, giving about 8%.
   - Fat tails, like the −9% day on Nov 5, push the real chance above the lognormal estimate.
2. **SPCX's own November realized volatility.** Daily closes this month:
   - Nov 4: −3.8% (to $135.92)
   - Nov 5: −9.05% (to $123.62)
   - Nov 6: +8.6% (to $134.27)
   - Then +5.8% (to $142.07 on Nov 9)
   - Nov 11: −2.3% (to $139.75)
   - Nov 13: −0.6% (to $139.11)
   - Nov 16: −1.3% (to $137.36)
   - Nov 17: +3.2% (to $141.70)
   - Nov 18: +1.3% (to $143.50)

   (MarketBeat/Quantral/Gotrade, Nov 2026). Realized volatility works out to roughly 4–5% a day, or about 65–80% annualized.

   The worst short-window drop this month ran from about $141 (Nov 3 close, implied) to the $120.39 intraday low on Nov 5. That's about −15% in two sessions, during a 5% QQQ selloff, and it still didn't reach a −20% equivalent.
3. **SPCX history since the June 2026 IPO** (about 110 sessions).
   - Moves of 20% or more within about 7 sessions have happened, mainly in the June–early August slide. The stock went from the $225.64 all-time high (Jun 16) to about −50% by late July. The all-time low was $104.83 on Aug 3, and Aug 6 saw single-day drops of 11–13.6% on AI capex fears and a lockup (Wikipedia; TradingView; Sentisense, Aug 2026).
   - Since mid-August, no 7-session window clearly shows a drop of 20% or more. October fell about 9% over the whole month, despite large unlocks on Oct 22 (1.3B shares) and Oct 24 (328M) (Yahoo Finance).
   - A rough estimate: 7-session ≥20% drawdowns showed up in under 10% of windows overall, and close to 0% after August. I couldn't count this exactly.

## 3. Current state of the world (most recent first)
- **Nov 19:** Trading around $144, intraday range $141.22–$146.30 (Yahoo Finance, midday Nov 19). Market cap is about $1.95T. The 52-week range is $104.83–$225.64. The IPO price was $135 (Jun 11/12).
- **Nov 18:** Closed at $143.50, up 1.27% (Gotrade, Nov 18). Motley Fool reported that SpaceX is now Nvidia's largest stock holding (Fool, Nov 18).
- **Nov 17:** Up 3.2% to $141.70 after the CFO talked about AI infrastructure plans, citing Q3 AI revenue up 830% (FX Leaders, Nov 18; Gotrade).
- **Nov 13–14:** Starship Flight 15 flew. The ship was caught by the tower for the first time. The booster catch was aborted and the booster crashed into the Gulf. 26 Starlink V3 satellites were deployed (Space.com; CBS, Nov 2026). The stock barely moved: $139.11 on Nov 13, $137.36 on Nov 16.
- **Nov 12:** Bloomberg reported that SpaceX–Tesla merger talks are advancing, with a possible announcement as soon as December, or the deal could slip into 2027. The combined value is about $3.4T. Neither company has confirmed. Tesla's Dec 3 meeting doesn't include a merger vote (Electrek, Nov 12; 247WallSt, Nov 13).
- **Nov 4–5:** After the midterms, SPCX fell 3.8% and then 9.05%, with a $120.39 intraday low on Nov 5. That was the lowest close since early August. The causes were Democratic regulatory worries plus an AI and chip selloff (QQQ −5%). TIKR adds that SpaceX spent $48.1B on capex in the first nine months of 2026 and guided another $35–40B for Q4 (Gotrade, Nov 6; TIKR; Kalkine).
- **October:** The stock fell about 9% on lockup expirations despite strong Q3 results (Yahoo Finance).
- **Scheduled before Nov 30:**
  - Thanksgiving holiday Nov 26 and a half session Nov 27, so thin liquidity.
  - Possible pre-positioning ahead of the **Dec 8 lockup** (about 798M shares, roughly 5.9% of shares outstanding), which falls after the window.
  - Possible merger headlines.
  - General AI and tech macro news. I couldn't confirm this quarter's Nvidia earnings date.

## 4. Drivers and scenarios
**Paths to YES (≥20% fall in about 6.5 sessions):**
1. A sharp AI/tech selloff like the Nov 5 one, but bigger or lasting several days. SPCX trades with a high beta to the AI complex.
2. Merger terms seen as bad for SPCX holders, such as an unfavorable exchange ratio or SpaceX taking on Tesla's problems. A failed or delayed deal is also possible, though the stock hasn't priced in much merger premium.
3. Heavy selling by early holders ahead of the Dec 8 unlock. This was cited as a factor on Nov 5.
4. A company-specific shock: a regulatory or political action after the midterms, a capex or guidance shock, or a Musk-related event.
5. A Pyth outlier print during a fast drop.

**Paths to NO:**
- The stock is in a recovery trend: up about 19% from the Nov 5 low, back above the $135 IPO price, and above roughly $140 support.
- The holiday-shortened week usually has lower volatility.
- There's no known binary company catalyst inside the window.
- Even the worst recent shock bottomed about $5 above the target.

## 5. Signposts
- **Toward YES:**
  - SPCX breaking back below $135 (the IPO price) and then $130 early next week.
  - QQQ or semiconductor stocks dropping more than 3% in a day.
  - Merger terms showing SpaceX paying a premium or taking on Tesla's liabilities.
  - New regulatory action.
  - Reports of large block sales or early lockup waivers.
  - Implied volatility rising back above 80%.
- **Toward NO:**
  - Holding above $140 through Nov 24–25.
  - Positive merger framing.
  - Implied volatility falling to the low 50s.
  - Each quiet session cuts the remaining time, so the probability falls roughly with √T.

## 6. Uncertainties
- I couldn't get current SPCX implied volatility for late-November expiries. The readings I found are of uncertain date, from 54% to 62%.
- I don't know when this market was created. I also don't know whether Pyth's 1-minute lows tend to undercut exchange lows for SPCX.
- I don't know the exact date of Nvidia's earnings or other macro events in the window.
- Some daily prices come from aggregator snippets (MarketBeat, Gotrade, Quantral) that sometimes disagree. WebFetch was blocked, so I couldn't read the full pages and check them.
- I don't know whether any early lockup releases or block trades are planned before Dec 8.

## Sources
- [SpaceX (SPCX) Stock price – Yahoo Finance](https://nz.finance.yahoo.com/quote/SPCX/)
- [Space Exploration Technologies Corp (SPCX) – Google Finance](https://www.google.com/finance/quote/SPCX:NASDAQ)
- [SpaceX Stock Price, Chart & IPO Details — TradingView](https://www.tradingview.com/symbols/NASDAQ-SPCX/)
- [SpaceX (SPCX) Stock Chart and Price History – MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/SPCX/chart/)
- [SpaceX Stock (SPCX) Rises 1.3% to $143.50 (Nov 18) – Gotrade](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-19-2026/)
- [SpaceX Stock (SPCX) Falls 1.3% as Tech Stocks Slide (Nov 16) – Gotrade](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-17-2026/)
- [SpaceX Stock (SPCX) Falls 0.6% to $139.11 (Nov 13) – Gotrade](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-16-2026/)
- [SpaceX Stock (SPCX) Falls 9.0% on Midterm Regulation Worries (Nov 5) – Gotrade](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-6-2026/)
- [SpaceX Stock (SPCX) Falls 2.3% Ahead of Starship Test Flight – Gotrade](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-12-2026/)
- [SpaceX Sinks 9% as AI Stocks Crater – TIKR](https://www.tikr.com/blog/spacex-sinks-9-as-ai-stocks-crater-absolute-slaughter)
- [What is pulling SpaceX down – Kalkine](https://kalkine.ca/news/industrials/what-is-pulling-spacex-nasdaqspcx-down-905-nearly-30-below-its-october-high)
- [SpaceX (SPCX) IPO date, lockup ends Dec 8 – Quantral](https://quantral.com/blog/spacex-ipo)
- [SpaceX Stock Fell to Its Lowest Level Since August After the Midterms – Motley Fool](https://www.fool.com/investing/2026/11/09/spacex-stock-fell-to-its-lowest-level-since-august/)
- [SpaceX's December Lock-Up Frees Another 17% of Its Shares – Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/spacex-december-lock-frees-another-025502691.html)
- [Will 798 Million Unlocked SpaceX Shares on December 8 Swamp Starship's Catch? – Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/798-million-unlocked-spacex-shares-183845254.html)
- [SpaceX stock slides back toward $140 – Yahoo Finance](https://finance.yahoo.com/markets/article/spacex-stock-is-testing-a-key-floor-level-after-surviving-its-biggest-share-lockup-expiration-170905606.html)
- [SpaceX New Low at $104.83 – IPO Bonanza](https://www.ipobonanza.com/news/2026-08-04-spcx-all-time-low-reversal)
- [$1,000 invested in SpaceX stock at all-time low – Finbold](https://finbold.com/1000-invested-in-spacex-stock-at-all-time-low-is-now-worth/)
- [SpaceX Shares Plunge 13.6% on AI Capex Surge and Lockup – Sentisense](https://app.sentisense.ai/stories/spacex-shares-plunge-13.6-percent-on-ai-capex-surge-and-lockup-08062026)
- [Initial public offering of SpaceX – Wikipedia](https://en.wikipedia.org/wiki/Initial_public_offering_of_SpaceX)
- [SpaceX Options May Not Follow the Standard IPO Playbook – OptionStrat](https://optionstrat.com/blog/spacex-options-may-not-follow-the-standard-ipo-playbook)
- [When the chain opens: trading options on SPCX – Saxo](https://www.home.saxo/content/articles/options/when-the-chain-opens-trading-options-on-the-fresh-spacex-spcx-listing-17062026)
- [SPCX Option Chain – Marketchameleon](https://marketchameleon.com/Overview/SPCX/OptionChain)
- [SpaceX launches Starship Flight 15, aborts booster catch – Space.com](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship)
- [SpaceX catches Starship after orbit in historic first – CBS Austin](https://cbsaustin.com/news/nation-world/spacex-catches-starship-after-orbit-in-historic-first-as-booster-explodes-over-gulf)
- [SpaceX Tesla merger announcement December report – Electrek](https://electrek.co/2026/11/12/spacex-tesla-merger-announcement-december-report/)
- [Tesla and SpaceX Could Announce a Merger as Soon as December – 24/7 Wall St](https://247wallst.com/investing/2026/11/13/tesla-and-spacex-could-announce-a-merger-as-soon-as-december/)
- [SpaceX Stock Rises 3.16% as AI Revenue Surges – FX Leaders](https://www.fxleaders.com/news/2026/11/18/spacex-stock-ai-revenue-q3-earnings-starship-flight-15/)
- [SpaceX Is Now Nvidia's Biggest Stock Holding – Motley Fool](https://www.fool.com/investing/2026/11/18/spacex-is-now-nvidia-s-biggest-stock-holding-ahead-of-intel-here-s-what-that-says-about-spacex/)