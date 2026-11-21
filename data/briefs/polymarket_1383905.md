# Research Brief: Extended (XTEN) FDV above $150M one day after launch

## 1. Resolution mechanics

- **YES requires two things.** (a) Extended's token (ticker XTEN) must launch by Dec 31, 2026, 11:59 PM ET, and be publicly transferable and tradable. (b) At 4:00 PM ET on the calendar day after launch, total token supply × price must be above $150M.
- **Price threshold.** Total supply is fixed at 1,000,000,000 XTEN, minted in full at genesis with no way to raise the cap (TokenPost / KuCoin, ~Oct 31–Nov 2026). $150M ÷ 1B means the price must be above **$0.15 per XTEN**. Because FDV uses total supply, the size of the unlocked float does not matter for the calculation.
- **Who decides.** The rules name "the most liquid price source available." That will probably be the main CEX spot pair or Extended's own spot market. The settlement uses one price at one moment (4 PM ET), not a daily average.
- **Edge cases:**
  - **Hyperliquid pre-market.** Hyperliquid's XTEN "hyperp" is a pre-launch perpetual contract. It is not the token, so it should not count as a launch or as the price source. It switches to a regular perp once XTEN lists on a centralized exchange (hyperliquidguide, ~Nov 2026).
  - **Late-December launch.** If launch happens on Dec 31, the measurement falls on Jan 1, 2027 at 4 PM ET, after the stated close date of Jan 1 05:00 UTC. The launch would still count, but resolution would be delayed.
  - **Claim vs. trading.** The allocation checker and terms-signing are live now. That is not a launch, because the tokens cannot be transferred yet.
  - **EU restriction.** EU users will not be able to spot trade XTEN on Extended at launch (TokenPost). This should not affect whether the launch counts.

## 2. Reference classes and base rates

**A. Launch timing: does a "coming [month]" TGE actually happen within about 6 weeks?**
- Extended said "Coming November 2026" (Extended on X, ~Oct 24, 2026). The whitepaper reportedly targeted Nov 2. By Nov 3, a tracker said the date was "not set, revised date to be announced" (Bitrue TGE calendar / CryptoDiffer, Nov 2026).
- Perp DEX TGEs often slip. edgeX rescheduled its TGE to Mar 31, 2026, citing market conditions (The Defiant; Cryptonews). Predict.Fun's TGE was postponed (Today in DeFi, Nov 2026).
- My rough prior from 2024–26 airdrops: when a team has already opened its allocation checker and named a launch month, the TGE usually follows within 2–8 weeks. Slips of one to two months happen maybe 20–35% of the time. This is my own estimate, not a counted statistic.

**B. Day-1 price compared with Hyperliquid pre-market price for airdrop tokens**
- **Lighter (LIT), Dec 2025.** Hyperliquid pre-market implied about $3.5B FDV. The token launched at roughly $2.0–2.5B, about 30–40% below pre-market (CryptoTimes, Dec 31, 2025; Cryptopolitan).
- **WLFI and PUMP (2025), from memory and unverified here.** Hyperp prices ran roughly at or 10–30% above where spot settled on day 1.
- **Overall pattern.** Hyperps for big airdrops tend to be priced too high, and day 1 often lands 0–40% below the hyperp price. A drop of more than 40% is uncommon but happens with large, fully unlocked airdrops in weak markets.

**C. Post-TGE performance of perp DEX tokens**
- Per CryptoRank data cited by secondary outlets, 7 perp DEX tokens launched over roughly the past year and only 2 (ASTER, EDGE) rose after launch. One write-up gives a 71% "failure" rate (HokaNews / CoinGabbar, May 2026).
- Most of the decline usually happens over weeks, not within the first day. But XTEN's 30% airdrop is fully unlocked at TGE, which makes heavy selling on day 1 more likely.

## 3. Current state of the world (most recent first)

- **Nov 21, 2026 (today).** I found no announced TGE date and no named CEX listing. Several trackers (Bitrue, CryptoDiffer, airdrops.io) still say "November 2026, estimated / date TBA."
- **Nov 11, 2026.** The XTEN allocation checker and terms went live. Eligible points holders sign in the Extended app. The signing window runs Nov 11 to **Dec 31, 2026, 23:59 UTC**. Allocations not accepted by then go to the Ecosystem Fund. Starknet users must nominate an EVM wallet. Tokens arrive "after TGE," which is undated (TokenPost; The Defiant; KuCoin; Phemex, ~Nov 11–12, 2026).
  - The signing deadline running to Dec 31 is ambiguous. It may mean the TGE comes before signing closes, with late signers receiving tokens later. Or it may hint that the TGE comes around or after the deadline.
