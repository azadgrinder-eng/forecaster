# Research brief: Will Bitcoin trade below $45,000 (CF BRTI) between Feb 5, 2026 and Jan 1, 2027 00:00 ET?

## 1. Resolution mechanics

- **What counts as YES:** the CF Bitcoin Real-Time Index (BRTI) prints below $45,000.00 at any point from Feb 5, 2026 to before Jan 1, 2027 at 12:00am ET (05:00 UTC). The rules say that if BRTI "crosses the threshold at any point," the market resolves early and immediately. In practice this is a one-touch barrier. About 40 days of 24/7 trading remain from Nov 22.
- **Who decides:** the exchange's settlement against CF Benchmarks' BRTI. BRTI combines order books from several constituent USD exchanges, so a sharp drop on a single exchange may not show up fully in the index. The rules talk about "BRTI values for each minute," so the trigger is probably minute-level index values, not single trades or intraday wicks on one exchange. Expect a touch on BRTI to need a market-wide move to roughly $44,9xx.
- **Ambiguity in the rules:** the text also describes a trimmed mean: all minute values from issuance, top and bottom 20% removed, the middle 60% averaged. Read literally, that average covers Feb to Dec 2026, when BTC mostly traded around $60k–$90k+, so it could never fall below $45k and the answer would be almost certainly NO. The title ("below $45,000 by Jan 1"), the early-expiration clause, and the "can resolve early if Bitcoin definitively crosses" clause all point to a touch market. The trimmed-mean paragraph looks like generic boilerplate. Forecasters should assume touch-based resolution, with a small discount for this ambiguity.
- **Already triggered?** No. The 2026 lows since Feb 5 are about $60,000 (Feb 6), about $57,700–57,800 (early July), and about $55,100–55,600 (Nov 20–21). None is below $45k (Bloomberg, Feb 6 2026; Trading Economics, Jul 2026; Altcoinbuzz, Nov 21 2026).
- **Missing data:** "If no data is available at the expiration time, the market resolves to No."

## 2. Reference classes and base rates

**A. Volatility-implied barrier probability.** This uses a driftless lognormal model, where P(touch) ≈ 2·N(ln(K/S)/(σ√T)), with S ≈ $60,000, K = $45,000 (a 25% drop, ln = −0.288), and T = 40/365.

| Annualized vol | P(touch $45k) from $60k | From $56k |
|---|---|---|
| 40% (DVOL around Nov 13) | ~3% | ~9% |
| 50% | ~8% | ~19% |
| 60% | ~15% | ~27% |
| 70% | ~21% | ~33% |

DVOL was 40.8 on Nov 13 and averaged 42.4 so far in 2026, the lowest annual average since 2021 (Coinotag/CryptoQuant, Nov 13 2026). It has almost certainly jumped since, after a ~9% one-day drop and $1.5–2B of liquidations on Nov 20–21. I found no reading after Nov 13. BTC returns have fat tails, so the lognormal model probably understates the chance of a crash-style touch. On the other hand, implied vol has historically overpriced realized vol about 74% of the time since 2022, by a median 10.5 points (CryptoQuant, Nov 2026).

**B. Late-bear-market capitulation legs.** These figures come from my own historical knowledge and are approximate.
- 2014–15 cycle: peak in Nov 2013. A capitulation in Jan 2015, about 14 months later, took BTC from roughly $320 to $170, about −47% in weeks.
- 2018 cycle: peak in Dec 2017. In Nov–Dec 2018, about 11–12 months later, BTC fell from about $6,300 to $3,200, roughly −49% in about 32 days.
- 2022 cycle: peak in Nov 2021. The FTX collapse in Nov 2022, about 12 months later, took BTC from about $21k to $15.5k, roughly −27% in about a week. The June 2022 leg fell about −43% in roughly 3 weeks.

All three prior cycles had a ≥25% capitulation leg about 11–14 months after the peak. The current peak was about $126k in early October 2025, which puts the analog window in October 2026 to January 2027, i.e. now. Some analysts explicitly projected a Q4 2026 bottom (Cointelegraph, "Here's Why Bitcoin Analysts Say BTC Market Will Bottom in Q4 2026"). Treat this as a weak, small-sample pattern (n=3).

