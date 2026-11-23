# Research brief: will CRYPTOCAP:OTHERS print a 1-minute low at or below $150B between Nov 3, 2025 and Dec 31, 2026?

**Short version:** The question turns on one fact I could not check: where CRYPTOCAP:OTHERS is today, and whether it has already touched $150B. TradingView and every news page I tried to open were blocked, so I only saw search-result snippets. Crypto crashed on Nov 20–22, 2026, and the evidence suggests OTHERS is now somewhere between $130B and $175B. Before forecasting, someone should open the TradingView chart and look at (a) the current value, (b) the lowest 1-minute candle since Nov 3, 2025, especially around Feb 5–6, 2026 and Nov 20–22, 2026.

## 1. Resolution mechanics
- **What counts as YES:** any TradingView 1-minute candle on CRYPTOCAP:OTHERS with a final "Low" of $150B or less.
- **Window:** Nov 3, 2025, 11:00 AM ET to Dec 31, 2026, 11:59 PM ET. As of today (Nov 23, 2026) about 38 days are left, and the past ~12.7 months also count.
- **Who decides:** only TradingView's CRYPTOCAP:OTHERS chart (1m, Candles). Other indices, exchanges or data sites don't count.
- **What the index is:** the total crypto market cap minus the top 10 coins. TradingView, not the market, decides which coins are in the top 10.
  - USDT and USDC are in the top 10, so they are excluded. Smaller stablecoins such as USDe, DAI/USDS and PYUSD are counted in OTHERS and act as a partial floor.
  - The top-10 list changes over time, so the index can jump without real price moves.
- **Edge cases:**
  - **Bad-data wicks:** a single faulty 1-minute wick from a data error would technically count as YES. Aggregated indices sometimes show these during flash crashes.
  - **Changing chart data:** "final Low" suggests TradingView's data as it stands when the market is checked. If TradingView later revises old candles, that creates ambiguity.
  - **Already resolved?** If any candle since Nov 3, 2025 already went to $150B or below, this is effectively YES already. I could not confirm or rule this out (see §3 and §6).

## 2. Reference classes and base rates
1. **Touch-probability model (most relevant).** If OTHERS is now X% above $150B, the chance it touches $150B within ~38 days can be estimated from its volatility. I assume about 4–5% daily volatility in a stressed altcoin market, which gives σ√T ≈ 0.25–0.30 over 38 days. Using the standard estimate P(touch) ≈ 2·Φ(−ln(1+X)/σ√T), with no drift:

   | OTHERS today | Distance above $150B | Chance of touching by Dec 31 |
   |---|---|---|
   | ~$165B | 10% | ~65–72% |
   | ~$180B | 20% | ~40–45% |
   | ~$195B | 30% | ~18–25% |
   | ~$225B | 50% | ~6–10% |

   1-minute wicks push these numbers up a little. These are my own calculations, not from a source.
2. **Past bear-market lows.** In earlier cycles (2018–19 and 2022), OTHERS made its lowest point about 12–14 months after the cycle peak, often during a fast capitulation move. The comparable peaks are around Dec 2024 (one source cites a ~$451B peak in 2024) or Oct 2025, so a Q4 2026 low fits that timing. This is my interpretation, not a sourced statistic.
3. **The 2026 support zone.** Analysts said OTHERS held a $160B–$190B support band through "several tests through 2025 and 2026" over about 1,000 days (KuCoin flash, ~Sept 2026). Repeated tests of the same floor during a downtrend tend to end in a break. One analyst said a clean break below $150B–$160B could open a move toward about $100B (TradingView ideas, undated).

## 3. Current state of the world (most recent first)
- **Nov 21–23, 2026, the crash:**
  - Bitcoin touched about $55,130–55,150, its lowest since Sept 2024 and roughly 60% below its all-time high. It then bounced to about $58K–60.4K but was still down about 12.5% on the week (crypto.news; Archyde; Altcoinbuzz, Nov 21–23, 2026). Reported causes were expectations of Fed rate hikes, heavy outflows from Bitcoin ETFs and a tech-stock selloff.
  - Total crypto market cap fell below $2T for the first time in more than two years (CryptoPotato, ~Nov 22, 2026). About $2.7B of positions were liquidated (crypto.news).
  - ETH briefly hit $1,542.97 and recovered to about $1,706, its seventh straight losing week. SOL is under $70 and XRP about $0.92 (CryptoTicker, Nov 20, 2026; snippets citing CoinMarketCap). Bitcoin dominance is about 58.9%. FXStreet (Nov 23) says BTC, ETH and XRP "remain vulnerable as bears drive prices toward yearly lows."
