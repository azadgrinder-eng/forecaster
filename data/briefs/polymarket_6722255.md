# Research brief: Will META trade at or below $600 in November 2026?

**Bottom line:** Several independent quote sources say META traded as low as **$583.80** during regular trading hours on **Thursday, Nov 5, 2026**. That is about $16 below the $600 strike. If the market was open before that session, which is normal for monthly "hit price" markets, the YES condition has almost certainly already been met. The only open issues are when the market was created and whether Pyth's prices match the exchange quotes.

---

## 1. Resolution mechanics
- **What counts as YES:** any 1-minute candle on Pyth (Equity.US.META/USD) with a Low at or below $600.00. It must occur during regular trading hours (9:30 AM–4:00 PM ET), at some point after the market was created and within November 2026. Pre-market and after-hours prices don't count. Pyth's prices are used exactly as published, with no rounding.
- **Deadline:** the last session is Mon Nov 30, 2026. The market closes Dec 1 at 04:59:59 UTC.
- **Who decides:** Pyth's 1-minute candle data. If Pyth data is unavailable, the primary exchange's (Nasdaq) official daily high/low is used instead.
- **Edge cases:**
  - **(a) Creation time.** Only prices after the market was created count. Monthly "hit price" markets are usually created at or before the start of the month, but I could not confirm this market's creation timestamp. If it was created on or before Nov 5 at about 10:50 AM ET, the Nov 5 drop below $600 counts.
  - **(b) Pyth vs. consolidated tape.** Pyth's prices are aggregated and can differ slightly from consolidated-tape prints. A $16 (2.7%) margin under the strike, with prints around $587 also reported at 10:50 AM, leaves no realistic room for Pyth to show a low above $600.
  - **(c) Stock split.** No split has been announced. Motley Fool ran a speculative "Stock-Split Watch" piece on Nov 6, but there is no corporate action. A split would adjust the target proportionally anyway.

## 2. Reference classes and base rates
- **Has the event already happened this month?** Yes, per the dated quotes below. That outweighs any base rate.
- **If the market was somehow created after Nov 5 (counterfactual):** META closed Nov 6 at about $610. Touching $600 means a drop of about 1.6–1.7% at some point over roughly 16 remaining sessions (Nov 9–30, with a half-day on Nov 27).
  - Volatility is currently very high: daily moves of 4–7% since Oct 22, and a 52-week range of $520.26–$779.82.
  - Rough estimate: annualized volatility of 40–50% means a daily standard deviation of about 2.5–3%. A one-sided barrier only about 0.6 daily standard deviations away is touched in roughly 85–90% of 16-day windows. This is my own reflection-principle approximation, not a sourced figure.
- **Recent history of the $600 level:** META already went below $600 in March 2026 (Yahoo Finance, "Meta Stock Slips Below $600"). It hit about $546 after Q2 earnings in late July 2026 (FX Leaders / Seeking Alpha coverage, Jul 30, 2026). So $600 has been crossed repeatedly this year.

## 3. Current state of the world (most recent first)
- **Nov 6 (Fri):** META rebounded modestly.
  - Sources disagree on the close: about $610.15 (+0.84%) in one snapshot; Yahoo says +1.14%. One intraday snapshot showed $623.38 (+3.0%) at 11:04 AM.
  - The reported day range was about $606.66–$625.52; Robinhood showed a session low of $603.
  - Blockonomi tied the gains to Meta closing a $15B bond sale and expanding its forward stock offering to 46M shares.
- **Nov 5 (Thu), the key session:**
  - Prices: open $632.30, high $634.99, **low $583.80**, close $605.08 (−3.96%), prior close $630.00 (TipRanks; Cryptonomist, Nov 6; Gotrade).
  - TradingView/GuruFocus reported META at **$587.39 (−6.76%) at 10:50 AM ET**, which is during regular hours. A MarketBeat snapshot showed $594.17 (−5.69%), which matches a $630.00 prior close.
  - It was the market's worst day since April 2025, with an AI-chip selloff spreading (StockTitan, Nov 5). Meta-specific news that day: COO Javier Olivan's insider sales (MarketBeat) and Meta pausing planned terms-of-service changes amid regulatory risk.
  - One Investing.com table lists a Nov 5 low of 613.44, which conflicts with the other sources. TipRanks and Cryptonomist agree on $583.80, and the TradingView and MarketBeat intraday prints support it.
- **Nov 2:** Motley Fool said META was down about 18% from its October high (the 52-week high is $779.82).
- **Oct 26:** Meta priced a $25B Class A common stock forward sale at $625 a share, plus about $12.5B of mandatory convertible preferred (Meta IR press release). It also proposed a roughly $60B at-the-market program in nonvoting Class C shares, starting in Q1 2027 or later.
- **Oct 21–22:** Q3 results.
  - Revenue was $64.6B (+26%, above estimates).
  - Meta took a $9.9B litigation charge.
  - Q3 capex was $34.9B, free cash flow was about −$2.1B, and 2026 capex guidance is $135–145B.
  - The stock fell about 7% to about $648.5 (CNBC; Fortune; GuruFocus). Trefis put the drop from Oct 13 to Oct 28 at about 19.7%.
- **Valuation snapshot (~Nov 6):** market cap about $1.59T, P/E about 21, forward P/E about 19, average analyst target about $848 (StockAnalysis).

