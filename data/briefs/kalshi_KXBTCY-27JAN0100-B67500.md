# Research Brief: BTC price at 12 AM EST on Jan 1, 2027 — will it be in the $65,000.00–$69,999.99 bucket?

## 1. Resolution mechanics

- **What counts:** The market uses CF Benchmarks' Bitcoin Real Time Index (BRTI). It takes the 60 one-second BRTI prints in the last minute before 12:00 AM EST on Jan 1, 2027, and averages them. The resolution moment is 05:00:00 UTC on Jan 1, 2027, which matches the close date of 2027-01-01T05:00Z. In practice the window runs from about 04:59:00 to 04:59:59 UTC.
- **What makes YES:** That average must be between $65,000.00 and $69,999.99. An average of exactly $70,000.00 falls in the next bucket up, and anything below $65,000.00 falls in the bucket below.
- **Who decides:** The exchange running the market, using CF Benchmarks data. Coinbase, Google and other quotes are only a guide. BRTI is built from several exchanges' order books, so it can differ from any single exchange by a few dollars to tens of dollars. That only matters if the price ends right at $65,000 or $70,000.
- **Edge cases:**
  - Liquidity is thin over New Year's Eve, and a sharp move in the final minute is mostly smoothed out by the 60-second average.
  - If BRTI is disrupted, the market's fallback rules apply. I did not find them in the text provided.
  - The bucket covers roughly 7.4% of the current price, and its lower edge sits just above where BTC trades now.

## 2. Reference classes and base rates

**A. Options-implied (lognormal) model.** This is my own calculation, not a published figure.
- Inputs: spot about $64,500 on Nov 18, 2026, and about 44 days to resolution (T ≈ 0.12 years).
- To land in the bucket, BTC needs a log return between +0.8% and +8.2%. With the usual small downward adjustment to the median (−σ²/2):

| Annualized vol | Probability of landing in $65k–$70k |
|---|---|
| 40% (about current DVOL) | ≈ 19.5% |
| 50% | ≈ 16% |
| 60% (closer to the long-run BTC average) | ≈ 13.5% |

- For context, Deribit's DVOL was 40.8 on Nov 13 and had a 2026 low of about 37 after the midterms. 30-day implied vol was 39.6% on Nov 6 (CryptoBriefing / Coinotag / OptionCharts, Nov 2026).
- Fat tails, if anything, put more probability near the current price. Since the bucket sits right next to spot, that slightly helps it.
- **Sensitivity to spot:** If spot is around $67,500 when the forecast is made (the middle of the bucket), the 45% vol figure rises to about 22%. If spot is around $61,000, it falls to about 12%.

**B. Historical "Nov 18 → Jan 1" BTC moves, 2014–2025.** These are approximate prices from my memory, not looked up for this brief; they need checking.
- Moves: 2014 ≈ −18%, 2015 ≈ +28%, 2016 ≈ +33%, 2017 ≈ +70%, 2018 ≈ −32%, 2019 ≈ −12%, 2020 ≈ +60%, 2021 ≈ −18%, 2022 (after FTX) ≈ −1%, 2023 ≈ +16%, 2024 ≈ +4%, 2025 ≈ −5% (2025 close $87,498 per bitcoin.com / coinotag reporting).
- Only 2024 (about 1 of 12 years, roughly 8%) landed in a window of +1% to +8.5%.
- The other years scatter widely: same-period moves have historically been much wider than the current low implied vol suggests. The 2022 case is the closest regime match (a post-shock bear market with low vol), and it ended flat, just below the matching window.

**C. December seasonality after a down November.**
- Since 2013, December has averaged about +4.8%, but the median is −3.2%. Through 2024, December was up in only 5 of 12 years.
- "In every year since 2013, a red November was followed by a red December" (Investing.com / Motley Fool, Nov–Dec 2025). The sample is small.
- November 2026 is currently down about 17% (Oct close $77,424 → about $64,500). By this pattern, the next six weeks lean flat to down, which favors the bucket just below this one. Treat this as weak evidence.