- **Late Oct to Nov 2026, pre-market pricing (token trading markets, not markets on this question):**
  - Hyperliquid listed the XTEN hyperp on **Oct 27, 2026** (up to 3x leverage, isolated margin only).
  - Early quote: about **$0.268**, roughly 18% below the listing-day high (implying a high near $0.33), on about $220K daily volume (KuCoin insight, ~late Oct).
  - Later snapshot: mark price **$0.2511**, open interest about 2.48M XTEN (~$623K) (hyperliquidguide).
  - CryptoRank pre-market: about **$0.237 (FDV ≈ $237M)**. Crypto.com: about **$0.20**, with a $0.30 high.
  - **Implied FDV is about $200–270M**, so the price would need to fall roughly 25–45% from these levels to reach $150M.
  - Liquidity is thin (open interest under $1M), so these prices are noisy.
- **~Oct 31 to early Nov 2026, tokenomics:**
  - 1B total supply.
  - **30% (300M) airdropped to points holders, fully unlocked at TGE.** Of this, 17,384,355 went to X10 Ltd.'s internal market-making desk.
  - Founders, team and investors hold 500M (50%), locked with a 12-month cliff.
  - A 50M ecosystem fund.
  - Staking starts at TGE (500 XTEN minimum for the "League" tier), with up to 5x yield boost on vaults.
  - Sources: TokenPost; KuCoin; PANews; Phemex; TechFlow.
- **Oct 22, 2026.** Extended moved settlement from Starknet to Circle's Arc, carrying about $114–120M TVL. Collateral is now USDC and cirBTC, with no trading pause (CryptoBriefing; Pluang). A deeper partnership with Circle was announced (KuCoin / Blockonomi).
- **Background:**
  - Built by ex-Revolut founders.
  - Over $200B lifetime volume (aggregator claim).
  - 100+ markets across crypto, stocks, FX and commodities. eToro is an investor.
  - Funding: $6.5M seed in Apr 2024 (Tioga, Semantic, Cherry, StarkWare, cyber.Fund) (CB Insights). Caplight lists $19M total including a strategic round in July 2026. Dealroom gives a $50–100M valuation band (2026). Mainnet launched on Starknet in 2025 (The Block).
- **Scheduled before close.** The TGE and listing date are not yet announced. The signing deadline is Dec 31, 23:59 UTC.

## 4. Drivers and scenarios

**Paths to YES:**
1. **TGE in late Nov or Dec 2026 with prices near pre-market.** If XTEN lists around $0.20–0.27, it clears $0.15 comfortably.
   - Supporting factors: a real product with about $120M TVL; the Circle/Arc story; the team allocation locked for 12 months; staking available from TGE, which absorbs some supply; and the market-maker desk holding about 17M tokens.
2. **A tier-1 CEX listing (Binance, Bybit, OKX) at TGE.** This usually supports day-1 prices.

**Paths to NO:**
1. **No TGE by Dec 31.** The date has already slipped once (Nov 2 to TBA). If the team waits for the signing window to close Dec 31, the launch moves into 2027. This is probably the single biggest NO risk.
2. **Heavy airdrop selling.** 300M tokens (30% of supply) unlock fully at once. The float at TGE is probably 30–40% of supply, high for a perp DEX, so airdrop selling meets thin liquidity, especially with weak listings (DEX only, or tier-2 CEXs) and EU trading blocked. It would take a day-1 price under $0.15 (about 25–45% below pre-market) to resolve NO.
3. **Weak broader market or crypto risk-off in Dec 2026.** This would cut altcoin TGE valuations across the board, the same reason edgeX postponed.
4. **Valuation anchoring.** Private valuations of $50–100M sit below $150M, and mid-tier perp DEX tokens have often traded down to low-hundreds-of-millions FDV.

## 5. Signposts

- **Official TGE date announced for Nov or early Dec**: big move toward YES on timing. **Silence through mid-December, or a "Q1 2027" or "after the claim window" statement**: strong move toward NO.
- **Which exchanges list it.** Binance, Bybit or OKX spot or perp at TGE moves toward YES. Only Extended's own spot market plus small CEXs moves toward NO.
- **Hyperliquid XTEN hyperp price trend before TGE.** Holding above $0.22 favors YES. Falling under $0.18 sharply raises NO risk.
- **Number of tokens claimed or staked** and any staking lock incentives at TGE. High staking means less selling.
- **Extended's TVL, volume and open interest after the Arc migration.** Growth supports a higher valuation.
- **Overall altcoin market and recent December TGE outcomes.**

## 6. Uncertainties

- **Exact TGE date.** It is unknown, and it is unclear whether the TGE happens before or after the Dec 31 signing deadline. This is the crux.
- **Float at TGE.** Possibly 30% airdrop plus ecosystem, liquidity and market-maker allocations. The full allocation table was not verified (I could not open primary pages).
- **Current pre-market price.** I could not get a live Nov 21 quote. The figures above ($0.20–0.27) are late October to mid November snapshots and may be out of date.
- **Exchange listings** are unknown.
- **Whether Extended's own spot market** would count as "the most liquid price source."
- **Funding and valuation figures conflict** across sources ($6.5M vs. $19M raised).
- **The WLFI and PUMP comparisons** are from memory and were not re-checked here.

