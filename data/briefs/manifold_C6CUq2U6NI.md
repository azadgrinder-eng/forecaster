## 1. Resolution mechanics

- **What counts as YES:** CoinGecko's BTC/USD spot price must reach or exceed **$85,000.00** at any moment between market creation and **Nov 30, 2026, 23:59:59 UTC**. One tick or print is enough to resolve YES immediately. If CoinGecko is unavailable or shows clear anomalies, CoinMarketCap or major spot exchanges such as Coinbase and Binance serve as backup.
- **Close-time mismatch:** The listed close is 2026-11-30 15:59 UTC, about 8 hours before the end of the resolution window. Whether prints in those last 8 hours count depends on the platform. The effect is small but not zero.
- **Market creation date is unknown, and it matters.** BTC traded above $85,000 in early October 2026: the intramonth high was about $87,249 on Oct 2 and the highest close about $86,507 on Oct 4 (Simplemining October 2026 report). It also touched about $85,248 on Sept 21, 2026 (Cointelegraph, Sept 21, 2026).
  - If the market opened before roughly Oct 5–6, 2026, it may already qualify for YES.
  - The background's wording ("reclaim the $85,000 mark", "traded predominantly in the $70,000 to $85,000 range") implies it opened after BTC fell below $84k around Oct 6 (The Block, Oct 6, 2026). The rest of this brief assumes that, so a new high of at least $85k is needed between now and Nov 30.
- **Data-source detail:** CoinGecko's aggregated, volume-weighted price usually smooths out wicks on a single exchange. A brief spike on one venue may not show on CoinGecko, though the fallback to individual exchanges creates some ambiguity.
- **Required move:** From about $73,600 on Nov 11, BTC needs to rise about **+15.5%** (ln ≈ 0.144) at some point in about 19.5 days.

## 2. Reference classes and base rates

**A. Barrier-hit probability from options-implied volatility (driftless lognormal, reflection principle: P ≈ 2·[1−Φ(ln(K/S)/σ√t)])**
- Deribit DVOL was about 39–40 on Nov 7–8, with Nov 13 at-the-money implied volatility about 39.7% and Nov 20 about 38.3% (GEX Monitor, Nov 7–8, 2026). DVOL has averaged 42.4 in 2026, the lowest yearly average since the index launched (Deribit data via cryptonews.net, Nov 2026). Implied volatility probably rose after the Nov 10 CPI selloff.
- Results for S = $73.6k, K = $85k, t = 19.5/365:
  - σ = 40%: σ√t ≈ 0.092, z ≈ 1.56, **P ≈ 12%**.
  - σ = 45%: **P ≈ 17%**.
  - σ = 30%, closer to recent realized volatility (one source put October realized volatility at about 20% against 38% implied; CryptoTicker, Oct 2026): **P ≈ 4%**.
- Downside skew is bid, meaning puts are priced above calls and the market leans bearish, so the upside tail is probably slightly thinner than a symmetric model assumes.

**B. Rallies of 15% or more within about 3 weeks in BTC's 2026 regime (rough count from news, not a systematic dataset)**
- 2026 contains one clear episode: BTC went from about $63.5–64.6k in August to above $80k on Aug 25 (IG, Aug 2026; The National, Aug 25, 2026). Over Aug–early Oct it ran to about $87k.
- The Feb 6 low of about $60k (Semafor and Fortune, Feb 2026) was followed by recoveries, but I could not establish their speed.
- The Nov 4 post-election squeeze moved only about 7% ($75.7k to $81k).
- Rough estimate: about 1–2 of roughly 15 three-week windows in 2026 produced a peak gain of 15% or more, so **roughly 7–13%**.
- Over BTC's longer history (2015–2024), when volatility was higher (typical realized 55–70%), 20-day windows with a 15% or larger peak gain were more common, very roughly 20–25%. This is my estimate, not a computed figure, and it overstates the current low-volatility regime.

**C. Seasonality and regime**
- November has historically been one of BTC's strongest months on average (CryptoTicker, "Bitcoin Monthly Returns: November", 2026). The average is skewed by bull-market years such as 2013, 2017, 2020 and 2024.
- In bear or tightening regimes such as 2018 and 2022, November was sharply negative. 2026 so far looks more like a bear or tightening year: the worst start to a year on record, a 7.3% October drop that was the weakest October since 2016, and a Fed in hiking mode.