## 3. Current state of the world (most recent first)

- **Nov 18, 2026:**
  - BTC is about $64,300–$64,900. CoinGecko showed about $64,932 (+1.3% in 24 hours, −12.5% on the week).
  - It is struggling to get back above $65,000, with support cited at $64,000 and $63,600.
  - The Fear & Greed Index reads 12 (Extreme Fear) (Finwire; KuCoin; CoinLore; Sunday Guardian, Nov 18, 2026).
- **Nov 17:** BTC was about $65,017 at 8:15 a.m. ET (Fortune) and about $63,496 at 11:56 a.m. ET (CoinDesk), in quiet trading near $64,800 (CryptoTimes, Nov 17).
- **Nov 14–15:**
  - BTC hit a three-month low of about $62,000–$62,112, down as much as 23% from early-November levels.
  - The drop came with roughly $0.75–2B of liquidations, about 80% of them longs (KuCoin; Bitbase; CryptoBriefing, mid-Nov 2026).
  - BTC was about $71,300 on Nov 12 (Aktualita).
- **Nov 13:** DVOL was 40.8 even though BTC was about 17% below its October high. Options are pricing much less fear than the spot drop would suggest (Coinotag/CryptoQuant, Nov 13).
- **Nov 5–13:** US spot BTC ETFs had seven straight sessions of net outflows totaling about $1.91B, after about $520M of outflows in October (CryptoLinks, Nov 2026).
- **Macro drivers cited:** a stronger dollar, expectations of a December Fed rate hike, and, in one unconfirmed source, an MSCI decision to drop bitcoin treasury companies such as Strategy from its indexes.
- **Oct 29–Nov 1:** A Binance hot-wallet hack took about $6.3B. Binance says it is covering the losses from SAFU and company funds, and withdrawals were restored in phases from Nov 1. TRM Labs attributes the hack to North Korea's TraderTraitor group (Cointelegraph; Tangem; BleepingComputer, Oct–Nov 2026).
- **October 2026:** BTC opened at $83,556, hit a high of $87,249 on Oct 2, and closed at $77,424 (−7.3%). It was the weakest October in about a decade (bitcoin.com / BGeometrics, Nov 1, 2026). The all-time high is about $126k (October 2025), so BTC is now about 48% below it.
- **Fed:**
  - On Sept 16, 2026, the Fed under Chair Kevin Warsh raised rates 25bp to 3.75–4.00%, its first hike since 2023. Twelve of 18 officials projected another hike in 2026 (Axios; Fox Business; Reuters via Dairy Herd, Sept 16, 2026).
  - The Fed held in October, with two dissents in favor of a hike.
  - One unconfirmed source says markets price about 88% odds of a December hike (InvestingLive).
  - Inflation has been pushed up by an energy shock tied to the Iran war.
- **Options positioning:**
  - The largest Deribit open-interest position is the Dec 25, 2026 $120k call (about 7.5k BTC), a stale bullish bet.
  - The Dec 25, 2026 $60k put holds about 6.2k BTC of open interest.
  - Max pain for the December expiry was cited at about $75k.
  - Total options open interest has fallen to about $35B from more than $65B in October.
  - The capture date of these figures is unclear (news.bitcoin.com / GNcrypto).

**Scheduled events before close:**

| Date | Event |
|---|---|
| Nov 27 | Deribit monthly options expiry |
| Dec 9, 2:00 pm ET | FOMC decision, with new projections (dot plot) and press conference (meeting Dec 8–9) |
| Dec 10 | November CPI |
| Dec 15 | November PPI |
| Dec 25 | Deribit quarterly/year-end expiry (large open interest) |
| Late Dec | Year-end tax-loss selling and fund rebalancing; thin holiday liquidity |

The early-December jobs report date was not confirmed.

## 4. Drivers and scenarios

