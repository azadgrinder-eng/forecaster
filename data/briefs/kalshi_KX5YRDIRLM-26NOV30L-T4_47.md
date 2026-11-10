# Research brief: will the 5-year Treasury par yield print at or below 4.46% on any business day in November 2026?

**As of Tuesday, Nov 10, 2026, before the October CPI release.** The 5-year was about 4.68–4.70%. To resolve YES it has to fall about 22–24 bp more on a daily closing basis. Its lowest close so far this month is 4.59% (Nov 5).

## 1. Resolution mechanics

- **What counts:** YES if the 5-year (5 Yr) figure in Treasury's *Daily Treasury Par Yield Curve Rates* is below 4.47% on any business day from Nov 1 to Nov 30, 2026. Treasury publishes these to two decimals, so a print of 4.46% or lower is YES. Intraday levels don't count, and neither do revisions made after expiration.
- **Path-dependent:** One qualifying day is enough, and the market can settle early under Rule 7.2. Otherwise it expires at 10:00 AM ET on Dec 1.
- **Days left:** Nov 1 was a Sunday. Treasury curve data are not published on Nov 11 (Veterans Day, bond market closed) or Nov 26 (Thanksgiving). Counting today, that leaves about 14 observations: Nov 10, 12, 13, 16–20, 23–25, 27 (early close, but a published rate is expected) and 30.
- **Which number to watch:** The Fed's H.15 5-year constant-maturity rate (FRED series DGS5) is read off this same Treasury par curve and normally matches it to the basis point. Secondary sites that cite Treasury's par data match H.15 for Nov 4 (4.69%). Live quotes from CNBC, Investing.com or Trading Economics are intraday or market-close quotes and can differ by 1–3 bp from the official figure.
- **Edge cases:** If no Expiration Value can be determined, Rule 7.1 applies. A data outage, such as a government shutdown like the 43-day one in 2025, could matter in principle, but nothing suggests one is coming before Nov 30.

## 2. Reference classes and base rates

1. **Random-walk barrier model (my own calculation, not a historical count).** Assume the start is 4.69% and the barrier is 22.5 bp below it, with 14 daily observations.
   - At 6 bp/day volatility, the 14-day SD is about 22 bp. A continuous barrier gives about 2·Φ(−1.0) ≈ 32%; with discrete daily monitoring it's about 27%.
   - At 5 bp/day: about 24% continuous, about 20% discrete.
   - At 7–8 bp/day: about 35–40%.
   - **Realized volatility right now is high.** The H.15 daily closes for Nov 2–6 were 4.70, 4.74, 4.69, 4.59, 4.64 (Federal Reserve H.15 via search, Nov 2026). The daily changes were +4, −5, −10, +5 bp, so about 6–7 bp/day.
   - The model has no drift. A December hike is now largely priced in (about 77–84%), so the market already prices the hawkish case. That gives some room for a dovish surprise to pull the yield down.
2. **Recent trend in 2026.** The 5-year peaked at 5.09% on Sep 30 (Macrotrends, Nov 2026). Weekly H.15 averages were then 4.95 (Oct 16 week), 4.89 (Oct 23), 4.80 (Oct 30) and about 4.67 (Nov 2–6), a fall of roughly 7–10 bp a week (FRED WGS5YR, Nov 2026). If that pace simply continued for three more weeks, the yield would reach about 4.45–4.50, right at the threshold. Momentum like this tends to fade, though, and the strong jobs report on Nov 6 reversed some of the drop.
3. **One-month moves in high-volatility regimes (approximate, from general knowledge, not fetched).** In 2022–2024 the monthly SD of 5-year yield changes was roughly 25–35 bp. A fall of 20 bp or more in a month happened in roughly 20–25% of months. The 52-week range of 3.51% to 5.09% (Macrotrends) shows that 2026 is one of these high-volatility regimes.

**Reading across the three:** they suggest roughly 20–35% before today's CPI, with the CPI surprise as the largest single factor.

## 3. Current state of the world (most recent first)

