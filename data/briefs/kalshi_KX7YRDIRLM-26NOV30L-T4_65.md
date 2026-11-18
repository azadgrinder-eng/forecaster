# Research brief: Will the 7-year Treasury par yield print below 4.65% on any business day in November 2026?

**Short answer:** The 7-year yield is about 4.95–5.01%, so it needs to fall roughly 31–36bp in the 8 business days left. I estimate about 4–12% chance it does, plus a small chance it already happened on Nov 5 that I could not rule out. Checking Treasury's par yields for Nov 2–6 is the most important open item.

**Data caveat:** My page fetches failed because the proxy refused the connection. That included Treasury.gov, FRED, H.15, Mortgage News Daily, Forbes and Newsquawk. Every figure below comes from search-result summaries of those pages, and some of them disagree. Before finalizing, a forecaster should check the Treasury Daily Par Yield Curve page directly.

---

## 1. Resolution mechanics

- **YES condition:** Treasury's published Daily Par Yield Curve Rate for the 7-year tenor is **4.64% or lower** (that is, below 4.65%) on at least one business day from **Nov 1 to Nov 30, 2026**. Only the published end-of-day number counts. Intraday prices and later revisions are ignored.
- **Early expiry:** The market expires as soon as the threshold is hit (Rule 7.2). Otherwise it expires at 10:00 AM ET on Dec 1. If no value can be determined, Rule 7.1 applies.
- **Business days already past:** Nov 1 was a Sunday. The past business days are Nov 2–6, 9, 10, 12, 13, 16 and 17. Nov 11 (Veterans Day) has no print in H.15 or FRED (DGS7 search summary, Nov 2026). Treasury's par curve and the Fed's H.15 7-year series are the same numbers, published by Treasury.
- **Business days left (including today, Nov 18):** Nov 18, 19, 20, 23, 24, 25, 27 and 30, for **8 prints**.
  - Nov 26 (Thanksgiving) has no print.
  - Nov 27 is normally an early-close bond day, but Treasury still publishes a curve. It is a thin, low-volume session.
- **Main ambiguity: did it already resolve YES on Nov 5?**
  - Mortgage News Daily is summarized as showing a 4.728% close on "Nov 04" and 4.810% on "Nov 01". Nov 1 was a Sunday, so its dates are suspect.
  - Bloomberg reported that on **Nov 5** Treasuries rallied by "as much as 12bp" across maturities to their lowest levels since early September, as the Nasdaq 100 fell about 6% (Bloomberg, Nov 5, 2026).
  - If 4.728% was the Nov 4 close and the 7-year fell close to 12bp on Nov 5, it could have touched about 4.61–4.65%.
  - Other data argue against that. The 10-year was summarized at about 4.84% on Nov 5 (fourweekmba tabulation) and 4.864% on Nov 6 (CNBC, Nov 6, 2026). The 10-year minus 7-year gap in mid-November was about 8–11bp. That implies a 7-year of about 4.73–4.76% on Nov 5–6, consistent with the H.15 print of **4.76% on Nov 9**.
  - My best guess is that the November low so far is about 4.72–4.76%, above the threshold. That fits with this market still being open on Nov 18. **Forecasters should confirm the Treasury par 7-year prints for Nov 2–6.** If any of them is ≤4.64%, the answer is already YES.

## 2. Reference classes and base rates

**A. Random walk using current volatility.** The yield needs to fall about 31–36bp from roughly 4.96–5.00% at some point in 8 sessions. Under a driftless random walk, the chance of touching the barrier is about 2 × P(the yield ends below it).
- At 6bp/day (normal for 2023–25), σ₈ ≈ 17bp, giving about **5%**.
- At 7bp/day, σ₈ ≈ 20bp, giving about **9%**.
- At 8.5bp/day (the recent realized pace), σ₈ ≈ 24bp, giving about **15–17%**.

Recent daily moves show high volatility: −12bp (Nov 5), +13bp (Nov 9→10), +13bp (Nov 10→12), +3bp (Nov 12→13), −3 to −4bp (Nov 13→16). Volatility tends to fall into Thanksgiving week, which pushes the estimate toward the lower end of the range.