**C. Rolling 40-day windows with a ≥25% drawdown from the start price.** I could not find a direct statistic. As a rough estimate from price history, about 10–15% of all 40-day windows since 2017 contain such a drop, and roughly 20–30% of windows in bear years (2018, 2022). For context: BTC has had more than 10 declines of 25% or more since 2017 (Kobeissi via Blockchain.News), and has crossed a 30% drawdown 21 separate times (Algorithmic Guys Substack). Drawdowns from cycle peaks have shrunk over time: about 86% → 84% → 77%/74% in 2022 (CryptoQuant via Decrypt). A move to $45k would be about −64% from the ~$126k ATH, which is shallower than any prior bear-market bottom.

## 3. Current state of the world (most recent first)

- **Nov 22, 2026:** BTC is around $60,000–60,300 after a weekend rebound. Overnight on Nov 21 it fell to about $55,000, then recovered above $60k. "Extreme fear" sentiment (GitHub crypto briefing, Nov 22; Eurasia Business News, Nov 21).
- **Nov 21:** Intraday low about $55,150, the weakest since September 2024. BTC traded around $55,842 at one point (−9.2% in 24h) before rebounding to about $60.4k (CoinDesk quote ~3:42pm ET). More than $1.5–1.8B in crypto liquidations, mostly leveraged longs (Altcoinbuzz, Nov 21; CoinDesk, Nov 21). Coinbase showed about $60,172, down 6% on the week.
- **Nov 20:** Reuters and Bloomberg: BTC hit a 2-year low, as low as $57,716 in their reporting, and broke below the July cycle low (~$57,800) and the 200-week moving average (~$68k). Cited causes: concern over AI-capex profitability, rising rates, the Democratic midterm sweep raising regulatory and AI-scrutiny fears, and Nvidia CEO Jensen Huang's departure (Reuters via Investing.com, Nov 20; Bloomberg, Nov 20).
- **Nov 19:** BlackRock's IBIT had a record $541M one-day outflow, and the spot-ETF complex lost $582M. Another ~$124.5M partial-day outflow followed on Nov 20. Cumulative spot ETF outflows were about $2.34B through Nov 16 (TFTC, Nov 2026).
- **Nov 15–21, Strategy (MSTR):** Strategy holds 850,849 BTC at an average cost of about $75,452, so its position is underwater. It sold $244.7M of MSTR stock from Nov 9–15, mostly to buy back preferred shares. Saylor said Strategy "can even sell bitcoin to buy STRC" and could shrink STRC to $5B. It reports a $35B "net reserve." MSTR is down about 44% in a month to roughly $78–80. **MSCI is removing Strategy from its global indexes effective after the close on Nov 30, 2026**, with estimates of up to $8.8B in passive selling (Yahoo Finance; Analytics Insight; Invezz, Nov 12; CryptoNews, Nov 2026).
- **Mid-Nov, macro:** The Nasdaq is in correction, about 12% below its Oct 6 ATH, after its worst single day since April 2025. The Fed hiked in September 2026, held in October, and as of mid-November futures priced a ~70–80% chance of another hike at the **Dec 8–9 FOMC** (Khaleej Times/Reuters, Nov 2026).
- **Nov 13:** BTC fell below $70k, its lowest since August (Forbes, Nov 13). It was about $75k on Nov 8 (Coinglass history).
- **On-chain reference levels:** realized price is about $53,700 (Glassnode via CoinStats) and the June low was about $58,500. Earlier in 2026, Willy Woo placed a likely bottom between realized price (~$54k) and the CVDD floor (~$45.5k). BitMEX Alpha noted that a 65% drawdown from the peak means about $44k, and that past bears ended at drawdowns of 73% or more. PlanB said BTC would "likely bottom below" realized price. On-chain models collectively ranged $40k–$54k (Cointelegraph; Bitbo; Bitcoin Foundation, Mar–Jul 2026).
- **Current analyst targets:** Wintermute calls the $50k zone decisive (cryptoticker). Arthur Hayes says $50k is "in play" if the Nasdaq keeps falling (Yahoo Finance). A CryptoQuant contributor's wave model ends near $50k (CryptoNews).

**Scheduled before close:** Deribit monthly expiry Nov 27 (analysts watch a DVOL close above 45 before it). MSCI's Strategy exclusion takes effect after the Nov 30 close. US CPI and jobs data in early December. FOMC Dec 8–9. Large Deribit quarterly expiry Dec 25 (a DVOL move above 50 before it was flagged as a repricing signal). Thin holiday liquidity in late December.

## 4. Drivers and scenarios

