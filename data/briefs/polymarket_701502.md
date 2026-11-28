# Research brief: will Binance BTC/USDT trade at or below $45,000 between Nov 24, 2025 and Dec 31, 2026?

## 1. Resolution mechanics

- **What counts as YES:** any Binance BTC/USDT 1-minute candle with a final Low of $45,000.00 or less. The window runs from Nov 24, 2025 14:00 ET to Dec 31, 2026 23:59 ET.
  - The market resolves YES immediately when that happens. Otherwise it resolves NO after the window ends (close date Jan 1, 2027 05:00 UTC, which is midnight ET).
- **Only one source counts:** Binance BTC/USDT. Coinbase, BTC/USD, index prices and futures do not count. A brief wick on Binance alone would be enough, and Binance's USDT book has sometimes printed lower lows than USD venues during liquidation cascades.
- **Where things stand:** no Binance low has come near $45,000 yet. The deepest lows in the window were about $60,000 on Feb 5–6, 2026 and about $55,130–55,250 on Nov 21, 2026. Venue-specific figures differ by a few hundred dollars. So YES requires a new low within the roughly 34 days left (Nov 28 to Dec 31).
- **Edge cases:**
  - A flash crash or bad print on Binance only would technically count.
  - A USDT depeg could distort BTC/USDT relative to BTC/USD. If USDT fell, BTC/USDT would rise, which works against YES.
  - The end time is in ET, so trading through New Year's Eve evening in the US counts.

## 2. Reference classes and base rates

**A. Volatility model (driftless lognormal, probability of touching the level)**
- Reference spot is about $60,000 (Nov 27 range: $59.6k–$61.5k). $45,000 is about 25% below, ln(0.75) = −0.288. The horizon is about 34/365 of a year.
- Results by annualized volatility:

| Volatility | 34-day σ | Probability of touching $45k |
|---|---|---|
| 40% | 0.122 | ≈ 2% |
| 50% | 0.153 | ≈ 6% |
| 60% | 0.183 | ≈ 11–12% |

- From $61.5k at 50% vol the figure is about 4%; from $57k it is about 9%.
- Deribit DVOL (30-day implied vol) averaged 42.4 in 2026 through early November and sat at 37–41 in mid-November (Cryptobriefing / CryptoQuant, Nov 2026). It has probably risen after the Nov 21 crash, but I could not find a late-November reading. Bitcoin's fat tails mean a lognormal model understates this kind of risk.

**B. Historical ~1-month drops of 25% or more (my rough count from memory, 2018–2026)**
- Episodes where BTC fell at least 25% within about 5 weeks:
  - Nov–Dec 2018
  - March 2020
  - January 2021
  - May 2021
  - June 2022
  - November 2022 (FTX, about 26%)
  - August 2024 (about 30%)
  - January–February 2026 (about $90k to $60k)
  - November 2026 (about $80k+ to $55k)
- That is roughly 9–10 episodes in about 8 years, or 1.2 per year. Since only some starting days in each episode qualify, about 6–10% of random 34-day windows would see a 25% drop from the starting price. In bear-market years (2018, 2022, 2026) the rate is higher, around 10–15%.

**C. Second leg after a capitulation (closest analogs)**
- After a bear-market liquidation crash and a 5–10% bounce, the next leg down within about 5 weeks has usually been about 20–24%, short of 25%. Approximate figures:
  - Late Nov 2018: about $4.2k to $3.2k by Dec 15, roughly −24%.
  - Late May 2021: about $35–37k to $28.8k on Jun 22, roughly −20–23%.
  - After June 2022 and after FTX in Nov 2022: no further 25% drop.
- So follow-on drops of about 20% are common, but 25% is at the edge. A 20–24% drop from here would mean a $46–48k low, just above $45k.

## 3. Current state of the world (most recent first)

