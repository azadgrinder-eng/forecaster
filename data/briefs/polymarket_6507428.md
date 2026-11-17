# Research brief: Will Binance ETH/USDT trade at or below $1,300 at any point in November 2026?

**Data-quality caveat:** I could not open any article pages directly; every fetch attempt was refused by the network proxy. All facts below come from search-result summaries. Some of those summaries contradict each other, and I flag the contradictions where they occur.

## 1. Resolution mechanics

- **What counts as YES:** any 1-minute ETH/USDT candle on Binance with a final Low of **$1,300.00 or lower**, between 00:00 ET Nov 1 and 23:59 ET Nov 30, 2026. In UTC that is 04:00 Nov 1 to 04:59 Dec 1. The market closes 2026-12-01 05:00 UTC.
- **It resolves early.** As soon as one candle qualifies, the market resolves YES. Only a single 1-minute wick is needed. The price does not have to close there or stay there.
- **The first half of the month did not trigger it.** The November low so far is about **$1,710–1,715**, set over the weekend of Nov 14–15 (Pluang, Nov 15; TradingNews, ~Nov 16; CapitalStreetFX, Nov 16). It is still worth checking the Binance chart directly to confirm no lower wick printed.
- **About 13.5 days remain** (from Nov 17 to the close).
- **Only Binance's ETH/USDT pair counts.** Prints on other exchanges, ETH/USD, or perpetual futures do not count, even if they wick lower than Binance spot. If USDT traded above $1 (rare), ETH/USDT would sit slightly lower than ETH/USD. That effect is negligible here.
- **Distance to the strike:** ETH was about **$1,816–1,828** on Nov 17 (Bybit, Investing.com, CoinPaprika via Bitcoinworld, CoinGabbar; Nov 17). Reaching $1,300 needs about a **−28.5%** move from here, or **−24%** below this month's low.

## 2. Reference classes and base rates

**A. Volatility model (driftless lognormal, chance of touching the level).**
- Inputs: required log move ln(1300/1820) = −0.337; time ≈ 13.5–14 days (T ≈ 0.038 yr).
- At ETH implied volatility ≈ 57–63% (Cryptoticker, ~Nov 10; The Block, Nov 15): σ√T ≈ 0.12, z ≈ 2.7–2.9, touch probability ≈ **0.4–0.7%**.
- At the 7-day at-the-money implied volatility of ~79% (The Block, Nov 15): z ≈ 2.15, touch probability ≈ **3%**.
- Crypto returns have fat tails, so the real number is probably above the lower end of these figures.

**B. Historical ETH 14-day drawdowns of 28.5% or more.** This is my own estimate from memory of ETH price history, not computed from a dataset.

| Episode | Approx. move |
|---|---|
| Jan–Feb 2018 | several qualifying windows |
| Nov–Dec 2018 | ~$210 → ~$83 |
| Mar 2020 | ~−55% |
| Sep 2020 | ~−35% in 3 days |
| Jan 2021 | ~−30% |
| Feb 2021 | ~−37% |
| May 2021 | $4,380 → ~$1,730 in 7 days |
| Jan 2022 | ~−36% |
| May 2022 | ~−42% |
| Jun 2022 | $1,900 → $880 |
| Nov 2022 (FTX) | ~−36% in 4 days |
| Aug 5, 2024 | Binance low ~$2,111, ~−34% from late July |
| Feb 3, 2025 | ~$3,300 → ~$2,120 on Binance, ~−36% in days |
| Mar–Apr 2025 | ~$2,100 → $1,385 on Apr 9, borderline over 14 days |
| Jan–Feb 2026 | possibly: year high $3,405 on Jan 14 to Feb low ~$1,743–1,755; exact timing unverified |

- **2017–2026:** roughly 20 episodes. Each produces several qualifying start days, giving about **4–5%** of all 14-day windows.
- **2023–2026 (the ETF era, lower volatility):** about **1.5–3%** of windows.
- **Big moves:** the largest single-day flash crash in recent years, Oct 10, 2025, took ETH down about −21% intraday. That alone would not reach −28.5% from here.

