# Research Brief: Will silver close above $49.99/oz on Nov 30, 2026, 5:00 PM EST?

## 1. Resolution mechanics

- **What counts as YES:** The 1-minute candle close for silver at 5:00 PM EST (22:00 UTC) on Monday, November 30, 2026 must be above $49.99/oz after rounding to 2 decimals. In practice the rounded price must be $50.00 or higher. A raw price of $49.995 or more rounds up and counts.
- **Which candle:** The rules say the close at 5:00 PM is the end of the preceding minute. That means the candle stamped 4:59 PM, covering 4:59:00–4:59:59 PM, which closes at 5:00:00 PM.
- **Source:** The question does not name the "source agency." Kalshi's commodity markets, including silver daily markets with this exact wording, settle on Pyth's silver price feed (Pyth "How Kalshi modernizes commodity resolution", 2026; Solflare mirror of KXSILVERD market, Jun 2026). That feed is very likely spot XAG/USD, not a COMEX futures contract. I could not see the exact contract page, so this is inferred.
- **Edge cases:**
  - **CME daily break.** 5:00 PM ET is when CME Globex closes for its daily maintenance break (5–6 PM ET). Spot/OTC feeds normally keep publishing around then, and the 4:59 candle is the last full minute before the break.
  - **Missing data.** If nothing is published for that minute, the most recent available data is used. That would probably be a price from a minute or so earlier, which hardly matters.
  - **Futures roll.** Nov 30 is the last business day of November and roughly first notice day for COMEX December silver. If a futures-based source were used, roll effects and contango could matter. December futures trade at a small premium to spot, about 0.3–0.5% at roughly 4% rates for a month.
  - **Feed differences.** Spot quotes differ by about $0.05–$1.00 between sources and timestamps (see section 3). With the price this close to the strike, that noise matters.
- **Timing:** The close date and resolution time are the same moment, about 17 days from today. Thanksgiving is Thursday Nov 26, with thin trading Nov 26–27.

## 2. Reference classes and base rates

1. **Random walk with the price at the strike.** Spot is about $50.0–50.6, essentially at the $50.00 threshold.
   - Silver's implied volatility is about 38–40% annualized (SLV at-the-money options for late-Oct to late-Nov expiries, per Market Chameleon, snapshot undated; SIVR at-the-money IV 37% on Sep 30, 2026). Realized volatility is probably higher right now, given recent daily moves of 3–6%.
   - Over the ~17 calendar days (~11 trading days) to Nov 30, one standard deviation is about 0.40 × √(17/365) ≈ 8.6%, or about ±$4.30.
   - Driftless lognormal estimates for the chance of ending at or above $50.00:
     - From $50.00: about 48–50% (the small volatility drag makes it slightly under 50%).
     - From $50.55: about 55% (z ≈ +0.13).
     - From $49.50: about 45%.
   - At the money, every $0.50 move in spot shifts this by about 4–5 percentage points.
2. **Silver's up/down frequency over 2–3 week windows.** Historically, silver ends higher over a ~12-trading-day window roughly 50–52% of the time. This is my approximation of the long-run drift-free behavior of daily returns, not a computed figure. The 2026 regime has been strongly down-trending: from the $121.6–121.7 peak on Jan 29 to about $50, roughly −58% (24/7 Wall St., Oct 30, 2026). Short-horizon momentum in commodities is weakly positive, which leans slightly toward continued weakness. Mean reversion after crashes leans the other way.
3. **What follows major silver crashes.** Rebounds after big silver drawdowns, as in 1980, 2008 and 2011, have often been sharp but irregular. A goldsilver.com piece on crash history (no date) discusses this. Over a 2–3 week window, this reference class doesn't clearly favor either side.

## 3. Current state of the world (most recent first)

- **Nov 13, 2026 (morning, Asia/Europe):**
  - Spot silver bounced about 1% to about $50.55 at 09:25, timezone not given (ChainCatcher, Nov 13).
  - BullionVault showed about $50.64 at 02:41 GMT (Nov 13).
  - Guardian Gold had $50.06 at 10am AEDT (Nov 13).