- **Nov 10 (today):** October CPI comes out at 8:30 ET. I could not find the actual print or the market reaction. Consensus is +0.3% headline and +0.2% core month-on-month, after +0.6% and +0.3% in September. The Cleveland Fed nowcast is 0.24% headline and 0.21% core. BLS will not publish 12-month changes because October 2025 data are missing after the shutdown; outside estimates put headline inflation near 3.7–4.0% year-on-year. One preview said risks are "skewed to the upside." This is the last CPI before the Dec 8–9 FOMC (CNBC, Nov 9; investinglive, Nov 2026; Kiplinger). Trading Economics showed the 5-year at 4.68% on Nov 10 (−2 bp), but its date stamp is unreliable.
- **Nov 9:** Yields rose ahead of CPI. The 2-year was at about 4.56% (+4 bp), the 10-year at 4.87–4.88% and the 30-year at about 5.26%. Fed funds futures priced about 84% odds of a December hike (rallies.ai/Reuters, Nov 9; Trading Economics, Nov 9). By inference from the 2-year and 10-year, the 5-year was about 4.70%. Goldman said the 10-year could settle into a 4.75–5.0% range if risk assets stabilize (CNBC, Nov 9). Oil fell after the midterms changed expectations about the US-Iran conflict; Brent dropped about 9% overnight (Finimize, Nov 2026).
- **Nov 6:** The October jobs report was strong: +165k payrolls against a consensus of about 59–65k, +84k in upward revisions, unemployment at 4.1%, and average hourly earnings up 0.4% on the month and 3.1% on the year. CME FedWatch put a December hike at 76.8%. The 5-year closed at 4.64% (+5 bp) (Morningstar; 24/7 Wall St, Nov 7; Forbes, Nov 6).
- **Nov 5:** A sell-off in tech and AI stocks sent money into safe havens. The 2-year fell more than 11 bp intraday to about 4.47%, and the 5-year closed at 4.59%, the lowest so far this month (CNBC, Nov 5; H.15).
- **Oct 28:** The FOMC held at 3.75–4.00% by a 10–2 vote, with two dissents in favor of a hike. Chair Warsh; most participants expect one more hike this year (Federal Reserve, Oct 28; Admiral Markets).
- **Oct 27:** The 5-year note auction cleared at 4.845% (yielddocket).
- **Sep 16:** The Fed hiked 25 bp, 12–0. Through 2026, the Iran war and the oil shock have driven large bond sell-offs (Morningstar/MarketWatch, Mar 2; Semafor, May 18; KEYT, Sep 1).

**Scheduled before Nov 30** (dates are approximate unless confirmed):
- PPI: Fri Nov 13
- Retail sales: mid-November
- Minutes of the Oct 28 FOMC meeting: about Nov 18
- 2-, 5- and 7-year note auctions: about Nov 23–25 (5-year auction Tue Nov 24, settling Nov 30)
- PCE/personal income data: possibly late November
- Fed speeches throughout

The November jobs report (about Dec 4) and the FOMC (Dec 8–9) both fall after the window.

## 4. Drivers and scenarios

**Paths to YES (a fall of about 22 bp or more):**
- **Soft CPI today and/or soft PPI on Nov 13** (core ≤0.1–0.2% with benign services). This would cut December hike odds sharply from about 80%. A 5-year move of 10–15 bp over a day or two is plausible, and the 2-year already traded intraday near 4.47% on Nov 5.
- **More risk-off from the AI/tech sell-off or an equity correction.** Nov 5 alone took 10 bp off the 5-year.
- **Further de-escalation with Iran and a falling oil price**, which would lower breakevens.
- **Dovish Fed commentary or minutes** suggesting the hike might be skipped.
- **Continuation of the 6-week downtrend** from 5.09.

**Paths to NO:**
- **Hot or in-line CPI** (core ≥0.3%). This would lock in the December hike and push the 5-year back toward 4.8%. The September CPI release took the 10-year up more than 6 bp, to 5.28%.
- **Strong retail sales or PPI.**
- **Renewed escalation with Iran or an oil spike.**
- **Fiscal or supply pressure around the late-November auctions.**
- **Range-bound trading** in a 4.6–4.8% band, which is Goldman's "stabilization" case.

## 5. Signposts

- **Today's CPI (largest single factor):** Core at 0.1–0.2% with a soft services breakdown would push the probability up materially; a 5-year close at 4.55% or lower makes YES plausible. Core at 0.3% or higher would cut it sharply.
- **The 5-year close relative to 4.59%:** A new monthly low strengthens the downtrend case. Closes back above 4.75% leave little room in the time remaining.
- **December hike odds (CME FedWatch):** Falling below about 50% would be consistent with the 5-year in the low 4.5s.
- **Brent and Iran headlines; equity volatility in the AI/tech names.**
- **The 2-year:** A close below about 4.40% would usually go with a 5-year at or below 4.47%.
- **Nov 13 PPI, the FOMC minutes and the Nov 24 5-year auction** (tail or stop-through).
- **Time decay:** If the 5-year is still above 4.60% around Nov 20, the remaining window is short, about 6 sessions.

## 6. Uncertainties

- I couldn't get today's (Nov 10) CPI result or the official Treasury par-curve values for Nov 9–10. The Treasury and FRED pages weren't reachable, so the Nov 2–6 values come from H.15 data quoted in search results, and the Nov 9 level (about 4.70%) is inferred.
- I couldn't confirm a 4.66% Yahoo reading or a 4.627% Investing.com quote; both are undated.
- Dates of the PCE and retail-sales releases are unconfirmed; the 2025 shutdown may still be shifting the BLS/BEA calendar.
- Realized volatility for October 2026 is estimated from weekly averages, not daily data.
- The historical base rates in reference class 3 are approximate and come from general knowledge, not a dataset I computed from.
- Some sources disagree on the payroll consensus (59k vs 65k) and on the December hike odds (65–84%).