**C. After a sharp weekly drop (ETH −15.7% in the 7 days to Nov 16; BingX, Nov 16).**
- Volatility tends to cluster, which raises tail risk somewhat. Several of the worst crashes (May 2022, June 2022, Nov 2022, Nov 2018) followed an initial 10–20% leg down.
- However, most 15% weekly drops do not turn into a further 28% decline within two weeks.
- A reasonable conditional range, my judgment rather than a computed figure, is about **2–6%**.

## 3. Current state of the world (most recent first)

- **Nov 17:** ETH ~$1,816–1,828, up about 0.5% on the day. The Bank of Russia's crypto-access ordinance takes effect (CoinDesk week-ahead, Nov 16).
- **Nov 16:** ETH ~$1,795–1,835. BTC ~$63.9K after dipping to about $62K. FxStreet describes selling pressure spreading. Fed Chair Kevin Warsh spoke at the SF Fed conference; the preview expected AI and labor-market themes rather than rates (Admiral Markets, Fool/Yahoo, CapitalStreetFX; Nov 16).
- **Nov 14–15 weekend:** ETH bottomed at about $1,710–1,715, its lowest since July. About $2.02B of crypto liquidations in 24 hours, $1.68B of them longs. Crypto's worst week since June; about $230B wiped from total market cap (Pluang, Nov 15; Yahoo "Crypto's worst week since June"; Fool, Nov 16).
- **Nov 13:** ETH broke below $2,000, the first time since August, to about $1,896–1,922, with $259M liquidated (CryptoTimes, Nov 13). An options expiry that day had puts outnumbering calls 2:1, with a large put position at $2,000 (Cryptoticker).
- **Nov 9–13:** US spot ETH ETFs had about **−$398.9M** of net outflows, the **7th straight week** of outflows (Bitcoinworld/crypto.news, Nov 16–17). BTC ETFs had about −$2.35B month to date (FxStreet, Nov 16). Combined BTC+ETH ETF outflows were −$1.464B in the latest week (Goodman Macro, Nov 16).
- **Macro:** US 10-year Treasury yield about **5.15%** (Investing.com). CPI came in at +0.4% month on month against +0.3% expected. The Fed hiked in September. Futures now fully price a **25 bp hike at the Dec 8–9 FOMC**, with about 8% odds of 50 bp. The Fed held at 3.75–4.00% in October on a 10–2 vote (CoinDesk/FxStreet/CoinGabbar, Nov 13–17).
- **Bigger picture:** ETH is about 63–64% below its all-time high of $4,946 (Aug 24, 2025). 2026 high: $3,405 (Jan 14). October 2026 was down about 13%, on track for the worst October in 8 years (Coinotag, Oct 26). Total crypto market cap is down about $800B since early October (OKX insight).
- **2026 low (conflicting):** reported as about **$1,505–1,566 in June 2026** (Cryptoticker cites $1,566 on Jun 26; an August article and a chart page cite about $1,505/1,506). One search found no confirmation of the June low. February 2026 low: about $1,743–1,755.
- **Support levels analysts cite:**
  - ~$1,700–1,710 (this month's low and a "four-year uptrend support"; Ted Pillows via crypto.news)
  - ~$1,525–1,585 (CryptoQuant realized price; dates unclear)
  - ~$1,500 (CryptoQuant's March 2026 downside target)
  - ~$1,414 (next support if $1,500 breaks; crypto.news, June)
  - ~$1,237 (Cointelegraph's UTXO-based possible cycle floor; date unclear)
- **Implication:** $1,300 sits **below the 2026 yearly low and below the realized price**. That level has not printed since around April 2025, when the low was $1,385 on Apr 9, 2025.

**Scheduled before the close:**
- **Nov 18, 2 p.m. ET:** FOMC minutes (Oct 27–28 meeting), expected to show a deeper split than the 10–2 vote.
- **Week of Nov 16:** Nvidia earnings and US retail sales.
- **Nov 22:** Russian exchanges may begin organized crypto trading.
- **Late November:** likely PCE release (date unconfirmed); US Thanksgiving holiday (~Nov 26–27) brings thin liquidity, which raises wick risk.
- **Nov 27:** likely month-end Deribit options expiry (date assumed, not verified).
- **Dec 8–9 FOMC** falls after the close, but expectations of a hike or a 50 bp move will be priced in beforehand.

## 4. Drivers and scenarios

**Paths to YES (ETH reaches $1,300 or lower):**
1. **Macro shock cascade:** hawkish minutes, hot data, or the 10-year yield moving well above 5.15% pushes the market to price a 50 bp December hike or more hikes. Risk assets sell off, and ETH loses $1,700, then $1,500 (the realized-price zone), triggering forced liquidations. This would likely need BTC to fall well below $60K, roughly −25% or more.
2. **Crypto-specific event:** a major hack, an exchange or stablecoin failure, or a large ETH treasury company or fund forced to sell (similar to FTX in Nov 2022, or the Oct 10, 2025 liquidation cascade). Thanksgiving's thin liquidity raises the risk of a liquidation wick.
3. **Steady grind:** continued ETF outflows (8 weeks or more) and capitulation below the June low take ETH through $1,500 and on to $1,300 over two weeks. That requires an average decline of about −2.3% per day. It has happened (June 2022), but it is rare.

**Paths to NO:**
1. **Bounce or range:** oversold conditions after a ~$2B liquidation flush and a test of multi-year trendline support lead to a range of $1,700–2,000. This is the base case in most technical commentary (TradingNews targets $2,260 if $2,000 is reclaimed).
2. **Further decline that stops short:** ETH falls to $1,500–1,600, where the June low and realized-price buyers are, without reaching $1,300.
3. **Calm macro:** the minutes and data come in benign, the December hike is already priced, and yields stabilize.

## 5. Signposts

**Toward YES:**
- A daily close below **$1,700** (this month's low), and especially below **$1,500–1,550** (the June 2026 low and realized price). At $1,500, $1,300 is only −13% away, so the probability would rise sharply, plausibly to 20–35% with a week left.
- BTC below about $58–60K.
- 10-year yield above 5.3%, or futures pricing a 50 bp December hike or a terminal rate above 4.5%.
- ETF outflows above $500M a week.
- ETH 7-day implied volatility above 90–100.
- Large open interest rebuilding with funding still positive (more fuel for a cascade).
- Any major exchange, stablecoin, or DeFi insolvency news.

**Toward NO:**
- ETH reclaims and holds $2,000.
- ETF flows turn positive.
- Dovish or benign FOMC minutes or PCE, and yields fall.
- Implied volatility falls back toward 50.
- Each passing day without a crash also counts: the window shrinks, so the touch probability decays roughly with √time.

## 6. Uncertainties

- **The exact 2026 low.** Sources conflict between ~$1,505 and $1,566 for June, and one search found no confirmation at all. I also could not confirm the exact Binance November low (reported at $1,710–1,715).
- **Current options data.** I found no reliable current ETH DVOL. Readings range from 52 to 63, with 7-day at-the-money implied volatility near 79%, and these may have different timestamps. I could not get any read on how much downside protection near $1,300–1,500 the put skew is pricing.
- **Leverage and positioning.** Open interest, funding, and liquidation-cluster maps below $1,700 were not obtained.
- **Late-November macro calendar.** The PCE and other late-November release dates are unverified.
- **The historical base rates in Section 2B** are estimated from memory of ETH price history, not from a dataset. Treat them as approximate within about ±2 percentage points.
- **Some search summaries were internally inconsistent,** for example one calendar describing Warsh as a "former" governor. Every fact here should be treated as coming from secondary sources, since no article pages could be opened directly.

## Sources
- [Current price of Ethereum for November 16, 2026 (Fortune)](https://fortune.com/article/price-of-ethereum-11-16-2026/)
- [Ethereum Price: ETH Live Price Today (Bybit)](https://www.bybit.com/en/price/ethereum/)
- [Ethereum Price Today (OKX)](https://www.okx.com/en-us/price/ethereum-eth)
- [Ethereum Historical Data (Investing.com)](https://www.investing.com/crypto/ethereum/historical-data)
- [Crypto News Nov 17: Bitcoin, Latest Hacks, Fed Rate Hike Odds and More (CoinGabbar)](https://www.coingabbar.com/en/crypto-news-nov-17-bitcoin-eth-defi-fear-index-fed-rate-hike)
- [Ethereum Falls 14% to $1,828 as Ether ETF Outflows Hit $399M (Bitcoinworld)](https://bitcoinworld.co.in/ethereum-14-percent-fall-four-year-support-etf-outflows/)
- [Ethereum price falls 14% as four-year support comes into focus (crypto.news)](https://crypto.news/ethereum-price-four-year-support-etf-outflows)
- [Why Is the Crypto Market Down This Week? (BingX)](https://bingx.com/en/news/post/why-is-the-crypto-market-down-this-week-btc-falls-as-eth-and-sol-lose-more-november)
- [Crypto Market Today, Nov. 16 (Motley Fool)](https://www.fool.com/coverage/stock-market-today/2026/11/16/crypto-market-today-nov-16-bitcoin-searches-for-stability-after-usd230-billion-crypto-sell-off/)
- [Crypto's Worst Week Since June (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/crypto-worst-week-since-june-202803450.html)
- [Ethereum price hits lowest since July (Pluang)](https://pluang.com/en/news-feed/harga-ethereum-jatuh-1715-63-persen-dibawah-rekor-tertinggi)
- [Ethereum Price Forecast — ETH-USD ($1,807) on 5-Year Trendline Test (TradingNews)](https://www.tradingnews.com/news/ethereum-eth-usd-holds-1807-on-5-year-trendline-after-1710-low-reclaiming-2000-opens-2260-usd)
- [Daily Crypto Report 16 Nov 2026 (CapitalStreetFX)](https://www.capitalstreetfx.com/market-analysis/daily-crypto-report-16-nov-2026/)
- [Why Is Ethereum Price Down Today? ETH Crashes Below $2,000 (CryptoTimes, Nov 13)](https://www.cryptotimes.io/2026/11/13/why-is-ethereum-price-down-today-eth-crashes-below-2000-as-259m-liquidated/)
- [Ethereum Price Prediction: $400M in Ether Liquidations (CryptoDaily)](https://cryptodaily.co.uk/2026/11/ethereum-price-prediction-400m-in-ether-liquidations-drag-it-toward-1-700)
- [Crypto's market cap has shed roughly $800B since early October (OKX)](https://www.okx.com/en-us/orbit/insight/92915613921696)
- [Ethereum price falls to $1,830: lowest since July (Cryptoticker)](https://cryptoticker.io/en/ethereum-price-1800-dollar-level/)
- [Ethereum Price History 2026 (CoinScreener)](https://www.blocfolio.com/coin/ethereum/history/2026)
- [Crypto Options Data (The Block)](https://www.theblock.co/data/crypto-markets/options)
- [Capital Flows: Bitcoin and Ethereum ETFs Lose $1.464 Billion (Goodman Macro)](https://www.goodman-macro.com/en/articles/20261116-crypto-flows/)
- [Ethereum options expiry: puts outnumber calls two to one (Cryptoticker)](https://cryptoticker.io/en/ethereum-options-expiry-november-13-put-wall-2000/)
- [FOMC minutes, Nvidia earnings, Russia's retail crypto rules: Crypto Week Ahead (CoinDesk)](https://www.coindesk.com/markets/2026/11/16/fomc-minutes-nvidia-earnings-russia-s-retail-crypto-rules-crypto-week-ahead)
- [What to watch this week as Bitcoin falls below $65K (FxStreet)](https://www.fxstreet.com/cryptocurrencies/news/what-to-watch-this-week-as-bitcoin-falls-below-65k-202611161341)
- [Warsh Speech Preview (Admiral Markets)](https://admiralmarkets.com/education/articles/fundamental-analysys/warsh-speech-preview-november-16-2026)
- [Bitcoin's Rate Shock Deepens as the 10-Year Yield Hits 5.15% (Investing.com)](https://www.investing.com/analysis/bitcoins-rate-shock-deepens-as-the-10year-yield-hits-515-200691685)
- [CryptoQuant says ETH could fall to $1,500 (The Block, Mar 12, 2026)](https://www.theblock.co/news/ecosystems/2026-03-12-cryptoquant-eth-price-fall-1500-ethereum-adoption-paradox-393431)
- [Ethereum tests $1,500 support as ETF selling and whale losses mount (crypto.news)](https://crypto.news/ethereum-tests-1500-support-as-etf-selling-and-whale-losses-mount-will-it-crash/)
- [Large demand zone below $2K (Cointelegraph)](https://cointelegraph.com/markets/large-demand-zone-below-dollar2k-eth-price-gives-signal-on-where-ether-may-go)
- [Ethereum ETH worst October in 8 years (Coinotag)](https://en.coinotag.com/ethereum-eth-worst-october-in-8-years-13-percent-drop)