**Paths to YES (≥25% further drop):**
1. **Capitulation cascade.** Price breaks the Nov 21 low (~$55k) and realized price (~$53.7k), triggering stop-losses and liquidations down to the CVDD/$45k area. This matches the analog of past cycles 11–14 months after the peak.
2. **Strategy stress.** MSCI-driven selling of MSTR, a falling mNAV, and STRC pressure lead to an actual BTC sale, or the fear of one. That would be a large reflexive shock, since Strategy holds about 4% of supply and its average cost is far above spot.
3. **Macro or AI-equity crash.** A Fed hike on Dec 9 plus a deeper Nasdaq/AI unwind cuts liquidity further, and ETF outflows speed up from the record $541M day.
4. **Idiosyncratic shock** such as an exchange failure, regulation from the new Democratic Congress, or a hack.

**Paths to NO:**
1. Realized price and $55k hold as support. The quick rebound from $55k to $60k suggests dip-buying. Extreme fear and heavy long liquidations often mark local lows.
2. The Fed skips the hike, or equities stabilize, and BTC chops between $55k and $70k into year-end.
3. Analysts' "bottom" targets cluster at $50–54k. A drop to about $50k would cause big losses but would not trigger this market.
4. Time is short: 40 days. Even in bear years, most 40-day windows do not include a 25% drop.

## 5. Signposts

- **Raise the probability sharply:** a daily close below $53–54k (realized price) or a break of the Nov 21 low near $55k. Any Strategy announcement of a BTC sale or STRC distress. Daily ETF outflows above $500M continuing. A hawkish Fed hike on Dec 9 together with a Nasdaq drop of more than 15% from its high. DVOL above 60. A crypto-lender or exchange failure.
- **Lower the probability:** BTC reclaiming $65–68k (the 200-week moving average). ETF flows turning positive. MSCI rebalancing passing without a cascade. The Fed holding or signaling a pause. DVOL falling back to the low 40s. As time passes without a touch, the probability decays roughly with √T.
- **Mechanical:** each week without a new low removes about 15–20% of the remaining touch probability, all else equal.

## 6. Uncertainties

- **Exact spot price on Nov 22.** Sources range from $55.8k to $61.8k depending on the timestamp. The best estimate is about $60k. I could not access primary price pages directly; the proxy refused several fetches.
- **Current implied volatility** after the Nov 20–21 crash. The last confirmed DVOL is 40.8 on Nov 13.
- **Exact BRTI low** on Nov 20–21. It is likely around $55.2–55.6k.
- Whether the **trimmed-mean language** has any effect on settlement. It almost certainly does not for a touch market, but the text is internally inconsistent.
- Size and timing of **MSCI-related passive selling** and Strategy's real willingness to sell BTC.
- The **Fed's December decision**, and whether the "Jensen Huang departure" and AI-capex story deepens.
- I could not find a sourced rolling-window frequency of ≥25% drops within 40 days. The figures in section 2C are rough estimates.

