# Research brief: will BTC's trimmed mean go below $72,500 by Nov 30, 2026, 11:59 PM ET?

## 1. Resolution mechanics

- **What counts as YES:** at any minute between when the market was issued and 11:59 PM ET on Nov 30, 2026 (04:59:59 UTC Dec 1), the "trimmed mean" settlement value must be below $72,500. This is a one-touch barrier market. Any single qualifying minute resolves it YES, and later recoveries don't matter. If data is missing, affected strikes resolve NO. The exchange (Kalshi, product family KXBTCMINMON) decides, using CF Benchmarks' Bitcoin Real-Time Index (BRTI).
- **The main ambiguity is how the trimmed mean is calculated.** I could not read the contract PDF, so this is unresolved.
  - **Literal reading.** The rules say "the top 20% and bottom 20% of the cumulative dataset are removed." Read literally, that is a running trimmed mean of every minute price since issuance. Such a number moves very slowly, and YES would need BTC to spend most of the month well below $72.5K.
  - **Operational reading, which I think is more likely.** Kalshi's own page for the 2025 yearly-low market describes averaging the BRTI over a 60-second window after dropping the top and bottom 20% of values (Kalshi KXBTCMINY-25 page, via search snippet). A third-party page describes the same thing: a 20% trimmed mean over 60 one-second readings (oddsreference, undated). A cumulative running mean would also make yearly-minimum markets nearly impossible to trigger, which suggests the product is a per-minute check that filters out brief spikes. Under this reading, YES needs about one minute of BRTI near or below $72.5K, with sub-minute wicks excluded.
  - **Issuance date.** Probably around Oct 31 or Nov 1, 2026, since this is a monthly series. I couldn't confirm it. BTC has evidently not yet gone below $72.5K, because the market is open and recent lows were about $75K.
- I couldn't read the governing rulebook (CRYPTOMINMAXMONTHLY.pdf, dated Jan 2026) because the fetch failed.

## 2. Reference classes and base rates

1. **Barrier-hit probability under a random-walk model (per-minute reading).** Spot is about $75.6K (Nov 6) and the barrier is $72.5K, so the distance is ln(72.5/75.6) ≈ −4.2%. About 24 days remain.
   - At 37% annualized volatility (DVOL was 37.3 on Oct 19; the Nov 27 expiry was near 36): σ over 24 days ≈ 9.5%, so P(touch) ≈ 2·N(−0.44) ≈ **66%**.
   - At 45%, a plausible level after the selloff: σ ≈ 11.6%, so P(touch) ≈ 2·N(−0.36) ≈ **72%**.
   - The 60-second trimmed mean shaves a little off this, because brief wicks don't count. Realized volatility had been much lower than implied: 20% realized against 38% implied in October (Cryptoticker, Oct 2026). If calm returns, the probability falls toward about 55%.
2. **Recent monthly ranges in 2026.**
   - September: high about $87.4K, low about $74.9K, a range of roughly 15% (StatMuse table).
   - October: high about $87.1K, low about $76.1K after the Binance hack, also roughly 15%.
   - A month's low landing about 4% below a price that is already near the bottom of the recent range happens often but not always. The September and October lows held near $75–76K both times, which suggests support there.
3. **Base rate under the cumulative reading.** The running trimmed mean is probably around $77–78K now (Nov 1–4 prices were roughly $76–80K). To pull it below $72.5K by Nov 30, BTC would likely need to break toward about $68–70K soon and stay there for most of the remaining ~24 days. As a rough guide, that means about 10–20% under the same volatility assumptions.

## 3. Current state of the world (most recent first)