- **Nov 12, 2026:**
  - Silver fell more than 3% on a hot inflation reading, Fed hike bets and a stronger dollar. It closed the New York session below $50: Kitco had $49.93–49.95 at about 6 PM ET (Kitco PM report, Nov 12; FXStreet "Silver tumbles over 3%", Nov 12).
  - Gold fell about 2.8% to about $3,876, a 13-month low, as the dollar hit a 19-month high (Kitco Nov 12; USAGold daily report, Nov 12).
  - Earlier in the day, FXStreet had silver at $50.91, down 1.57% from $51.72 and down 28.4% year to date (FXStreet, Nov 12).
- **Nov 11–12, 2026:** Fed officials turned hawkish:
  - Governor Bowman said inflation is broadening (Yahoo Finance, Nov 11).
  - Governor Waller suggested a 50bp hike in December may be needed, and Dallas Fed President Logan backed at least two more 25bp hikes (Trading Economics, cited Nov 12).
  - Oil is around $96, which is feeding bets on bigger Fed hikes (Investing.com, Nov 2026).
- **Nov 10–11, 2026:** Silver was about $51.86 (Nov 10) and $52.2–52.7 (Nov 11) before the latest drop (various technical notes).
- **October 2026 data:** CPI rose 0.4% month on month, with core at 0.3%. Payrolls rose 165k against a ~65k consensus, and unemployment was 4.1% (BBN Times; CNBC via search summary).
- **Nov 10, 2026:** Futures markets priced roughly an 80–86% chance of a 25bp hike at the Dec 8–9 FOMC, and after CPI it was described as fully priced (CME FedWatch via secondary sources; CNBC).
- **Oct 30, 2026:** Silver broke below $50 for the first time since Nov 2025, falling 5.8% to $49.34 (Mining.com; 24/7 Wall St., Oct 30).
  - The 2026 intraday low is cited as about $48.62–48.87, depending on source. Technical analysts treat $48–50 as key support. A daily close below $48 would open the way to $44–45 (FXEmpire; EBC; InvestingCube).
  - CPM Group sees support at $45–48.
  - Resistance is cited at about $53.
- **Oct 28, 2026:** The FOMC held at 3.75–4.00% by a 10–2 vote, with Hammack and Cook dissenting in favor of a hike. This followed a 25bp hike in September, the first since July 2023 (CNN; Fox Business, Oct 28).
- **Oct 14, 2026:** Silver fell 6.29% to $55.74, then its lowest close of 2026, on hot inflation data (goldsilver.com).
- **Fundamentals and analyst views:**
  - Metals Focus and the Silver Institute still project a 2026 deficit of 46.3 Moz, the sixth straight year. Metals Focus forecasts a 2026 average of $72.60 (Kitco opinion, Nov 5).
  - Banks have cut forecasts: HSBC $70 year-end; JPMorgan Q4 average about $63; UBS year-end $80. All of these sit well above spot, which suggests sell-side lag rather than a near-term signal.
  - JPMorgan reportedly says investor positioning in gold and silver has "turned light" (ExchangeRates.org.uk, Nov 12). Traders have been buying downside protection (Kobeissi, cited in search summaries).
- **Scheduled before Nov 30:**
  - Silver Institute/Metals Focus interim market review, "mid-November," exact date not found.
  - Minutes of the Oct 28 FOMC meeting, around Nov 18 (inferred from the usual 3-week lag).
  - Weekly jobless claims.
  - October PCE inflation, likely late November; date not confirmed.
  - US Thanksgiving on Nov 26, with a shortened Nov 27 session and thin liquidity.
  - The Dec 8–9 FOMC and the November jobs report (early December) both come after resolution. Markets will trade in anticipation of them.

## 4. Drivers and scenarios

**Paths to YES (price ≥ $50.00 at 4:59 PM ET on Nov 30):**
- **Relief bounce.** The $48–50 support holds, a December hike is already fully priced, and light positioning lets short-covering lift silver back to $52–53.
- **Softer data.** Softer PCE or labor data, or less hawkish FOMC minutes, cause the dollar and yields to pull back.
- **Physical demand.** The interim review confirms or widens the deficit, and physical buying appears near $50 (Indian demand around festivals; ETF inflows).
- **Geopolitics.** Safe-haven buying related to oil or conflict lifts precious metals generally, though so far higher oil has hurt metals through Fed expectations.