**Paths to YES** (BTC recovers about 1–8% and settles in $65k–$70k):
- The market stays rangebound and slowly mean-reverts after the capitulation. Extreme Fear readings and liquidated longs often come before relief rallies, and the 2022 analog went sideways for six weeks.
- ETF outflows slow or reverse.
- A December hike is already priced in, so a "hike and done" signal could produce a relief bid.
- An oversold bounce toward the $70k resistance (the Nov 12 level) fades somewhat but holds above $65k.

**Paths to NO, downside** (below $65k; probably the bigger mass):
- Momentum and the red-November → red-December pattern continue.
- Persistent ETF outflows, a hawkish Fed dot plot, or hot CPI.
- A break below $62k could target $60k, where puts are concentrated, and then the $50s.
- Year-end tax-loss selling.
- Further fallout from the Binance hack or the treasury-company/MSCI story, such as forced selling by leveraged BTC holders.

**Paths to NO, upside** (≥ $70,000):
- A sharp short squeeze or a dovish surprise, such as the Fed skipping the hike.
- A rebound in risk assets (an "AI stock rebound" was noted on Nov 18).
- Renewed ETF inflows. A rally of 9% or more in six weeks is common for BTC.

## 5. Signposts

- **Spot price over the coming days:**
  - Holding $64–65k and reclaiming $67–68k moves the bucket toward the center of the distribution (probability up).
  - A daily close below $62k (the November low) shifts the distribution down (probability falls to the low teens or lower).
  - A fast rally through $70k lowers it.
- **ETF flow data (Farside):** a turn to inflows is bullish, so watch for overshoot above $70k. Continued outflows of more than $200M a day are bearish.
- **FOMC Dec 9 and CPI Dec 10:** A hike with a "done" signal favors stabilization. A hawkish dot plot or hot CPI favors a drop below $65k.
- **DVOL:** Implied vol is about 40 now. A rise to 55–60 widens the distribution and lowers the probability for any single bucket. Continued compression helps the bucket next to spot.
- **Late-December spot:** Inside the last week, spot location dominates everything else. Holiday volatility is typically lower.

## 6. Uncertainties

- Exact BRTI level on Nov 18. Sources range from $63.9k to $65.0k, which matters because the bucket's lower edge is $65,000.
- Current DVOL, realized vol and skew after Nov 15. A CryptoQuant note gives 30-day realized vol of about 21% against about 37% implied, but its date is unconfirmed.
- Whether the December hike is fully priced. The roughly 88% figure comes from a single unverified source.
- Whether the MSCI delisting of treasury companies is real and when it takes effect. Only one source mentions it.
- The historical Nov 18 → Jan 1 returns in section 2B are from memory and approximate.
- The market's fallback rules if BRTI is unavailable.