## Sources
- [Current price of Bitcoin for November 20, 2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-20-2026/)
- [Bitcoin price today, BTC to USD (CoinDesk)](https://www.coindesk.com/price/bitcoin)
- [Bitcoin Falls Below $56,000 as Crypto Sheds $90 Billion (Altcoinbuzz)](https://altcoinbuzz.io/bitcoin-falls-below-56-000-as-crypto-sheds-90-billion)
- [Bitcoin Price Today, November 21, 2026: BTC Rebounds Above $60,000 (Eurasia Business News)](https://eurasiabusinessnews.com/2026/11/21/bitcoin-price-today-november-21-2026-btc-rebounds-above-60000-as-solana-leads-crypto-gains/)
- [Bitcoin Price Today (Coinglass)](https://www.coinglass.com/currencies/BTC)
- [Bitcoin (BTC) Price (Coinbase)](https://www.coinbase.com/price/bitcoin)
- [Bitcoin falls to its lowest in two years (Reuters via Investing.com)](https://www.investing.com/news/forex-news/bitcoin-falls-357-to-56814-5043137)
- [Bitcoin Falls to More than Two-Year Low as Global Markets Sink (Bloomberg)](https://www.bloomberg.com/news/articles/2026-11-20/bitcoin-falls-to-more-than-two-year-low-as-global-markets-sink)
- [Bitcoin Falls Below $70,000 To Reach Lowest Since August (Forbes)](https://www.forbes.com/sites/digital-assets/2026/11/13/bitcoin-falls-below-70000-to-reach-lowest-since-august/)
- [Bitcoin Plunges to $55,000, Then Reclaims $60,000 (GitHub crypto briefing, Nov 22)](https://github.com/elixirevo/agentic-blog/releases/tag/post-2026-11-22-crypto-briefing)
- [Bitcoin selloff explained (Bloomberg, Feb 6 2026)](https://www.bloomberg.com/news/articles/2026-02-06/bitcoin-selloff-explained-what-triggered-the-crypto-selloff-and-what-comes-next)
- [Bitcoin Slides to Nearly 2-Year Low (Trading Economics)](https://tradingeconomics.com/btcusd:cur/news/563281)
- [Bitcoin price analysis: BTC breaks the July low, is $50,000 next? (cryptoticker)](https://cryptoticker.io/en/bitcoin-price-analysis-july-low-50000/)
- [Bitcoin price prediction: summer low broken, record losses (cryptoticker)](https://cryptoticker.io/en/bitcoin-price-prediction-summer-low-57700-capital-underwater/)
- [Bitcoin (BTC) News Today (CoinStats)](https://coinstats.app/ai/a/latest-news-for-bitcoin)
- [Arthur Hayes Says Bitcoin's Break Below Local Low Puts $50,000 In Play (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/arthur-hayes-says-bitcoins-break-035344264.html)
- [Bitcoin Faces $50K Risk as Analyst Maps Bear Market Correction (CryptoNews)](https://cryptonews.net/news/bitcoin/33768884/)
- [Bitcoin options DVOL 40.8 (Coinotag)](https://en.coinotag.com/bitcoin-btc-options-volatility-dvol-40-8-half-norm-drawdown)
- [Bitcoin options calmest year, Deribit DVOL (Crypto Briefing)](https://cryptobriefing.com/bitcoin-options-calmest-year-deribit-dvol/)
- [CryptoQuant Quicktake: Options price half the usual selloff fear](https://cryptoquant.com/insights/quicktake/6af698efcd57dd300eaa6e6e-Bitcoin-Is-17-Off-Its-30-Day-High-and-Options-Price-Half-the-Usual-Selloff-Fear)
- [IBIT Posts Record $541M Single-Day Outflow (TFTC)](https://www.tftc.io/ibit-record-541m-outflow-bitcoin-etf-november-2026)
- [Strategy Is Down 44% in a Month (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/strategy-down-44-month-crypto-200235875.html)
- [MSCI Removes Strategy from Global Indexes (Analytics Insight)](https://www.analyticsinsight.net/cryptocurrency-analytics-insight/msci-removes-strategy-from-global-indexes-as-bitcoin-slides-and-mstr-faces-potential-selling)
- [MSCI moves to exclude Strategy (Invezz)](https://invezz.com/news/2026/11/12/msci-moves-to-exclude-strategy-could-bitcoin-price-crash-to-70000/)
- [Saylor Says Strategy Could Shrink STRC to $5B and Even Sell Bitcoin (CryptoNews)](https://cryptonews.net/news/bitcoin/33782807/)
- [Trader angst pivots from inflation to growth as tech rout deepens (Khaleej Times)](https://www.khaleejtimes.com/business/trader-angst-pivots-from-inflation-to-growth-as-tech-rout-deepens)
- [Wall St Week Ahead: As tech swoon roils market, US inflation data on tap (Khaleej Times)](https://www.khaleejtimes.com/business/wall-st-week-ahead-as-tech-swoon-roils-market-us-inflation-data-on-tap-3)
- [Bitcoin Will 'Likely Bottom Below' Its $53,000 Realized Price (Cointelegraph)](https://cointelegraph.com/markets/bitcoin-is-just-a-5k-drop-away-from-its-best-investment-opportunity-analysis)
- [Here's Why Bitcoin Analysts Say BTC Market Will Bottom in Q4 2026 (Cointelegraph)](https://cointelegraph.com/markets/bitcoin-to-30k-analysts-debate-when-what-price-btc-price-will-bottom)
- [Analysts: Bitcoin Models Point to $40K–$50K Potential Bottom (Bitbo)](https://bitbo.io/news/bitcoin-models-40k-50k-bottom/)
- [BitMEX Says Bitcoin Bottom May Sit at $45K (Bitcoin Foundation)](https://bitcoinfoundation.org/news/bitcoin/bitmex-says-bitcoin-bottom-may-sit-at-45k/)
- [This is Bitcoin's shallowest bear market (Decrypt)](https://decrypt.co/370495/this-is-bitcoins-shallowest-bear-market-but-is-the-%25253D)
- [Living in Drawdown: Bitcoin's Pain Profile (Algorithmic Guys Substack)](https://algorithmicguys.substack.com/p/anatomy-of-bitcoin-drawdowns)
- [Bitcoin drawdown stats since 2017 (Blockchain.News)](https://blockchain.news/flashnews/bitcoin-btc-drawdown-stats-since-2017-10-25-6-50-3-75)