# Research Brief: Will the 10-year Treasury yield close below 4.76% on any business day from November 3 to 30, 2026?

## 1. Resolution mechanics
- **What counts as YES:** the "10 Yr" column of Treasury's *Daily Treasury Par Yield Curve Rates* shows a value below 4.76 for any date from Nov 3 to Nov 30, 2026. Treasury publishes two decimals, so the first qualifying print is **4.75% or lower**. A print of exactly 4.76 is NO.
- **Which number counts:** Treasury's official daily par yield. It is built from indicative bid-side quotes taken around 3:30 PM ET, so it can differ by 1–3 bp from the CNBC, Tradeweb or Trading Economics "close" quoted in the news. Intraday dips below 4.76 do not count. FRED's DGS10 series is the same Treasury data and is a useful mirror.
- **Timing:** the market resolves YES as soon as one qualifying print is published. Otherwise it resolves NO once data for Mon Nov 30 is posted. If that data is missing by Dec 14, 11:59 PM ET, it resolves NO.
- **Holidays:** Treasury normally publishes nothing on Veterans Day (Wed Nov 11) or Thanksgiving (Thu Nov 26). Fri Nov 27 is an early-close day but normally has a print.
- **Days remaining:** counting Nov 6 (today), about 15 business days are left: Nov 6, 9, 10, 12, 13, 16–20, 23–25, 27 and 30.
- **Days already printed:** Nov 3 was about 4.94% on Election Day, and the official Nov 4 value was reported as about 4.90%. Neither qualifies. I could not confirm the official Nov 5 print (see §3).

## 2. Reference classes and base rates
1. **Random-walk / first-passage estimate (my own calculation, not a published figure).**
   - The 10-year needs to fall about 8–9 bp from the Nov 5 level (about 4.83–4.85) to reach 4.75 or lower, with about 15 daily prints left.
   - Assumptions:
     - Normal-regime daily standard deviation of the 10-year is about 6–7 bp.
     - The autumn 2026 regime looks hotter, about 8 bp or more: 5.31% on Oct 5 to about 4.84% on Nov 5 is roughly a 47 bp move in a month, and the 10-year fell "nearly 40 bp during October" (Private Banker, Nov 5, 2026).
   - With no drift, the reflection principle gives P(minimum ≤ −9 bp over 15 days) of about 2·Φ(−9/(σ√15)):
     - σ = 6 bp: about 0.70.
     - σ = 8 bp: about 0.77.
   - Checking only daily closes (rather than continuously) cuts this by roughly 5–10 points, giving **about 0.60–0.70** with no drift.
2. **Typical monthly ranges (approximate, from my general knowledge of 2022–2025 DGS10 data, not recomputed here).**
   - The 10-year's high-to-low range within a month has typically been about 30–50 bp in the post-2022 regime.
   - A range of under 10 bp on the downside from a point a few days into the month is uncommon, but it depends on direction. Months that start in a strong uptrend often never revisit lower levels.
3. **Behaviour after a big equity shock.**
   - Large flight-to-safety rallies in bonds are often partly reversed within days once equities stabilise. Rallies driven by policy repricing, such as a lost Fed hike or weak data, tend to persist.
   - The Nov 5 drop was explicitly safe-haven driven (CNN, Nov 5, 2026), so it is more prone to reversal.
   - The 2-year also fell 11 bp (Private Banker, Nov 5, 2026). That suggests markets were also pricing out some of the expected December hike, which tends to last longer.

## 3. Current state of the world (most recent first)
- **Nov 6 (today):**
  - The October jobs report came out at 8:30 ET. I could not find the actual numbers.
  - Consensus was about 59k (Dow Jones) to 65k (Reuters/FactSet) jobs, with unemployment at 4.2%. Vanguard was the high outlier at 120k and KPMG the low one at 45k.
  - ADP private payrolls for October were +86k against 69k expected (Fox Business, Nov 2026).
  - A previews piece said a payrolls print above 100k with faster wage growth would revive hike bets, while unemployment at 4.3% or higher would push yields down (TradingKey/FXStreet, Nov 6).
  - Pre-report intraday quote: 10-year at about 4.839% (Rio Times, Nov 6).
- **Nov 5:**
  - The Nasdaq fell 5.5% into a correction, the S&P 500 fell 4.4% and the semiconductor index fell 12.3%. The VIX rose to about 27–28. Causes cited: a Democratic sweep of Congress and fears for AI data-center spending (CNN, Nov 5, 2026).
  - The 10-year fell about 5–6 bp to about 4.83–4.845%, its lowest since early September. The 2-year fell to 4.471% (down 11 bp) and the 30-year to 5.245% (Private Banker, Nov 5).
  - Trading Economics was also reported showing 4.90% for Nov 5, which conflicts with the above. That figure probably reflects the Nov 4 print, but **this needs checking against Treasury.**
  - Pricing of a December hike fell from about 85% around the October FOMC to about 66% before payrolls (FXStreet, Nov 5–6).