- **Nov 6, 2026:** BTC fell more than 6% toward $75,000 (quoted at $75,617). Crypto liquidations were about $1.08–1.1B, mostly longs. The cause was an AI and chip stock selloff that pushed the Nasdaq into a correction (crypto.news, Nov 6; CoinTurk, Nov 6).
- **Nov 5:** BTC was down 5.65% to about $75,880 as Wall Street had its worst day in 18 months, erasing the post-election bounce. Earlier that day it was about $80.2K (Motley Fool, Nov 5; Fortune, Nov 5).
- **ETF flows, early November:** about $1.16B of outflows over three days, with roughly $900M from IBIT, after the hack. There was a $74.6M inflow on Nov 4 (search summaries, Nov 2026).
- **Nov 3–4, midterms:** Democrats reportedly won both chambers, and crypto dipped to a six-week low (tech-insider, shattered.io; these are lightly sourced).
- **Nov 2–3:** BTC was flat around $78K, about 4% below its pre-hack level. Binance said it had replenished 98% of the stolen funds by Nov 3 (Bloomberg, Nov 2; Wikipedia).
- **Oct 29:** the $6.3B Binance hack, the largest on record, attributed to the North Korea-linked group TraderTraitor. BTC fell from about $81.9K to a low near $76.1K (Wikipedia; CoinJar).
- **Oct 31:** BTC about $77.6K (BGeometrics). October opened near $83.5K, so the month was down roughly 7%.
- **Year context:** the 2026 low was about $59.1K–61K in early June (Bitcoin.com; Manifold page). BTC consolidated in the low $70Ks in late August and recovered to $83–87K in September and October. Q1 2026 was down 22%.
- **Scheduled events before Nov 30.** Typical calendar dates, not verified:
  - October jobs report around Nov 6
  - October CPI around Nov 12–13
  - Nvidia earnings around Nov 18–19, which matters given the AI-led selloff
  - Deribit monthly options expiry Nov 27
  - Thanksgiving Nov 26, with thin liquidity
  - The next FOMC meeting (around Dec 8–9) falls after the close.
- **Analyst framing:** 21Shares says November depends on BTC holding $76–78K, Binance proving its reserves, and ETF flows recovering. It cites a median November gain of +10.3% since 2010 (21Shares, Nov 2026). Some support analyses name $70–74K as the key band, with $68K and the mid-$60Ks below a break (Analytics Insight, Bitcoin.com, undated or earlier in 2026).

## 4. Drivers and scenarios

**Paths to YES**
- **Continued risk-off move.** The Nasdaq correction deepens, Nvidia or AI earnings disappoint, and long liquidations cascade. A further 4% fall is a modest move given BTC dropped about 6% on Nov 5–6 alone.
- **Binance fallout.** Proof-of-reserves problems or withdrawal trouble, or continued ETF outflows.
- **Policy shock after the midterms.** A Democratic Congress is perceived as less crypto-friendly, for example if the market-structure bill stalls.
- **Thin support.** Losing $75K, which was the floor in September and October, could quickly bring tests of $72–73K.

**Paths to NO**
- **Support holds.** $75–76K held in both September and October. Mean reversion after leverage is flushed out is common.
- **Equities stabilize,** ETF inflows resume, and Binance's reimbursement calms markets. November has historically been a strong month for BTC.
- **Cumulative reading applies.** If the running trimmed mean is the real mechanic, a short dip doesn't count; YES needs a sustained regime below about $70K.

## 5. Signposts

- **BTC price path in the next 3–7 days.** This matters most. A daily close below $74K raises P(YES) sharply under the per-minute reading. A recovery above $80K lowers it a lot.
- **Clarifying the trimmed-mean rule.** Read the CRYPTOMINMAXMONTHLY rulebook text, or check how past monthly minimum strikes settled relative to that month's intraday lows. This could move the estimate by 40+ points.
- **Nasdaq and semiconductor trend,** and the Nvidia earnings reaction.
- **Spot BTC ETF daily flows,** and Binance reserve and withdrawal news.
- **DVOL and funding or open interest.** A volatility spike above 50 raises P(touch). Rebuilt leverage raises the risk of another liquidation cascade.

## 6. Uncertainties

- **The rule itself:** whether the trimmed mean is a 60-second window or cumulative since issuance. This is the single biggest uncertainty. I also don't know the exact issuance timestamp.
- **Exact current price and intraday low:** I don't know Nov 6's exact intraday low. Reports say "towards $75,000", and the BRTI may already have printed lower.
- **Current implied volatility:** the latest DVOL I found is from Oct 19. It is likely higher after this week.
- **Source quality:** many figures come from secondary or aggregator crypto sites with some conflicts. Examples are the hack drawdown (4–6%) and the share of funds Binance had covered (95% vs 98%). I verified no scheduled macro dates directly.