**B. Historical 30bp+ falls in two weeks.** From memory, not verified this session, 7-year drops of ≥30bp within about 8 sessions have happened in a handful of episodes since 2020:
- March 2020 (COVID)
- March 2023 (SVB, about −70bp)
- Early-to-mid November 2023 (Fed pivot and soft CPI, about −40bp)
- Late July to Aug 5, 2024 (weak jobs report and carry-trade unwind, about −40bp)

My rough estimate is that about **3–7% of 8-day windows** since 2022 contain a drop of this size. These moves usually need a growth or financial-stability scare, or a dovish Fed shock. Fresh evidence from this year: the 10-year fell 44bp between Oct 2 and Nov 5, 2026 during an AI and chip selloff, but that took about 23 sessions (fourweekmba, Nov 2026).

**C. A hawkish Fed with a hike nearly priced in.** When a hike is priced at more than 90% two to three weeks before a meeting, front and belly yields seldom fall 30bp or more unless a crisis hits. The mid-2000s and 2022–23 hiking cycles offer few such cases outside March 2023. That points toward the lower end, about **3–6%**.

## 3. Current state of the world (most recent first)

- **Nov 18 (today):** Minutes of the Oct 27–28 FOMC meeting are due at 2:00 PM ET. In October the Fed held rates steady at 3.75–4.00% (TradingKey/Intellectia week-ahead, Nov 2026). Market reaction to Nvidia's results is still coming in.
- **Nov 17:**
  - The 10-year slipped 1bp to about 5.109% (5.10% per Trading Economics). The 2-year was at 4.806% and the 30-year at 5.46% (CNBC, Nov 17, 2026).
  - Bloomberg separately reported a haven bid as stocks fell after an NSA network outage and tech losses, with yields down as much as 4–5bp (Bloomberg, Nov 17, 2026).
  - October retail sales came out. Nvidia reported after the close; one account says it beat estimates and guidance, but I found no second source.
  - The market priced about 93–98% odds of a 25bp hike on Dec 8–9 (CNBC, Nov 17, 2026).
  - St. Louis Fed President Musalem said up to four more hikes may be needed (CNBC, Nov 17, 2026). Dallas Fed President Logan wants at least two more (Yahoo, Nov 2026).
- **Nov 16:** The 7-year settled at **5.009%**, down 3.2bp, as the tech rout resumed (Newsquawk, Nov 16). Forbes and FRED-tracker sites show 5.01%. The Dow fell more than 800 points and the S&P 500 had its lowest close since July (CNBC, Nov 16, 2026).
- **Nov 9–13 (H.15 7-year):** 4.76 (Nov 9), 4.89 (Nov 10), holiday (Nov 11), 5.02 (Nov 12), 5.05 (Nov 13). A hot October CPI and hawkish Fed comments drove the move. Treasuries had their worst weekly selloff in about 18 months (economies.com and Bloomberg, Nov 10–13, 2026). Bloomberg noted on Nov 13 that the haven rally "didn't last".
- **Nov 6:** The October jobs report was strong: +165k payrolls against about 59k expected, with unemployment at 4.1%. The 10-year rose to 4.864% (CNBC, Nov 6, 2026).
- **Nov 5:** A haven rally of up to 12bp took yields to their lowest since early September as the Nasdaq 100 fell about 6% (Bloomberg, Nov 5, 2026).
- **Nov 3–4:** Yields moved around the midterm election, jobs data and Iran tensions. The 10-year was about 4.90% on Nov 4 (CNBC, Nov 3–4, 2026).
- **Oct 29:** The 7-year auction cleared at **4.894%**, down from 5.085% at the prior auction, with a bid-to-cover of 2.46 (MarketScreener, Oct 29, 2026).
- **Background for 2026:** Kevin Warsh became Fed chair around May. Inflation is elevated, linked to the Iran war and oil. In September the 10-year rose more than 50bp to about 5.3% and the 30-year reached its highest level since 2002 (Fortune, Oct 11, 2026). Forbes reports a 12-month average 7-year yield of 4.32% (Forbes, Nov 17, 2026).

**Scheduled before Nov 30:**
- FOMC minutes (Nov 18)
- Weekly jobless claims (Nov 19)
- Probably 2-, 5- and 7-year note auctions around Nov 23–25 (not verified)
- **October PCE and the second estimate of Q3 GDP at 8:30 AM on Nov 25**
- Thanksgiving close (Nov 26) and a likely early bond close (Nov 27)
- The November jobs report (about Dec 4) and the FOMC decision (Dec 8–9) both fall **after** the window.