**Paths to NO (price below $50.00):**
- **More hawkishness.** Hawkish Fed repricing continues, with talk of 50bp or two more hikes, and the dollar keeps making new highs.
- **Technical breakdown.** A daily close below the $48.6–48.9 year low triggers stop-loss and margin-driven selling toward $44–45.
- **Equity sell-off.** Another tech sell-off forces liquidation of metals.
- **Rising real yields.** Higher real yields outweigh the deficit story. FXEmpire (Nov 2026) said real yields are overshadowing supply deficits.

**Overall:** The outcome is close to a coin flip set by spot versus $50 near the end of the window. With about 8–9% one-sigma moves over the period, the starting point matters less than which way the macro picture breaks.

## 5. Signposts

- **Spot level in the final days (most important).** At-the-money sensitivity is about 4–5 percentage points per $0.50. Each day closer to Nov 30 makes the spot-to-$50 distance count for more.
- **A daily close below $48.6** (the 2026 low) is strongly bearish and points to $45. **A reclaim of $53** is strongly bullish.
- **Dollar index and 2-year Treasury yield.** A new dollar high and rising 2-year yields point to NO. A reversal points to YES.
- **Fed communication.** FOMC minutes and Fed speakers before the Nov 28-ish blackout (it starts the second Saturday before the meeting, so about Nov 28). Talk of 50bp in December is bearish for silver; pushback against it is bullish.
- **October PCE, jobless claims and other US data.** Hot readings point to NO.
- **Interim silver review.** A larger deficit or strong investment demand leans YES, modestly.
- **Oil.** Around $96 now. A move up has been bearish for metals through Fed expectations.
- **Positioning and ETF flows.** CFTC Commitments of Traders data and SLV holdings. Capitulation-level shorts or a turn to ETF inflows lean YES.

## 6. Uncertainties

- **Exact spot right now.** Sources differ by up to about $1 depending on timestamp. The latest readings (Nov 13 morning) are about $50.0–50.6, just above the strike. I could not get a Friday US-session price.
- **Resolution feed.** Pyth spot is inferred, not confirmed, and it may differ by a few cents to tens of cents from Kitco or COMEX. That matters at the money.
- **Current implied volatility.** I found no current silver CVOL reading. 38–40% comes from undated or September SLV/SIVR data, and real volatility may be 45%+ after recent 3–6% daily moves.
- **Data dates.** I could not confirm the October PCE release date or the interim review date.
- **Source quality.** Several figures come from secondary or aggregator sites, and most direct page fetches failed (proxy blocked), so some details rest on search-result summaries.
- **The "conflict" context.** It is referenced in a JPMorgan note but I could not establish its details or how it currently affects oil and metals.