## Sources
- [Treasury Yield 5 Years (^FVX) – Yahoo Finance](https://finance.yahoo.com/quote/%5EFVX/)
- [5 Year Treasury Yield (1962-2026) – Macrotrends](https://www.macrotrends.net/2522/5-year-treasury-bond-rate-yield-chart)
- [Market Yield on U.S. Treasury Securities at 5-Year Constant Maturity (WGS5YR) – FRED](https://fred.stlouisfed.org/series/WGS5YR)
- [5-Year Constant Maturity (DGS5) – FRED](https://fred.stlouisfed.org/series/dgs5)
- [5-Year Inflation-Indexed (DFII5) – FRED](https://fred.stlouisfed.org/series/DFII5)
- [Federal Reserve Board – H.15 Selected Interest Rates](https://www.federalreserve.gov/releases/h15/)
- [2026-11-05 Selected Interest Rates – FRED release tables](https://fred.stlouisfed.org/release/tables?eid=289&rid=18)
- [United States 5 Year Note Yield – Trading Economics](https://tradingeconomics.com/united-states/5-year-note-yield)
- [US 10 Year Treasury Note Yield – Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield)
- [Treasury Rates Today: November 6, 2026 – Forbes](https://www.forbes.com/advisor/investing/treasury-rates/)
- [Treasury Yield Curve Today – Spot the Money](https://spotthemoney.com/rates/treasury-yields/)
- [Treasury Auction Results, Nov 2-8, 2026 – yielddocket](https://yielddocket.com/treasury-auctions/)
- [Treasury Auction Schedule – fedratecalc](https://fedratecalc.com/treasury-auction-schedule/)
- [10-year Treasury yield falls as traders exit tech stocks – CNBC, Nov 5, 2026](https://www.cnbc.com/amp/2026/11/05/treasury-yields-bonds-interest-rates.html)
- [Closing Look — Monday, November 9, 2026 – cappnotes](https://cappnotes.substack.com/p/closing-look-monday-november-9-2026)
- [Markets today – BNN Bloomberg, Nov 9, 2026](https://bnnbloomberg.ca/markets/dow-jones/2026/11/09/world-markets-bounce-back-after-a-recovery-for-ai-stocks-on-wall-street)
- [October jobs report beats forecasts, lifting December Fed hike odds – InvestmentNews](https://www.investmentnews.com/fixed-income/october-jobs-report-beats-forecasts-lifting-december-fed-hike-odds/268915)
- [Hot October Jobs Report Raises Odds of December Rate Hike – Morningstar](https://www.morningstar.com/economy/hot-october-jobs-report-raises-odds-december-rate-hike)
- [Odds of a December Rate Hike Jump to 77% – 24/7 Wall St., Nov 7, 2026](https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/)
- [Gold, silver advance… Fed rate expectations face inflation test – Kitco, Nov 9, 2026](https://www.kitco.com/news/article/2026-11-09/gold-silver-advance-dollar-weakens-fed-rate-expectations-face-inflation)
- [Treasury yields edge up before Tuesday's CPI release – rallies.ai](https://rallies.ai/news/treasury-yields-edge-up-before-tuesdays-cpi-release-1ef540bccd9a7e44)
- [Treasury yields rise as investors await October CPI – CNBC, Nov 9, 2026](https://www.cnbc.com/2026/11/09/us-treasurys-bonds-yields.html)
- [Goldman says 'the pieces are in place' for a shift in Treasury yields – CNBC, Nov 9, 2026](https://cnbc.com/2026/11/09/goldman-treasury-yields-bonds.html)
- [A key report for where inflation stood in October comes out Tuesday – CNBC, Nov 9, 2026](https://www.cnbc.com/2026/11/09/october-cpi-report-2026-inflation.html)
- [US CPI preview: 43-day shutdown leaves no official annual rate – investinglive](https://investinglive.com/news/us-cpi-preview-43-day-shutdown-leaves-no-official-annual-rate-as-monthly-pace-seen-easing)
- [US CPI takes centre stage… after the midterm selloff – investinglive](https://investinglive.com/news/us-cpi-takes-centre-stage-as-markets-look-to-steady-the-ship-after-the-midterm-selloff/)
- [Treasury yields rise as CPI data tests mortgage rate outlook – MPA](https://www.mpamag.com/us/mortgage-industry/industry-trends/treasury-yields-rise-as-cpi-data-tests-mortgage-rate-outlook/596712)
- [October CPI Report: What to Expect – Kiplinger](https://www.kiplinger.com/investing/economy/october-2026-cpi-report-what-to-expect)
- [Fed press release, October 28, 2026 – Federal Reserve](https://federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)
- [FOMC October 2026: Fed Holds Rates in a 10-2 Vote – Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates)
- [Oil slid as US midterms shifted the Iran war math – Finimize](https://finimize.com/content/oil-slid-as-us-midterms-shifted-the-iran-war-math)
- [Bonds log biggest selloff in 9 months as Iran conflict sparks unusual Treasury moves – Morningstar/MarketWatch](https://www.morningstar.com/news/marketwatch/20260302112/)
- [Bond sell-off over Iran war drives borrowing costs – Semafor, May 18, 2026](https://www.semafor.com/article/05/18/2026/bond-sell-off-over-iran-war-drives-borrowing-costs)
- [Global bonds sell off as Middle East conflict escalates – KEYT, Sep 1, 2026](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/09/01/global-bonds-sell-off-as-middle-east-conflict-escalates-further-stoking-inflation-fears/)