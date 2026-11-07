# Research brief: Will BTC's trimmed mean go above $85,000 by 11:59 PM ET on Nov 30, 2026?

*Prepared Nov 7, 2026. No prediction-market or betting prices were looked up or used.*

**Bottom line:** BTC is at about $75.8k, so YES needs a rise of about 12% to a minute-level print above $85,000 within about 23.5 days. A standard volatility model puts that at roughly 23–33% before adjusting for the bearish trend and macro backdrop.

---

## 1. Resolution mechanics

- **Market:** Kalshi KXBTCMAXMON-BTC-26NOV30-8500000 ("How high will BTC get in November?"). It opened 2026-11-01T04:10Z (00:10 ET Nov 1). It closes 2026-12-01T04:59:59Z (11:59:59 PM ET Nov 30), or earlier if the threshold is hit. The early-close condition reads: "close and expire early if the price criterion is met" (Kalshi API, event KXBTCMAXMON-BTC-26NOV30, retrieved Nov 7, 2026).
- **YES condition:** At any minute in the period, the "trimmed mean" of CF Benchmarks' BRTI price must be above $85,000.00. The trimmed mean drops the top and bottom 20% of values before averaging. Kalshi decides, using CF Benchmarks data.
- **The rule wording is ambiguous, but actual settlements show how it works.** The rules mention removing the top and bottom 20% "of the cumulative dataset." Read literally, that is an average of every minute since Nov 1, which would move slowly. Kalshi's own settlements show it behaves almost like spot price, probably a trimmed average over roughly one minute of BRTI values:
  - **Nov 2026 $80k strike:** resolved YES on Nov 4 at 15:34 UTC, with expiration value $80,047.53. BTC had spent Nov 1–3 around $77k–78k. A cumulative average since Nov 1 could not have reached $80k by Nov 4.
  - **Oct 2026 $85k strike:** resolved YES on Oct 1 at 18:51 UTC (value $85,023.11), less than 15 hours after opening. The month opened at about $83.5k.
  - **Oct 2026 $87.5k strike:** resolved NO, even though Coinbase recorded an intraday high of $87,249 on Oct 2. That is consistent with a near-spot measure that just missed.

  **Practical reading:** BTC must trade above $85,000 on BRTI for roughly a minute, not just a single-tick wick. A brief spike can be filtered out; a sustained minute above $85k will count.
- **Edge cases:**
  - If CF Benchmarks data is "unavailable or incomplete at the expiration time," affected strikes resolve NO.
  - CF values can be revised after the fact.
  - The window ends at 11:59 PM ET Nov 30, not at UTC month-end.

## 2. Reference classes and base rates

**A. Volatility (driftless "touch") model.** This estimates the chance that the highest price over about 23.5 days reaches at least $85k from $76k (+11.8%, or 0.112 in log terms). The formula is P ≈ 2·(1−Φ(z)).

| Annualized volatility | z | P(touch) |
|---|---|---|
| 37% (DVOL low after the midterms) | 1.19 | ~23% |
| 40% (DVOL Nov 4) | 1.10 | ~27% |
| 45% (2025 average DVOL) | 0.98 | ~33% |
| 50% | 0.88 | ~38% |

DVOL was 39.6 on Nov 4 and fell to 37.0 after the midterms. Its 2026 average is 42.4, the lowest on record (Crypto Briefing, early Nov 2026). Implied volatility probably rose after the Nov 5 crash, but I found no reading after Nov 5. Realized volatility usually runs slightly below implied, and the minute-averaging rule removes very short spikes. Both would trim the model figures a little.

**B. Empirical "+12% within about 3.5 weeks" frequency for BTC.** This is my approximation, not computed from data. Across 2014–2025, BTC's highest price over the next ~24 days exceeded the starting price by 12% or more on very roughly 30–35% of days. In low-volatility or bear-trend regimes like 2026 it is more like 15–25%.

**C. Kalshi's own monthly "max" ladders in 2026.**
- October 2026: the strike about 2% above the opening price hit on day 1. The strike +4.7% above the open never hit. The month's total range was about $76k–$87k, roughly ±7% around the open (Simple Mining; The Markets Unplugged, Oct 2026 recaps).
- November seasonality: November was up in 8 of the last 12 years (Coinglass via CoinCentral). The median November return is about +10%, but that is skewed by bull years such as 2013, 2017 and 2020.

## 3. Current state of the world (most recent first)

- **Nov 7 (Sat):** BTC is about $75.8k, testing support at about $75.5k–75.8k.
  - **Moving averages:** the 20-day is about $79.7k and the 50-day about $82.0k, both overhead. The 200-day is about $73.2k.
  - **Resistance:** about $79.3k, then about $82.8k.
  - **Support:** about $73.7k, then $71.65k. A weekly close below $75.5k could lead to targets as low as $57.8k (Interactive Crypto, Nov 7; Blockchain.News, Nov 6; CryptoNews, Nov 6–7).