## Sources
- [Why is Bitcoin price down today? (crypto.news)](https://crypto.news/why-is-bitcoin-price-down-today-4/)
- [Bitcoin falls 6% to $75,700 as AI stock selloff triggers $1.1 billion in liquidations (CoinTurk)](https://en.coin-turk.com/bitcoin-falls-6yuzde-to-75700-as-ai-stock-selloff-triggers-1-1-billion-in-liquidations/)
- [Crypto Market Today, Nov. 5 (Motley Fool)](https://fool.com/coverage/stock-market-today/2026/11/05/crypto-market-today-nov-5-bitcoin-erases-post-election-rally-as-wall-street-suffers-worst-day-in-18-months)
- [Current price of Bitcoin for November 5, 2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-05-2026/)
- [Bitcoin Price Today: BTC Falls Below $77K (CryptoTimes)](https://www.cryptotimes.io/2026/11/05/bitcoin-price-today-btc-falls-below-77k-as-crypto-liquidations-reach-718-5m/)
- [2026 Binance hack (Wikipedia)](https://en.wikipedia.org/wiki/2026_Binance_hack)
- [Bitcoin Holds Steady After Binance Hack (Bloomberg, Nov 2 2026)](https://www.bloomberg.com/news/articles/2026-11-02/bitcoin-s-resilience-after-binance-hack-masks-market-jitters)
- [Binance loses $6.3bn in the largest crypto hack on record (CoinJar)](https://www.coinjar.com/global/blog/binance-loses-6-3bn-in-the-largest-crypto-hack-on-record)
- [Bitcoin post-Binance hack: What recovery needs in November (21Shares)](https://www.21shares.com/en-eu/insights/bitcoin-outlook-november-2026)
- [Crypto Dips After Midterms, $6.3B Binance Hack (tech-insider)](https://tech-insider.org/crypto-dips-democrat-midterm-wins-binance-hack-6-3b-2026/)
- [Bitcoin Hits 6-Week Low: Midterms & Binance Hack (shattered.io)](https://shattered.io/bitcoin-six-week-low-78070-midterms-binance-hack-2026/)
- [Bitcoin Monthly Report Oct 2026 (BGeometrics)](https://bgeometrics.com/reports/monthly/2026-10.html)
- [Bitcoin price last 6 months (StatMuse)](https://www.statmuse.com/money/ask/bitcoin-price-last-6-months)
- [Bitcoin price prediction: options price in 38.3% vol, price delivers 20.2 (Cryptoticker, Oct 2026)](https://cryptoticker.io/en/bitcoin-price-prediction-volatility-premium-20-october-2026/)
- [Bitcoin options implied volatility hits 92% lows since 2021 (KuCoin)](https://www.kucoin.com/news/flash/bitcoin-options-implied-volatility-hits-92-lows-since-2021)
- [Here's why Bitcoin's 50% drop looks mild (Bitcoin.com)](https://news.bitcoin.com/heres-why-bitcoins-50-drop-looks-mild-next-to-what-several-altcoin-holders-are-sitting-on/)
- [Bitcoin Drops 22% in Q1 2026 (KuCoin)](https://www.kucoin.com/news/flash/bitcoin-drops-22-in-q1-2026-worst-since-2018)
- [Bitcoin price trades between 76000 and 78000 in key zone (Analytics Insight)](https://www.analyticsinsight.net/amp/story/cryptocurrency-analytics-insight/bitcoin-price-trades-between-76000-and-78000-in-key-zone)
- [Bitcoin breaks lower range as pressure builds beneath 71K (Bitcoin.com)](https://news.bitcoin.com/bitcoin-breaks-lower-range-as-pressure-builds-beneath-71k)
- [Kalshi KXBTCMINMON BTC one-touch minimum market page](https://kalshi.com/markets/kxbtcminmon/btc-one-touch-minimum/kxbtcminmon-btc-26jan31)
- [Kalshi: How low will Bitcoin get this year (2025)](https://kalshi.com/markets/kxbtcminy/how-low-will-bitcoin-fall-this-year/kxbtcminy-25-2)
- [Kalshi CRYPTOMINMAXMONTHLY contract terms (PDF; not readable)](https://kalshi-public-docs.s3.amazonaws.com/contract_terms/CRYPTOMINMAXMONTHLY.pdf)
- [Kalshi crypto binary options research (oddsreference)](https://oddsreference.pages.dev/predictions/research/kalshi-crypto-binary-options)