## Sources
- [Silver Price Today – Kitco](https://www.kitco.com/charts/silver)
- [Gold, silver slide as Treasury yields surge, Fed hike concerns intensify – Kitco PM Report (Nov 12, 2026)](https://www.kitco.com/news/article/2026-11-12/gold-silver-slide-treasury-yields-surge-fed-hike-concerns-intensify-kitco)
- [Gold falls below $4,000 as dollar surges, Fed hike bets rise – Kitco PM Report (Nov 11, 2026)](https://www.kitco.com/news/article/2026-11-11/gold-falls-below-4000-dollar-surges-fed-hike-bets-rise-kitco-pm-report)
- [Silver price today: falls on November 12 – FXStreet](https://fxstreet.com/news/silver-price-today-silver-falls-according-to-fxstreet-data-202611120930)
- [Silver tumbles over 3% as hot US inflation boosts Fed hike bets – FXStreet](https://fxstreet.com/news/silver-tumbles-over-3-as-fed-rate-hike-bets-fuel-us-dollar-rally-202611121711)
- [Current price of silver as of Thursday, Nov. 12, 2026 – Fortune](https://fortune.com/article/current-price-of-silver-11-12-2026/)
- [Overnight Summary – Precious Metals Prices 13/11/2026 – Guardian Gold](https://guardian-gold.com.au/market-updates/overnight-summary-precious-metals-prices-13-11-2026/)
- [Spot gold and silver both rose by 1% – ChainCatcher](https://www.chaincatcher.com/en/article/2304354)
- [Live Silver Price Chart – BullionVault](https://www.bullionvault.com/silver-price-chart.do)
- [Gold Tumbles 3% To $3,866 As Dollar Hits 19-Month High; Silver Slides Under $50 – USAGold (Nov 12, 2026)](https://www.usagold.com/daily-precious-metals-market-report-november-12-2026/)
- [Silver price today, Nov 11, 2026: Silver opens lower as the Fed signals readiness to raise rates – Yahoo Finance](https://finance.yahoo.com/personal-finance/investing/article/silver-price-today-wednesday-november-11-2026-silver-prices-open-lower-as-the-fed-signals-theyre-prepared-to-raise-rates-122453770.html)
- [Gold languishes near 13-month low as $96 oil fuels bets on bigger Fed hikes – Investing.com](https://www.investing.com/news/commodities-news/gold-languishes-near-13month-low-as-96-oil-fuels-bets-on-bigger-fed-hikes-5023860)
- [Silver – Trading Economics](https://tradingeconomics.com/commodity/silver)
- [Gold price slumps to one-year low, silver price breaks $50 – Mining.com](https://www.mining.com/gold-price-slumps-to-one-year-low-silver-price-breaks-50-as-mining-stocks-tank/)
- [Silver Has Lost More Than Half Its Value Since January – 24/7 Wall St. (Oct 30, 2026)](https://247wallst.com/investing/2026/10/30/silver-has-lost-more-than-half-its-value-since-january/)
- [Gold and Silver's October Selloff – goldsilver.com](https://goldsilver.com/industry-news/goldsilver-news/gold-silver-october-selloff-2026/)
- [Silver Price Crash History – goldsilver.com](https://goldsilver.com/industry-news/article/silver-price-crash-history-what-happens-after-the-biggest-drops/)
- [Silver Price Forecast: Tech Sell-Off Raises Risk of a Drop to $45 – FXEmpire](https://www.fxempire.com/forecasts/article/silver-price-forecast-tech-sell-off-raises-risk-of-a-drop-to-45-1641801)
- [Silver Falls as Rising Real Yields Overshadow Supply Deficits – FXEmpire](https://www.fxempire.com/forecasts/article/silver-falls-as-rising-real-yields-overshadow-supply-deficits-1644169)
- [Silver Price Forecast for November 2026: Can XAG/USD Hold $50? – EBC](https://www.ebc.com/forex/silver-price-forecast-november-2026)
- [Silver Price Prediction: $50 Holds, $53 Is the Test – InvestingCube](https://www.investingcube.com/commodities/silver-price-prediction-50-holds-53-is-the-test/)
- [Silver Price Outlook: Positioning In Gold, Silver Turned Light Says JP Morgan – ExchangeRates.org.uk (Nov 12, 2026)](https://www.exchangerates.org.uk/news/47757/2026-11-12-silver-price-outlook-positioning-in-gold-silver-turned-light-says-jp-morgan.html)
- [Why the silver price case now rests on investors – Kitco (Nov 5, 2026)](https://www.kitco.com/opinion/2026-11-05/why-silver-price-case-now-rests-investors)
- [Fed keeps interest rates unchanged, two officials dissent – CNN (Oct 28, 2026)](https://www.cnn.com/2026/10/28/business/live-news/federal-reserve-interest-rate-october)
- [October FOMC: Fed holds rates steady – Fox Business](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-october-28-2026)
- [Will the Fed Raise Interest Rates in December 2026? – BBN Times](https://www.bbntimes.com/financial/will-the-fed-raise-rates-in-december-2026)
- [Metals Options Report October 2026 – CME Group](https://www.cmegroup.com/newsletters/metals-options-update/metals-options-report-october-2026.html)
- [SLV Option Chain – Market Chameleon](https://marketchameleon.com/Overview/SLV/OptionChain/)
- [SIVR Volatility Skew – Options Analysis Suite](https://www.optionsanalysissuite.com/etf/sivr/volatility)
- [How Kalshi modernizes commodity resolution with Pyth Pro – Pyth Network](https://www.pyth.network/success-stories/how-kalshi-modernizes-commodity-resolution-with-pyth-pro)
- [Silver price on June 09, 2026 at 5:00 PM EDT (KXSILVERD mirror) – Solflare](https://www.solflare.com/prediction/commodities/event/KXSILVERD-26JUN0917/)