- **Nov 4:** the 10-year fell more than 6 bp to about 4.884% (CNBC) after the Democratic midterm wins and lower oil prices. The official Treasury print was reportedly about 4.90%.
- **Nov 3 (Election Day):** 10-year about 4.94%. September job openings (JOLTS) rose sharply (CNBC, Nov 3).
- **Oct 30:** DGS10 at 4.94. Oct 29: 4.98. Oct 28: 5.05. Oct 27: 4.99 (FRED).
- **Oct 28 FOMC:**
  - The Fed held at 3.75–4.00% on a 10–2 vote, with two dissents in favour of a hike. Sources disagree on who dissented.
  - Chair Warsh did not commit to a December hike and said inflation has been above 2% for about six years (Benzinga / pomegra / ING, Oct 28–29).
  - The Fed had hiked in September (CNBC, Sep 16, 2026).
- **Oct 14:** September CPI was 3.7% year on year, up from 3.4%, and about 0.6% month on month. September payrolls were only +29k (Washington Post, Oct 2).
- **Autumn peak:** about 5.16% on Sep 24, the highest since 2007 (CNBC, Sep 25), and about 5.31% on Oct 5. Early-September lows were about 4.77–4.80% (Macrotrends). **4.75 is therefore below the September floor**, and breaking it would mean the lowest level since roughly August.
- **Term premium:** one analysis says most of the roughly 107 bp one-year rise in the 10-year is real yield, about half of it term premium (Longhand Research substack). That implies fiscal and term-premium news matters as much as Fed expectations.

**Scheduled before Nov 30:**
- Oct CPI on **Tue Nov 10, 8:30 ET**.
- PPI, retail sales and jobless claims in mid-November (exact dates not verified).
- FOMC minutes, likely around Nov 18 (not verified).
- November refunding auctions of 3-, 10- and 30-year debt, likely the week of Nov 9 (not verified).
- Nvidia earnings, likely around Nov 18–19 (not verified). This is relevant given the AI-led selloff.
- October PCE, likely in late November (not verified).
- The next jobs report and the Dec 8–9 FOMC fall **after** the window.

## 4. Drivers and scenarios
**Paths to YES (needs a further drop of about 8–9 bp):**
- A soft jobs report today (payrolls well under 60k, unemployment at 4.3% or higher) cuts December hike odds further.
- A tame October CPI on Nov 10, after September's hot 3.7%.
- The tech/AI selloff continues into a broader risk-off move with sustained safe-haven buying, a VIX above 30, and credit spreads widening (Benzinga already flagged tighter credit in late October).
- A divided government is read as fiscally restraining, lowering term premium (CNBC, Nov 3).
- Lower oil prices feed into lower inflation expectations.
- Momentum: the 10-year fell about 40 bp in October and is on course for its first monthly decline since February.

**Paths to NO:**
- A firm jobs report (ADP already beat) and hot CPI revive pricing of a December hike, which was about 85% before the selloff.
- Equities stabilise (a strategist called the selloff "knee-jerk") and the haven bid unwinds, so the 10-year returns to 4.9–5.0%.
- Weak demand at the refunding auctions, or concerns about supply or term premium.
- Early-September support around 4.77–4.80 holds, with closing prints bottoming at 4.76–4.80, just short of the threshold.
- Note the gap between intraday or other-vendor closes and the Treasury print. A dip to 4.75 intraday is not enough.

## 5. Signposts
- **Today's payrolls and unemployment (largest single input):**
  - Below 40k and/or unemployment at 4.3% or higher: strongly toward YES. A 10–15 bp rally could hit 4.75 or below today or early next week.
  - Above 100k with strong wages: toward NO, with a likely 5–10 bp back-up.
- **Official Treasury prints for Nov 5 and 6:** each day closer to 4.76 raises the odds sharply. A close at 4.78 or below would make YES likely.
- **Oct CPI (Nov 10):** headline or core at or below 0.2% month on month moves toward YES; 0.4% or higher toward NO.
- **Equity and volatility path:** a further Nasdaq drawdown, VIX above 30, or credit stress moves toward YES; a quick rebound moves toward NO.
- **Fed communication:** Warsh or other officials talking down a December hike moves toward YES; hawkish dissenters or speeches toward NO.
- **10-year auction:** the tail or stop-through at the auction, and term-premium headlines (fiscal, Treasury refunding guidance).

## 6. Uncertainties
- **The actual October jobs report** and today's market reaction: the most important unknown.
- **The exact official Treasury par yields for Nov 3–5:** sources conflict between 4.83 and 4.90 for Nov 5.
- **Exact dates** of the refunding auctions, PPI, retail sales, FOMC minutes and Nvidia earnings in November 2026.
- **Realized volatility:** the 6–8 bp per day assumption is inferred, not measured. Recent moves suggest the high end, which favours YES. The base-rate figures in §2 are my calculations, not published statistics.
- **Fed details:** the identity of the October dissenters and exact current December-hike pricing after the payrolls report.
- **Treasury publication:** whether Treasury publishes a Veterans Day value. It normally doesn't, which removes one chance.