## 4. Drivers and scenarios

**Paths to YES (a drop of more than 31–36bp):**
1. **Equity or financial crash and flight to safety.** The AI and tech selloff gets much worse, for example a fallout from Nvidia, credit stress tied to AI capex, or a market-structure or outage shock. This needs several more days like Nov 5's −12bp. It is the most plausible path, given that the October and early-November tech rout already pulled the 10-year down 44bp.
2. **Dovish surprise.** A soft October PCE on Nov 25, dovish FOMC minutes, or Warsh signalling a pause would lead markets to remove the December hike and later hikes. About 62bp of hikes is priced over the next three meetings (MarketScreener, Nov 2026), so there is room to reprice. But removing a priced hike alone probably moves the 7-year only 15–25bp.
3. **Geopolitical de-escalation or an oil collapse** (Iran), which would lower inflation expectations.

**Paths to NO:**
- Yields stay around 4.9–5.1% while the market waits for the December hike.
- The term-premium and supply story (debt above $39T, Fed balance-sheet runoff) holds up yields.
- A hot PCE print, or hawkish Fed speakers (Musalem, Logan) confirming more hikes.
- Thin Thanksgiving trading lowers volatility.

Even large haven rallies this month (Nov 5, Nov 16–17) moved yields only 3–12bp per day and then reversed.

## 5. Signposts

- **Strongly toward YES:**
  - The Treasury par print for **Nov 5** turns out to be ≤4.64%, which would mean the market has already resolved YES.
  - A 7-year close at or below about 4.85% by Nov 20–23.
  - The Nasdaq falling more than 5% in a day, or signs of credit or funding stress.
  - A Fed official (especially Warsh) leaning against a December hike, or December hike odds dropping below about 60%.
  - A soft core PCE on Nov 25, at or below 0.1% month on month.
- **Toward NO:**
  - The 7-year staying at or above 4.95% through Nov 20, which leaves about 6 prints to fall more than 30bp.
  - Hawkish minutes, hot claims or PCE, or a weak (tailing) 7-year auction.
  - Nvidia-driven relief in risk assets, which reduces the haven bid.
- **Note:** Each business day that passes without a large rally sharply cuts the remaining odds, because the touch probability scales roughly with the square root of the days left.

## 6. Uncertainties

- **The actual Nov 2–6 par 7-year prints.** Sources conflict: Mortgage News Daily's 4.728% "Nov 4" figure plus Bloomberg's "as much as 12bp" rally on Nov 5 could imply a dip below 4.65%. The 10-year levels and the 4.76% print on Nov 9 suggest it did not. This is the single most important fact to verify.
- **Exact 7-year level on Nov 17 and today.** My estimate of about 4.95–5.00% is inferred from the 10-year at 5.10–5.11% and the 7-year's 8–11bp gap below it.
- **Nvidia earnings reaction and the content of the FOMC minutes** were not available when I searched.
- **Whether the Fed hiked in September 2026.** This rests on a single source. The current target range of 3.75–4.00% is reported consistently.
- **Historical base rates** for 30bp+ drops in 8 days are approximate, from memory, and I did not compute them from DGS7 data this session.