- **Nov 6:**
  - **Jobs report:** October payrolls came in hot at +165k against forecasts of roughly 59–131k, with unemployment at 4.1%.
  - **Fed:** futures priced about 80% odds of a 25 bp rate *hike* in December, up from 75% (Reuters via CoinMarketCap Academy and CoinDesk, Nov 6).
  - **BTC vs stocks:** the Nasdaq 100 rebounded about 2%, but BTC stayed near $75.5k–76k.
  - **ETFs:** spot BTC ETF outflows of about $430M (Fortune/Tech-Insider, Nov 6).
- **Nov 5 (Thu):** An AI- and chip-led Nasdaq selloff pushed BTC down about 6%, from an intraday peak of $80,721 to about $75.4k. More than $1–1.25B of crypto positions were liquidated, mostly longs (CoinDesk, Nov 6; CryptoTimes, Nov 6; Coinbase price page).
- **Nov 4:** BTC rose above $80k; the Kalshi $80k strike settled at $80,047.53 at 15:34 UTC.
- **Nov 2–3:** BTC was about $77.75k on Nov 2 and $77.0k on Nov 3, about 9% below a month earlier and about 28% below a year earlier (Fortune, Nov 3–4). U.S. midterm elections were held around Nov 3.
- **October 2026:**
  - **Price:** BTC fell 7.3%, from $83.6k to $77.4k. The high was $87.2k (Oct 2); the low was about $77.2k on Oct 30.
  - **Flows and liquidations:** ETF net outflow of about $515M, the first outflow month since June. October liquidations totalled $12.5B (Simple Mining; Crypto Briefing).
- **2026 context:**
  - The all-time high was about $126k (Oct 6, 2025). The 2026 low was about $58.5k (Jun 30), roughly a 52% drawdown (Datawallet/Cointelegraph).
  - BTC was about $85.3k in late September. It is now about 40% below the all-time high.
- **Scheduled events before Nov 30:**
  - Oct CPI on **Nov 10, 8:30 ET** (September CPI was 3.7% y/y against 3.6% expected).
  - AI/chip earnings in mid-to-late November (exact dates not confirmed).
  - The Thanksgiving week (Nov 26) is typically thin trading.
  - The December FOMC (about Dec 8–9) and Nov CPI (Dec 10) fall *after* the close, but expectations around them will move prices in November.

## 4. Drivers and scenarios

**Paths to YES (BTC above $85k for about a minute by Nov 30):**
- A relief rally after the liquidation flush (leverage was reset on Nov 5). BTC would need to reclaim the 20-day and 50-day averages at about $80k–82k, then push about 3–4% higher.
- A soft Oct CPI on Nov 10, which would cut the odds of a Fed hike.
- A rebound in AI and tech stocks, with BTC catching up after lagging.
- ETF inflows resuming.
- Note: $85k was the level as recently as late September and early October, so it is not an extreme level for the past 2–3 months.

**Paths to NO:**
- The bearish structure continues: lower highs since early October, BTC below its short- and medium-term averages, ETF outflows, and BTC lagging equities.
- A hot CPI strengthens the case for a December hike.
- A break below $75.5k could lead toward $73k, $68k or lower, after which $85k would need a 15–25% rally.
- Implied volatility near record lows means options traders expect smaller moves than history suggests.

## 5. Signposts

- **Toward YES:**
  - A daily close above about $80k–82k, i.e. back above the 20-day and 50-day averages. That would roughly halve the distance needed.
  - A soft CPI on Nov 10.
  - Several days of ETF inflows.
  - A spike in DVOL with upside skew.
  - A reclaim of $82.8k resistance. From there a touch of $85k becomes roughly a coin flip or better.
- **Toward NO:**
  - A weekly close below $75.5k, or a break of $73k.
  - Continued ETF outflows.
  - Hot CPI or Fed hike odds above 90%.
  - Another AI-led equity selloff.
- **Timing:** each week without a rally takes away about 20% of the remaining window. By Nov 20, with BTC still near $76k, the model probability falls to roughly 10–15%.

## 6. Uncertainties

- **Calculation method:** the exact trimmed-mean computation is unclear, because the rules text conflicts with observed behaviour. The settlement evidence strongly supports a near-spot, roughly one-minute trimmed average. A cumulative average would make YES nearly impossible, so this is the key structural assumption.
- **Live data:** I have no BTC price or implied-volatility reading after Nov 5–7. Volatility probably rose after the crash, which would push the model figure toward 30% or above.
- **Base rate B:** the historical figure is approximate, not computed from a dataset.
- **Calendar gaps:** I did not confirm the exact date of Nvidia earnings, the official December FOMC date, or the 2026 rate-hike path (the Fed shifting to hikes is unusual and from secondary sources).
- **Source spread:** sources disagree on intraday highs and lows by a few hundred dollars (Coinbase vs. CoinMarketCap vs. BRTI).