## Sources
- [Treasury Yields Slide as Tech Rout Fuels Haven Bid, With Two-Year Down 11 bp Before Friday's Payrolls (Private Banker, Nov 5, 2026)](https://leprivatebanker.com/2026/11/05/treasury-yields-slide-as-tech-rout-fuels-haven-bid-with-two-year-down-11-basis-points-before-fridays-payrolls/)
- [Stock markets plunge as massive tech sell-off wipes $2.5 trillion (CNN, Nov 5, 2026)](https://www.cnn.com/2026/11/05/investing/tech-heavy-nasdaq-plunges)
- [Wall Street Plunges 4.4% as Fear Gauge Jumps (Rio Times, Nov 6, 2026)](https://riotimesonline.com/global-economy-briefing-november-6-2026)
- [Treasury yields fall as Democrats win big in U.S. midterm elections (CNBC, Nov 3, 2026)](https://www.cnbc.com/2026/11/03/treasury-yields-fall-as-democrats-win-big-in-us-midterm-elections.html)
- [US 10-Year Treasury Yield Up to 4.9% (Trading Economics)](https://tradingeconomics.com/united-states/government-bond-yield/news/598668)
- [US 10 Year Treasury Note Yield (Trading Economics)](https://tradingeconomics.com/united-states/government-bond-yield)
- [Treasury Yields Today (Stockmarketwatch)](https://stockmarketwatch.com/bonds)
- [DGS10 (FRED)](https://fred.stlouisfed.org/series/DGS10)
- [10 Year Treasury Yield 1962–2026 (Macrotrends)](https://www.macrotrends.net/2016/10-year-treasury-bond-rate-yield-chart)
- [10-year Treasury yield little changed to end a volatile week (CNBC, Sep 25, 2026)](https://www.cnbc.com/2026/09/25/treasury-yields-bonds-debt.html)
- [10-year Treasury yield climbs back to 5% after Fed hikes rates (CNBC, Sep 16, 2026)](https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html)
- [10-Year Treasury Yield Falls to 4.90%, Erasing the Autumn Spike (24/7 Wall St.)](https://247wallst.com/cards/the-benchmark-yield-has-retraced-the-entire-autumn-spike-ba-macro-release-01m6q2hm6v01xbx6a5xjzcyq5y)
- [Treasury Yields Snapshot: October 9, 2026 (Advisor Perspectives)](https://www.advisorperspectives.com/dshort/updates/2026/10/09/treasury-yields-snapshot-october-9-2026)
- [FOMC October 2026: Fed Holds Rates in a 10-2 Vote (Admiral Markets)](https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates)
- [Fed Rate Held at 3.75-4.00% as Warsh Keeps December Open (pomegra)](https://pomegra.io/news/fed-rate-held-at-375-400-as-warsh-keeps-december-open)
- [Warsh Won't Commit to December Hike as Bond Market Tightens (Benzinga, Oct 2026)](https://www.benzinga.com/markets/macro-economic-events/26/10/62672193/warsh-december-hike-bond-market-tightening-credit-spreads)
- [Fed holds rates steady despite inflation being too high (ING)](https://think.ing.com/articles/fed-holds-rates-steady-despite-inflation-being-too-high/)
- [The Warsh Reaction Function (Longhand Research)](https://struggleman.substack.com/p/the-warsh-reaction-function)
- [The October jobs report is out Friday. Here's everything to expect (CNBC, Nov 5, 2026)](https://www.cnbc.com/2026/11/05/october-jobs-report-preview.html)
- [Can the October jobs report revive market sentiment after the US stock selloff? (FXStreet, Nov 6, 2026)](https://www.fxstreet.com/news/can-the-october-jobs-report-revive-market-sentiment-after-the-us-stock-selloff-202611060537)
- [US October Nonfarm Payrolls Preview (TradingKey)](https://www.tradingkey.com/analysis/stocks/us-stocks/262279310-us-nfp-preview-october-employment-recovery-stocks-dollar-gold-test-tradingkey)
- [ADP report October 2026: Private sector adds 86,000 jobs (Fox Business)](https://foxbusiness.com/economy/private-sector-added-86000-jobs-october-above-expectations-adp-says)
- [U.S. economy added 29,000 jobs in September (Washington Post, Oct 2, 2026)](https://www.washingtonpost.com/business/2026/10/02/us-economy-added-29000-jobs-september-missing-estimates/)
- [When Is the Next CPI Report? November 10, 2026 (cpichart)](https://cpichart.com/cpi-release-calendar/)
- [BLS CPI release](https://www.bls.gov/news.release/pdf/cpi.pdf)
- [Job openings posted big September gain (CNBC, Nov 3, 2026)](https://cnbc.com/2026/11/03/job-openings-posted-big-september-gain-in-positive-sign-for-labor-market-ahead-of-payrolls-report.html)
- [Treasury Daily Par Yield Curve Rates (resolution source)](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)