**Price action**
- **Nov 27, 2026:** BTC around $59.8k–$61.5k. Intraday it rallied to $62,249, then faded to about $59,830 (crypto.news). Rio Times had it at $61,482 (+1.6%), about 29% below its September 2026 high. A $6.8B Deribit options expiry was due that day (crypto.news, Nov 27).
- **Nov 25–26:** low about $57,200–57,300, then an 8% bounce to $61,780. Yahoo Finance tied the dip to hot inflation data that it said "sealed" a December Fed hike. It named support at $60k (the June/July floor) and resistance at $64.6k. Fortune's morning price on Nov 25 was $58,564 (Yahoo Finance; Fortune, Nov 25; Univest, Nov 26).
- **Nov 21:** cycle low of about $55,130–55,250, the lowest since September 2024. It broke the 2026 low from June 30/July 1 (about $57.7–57.8k) after $1.9–2.7B of liquidations, alongside a sell-off in stocks and gold. Price then bounced above $60k (Coinpaper; CoinJar; World Today News; CoinGlass, Nov 21–22).
- **Nov 12–13:** BTC fell to $71k on Nvidia and Strategy worries plus Fed tightening fears, then went below $70k for the first time since August (Forklog, Nov 13).
- **Early November:** BTC slipped below $80k ahead of the Fed meeting and the Nov 3 midterms (Decrypt).

**Flows and sentiment**
- November spot-ETF outflows were a record, about $5.39B by one count (Yahoo Finance / Univest, late Nov).
- CoinDesk said BTC was on course to end a seven-week losing streak.
- Grayscale called the market oversold (cryptonews.net, Nov 2026).