## Sources
- [Current price of Bitcoin for November 17, 2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-17-2026/)
- [Bitcoin price today (CoinDesk)](https://www.coindesk.com/price/bitcoin)
- [Bitcoin Price Today: Market Holds Steady Near $64,800 (CryptoTimes)](https://www.cryptotimes.io/2026/11/17/bitcoin-price-today-market-holds-steady-near-64800-on-unusually-quiet-monday/)
- [Bitcoin Today, November 18, 2026 (Aktualita)](https://aktualita.co/en/economy/bitcoin-today-november-18-2026-still-under-pressure-price-at-rp118-billion-as-investors-brace-for-further-declines)
- [Bitcoin price stuck below $65,000 (Finwire)](https://finwire.io/news/crypto-news/bitcoin-price-stuck-below-65000-as-etf-outflows-and-bearish-signals-persist)
- [BTC Consolidates at $64K Amid AI Stock Rebound (KuCoin)](https://www.kucoin.com/news/articles/123457)
- [Bitcoin price (CoinGecko)](https://www.coingecko.com/en/coins/bitcoin)
- [Bitcoin forecast / Fear & Greed (CoinLore)](https://www.coinlore.com/coin/bitcoin/forecast/price-prediction)
- [Bitcoin slides as much as 23% in November 2026 (CryptoBriefing)](https://cryptobriefing.com/bitcoin-falls-23-november-2026-bear-market/)
- [Why Is Bitcoin Crashing in November 2026? (KuCoin)](https://www.kucoin.com/blog/why-is-bitcoin-price-crashing-in-november-2026)
- [Bitcoin Falls to Three-Month Low (Bitbase)](https://www.bitbase.com/news/bitcoin-price-falls-62000-etf-outflows-liquidations)
- [Bitcoin Slips Below $66K as ETF Outflows Hit $1.91B (CryptoLinks)](https://cryptolinks.com/news/bitcoin-etf-outflows-seven-sessions-november-2026)
- [Bitcoin options calmest year — Deribit DVOL (CryptoBriefing)](https://cryptobriefing.com/bitcoin-options-calmest-year-deribit-dvol/)
- [BTC options volatility DVOL 40.8 (Coinotag)](https://en.coinotag.com/bitcoin-btc-options-volatility-dvol-40-8-half-norm-drawdown)
- [BTC Volatility Skew (OptionCharts)](https://optioncharts.io/options/BTC/volatility-skew)
- [CryptoQuant quicktake: options implied vs realized](https://cryptoquant.com/insights/quicktake/6ae935c44d08081b8394da24-Bitcoin-Options-Charge-368-Volatility-for-214-Delivered-Realized-Caught-Up-1-in-)
- [Bitcoin's Uptober goes bust (bitcoin.com)](https://news.bitcoin.com/market-updates/bitcoins-uptober-goes-bust-with-worst-october-finish-since-2014/)
- [Bitcoin Monthly Report Oct 2026 (BGeometrics)](https://bgeometrics.com/reports/monthly/2026-10.html)
- [Recap: Binance's record $6.3B hack (Cointelegraph)](https://cointelegraph.com/news/recap-binances-record-63b-hack-unfolded?rand=50490)
- [Binance Hack 2026 (Tangem)](https://tangem.com/en/blog/post/binance-hack-2026-how-it-happened/)
- [Fed raises rates a quarter point in first move of Warsh era (Axios)](https://www.axios.com/2026/09/16/fed-rates-warsh-trump)
- [Federal Reserve hikes rates for first time since 2023 (Fox Business)](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-september-16-2026)
- [Fed Hikes Rates, Sees More Tightening Ahead (Dairy Herd/Reuters)](https://www.dairyherd.com/news/fed-hikes-rates-search-timelier-drop-inflation-sees-more-tightening-ahead)
- [Fed chair Warsh talks up a storm but December rate hike bets barely budge (InvestingLive)](https://investinglive.com/central-banks/much-ado-about-nothing-fed-chair-warsh-talks-up-a-storm-but-december-rate-hike-bets-barely-budge/)
- [FOMC Meeting Schedule — December 2026 (FedRateCalc)](https://fedratecalc.com/fomc-meeting-schedule/december-2026/)
- [Fed December 2026 meeting: what to watch (IfYouSpent)](https://news.ifyouspent.com/en/news/fed-december-2026-meeting-jobs-cpi-what-to-watch)
- [CPI Release Dates 2026 (Thrive in Markets)](https://thriveinmarkets.com/calendar/dates/cpi-2026/)
- [BLS PPI release schedule](https://www.bls.gov/schedule/news_release/ppi.htm)
- [Traders Pile Into $120K Bitcoin Call for Dec. 2026 (GNcrypto)](https://www.gncrypto.news/news/traders-pile-into-120k-bitcoin-call-deribit-dec-2026/)
- [Bitcoin options traders load up on $120K strike through December 2026 (bitcoin.com)](https://news.bitcoin.com/bitcoin-options-traders-load-up-on-120k-strike-through-december-2026/)
- [Here's what history says to expect for Bitcoin in December (Motley Fool)](https://www.fool.com/investing/2025/11/30/heres-what-history-says-to-expect-for-bitcoin-in-d)
- [Bitcoin price history: why this December might be bullish (Investing.com)](https://www.investing.com/news/cryptocurrency-news/bitcoin-btc-price-history-secret-heres-why-this-december-might-be-bullish-3244748/)