## Sources
- [Federal Reserve Board - H.15 Selected Interest Rates (Daily), Nov 16, 2026](https://www.federalreserve.gov/releases/h15/)
- [FRED DGS7 – 7-Year Constant Maturity](https://fred.stlouisfed.org/series/dgs7)
- [DGS7: 5.01 (2026-11-16) – finzdata](https://data.finzdata.com/macro/dgs7)
- [Mortgage News Daily – 7 Year Treasury Yield](https://www.mortgagenewsdaily.com/treasury/7yr)
- [Forbes – Treasury Rates Today: November 17, 2026](https://www.forbes.com/advisor/investing/treasury-rates/)
- [Newsquawk – US Market Wrap, 16th November 2026](https://www.newsquawk.com/headlines/us-market-wrap---16th-november-2026-risk-off-trade-as-tech-rout-resumes-supporting-havens-)
- [Bloomberg – US Bonds Rally as Stock Selloff Follows NSA Network Outage (Nov 17, 2026)](https://www.bloomberg.com/news/articles/2026-11-17/treasuries-rise-as-risk-averse-investors-dump-stocks-buy-bonds)
- [CNBC – Treasury yields: investors digest retail sales data (Nov 17, 2026)](https://www.cnbc.com/2026/11/17/treasury-yields-bonds-inflation.html)
- [CNBC – Musalem says four more rate hikes may be needed (Nov 17, 2026)](https://cnbc.com/2026/11/17/alberto-musalem-fed-interest-rates.html)
- [CNBC – Dow drops more than 800 points (Nov 16, 2026)](https://www.cnbc.com/2026/11/16/stock-market-today-live-updates.html)
- [Bloomberg – That Haven Trade in Treasury Bonds Didn't Last Long (Nov 13, 2026)](https://www.bloomberg.com/news/newsletters/2026-11-13/that-haven-trade-in-treasury-bonds-didn-t-last-long)
- [Bloomberg – US Bond Market Selloff After Fed Officials Signal Rate Hikes (Nov 10, 2026)](https://www.bloomberg.com/news/articles/2026-11-10/traders-who-rushed-to-safety-of-bonds-get-rattled-in-reversal)
- [Yahoo Finance – Bond yields surge most in 19 months as traders brace for Fed hikes](https://finance.yahoo.com/economy/policy/articles/bond-yields-surge-most-19-221447570.html)
- [economies.com – US Treasury bonds head for worst weekly selloff in 18 months](https://www.economies.com/stocks/united-states-news/us-treasury-bonds-head-for-worst-weekly-selloff-in-18-months-as-inflation-fears-intensify-50654)
- [MarketScreener – Treasury Yields Fall, German Bunds Tick Higher](https://www.marketscreener.com/news/treasury-yields-fall-german-bunds-tick-higher-2nd-update-ce785edfdd8cfe25)
- [CNBC – 10-year yield rises after stronger-than-expected October jobs report (Nov 6, 2026)](https://www.cnbc.com/2026/11/06/treasury-yields-inch-lower-as-investors-look-ahead-to-key-jobs-data-.html)
- [CNBC – Treasury yields rise as investors weigh midterm vote, jobs data and Iran tensions (Nov 3, 2026)](https://www.cnbc.com/2026/11/03/us-treasury-yields-bonds.html)
- [Bloomberg – Treasuries Soar as Tech-Stock Selloff Stokes Haven Demand (Nov 5, 2026)](https://www.bloomberg.com/news/articles/2026-11-05/treasuries-extend-advance-as-technology-shares-resume-slide)
- [fourweekmba – Treasuries Tracked AI Chips for a Month: 10-Year Fell 44bp](https://fourweekmba.com/ai-treasuries-tracked-ai-chips-for-a-month-10-year-fell-44bp/)
- [MarketScreener – U.S. 7-Year Treasury Auction Shows In-Line Demand (Oct 29, 2026)](https://www.marketscreener.com/news/u-s-7-year-treasury-auction-shows-in-line-demand-ce785fdada8df626)
- [TradingKey – Week Ahead: Nvidia Q3 Earnings, Retail Sales, FOMC Minutes](https://www.tradingkey.com/analysis/stocks/us-stocks/262305825-week-ahead-nvidia-q3-earnings-us-october-retail-sales-fomc-minutes-walmart-tradingkey)
- [Intellectia – Stock Market Week Ahead: Nvidia Earnings and Fed Minutes (Nov 16, 2026)](https://intellectia.ai/blog/stock-market-week-ahead-nvidia-earnings-fed-minutes-nov-16-2026)
- [Kiplinger – This Week's Economic Calendar (Nov 16–20)](https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar)
- [Delta Exchange – November 2026 Global Market Calendar](https://www.delta.exchange/blog/november-2026-global-market-calendar-key-economic-events-earnings-and-release-times)
- [Fortune – The hawk Fed chair who broke the bond market (Oct 11, 2026)](https://fortune.com/2026/10/11/the-hawk-fed-chair-who-broke-the-bond-market/)
- [Advisor Perspectives – Bond Market Ushers in Warsh Era With Bets on 2026 Hike (May 26, 2026)](https://www.advisorperspectives.com/articles/2026/05/26/bond-market-ushers-warsh-era-bets-2026-hike)
- [Trading Economics – US 10 Year Treasury Note Yield](https://tradingeconomics.com/united-states/government-bond-yield)