## 4. Drivers and scenarios
- **YES (dominant):** The market was created before Nov 5 (typical for monthly markets), and Pyth's 1-minute candles show a low at or below $600 on Nov 5. The only things needed are the creation timing and Pyth data matching consolidated prices.
- **YES (backup):** Even if Nov 5 is somehow excluded, META at about $610 needs only about a 1.7% drop over the remaining 16 sessions, amid high volatility, worries about AI capex and dilution, and a market-wide AI selloff.
- **NO:** Either (i) the market was created after Nov 5's lows and META stays above $600 through Nov 30, or (ii) Pyth's feed for Nov 5 shows nothing at or below $600. Option (ii) is very unlikely given a $583.80 low, and if Pyth data was missing, the exchange's daily low ($583.80) would be used.

## 5. Signposts
- The Pyth chart for Nov 5, 2026, around 10:30–11:30 AM ET (Unix timestamp ≈ 1762357800). If it shows a 1-minute low at or below $600, the question is settled.
- The market's creation timestamp.
- If the creation date turns out to be after Nov 5: META's moves from Nov 9 onward, AI-sector sentiment (Nvidia reports earnings around Nov 18–19), news on equity-offering settlements or the ATM program, and regulatory headlines. A fresh close under about $605 would make a touch very likely.

## 6. Uncertainties
- I could not confirm the market's exact creation time.
- I could not view Pyth's own Nov 5 candles directly; the proxy blocked page fetches.
- One data vendor (Investing.com) shows a much higher Nov 5 low (613.44). That looks like a mislabeled row, since the other sources agree on $583.80 and the intraday prints support it, but I didn't independently confirm that.
- Sources disagree slightly on the exact Nov 6 close ($610.15 vs. a +1.14% move).

## Sources
- [Meta Platforms (META) Stock Price, Chart & News – StockAnalysis](https://stockanalysis.com/stocks/meta/)
- [Meta Platforms (META) Stock Price, Quote & Analysis – TipRanks](https://www.tipranks.com/stocks/meta)
- [Meta stock Analysis: closes at $605.08, down 3.96% – Cryptonomist](https://en.cryptonomist.ch/2026/11/06/meta-stock-analysis-closes-605-08/)
- [Meta Platforms Stocks Fall 6.76% as AI Investment Tests Cash Flow – TradingView/GuruFocus](https://www.tradingview.com/news/gurufocus:a1c9585bc094b:0-meta-platforms-stocks-fall-6-76-as-ai-investment-tests-cash-flow/)
- [Meta Platforms Shares Down 4% on Insider Selling – MarketBeat](https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-shares-down-4-on-insider-selling-2026-11-05/)
- [Meta - Facebook (META) Stock Price: Nov 5 Close $605.08 – Gotrade](https://www.heygotrade.com/en/us-stock/meta/)
- [The Stock Market Today, November 5, 2026 – StockTitan](https://www.stocktitan.net/articles/stock-market-today-live-november-5-2026)
- [Meta Platforms Stock Price History – Investing.com](https://www.investing.com/equities/facebook-inc-historical-data)
- [META Stock Price & Analyst Rating – Morningstar](https://www.morningstar.com/stocks/xnas/meta/quote)
- [Meta Platforms (META) Stock: Rises 2.68% as Company Closes $15 Billion Bond Sale – Blockonomi](https://blockonomi.com/meta-platforms-meta-stock-rises-2-68-as-company-closes-15-billion-bond-sale/)
- [Meta Stock Falls 4% Amid Widening Regulatory Risk – Gokhshtein](https://gokhshtein.com/news/2026-11-06-meta-pauses-planned-terms-updates-keeps-existing-rules-in)
- [Meta reports third-quarter revenue beat – CNBC](https://www.cnbc.com/2026/10/21/meta-earnings-q3-2026-live-updates.html)
- [Meta's revenue surges 26% to $64.6 billion… – Fortune](https://fortune.com/2026/10/21/meta-q3-earnings-mark-zuckerberg-capex-muse/)
- [Meta Platforms Shares Drop 7% After Q3 Earnings – GuruFocus](https://www.gurufocus.com/news/9137792/meta-platforms-meta-shares-drop-7-after-q3-earnings-reveal-litigation-charge-and-rising-expenses)
- [Is Meta Stock's Fall A Bargain Or A Warning? – Trefis](https://www.trefis.com/stock/meta/articles/621256/is-meta-stocks-fall-a-bargain-or-a-warning/2026-10-29)
- [Down 18% From Its October High, Should You Buy the Dip on Meta Stock? – Motley Fool](https://www.fool.com/investing/2026/11/02/down-18-from-its-october-high-should-you-buy-the-d/)
- [Meta Announces Pricing of Offering… Forward Sale Agreements – Meta IR](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Pricing-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx)
- [Meta Stock Offering: Meta Goes From Buying Back Stock to Selling $37.5 Billion – StockTitan](https://www.stocktitan.net/articles/meta-stock-offering-2026-35-billion-now-60-billion-no-vote)
- [Meta Stock Slips Below $600. Time to Buy? – Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/meta-stock-slips-below-600-202300840.html)
- [META Stock Crashes Below $550 as AI Spending Wipes Out Cash Flow – FX Leaders](https://www.fxleaders.com/?p=465120)
- [Stock-Split Watch: Is Meta Platforms Next? – Motley Fool](https://www.fool.com/investing/2026/11/06/stock-split-watch-is-meta-platforms-next/)