## 3. Current state of the world (most recent first)

- **Nov 11, 2026:** BTC at about **$73,600** (CoinGlass via an Indonesian outlet; aktualita.co, Nov 11), down about 2% on the day. This is an 11-week low.
- **Nov 10, 2026:** October US CPI came in hot: headline +0.4% month on month against +0.3% expected, core +0.3% against +0.2% (Quartz; Bitbo; crypto.news, Nov 10).
  - BTC fell below $74k. Crypto liquidations reached about $630M, mostly longs (Cointelegraph, Nov 10).
  - Markets price a **25bp Fed hike at the Dec 9 FOMC** with about 89–96% probability (CME FedWatch via Cointelegraph and Yahoo Finance, Nov 10). Fed Governor Waller backed a December hike and floated 50bp if core inflation stays firm.
  - The Fed funds rate is 3.75–4.00%. The Fed hiked in September and held in October.
  - Fortune put BTC at $74,261 on Nov 10, about $31.7k below its level a year earlier (Fortune, Nov 10). Separately, US spot BTC ETFs saw about $201M of outflows (Crypto Times, Nov 10).
- **Nov 7, 2026:** US spot BTC ETFs had **$1.28B of net outflows** for the week, the worst since late June, and flows flipped negative for 2026 year to date (The Block, Nov 7).
  - About $430M left on Nov 5 and $412M on Nov 6 (Crypto Briefing).
  - Cumulative outflows since Nov 2 are about $1.48B (aggregated news, Nov 10).
- **Nov 4–5, 2026:** BTC squeezed from about $75.7k on election night to an intraday high of about **$81.0k**, the November high so far; other sources say $80.8–80.9k.
  - Drivers: the US midterms (reported Democratic sweep of both chambers), about $378M of short liquidations in one hour, and oil sliding on hopes for an end to the Iran war (Cointelegraph; The Block, Nov 4).
  - The Block's Nov 4 headline also mentions a **Binance hack** that markets "shrugged off".
  - The rally faded within days.
- **Nov 4, 2026:** Glassnode put the short-term-holder cost basis at about $75.7k (CryptoTicker, Nov 7). BTC is now below it, a level often read as bearish when lost.
- **Oct 2026:** BTC fell 7.3%, from a $83,556 open to a $77,424 close (Coinbase). The month's high was about $87.2k on Oct 2. BTC broke below $84k on Oct 6 with about $487M in long liquidations (Simplemining; The Block, Oct 6). Spot ETFs lost $643M on Oct 30 alone.
- **Earlier 2026:** The all-time high is $126,198 (Oct 6, 2025). BTC hit about $60k on Feb 6, 2026, recovered to above $80k by Aug 25 and to $85.2k on Sept 21, the highest since Jan 29 (various sources). One unverified source mentions a break below the February low and a realized price of $53–54k; I could not date it.

**Scheduled events before Nov 30:**
- Nov 13, 20 and 27: Deribit options expiries. Nov 27 open interest is reportedly about 69K BTC (unverified KuCoin post).
- Around Nov 17–18 (unconfirmed; one calendar says Nov 25): Nvidia Q3 FY27 earnings, a risk-sentiment catalyst.
- Late November: FOMC minutes and October PCE, dates not confirmed.
- Nov 26–27: US Thanksgiving, with thin liquidity.
- Dec 9 FOMC decision is **after** the close; only anticipation of it falls inside the window.

## 4. Drivers and scenarios

**Paths to YES (needs about +15.5%):**
1. **Macro relief:** Softer data (PCE, jobs, Fed speakers) talks down the December hike odds, which are about 90% or more now. A repricing toward "no hike" could trigger a sharp squeeze, since positioning has been flushed and funding is reset.
2. **Short squeeze plus ETF flows reversing:** The Nov 4 squeeze showed $5k+ moves in a day are possible. YES needs roughly two such legs, plus ETF inflows returning to break $80–82k resistance (The Block; cryptonews.net, Nov 5).
3. **Geopolitical or exogenous positive shock:** for example, an Iran war ceasefire pushing oil down and risk assets up, a strong Nvidia result lifting tech, or pro-crypto policy news.