- **Nov 20–21, 2026:** TOTAL3 (total market cap minus BTC and ETH) fell to about $639B, its lowest since Nov 7, 2024 (KuCoin insight posts citing Coinkolik, ~Nov 20–21, 2026). That means TOTAL3 is now below its February 2026 low.
  - I dated these KuCoin posts from their post-ID timestamps, so the dates are my inference.
- **~Nov 17, 2026:** a KuCoin community post says altcoin market cap "dropped below the 200-w[eek moving average]" (ID-dated).
- **Rough estimate of OTHERS today (my calculation, not sourced):** TOTAL3 at about $639B, minus the eight non-BTC/ETH top-10 coins, leaves roughly $130–175B. Those eight are USDT and USDC (stablecoins total about $284B per KuCoin), BNB, XRP (~$55B), SOL (~$39B), TRX, DOGE and one more, adding up to roughly $470–510B. This range is very uncertain, but it puts OTHERS at or close to $150B.
- **~Oct 11, 2026:** a KuCoin post says "$OTHERS … sitting at a m[ulti-year low?]". Only a fragment was visible.
- **~Sept 20, 2026:** OTHERS rose about 10–12% in a week to about $219.8B while testing a two-year downtrend line. It was up 38% in a month (which implies a base around $159B in Aug 2026) and down 32.6% year on year (Cryptorank; KuCoin flash).
- **~Aug 2026:** KuCoin "Altcoin Market Cap Support Zone" post: support at $160–190B.
- **~Feb 2026:** BTC crashed to about $60K. A TradingView idea dated about 271 days ago (late Feb 2026) says OTHERS "printed a multi-year low at ~$140B earlier this year" and was then about $180.8B, below its 200-week SMA of about $197.6B. Another Feb 2026 idea is titled "$170b OTHERS total."
  - If the $140B figure is right and falls in the window (Feb 2026 does), the question would already be YES. But it conflicts with the "support held at $160–190B" story.
- **Scheduled before Dec 31:** the FOMC meeting on about Dec 15–16, 2026 (the selloff is being tied to fears of rate hikes), plus US CPI and jobs data in early-to-mid December. Year-end liquidity is typically thin and weekends often bring liquidation cascades, which favors 1-minute wicks.

## 4. Drivers and scenarios
**Paths to YES:**
- It has already happened: in the Feb 2026 crash, the Nov 20–22 crash, or another wick since Nov 2025. This is plausible given the $140B claim and my estimate of where OTHERS is now.
- The selloff continues: BTC falls below $55K, ETH below $1,500, and long-tail tokens fall faster than the majors, as they usually do. A further 5–20% drop in OTHERS from current levels may be enough.
- A liquidation cascade or exchange incident produces a 1-minute wick.
- A coin falling out of the top 10 adds to OTHERS (it would then be counted), but a coin rising into the top 10 removes its value from OTHERS. Either can shift the index mechanically.

**Paths to NO:**
- OTHERS never went below $150B (the $140B claim was wrong or used a different measure), and the late-November bounce holds. This would come from BTC recovering to $65–72K and the Fed being less hawkish than feared.
- Smaller stablecoins inside OTHERS and the year-end calendar keep the index cushioned for the remaining ~38 days.

## 5. Signposts
- **Biggest single factor:** the actual lowest 1-minute OTHERS candle since Nov 3, 2025. At or below $150B means resolved YES; around $155–165B means high odds; $175B or more means much lower odds.
- **Toward YES:** BTC losing $55K, ETH losing about $1,540, continued ETF outflows, more stablecoin supply shrinking, hawkish Fed comments, a jump in liquidations.
- **Toward NO:** BTC back above about $65K, ETF inflows resuming, OTHERS getting back above its 200-week SMA (around $195B).