## Sources
- [Kalshi API – event KXBTCMAXMON-BTC-26NOV30 (rules, open/close times)](https://api.elections.kalshi.com/trade-api/v2/events/KXBTCMAXMON-BTC-26NOV30)
- [Kalshi API – market KXBTCMAXMON-BTC-26NOV30-8000000 (settlement value)](https://api.elections.kalshi.com/trade-api/v2/markets/KXBTCMAXMON-BTC-26NOV30-8000000)
- [Kalshi API – event KXBTCMAXMON-BTC-26OCT31 (October settlements)](https://api.elections.kalshi.com/trade-api/v2/events/KXBTCMAXMON-BTC-26OCT31)
- [Kalshi Help – Market rules](https://help.kalshi.com/en/articles/13823838-market-rules)
- [CF Benchmarks – Kalshi crypto event contracts](https://www.cfbenchmarks.com/blog/kalshi-leads-surging-crypto-event-contract-market-powered-by-cf-benchmarks)
- [Fortune – Price of Bitcoin Nov 6, 2026](https://fortune.com/article/price-of-bitcoin-11-06-2026/)
- [Fortune – Price of Bitcoin Nov 3, 2026](https://fortune.com/article/price-of-bitcoin-11-03-2026/)
- [Fortune – Price of Bitcoin Nov 4, 2026](https://fortune.com/article/price-of-bitcoin-11-04-2026/)
- [Tech-Insider – Bitcoin price today Nov 6, 2026](https://tech-insider.org/bitcoin-price-today-november-6-2026-76023-87-after-5-1-percent-drop/)
- [CryptoTimes – BTC slides to $75.6K (Nov 6, 2026)](https://www.cryptotimes.io/2026/11/06/bitcoin-price-today-btc-slides-to-75-6k-as-crypto-liquidations-top-1-25b-after-nasdaq-rout/)
- [CryptoTicker – Bitcoin price ahead of US jobs report](https://cryptoticker.io/en/bitcoin-price-jobs-report-100-day-line)
- [CoinDesk – Bitcoin steadies near $76,000 (Nov 6, 2026)](https://www.coindesk.com/markets/2026/11/06/bitcoin-steadies-near-usd76-000-after-ai-led-selloff)
- [CoinMarketCap Academy – Bitcoin lags Nasdaq rebound as hot jobs data lifts Fed hike bets](https://coinmarketcap.com/academy/article/bitcoin-lags-nasdaq-rebound-jobs-fed-hike-bets)
- [Coinbase – Bitcoin price page](https://www.coinbase.com/price/bitcoin)
- [Interactive Crypto – Bitcoin's $75,775 support under pressure](https://interactivecrypto.com/bitcoin-s-75-775-support-under-pressure-can-bulls-reverse-the-slide)
- [Blockchain.News – BTC loses short-term trend support (Nov 6, 2026)](https://blockchain.news/news/20261106-price-prediction-btc-bitcoin-loses-short-term-trend-support)
- [CryptoNews – Weekly breakdown targets $57,800](https://cryptonews.net/news/bitcoin/33713996/)
- [Simple Mining – Bitcoin market report October 2026](https://www.simplemining.io/insights/post/bitcoin-market-report-october-2026)
- [The Markets Unplugged – October 2026](https://www.themarketsunplugged.com/the-month-unplugged-october-2026/)
- [Crypto Briefing – October 2026 liquidations](https://cryptobriefing.com/crypto-liquidations-october-2026-longs/)
- [Crypto Briefing – Bitcoin options calmest year (DVOL)](https://cryptobriefing.com/bitcoin-options-calmest-year-deribit-dvol/)
- [BLS – CPI release schedule](https://www.bls.gov/schedule/news_release/cpi.htm?mod=article_inline)
- [Datawallet – Bitcoin statistics 2026](https://www.datawallet.com/crypto/bitcoin-statistics)
- [Cointelegraph – Bitcoin drawdown less dramatic this cycle](https://cointelegraph.com/news/bitcoin-drawdown-much-less-dramatic-this-cycle-fidelity)
- [Axel Adler Jr – Bitcoin monthly returns](https://axeladlerjr.com/charts/bitcoin-monthly-returns/)
- [Pluang – Bitcoin November average return 2010–2025](https://pluang.com/en/news-feed/rata-rata-pengembalian-bitcoin-november-2010-2025-34-persen)