**Paths to NO:**
1. **Base case:** Hawkish Fed pricing persists, ETF outflows continue and BTC chops in the $68–80k range. Even a strong rebound to the November high (about $81k) falls short.
2. **Further breakdown:** BTC loses $70k support and heads for the 2026 lows.
3. **Rally that falls short:** Even a 10% bounce reaches only about $81k. Overhead supply sits at $80–82k (the November high) and about $85.6k (a Glassnode cost-basis level cited in September).

## 5. Signposts

**Toward YES (big moves):**
- BTC reclaims $80–82k with a daily close above it before about Nov 20.
- Several consecutive days of spot ETF net inflows of $300M or more.
- Fed funds futures cut the December hike odds below about 50%.
- DVOL spikes with call skew turning positive.
- Large short liquidations.

**Toward YES (modest moves):** Nvidia beats and the Nasdaq rallies; oil falls on Iran de-escalation.

**Toward NO:**
- BTC closes below $70k.
- ETF outflows continue (running about $1B+ a week).
- Hot PCE, or Fed talk of a 50bp hike.
- Fresh exchange-security fallout (Binance hack details).
- Implied volatility compresses back to the high 30s as time runs down. Each week without a move cuts the probability nonlinearly. With about 12 days left and BTC still around $74k, a σ = 40% model gives about 5%.

## 6. Uncertainties

- **Market creation date.** It decides whether the early-October 2026 prints above $85k count; this could make the answer close to certain YES.
- **Exact current price and volatility after the CPI shock.** Sources disagree slightly ($73.1–74.6k), and one TradingKey report mentions a test of $70k that I could not confirm. I found no DVOL reading after Nov 8.
- **Binance hack:** size and any lingering effects not established.
- **Iran war status and the oil channel:** not established in detail.
- **Exact dates** for Nvidia earnings, PCE and the FOMC minutes are unconfirmed.
- **Base rates B and C** are rough estimates from news, not computed from price data.
- **Data quality:** Several search results mixed up 2025 and 2026 events, for example October and November ETF outflow "records" and the $126k high. I tried to use only items clearly dated 2026.
- **Page access:** I could not open the full pages (the proxy blocked fetches); all facts come from search-result summaries.