**Analyst levels**
- Wintermute and Benjamin Cowen see a possible $50–54k bottom.
- Glassnode reports the strongest buy-side liquidity since August in the $50–58k band (TokenPost / Coinpaper, late Nov).
- Support levels cited: $55,150, $53,949 and $50,000.
- EGRAG Crypto's bear case is a $45–50k macro bottom (KuCoin; 36Crypto).
- The realized price (holders' average cost) was about $52–53.5k in mid-2026. Past bear markets have usually traded below realized price before bottoming (Cointelegraph; CryptoSlate, ~June 2026). This is the main argument that the low can still fall into the high $40s.

**Cycle context**
- The all-time high was about $126.2k on Oct 6, 2025.
- The Nov 21 low is about 56% below that peak. Past bear-market drawdowns were about 77% in 2022 and 84% in 2018, so a deeper drawdown is historically normal, but probably over more than a month.
- The 2026 high was about $97–98k in mid-January.

**Macro**
- A Morningstar preview says the Fed hiked in September 2026 (its first hike in three years) to 3.75–4.00%. Markets were pricing about a 75% chance of a hike by December. Sources conflict on the current rate range.
- The FOMC meets Dec 8–9, 2026 (Kiplinger; MNI).

**Strategy (MSTR)**
- Management has said it would sell BTC only as a last resort if mNAV stays below 1x for a long time and it can't raise capital. It holds a dollar reserve of about $1.44B (Yahoo Finance / Pepperstone, earlier reports).
- I found no November 2026 reports of forced selling.

**Scheduled before close:** FOMC decision Dec 9 (with CPI around Dec 10, date unverified); late-December quarterly options expiry (Dec 25 falls on Christmas, so probably Dec 24); thin holiday liquidity in late December.

## 4. Drivers and scenarios

**Paths to YES (low of $45k or less on Binance by Dec 31)**
1. **Capitulation leg below realized price:** BTC loses $55k and the $50–54k band, and stops are triggered below $50k. This depends on continued ETF outflows (another week of $1B+), a hawkish Dec 9 hike with hawkish guidance, and a renewed AI/tech equity sell-off.
2. **Credit or contagion shock:** a forced seller emerges, such as a treasury company (Strategy or a smaller one), a miner, a lender or an exchange. It could also be a stablecoin problem. Liquidation cascades have produced 10–15% intraday wicks before.
3. **Thin-liquidity wick:** a flash crash on Binance during holiday trading. This needs the price already near $50k to be plausible.

**Paths to NO**
1. **Base holds:** the Nov 21 low proves to be local capitulation, consistent with oversold readings and the strong $50–58k bid zone, and BTC trades in a $55–65k range into year-end.
2. **Drop stops short:** another leg falls to $48–52k, which is the most likely "bad" outcome and stops above $45k.
3. **Relief rally:** a dovish surprise or a Fed hike that is already fully priced, plus equities recovering.

**Key dependency:** YES needs a roughly 25% decline from about $60k in about 34 days. That is about 1.6–2.4 standard deviations depending on volatility, and bigger than most second legs historically.

## 5. Signposts

**Toward YES (large moves)**
- A daily close below $55k, the Nov 21 low. That cuts the remaining distance to about 18%.
- A break below $50k, after which $45k is only 10% away.
- DVOL jumping above 60.
- ETF outflows continuing at more than $1B a week.
- A hawkish FOMC surprise on Dec 9, or a sharp drop in the Nasdaq or AI stocks.
- Strategy's mNAV falling below 1 or any hint of BTC sales; stress at a miner, treasury company or exchange.
- A large USDT premium or discount on Binance.

**Toward NO**
- BTC reclaiming $64.6k, the top of the June–August range.
- ETF inflows returning.
- The FOMC passing without a sell-off.
- Implied volatility staying around 40.
- Every passing day without a new low, since time decay is steep in a 34-day window.

## 6. Uncertainties

- **Exact Binance figures:** I could not confirm the exact Binance BTC/USDT lows (sources give $55,130–55,600 for Nov 21) or the Nov 28 price. Page fetches were blocked, so everything here comes from search summaries, which sometimes conflicted.
- **Current volatility:** no DVOL reading after the crash was available. Mid-November readings (37–41) are probably understated now.
- **Fed path:** the rate path and range for late 2026 conflict across sources. Whether a December hike is fully priced is unclear.
- **Strategy:** current mNAV, holdings and financing stress for November 2026 are unverified, with conflicting figures (650k vs. 843k BTC).
- **Historical counts:** the frequencies in section 2 are approximate, reconstructed from memory of past episodes rather than computed from a dataset.
- **Unchecked factors:** Binance-specific risks (regulation, wick behavior) and USDT conditions in late 2026 were not checked.

## Sources
- [Bitcoin Rises 1.63% to US$61,482 as Stocks Rally (Rio Times)](https://riotimesonline.com/crypto-markets-bitcoin-majors-friday-november-27-2026)
- [Bitcoin reclaims $61,000 as Chainlink leads the week (Company Chronicle)](https://thecompanychronicle.com/story/crypto-prices-today-november-27-2026)
- [Bitcoin Price Today: 60,948 Dollar Close, ETF Outflows (Univest)](https://univest.in/blogs/bitcoin-price-today-60948-dollars-etf-outflows-death-cross-options-expiry-key-levels-26-november-2026)
- [Current price of Bitcoin for November 25, 2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-25-2026/)
- [Bitcoin News Today: BTC Rebounds 8% (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/bitcoin-news-today-btc-rebounds-104410814.html)
- [Bitcoin price slips below $60K as traders watch $55K (crypto.news)](https://crypto.news/bitcoin-price-slips-below-60k-traders-watch-55k/)
- [Bitcoin price reclaims $61K ahead of $6.8B options expiry (crypto.news)](https://crypto.news/bitcoin-price-rebounds-68b-options-expiry-november-27/)
- [Bitcoin Price in 2026 (CoinGlass)](https://www.coinglass.com/currencies/BTC/historical-data/2026)
- [Bitcoin just hit a new 2026 low of $55,150 (KuCoin)](https://www.kucoin.com/news/insight/BTC/6b04dd589278e40007d94223)
- [Why Is Bitcoin Crashing Today? BTC Hits $55K as $2.5B Wiped Out (Coinpaper)](https://coinpaper.com/39174/why-is-bitcoin-crashing-today-btc-hits-55-k-as-2-5-b-wiped-out)
- [Bitcoin drops to $55,000 as Wall Street heads for the exit (CoinJar)](https://www.coinjar.com/blog/bitcoin-drops-to-55000-as-wall-street-heads-for-the-exit)
- [Bitcoin Dropped to $55,000 on November 21, 2026 (World Today News)](https://www.world-today-news.com/bitcoin-dropped-to-55000-on-november-21-2026-marking-its-lowest-valuation-in-over-two-years/)
- [Bitcoin falls to $55,000, Grayscale cites oversold market (cryptonews.net)](https://cryptonews.net/news/bitcoin/33804714/)
- [Bitcoin flash crashes to $60,000 (The Block, Feb 2026)](https://www.theblock.co/news/markets/2026-02-05-bitcoin-sees-flash-crash-60000-388759)
- [Crypto market loses $265 billion as Bitcoin dips to $60,000 (FXStreet)](https://www.fxstreet.com/amp/cryptocurrencies/news/crypto-market-loses-265-billion-as-bitcoin-dips-to-60-000-amid-bearish-sentiment-202602060534)
- [Bitcoin falls below $70,000 for first time since August (Forklog)](https://www.forklog.com/en/news/bitcoin-falls-below-70000-for-first-time-since-august)
- [Bitcoin dips below $80,000 ahead of Fed decision, midterms (Decrypt)](https://decrypt.co/381802/bitcoin-dips-below-80000-ahead-of-fed-decision-midterms%2A)
- [Bitcoin Price Dips Below $57,000 as Analysts Predict $50,000–$54,000 Bottom (KuCoin)](https://www.kucoin.com/news/flash/bitcoin-price-dips-below-57-000-as-analysts-predict-50-000-54-000-bottom)
- [Bitcoin Buyers Form $50,000-$58,000 Support Zone (TokenPost)](https://www.tokenpost.com/news/investing/63644)
- [Bitcoin Price Could Bottom at $45K (36Crypto)](https://36crypto.com/bitcoin-price-could-bottom-at-45k-as-analyst-reveals-critical-50k-support-level/)
- [Bitcoin options calmest year, Deribit DVOL (Cryptobriefing)](https://cryptobriefing.com/bitcoin-options-calmest-year-deribit-dvol/)
- [CryptoQuant Quicktake on BTC options implied vs realized vol](https://cryptoquant.com/insights/quicktake/6ae935c44d08081b8394da24-Bitcoin-Options-Charge-368-Volatility-for-214-Delivered-Realized-Caught-Up-1-in-)
- [What to Expect from the October 2026 Fed Meeting (Morningstar)](https://www.morningstar.com/markets/what-expect-october-2026-fed-meeting)
- [October 2026 Fed Meeting: Live Updates (Kiplinger)](https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026)
- [MNI Fed meeting calendar](https://www.mnimarkets.com/events/104452-X)
- [Will Michael Saylor Do the Unthinkable? (Yahoo Finance)](https://finance.yahoo.com/news/michael-saylor-unthinkable-mstr-ceo-185018018.html)
- [Bitcoin treasury entity risk explained (Pepperstone)](https://pepperstone.com/en-au/insights/market-analysis/crypto/bitcoin-treasury-entity-risk-explained-why-strategy-mstr-matters-as-btc-slides)
- [Bitcoin price just tagged 200-week trend line (Cointelegraph)](https://cointelegraph.com/news/bitcoin-price-just-tagged-200-week-trend-line-that-defined-2022-bear-market)
- [Research: Bitcoin's realized price shows a bottom could be forming (CryptoSlate)](https://cryptoslate.com/research-bitcoin-realized-price-shows-bottom-could-be-forming/)