## 6. Uncertainties
- **The current OTHERS value and the low since Nov 2025.** These could not be obtained because TradingView and the news sites were blocked; most numbers above come from search snippets with dates I inferred.
- **The ~$140B low "earlier this year" (posted ~Feb 2026).** It is unconfirmed, it may be on a different scale or a misreading, and it conflicts with the claim that $160–190B support held through 2026.
- **Dates of some search results.** Several snippets may have mixed up 2025 and 2026; I dated the KuCoin posts from their ID timestamps.
- **The top-10 composition and stablecoin amounts** that feed my OTHERS estimate are approximate.
- **The volatility figure** used in §2 is assumed, not measured.

## Sources
- [Bitcoin price stalls near $60K as Pi Network rebounds, VVV jumps 20% (crypto.news)](https://crypto.news/bitcoin-price-pi-network-vvv-weekend-recovery/)
- [Bitcoin price rebounds from $55K after historic sell-off (crypto.news)](https://crypto.news/bitcoin-price-rebounds-55k-2-7b-liquidations)
- [Bitcoin Fell Below $56,000 on November 22, 2026 (Archyde)](https://archyde.com/bitcoin-fell-below-56000-on-november-22-2026-dropping-nearly-60-from-its-all-time-high)
- [Bitcoin Falls Below $56,000 as Crypto Sheds $90 Billion (Altcoinbuzz)](https://www.altcoinbuzz.io/bitcoin-falls-below-56-000-as-crypto-sheds-90-billion)
- [Crypto Market Cap Dumps Below $2T (CryptoPotato)](https://cryptopotato.com/crypto-market-cap-dumps-below-2t-as-bitcoin-rollercoaster-intensifies-weekend-watch/)
- [Ether below $1,700, Solana below $70 (CryptoTicker)](https://cryptoticker.io/en/ether-below-1700-solana-below-70-altcoins-crash/)
- [Top 3 Price Prediction: BTC, ETH, XRP (FXStreet, Nov 23, 2026)](https://fxstreet.com/cryptocurrencies/news/top-3-price-prediction-bitcoin-ethereum-ripple-btc-eth-and-xrp-remain-vulnerable-as-bears-drive-prices-toward-yearly-lows-202611230352)
- [The altcoin market has dropped to its lowest level since… (KuCoin insight)](https://www.kucoin.com/news/insight/BTC/6b00dce49278e40007d8e23e)
- [Altcoin market capitalization has fallen to its lowest level (KuCoin insight)](https://www.kucoin.com/news/insight/BTC/6b0090049278e40007d8d8ed)
- [Total market cap of altcoins dropped below the 200-w (KuCoin community)](https://www.kucoin.com/news/community/ALT/6afbbca0e5453b00076de2c7)
- [$OTHERS sitting at a m… (KuCoin insight)](https://www.kucoin.com/news/insight/BTC/6acb782444c2130007892aeb)
- [Altcoin Market Cap Rises 10% as It Tests 2-Year Downtrend Breakout (KuCoin)](https://www.kucoin.com/news/flash/altcoin-market-cap-rises-10-as-it-tests-2-year-downtrend-breakout)
- [Altcoin Market Cap Rallies 12% as Two-Year Downtrend Faces First Major Breakout Attempt (Cryptorank)](https://cryptorank.io/news/feed/2a2f1-altcoin-market-cap-rallies-12-as-two-year-downtrend-faces-first-major-breakout-attempt)
- [Altcoin Market Cap Support Zone (KuCoin Square)](https://www.kucoin.com/square/post/content_6a7c1936ef28ee000771bd47)
- [Stablecoin market cap falls to $284.215 billion (KuCoin)](https://www.kucoin.com/news/flash/stablecoin-market-cap-drops-to-284-215-billion-lowest-since-year-start)
- [CRYPTOCAP:OTHERS Ideas (TradingView)](https://www.tradingview.com/symbols/OTHERS/ideas/)
- [Total Altcoin Market Cap — Chart and Ideas (TradingView)](https://www.tradingview.com/symbols/OTHERS/)
- [Is the OTHERS Chart Signaling Change for Altcoins? (CoinDailies)](https://coindailies.com/news/others-chart-altcoins-reversal-trends-2026/)