## Sources
- [Bitcoin Price Today, November 11, 2026: BTC Drops Under Pressure from US Inflation and ETF Outflows (aktualita.co)](https://aktualita.co/en/economy/bitcoin-price-today-november-11-2026-btc-drops-under-pressure-from-us-inflation-and-etf-outflows)
- [Current price of Bitcoin for November 10, 2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-10-2026/)
- [Bitcoin Price Today, November 10, 2026 (Sunday Guardian)](https://sundayguardianlive.com/trending/bitcoin-price-today-november-10-2026-btc-trades-at-74596-after-retreating-from-80935-check-latest-price-in-india-market-trends-key-drivers-320124/)
- [Bitcoin Price Today Holds Near $75K: ETF Outflows Hit $201M (Crypto Times)](https://www.cryptotimes.io/2026/11/10/bitcoin-price-today-holds-near-75k-as-btc-etf-outflows-hit-201m-liquidations-top-269m/)
- [Bitcoin Retests $73,500 on High US CPI Inflation (Cointelegraph)](https://cointelegraph.com/markets/bitcoin-11-week-low-discouraging-us-cpi-inflation)
- [Bitcoin Falls Below $74K After Hot US Inflation Fuels Fed Rate Hike Bets (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/bitcoin-falls-below-74k-hot-144004327.html)
- [Bitcoin falls to 11-week low after hotter-than-expected inflation (Quartz)](https://qz.com/bitcoin-11-week-low-october-inflation-fed-rate-hike-111026)
- [Bitcoin Drops to $73,600 as Hot October CPI Fuels Fed Hike Bets (Bitbo)](https://bitbo.io/news/bitcoin-drops-hot-october-cpi/)
- [Bitcoin Drops 2%, Threatening $70,000 Mark (TradingKey)](https://www.tradingkey.com/analysis/cryptocurrencies/btc/262299781-crypto-bitcoin-btc-cpi-ppi-fed-fomc-tradingkey)
- [Bitcoin rebounds past $80,000 as markets shrug off midterms and Binance hack (The Block)](https://theblock.co/news/markets/2026-11-04-bitcoin-price-midterm-elections-binance-hack-recovery-433030)
- [Bitcoin price / US stocks rally on midterm result (Cointelegraph)](https://cointelegraph.com/news/bitcoin-price-us-stocks-rally-midterm-election-result)
- [Why did Bitcoin climb back above USD 80,000 (Kalkine)](https://kalkine.ca/news/general-news/why-did-bitcoin-btc-climb-back-above-usd-80000-after-sliding-to-about-usd-75700)
- [Bitcoin Price Holds $80K, but Can Bulls Break $81,970 Resistance? (cryptonews.net)](https://cryptonews.net/news/bitcoin/33708639/)
- [Bitcoin ETFs flip negative for 2026 after $1.28 billion outflow week (The Block)](https://theblock.co/news/markets/2026-11-07-bitcoin-etfs-flip-negative-for-2026-after-1-28-billion-outflow-week-worst-since-june-435984)
- [Bitcoin spot ETFs see $412 million in net outflows on November 6 (Crypto Briefing)](https://cryptobriefing.com/bitcoin-spot-etfs-412m-outflows-november-6/)
- [Bitcoin Price October 2026: Down 7.3%, $515M ETF Outflows (Simplemining)](https://www.simplemining.io/insights/post/bitcoin-market-report-october-2026)
- [Crypto Monthly Recap October 2026 (CryptoTicker)](https://cryptoticker.io/en/crypto-monthly-recap-october-2026/)
- [The Month Unplugged: October 2026](https://www.themarketsunplugged.com/the-month-unplugged-october-2026/)
- [Bitcoin briefly slides below $84,000 as crypto long liquidations reach $487 million (The Block, Oct 6, 2026)](https://theblock.co/news/markets/2026-10-06-bitcoin-slides-crypto-long-liquidations-surge-417882)
- [BTC price nears eight-month high above $85K (Cointelegraph)](https://cointelegraph.com/markets/btc-price-nears-eight-month-high-above-85k-five-things-to-know-in-bitcoin-this-week)
- [Bitcoin crosses $80,000 to reach highest level in three months (The National, Aug 25, 2026)](https://www.thenationalnews.com/business/money/2026/08/25/bitcoin-crosses-80000-to-reach-highest-level-in-three-months/)
- [Why is bitcoin dropping (IG)](https://www.ig.com/uk/trading-strategies/why-is-bitcoin-dropping-260814)
- [BTC Options Daily Market Observation, Nov 7 (GEX Monitor)](https://gexmonitor.com/daily-research/btc/2026-11-07)
- [BTC Options Daily Market Observation, Nov 8 (GEX Monitor)](https://gexmonitor.com/daily-research/btc/2026-11-08)
- [Bitcoin price prediction: volatility falls to 37 after vote (CryptoTicker)](https://cryptoticker.io/en/bitcoin-price-prediction-volatility-after-election-november-4-2026/)
- [Bitcoin price prediction: 38.3% implied, 20.2% real (CryptoTicker)](https://cryptoticker.io/en/bitcoin-price-prediction-volatility-premium-20-october-2026/)
- [Bitcoin options are pricing in the calmest year on record (cryptonews.net)](https://cryptonews.net/news/bitcoin/33702876/)
- [Bitcoin After $2.65B Expiry (KuCoin)](https://www.kucoin.com/square/post/content_6aee0ad31eb482000796e89b)
- [Bitcoin Price Prediction: BTC at Recent Buyers' Cost Basis (CryptoTicker, Nov 7, 2026)](https://cryptoticker.io/en/bitcoin-price-prediction-short-term-holder-cost-basis-november-7-2026/)
- [Bitcoin Monthly Returns: What November Holds in 2026 (CryptoTicker)](https://cryptoticker.io/en/bitcoin-monthly-returns-november/)
- [Bitcoin value drops to lowest level in a year (Semafor, Feb 6, 2026)](https://www.semafor.com/article/02/06/2026/bitcoin-value-drops-to-lowest-level-in-a-year)
- [Bitcoin/Ethereum worst starts in history (Fortune, Feb 20, 2026)](https://fortune.com/2026/02/20/bitcoin-ethereum-price-today-worst-starts-in-history-rebound-in-sight/)
- [NVDA earnings date (Earnings Whispers)](https://www.earningswhispers.com/stocks/Nvda)
- [NVDA earnings (ChartRow)](https://chartrow.com/quote/nvda/earnings)