## Sources
- [Extended on X: "The ticker is $XTEN. Coming November 2026…"](https://x.com/extendedapp/status/2113662104536285612)
- [Extended on X: XTEN Tokenomics Breakdown](https://x.com/extendedapp/status/2117309226423108056)
- [Extended Sets XTEN Supply at 1 Billion With a 12-Month Cliff (TokenPost)](https://www.tokenpost.com/news/business/47249)
- [Extended Opens XTEN Checker With Dec. 31 Acceptance Deadline (TokenPost)](https://www.tokenpost.com/news/business/55046)
- [Extended Opens XTEN Checker With Dec. 31 Signing Deadline (The Defiant)](https://thedefiant.io/news/tokens/extended-opens-xten-checker-with-dec-31-signing-deadline)
- [Extended DEX Opens XTEN Allocation Inquiry (KuCoin)](https://www.kucoin.com/news/flash/extended-dex-opens-xten-allocation-query-sign-up-deadline-set-for-dec-31)
- [EXTENDED Opens $XTEN Checker (Phemex)](https://phemex.com/news/article/extended-opens-xten-checker-as-unaccepted-allocations-redirect-to-ecosystem-fund-103224)
- [Extended XTEN Tokenomics: 30% Airdrop Fully Unlocked at TGE (Phemex)](https://phemex.com/news/article/extended-unveils-xten-tokenomics-30-supply-airdropped-fully-at-tge-team-tokens-locked-12-months-102185)
- [Extended Reveals XTEN Tokenomics: 30% Airdropped at TGE (KuCoin)](https://www.kucoin.com/news/flash/extended-reveals-xten-tokenomics-30-airdropped-at-tge)
- [Extended unveils XTEN tokenomics (PANews)](https://panews.io/articles/01a19f5b-04b0-75f4-9d11-a81b326ab00c)
- [Extended, built by former Revolut team, announces XTEN tokenomics (TechFlow)](https://www.techflowpost.com/en-US/article/35058)
- [KuCoin insight: XTEN pre-market $0.268 on Hyperliquid](https://www.kucoin.com/news/insight/BTC/6ae795cdbbcb520007457477)
- [Hyperliquid Hyperps Explained (hyperliquidguide)](https://hyperliquidguide.com/guides/trading/hyperliquid-hyperps-explained)
- [Extended Price (CryptoRank)](https://cryptorank.io/price/x-10)
- [Extended (XTEN) Price (Crypto.com)](https://crypto.com/en/price/extended)
- [Extended Token Launch (CoinGabbar)](https://www.coingabbar.com/en/extended-token-launch-date-xten-airdrop-tokenomics)
- [Extended ($XTEN) TGE Date & Launch Info (CryptoDiffer)](https://cryptodiffer.com/upcoming-tges/extended-ext-token-generation-event)
- [Crypto TGE Calendar November 2026 (Bitrue)](https://www.bitrue.com/blog/upcoming-crypto-tge-november-2026)
- [Extended Airdrop (airdrops.io)](https://airdrops.io/extended/)
- [Extended moves settlement from Starknet to Circle's Arc on October 22 (CryptoBriefing)](https://cryptobriefing.com/extended-migrates-settlement-starknet-to-arc/)
- [Extended completes migration to Circle's Arc (CryptoBriefing)](https://cryptobriefing.com/extended-migrates-arc-usdc-cirbtc-collateral/)
- [Pluang: Extended moves settlement to Arc](https://pluang.com/en/news-feed/perpindahan-penyelesaian-starknet-ke-arc-circle-22-oktober)
- [Ex-Revolut team's perp DEX Extended goes live on Starknet mainnet (The Block)](https://www.theblock.co/post/366529/ex-revolut-team-perp-dex-extended-live-on-starknet)
- [X10 financials (CB Insights)](https://www.cbinsights.com/company/x10/financials)
- [X10 (Caplight)](https://www.caplight.com/company/x10)
- [Extended (Dealroom)](https://dealroom.co/companies/extended/)
- [Amber Group-Backed Perp DEX edgeX to Launch Token on March 31 (The Defiant)](https://thedefiant.io/news/defi/amber-group-backed-perp-dex-edgex-to-launch-token-on-march-31)
- [7 Perp DEX Tokens Launched, Only 2 Survived TGE (HokaNews)](https://www.hokanews.com/2026/05/7-perp-dex-tokens-launched-only-2.html)
- [7 Perp DEX Tokens Launched, Only 2 Succeed After TGE (CoinGabbar)](https://www.coingabbar.com/en/crypto-currency-news/7-perp-dex-tokens-launched-only-2-succeed-after-tge-aster-edge)
- [Lighter Token Launches With $2B+ FDV (CryptoTimes)](https://www.cryptotimes.io/2025/12/31/lighter-token-launches-with-2b-fdv-ranks-third-among-perp-dexs/)
- [Lighter launched its LIT token (Cryptopolitan)](https://www.cryptopolitan.com/lighter-perpetual-dex-launched-its-lit-token/)
- [Today in DeFi: Extended checker live, Predict.Fun TGE postponed](https://news.todayindefi.com/p/extended-checker-live-predictfun)