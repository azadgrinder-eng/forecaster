# Research Brief: Will ICE WTI (Pyth "CLL", Active Month) reach $120 in November 2026?

Date of brief: Nov 14, 2026 (Saturday). About 10–11 trading sessions remain, Nov 16 to Nov 30. I could not open any article pages (WebFetch was blocked), so every fact below comes from search-result summaries of the cited articles.

## 1. Resolution mechanics

- **What counts as YES:** any Pyth 1-minute candle for CLL (ICE Futures Europe WTI, Active Month) with a High of $120.00 or more. It must occur after the market was created and inside a Pyth market session on a November 2026 business day. Prices are used exactly as Pyth publishes them, with no rounding. One intraday print is enough; the price does not need to settle there.
- **Who decides:** Pyth's published candles. ICE Futures Europe's official daily high/low is a fallback only if Pyth has an outage. Anything after Pyth's scheduled session close does not count.
- **Contract roll matters:**
  - By my reading of the spec, the ICE WTI December 2026 contract's last trading day is Thu Nov 19. That is the 4th US business day before Wed Nov 25, which is itself a business day.
  - So the January 2027 contract should become the Active Month at the open of the Nov 17 session (about 8:00 PM ET Sun/Mon Nov 16).
  - For roughly 10 of the remaining ~11 sessions, the price that counts is the January contract.
  - The curve has been in backwardation. Brent's Dec–Jan step was about $3/bbl and WTI Nov26–Dec27 about $14/bbl (commodity-board, undated, autumn 2026). So January probably trades a dollar or more below December, which makes $120 slightly harder.
  - **Check this date on ICE's expiry page.** I computed it from the rule and did not confirm it.
- **Holidays:** Thanksgiving (Thu Nov 26) and the Nov 27 half-day probably mean reduced or modified Pyth sessions.
- **Small ambiguities:**
  - The question closes Dec 1 04:59 UTC (Nov 30, 11:59 PM ET). The Sunday/Monday evening session that opens on Nov 30 belongs to the Dec 1 business day and may not count.
  - "After market creation": the creation date is unknown. It doesn't matter here, because WTI has not been near $120 at any point in November.
- **Benchmark tracking:** ICE WTI is cash-settled against NYMEX WTI and tracks it to within cents, so NYMEX WTI news is a good proxy.

## 2. Reference classes and base rates

1. **WTI front month at or above $120 at any time in history.** This has happened only in 2008 (peak $147.27, July 2008) and 2022 (intraday about $130.50 on Mar 8 and about $123 in June). Even at the worst of the 2026 Iran war, with Hormuz effectively shut in March–April, WTI did not reach $120:
   - Highest daily spot: $114.58 on Apr 7, 2026 (Macrotrends).
   - Highest settlement: about $112.95 on Apr 7, with intraday spikes "near $117" (unverified).
   - Investing.com's 52-week futures high is $117.63.
   - The October 2026 peak was about $107.56 to roughly $110 for WTI. The "four-year high of $114" on Oct 30 that CNN cites is probably Brent.
   - **In about 8.5 months of a hot war centred on Hormuz, WTI never printed $120.**
2. **A rise of 35% or more within about 2.5 weeks.** From $88.56 (Nov 13 settle), $120 needs +35.5%, or more like +37–40% on the January contract. Historical cases are almost all sudden, severe supply shocks:
   - Aug 1990, the Iraq invasion of Kuwait, though that move took longer than 2.5 weeks.
   - Late Feb to mid-Mar 2022 (about $92 to $130 in roughly 2 weeks).
   - March 2026 (a record monthly gain of more than 50%; Trading Economics).
   - Excluding the 2020 rebound from negative prices, perhaps 3–4 such episodes in about 40 years of trading. That is well under 1% of random 2.5-week windows. Conditional on an active war, the rate is clearly higher.
3. **Volatility-model touch probability.** NYU V-Lab's model (Nov 5) projected about 91% annualised one-day-ahead volatility and about 102% one month out. OVX was about 50 in late September and peaked at 118–125 in March. Using the standard probability of touching a level (log-normal, no drift) over about 11 sessions (T ≈ 0.044 years), starting from about $87 to reflect the January discount:
   - 60% volatility: about 1–2%.
   - 75% volatility: about 4–5%.
   - 90% volatility: about 8–10%.
   - Oil's returns have fat tails, which pushes these up. Momentum is currently negative and the IEA now forecasts a surplus, which pushes them down.

## 3. Current state of the world (most recent first)

- **Nov 13 (Fri):** WTI settled at $88.56 (−18¢) and Brent at $95.84 (+2¢); both fell about 2.5% for the week (Reuters via Newsbeep, Nov 13). HDFC Sky has WTI December at $88.52. Benzinga's higher figures look like the previous week's numbers. Macrotrends spot: $88.39–88.81.
- **Nov 13: IEA Oil Market Report.** The IEA switched from a forecast Q4 deficit to a forecast Q4 2026 surplus of about 1.7 mb/d, and about 3.8 mb/d for 2027 (BNN Bloomberg / The National, Nov 13).
  - Gulf exports are recovering but remain about 26% below pre-war levels.
  - Some tankers are making "dark crossings" through Hormuz with tracking switched off.
  - OPEC October crude output was 41.23 mb/d, up 2.04 mb/d month on month and 97% of the February (pre-war) level.
  - Diesel and other refined products remain tight.
- **Nov 12:** Brent rose 3.3% to $95.82 after Trump said "we don't need a deal with Iran… we've got their Strait." The US blockade of Iranian oil stays in place (CNBC, Nov 12; CBS live updates).
  - Iran's military said four tankers were hit by explosions in the strait.
  - US officials are reportedly split: Rubio favours the blockade, Vance favours a deal; one report says Trump sidelined Vance from Iran diplomacy (Investing.com).
- **Nov 10–11:** WTI hit a two-month low near $86.5 (Reuters via Investing.com, Nov 11). Earlier in the week, Brent fell 3.6% to $94 as Qatar's PM took an Iranian Hormuz proposal (reported as an "$8 billion" deal) to the White House; Iran's security council secretary called the talks "fake news" (OilPrice.com).
  - UKMTO reported two attacks on ships on Nov 10 and one on Nov 11; the tanker DOMINICA PROSPERITY was hit near Ras al Khaymah (UANI, Nov 13; GlobalSecurity, Day 258 update, Nov 12).
  - The IMO counts 136 incidents and 25 seafarers killed since the war began. October had 37 ships attacked, the most of any month.
- **Week ending ~Nov 6:** WTI fell 13% and Brent 16%. Brent dropped about $25 from its Oct 30 high to below $90 on Nov 10 (CNN, Nov 11).
  - Trump, who had hinted that strikes would resume after the midterms, said just before the election that new attacks were no longer needed. CBS reported "new U.S. strikes on eve of midterm elections."
  - Democrats won the midterms, which may increase pressure on Congress to constrain the war (CNN).
  - EIA data showed US crude stocks up 4.7 mb to 414.4 mb, against expectations of a draw.
- **October 2026:** Oil stayed above $100 every day (CNN; probably Brent). WTI averaged about $98–102, peaked at about $107.5–110, and the front-month futures high between Oct 13 and Nov 13 was $104.99 (Investing.com).
- **War background:** The war started around late February / early March 2026. An April ceasefire collapsed on Jul 8, and a June "peace deal" and August Qatar-brokered framework both failed. The 50-day moving average is about $95.4 and the 200-day about $87.7.
- **Scheduled before Nov 30:**
  - Dec contract expiry and roll to January (Nov 17–19).
  - Weekly EIA inventory reports (about Nov 18 and Nov 25; the Thanksgiving week release may be moved).
  - Thanksgiving holiday sessions (Nov 26–27).
  - An OPEC+ meeting, likely around Nov 30 / early December (date unconfirmed).
  - Ongoing Qatar-mediated US–Iran talks; there is no fixed deadline.

## 4. Drivers and scenarios

**Paths to YES (all need a large, sudden shock):**
- The US and/or Israel resume large-scale strikes on Iran, and Iran retaliates against Gulf export infrastructure (Saudi Abqaiq or Ras Tanura, UAE Fujairah, Qatar), taking several mb/d offline. This is the most plausible path.
- A sharp escalation of mining and tanker attacks that stops the partial "dark crossing" recovery and returns Hormuz to near-total closure, as in March.
- Even in these scenarios, WTI topped out around $113–117 in spring and about $110 in October. Getting to $120 from $87–88 within about 2 weeks would require something worse than anything seen so far in 2026.

**Paths to NO:**
- The status quo: a stalemate with sporadic attacks, Gulf flows slowly recovering, the IEA surplus narrative, and US inventories building. This keeps WTI around $80–100.
- A Qatar-brokered Hormuz deal or truce, which would push prices further down toward $70s–80s.
- An escalation that is only moderate, such as a spike back to $100–110.
- Roll mechanics: the January contract's backwardation discount removes roughly $1–3 of headroom.

## 5. Signposts

- **Toward YES:**
  - The US announces resumed strikes, or Israel strikes Iran.
  - Iranian attacks on Saudi, UAE or Qatari onshore facilities.
  - A confirmed sharp drop in Hormuz transits.
  - WTI back above $100–105 early in the week of Nov 16, which would bring $120 within a plausible one-day jump.
  - OVX or implied volatility back above 90–100.
- **Toward NO:**
  - A signed or announced Hormuz framework.
  - More IEA/OPEC surplus data or further US inventory builds.
  - WTI staying below $95 into Thanksgiving week. Each quiet session uses up the remaining window.
  - Trump continuing to signal no new attacks.

## 6. Uncertainties

- I could not confirm the exact all-time 2026 intraday high of ICE WTI or Pyth CLL (somewhere between $114.58 spot and $117.63 futures), nor the current December–January WTI spread.
- I did not verify the Pyth CLL session schedule or the ICE expiry date. The Nov 19 last trading day and Nov 17 roll are my calculation from the stated rule.
- I could not establish the market's creation date. It probably doesn't matter, because November's WTI high so far is under about $100.
- I found no current OVX reading; the V-Lab figure is a model estimate from Nov 5.
- I could not confirm the date of the next OPEC+ meeting.
- Reporting on the war is fast-moving and contested: Iranian claims are unverified, and UKMTO says most attacked ships no longer report.

## Sources
- [Reuters via Newsbeep – Oil prices set for second straight weekly drop (Nov 13, 2026)](https://www.newsbeep.com/809372/)
- [HDFC Sky – Brent Crude Falls 2.4% as OPEC+ Supply Rises](https://hdfcsky.com/news/crude-oil-slides-2-4percent-to-95-41-as-opec-output-surge-and-us-inventory-build-overpower-hormuz-risk-premium)
- [The National – Oil on track to post second weekly decline (Nov 13, 2026)](https://www.thenationalnews.com/business/energy/2026/11/13/oil-on-track-to-post-second-weekly-decline-as-trump-eases-fears-of-renewed-war-with-iran/)
- [BNN Bloomberg – World oil market returning to surplus, IEA says (Nov 13, 2026)](https://www.bnnbloomberg.ca/markets/oil/2026/11/13/world-oil-market-is-returning-to-surplus-as-gulf-exports-recover-iea-says/)
- [The National – Oil market to return to surplus, IEA (Nov 13, 2026)](https://www.thenationalnews.com/business/energy/2026/11/13/oil-market-to-return-to-surplus-for-first-time-since-start-of-iran-war-iea-says/)
- [CNBC – Oil prices rise after Trump says no Iran deal needed (Nov 12, 2026)](https://www.cnbc.com/2026/11/12/oil-prices-jump-after-trump-says-no-iran-deal-needed-weve-got-their-strait.html)
- [CNN – Trump's peaceful mood doesn't fully explain why energy prices are plunging (Nov 11, 2026)](https://www.cnn.com/2026/11/11/economy/oil-price-iran-trump)
- [Investing.com/Reuters – Oil rises from two-month low as Hormuz attacks offset truce hopes](https://www.investing.com/news/commodities-news/oil-rises-from-twomonth-low-as-hormuz-shipping-attacks-offset-iran-truce-hopes-5017512)
- [Investing.com – Oil set for second weekly loss as Trump says U.S. no longer needs Iran deal](https://www.investing.com/news/commodities-news/oil-prices-hold-gains-as-trump-sidelines-vance-from-iran-diplomacy-5023781)
- [OilPrice.com – Oil Sinks to $94 as Iran's $8 Billion Hormuz Deal Heads to Trump](https://oilprice.com/Latest-Energy-News/World-News/Oil-Sinks-to-94-as-Irans-8-Billion-Hormuz-Deal-Heads-to-Trump.html)
- [UANI – Iran Shipping Update (Nov 13, 2026)](https://www.unitedagainstnucleariran.com/analysis/iran-shipping-update-november-13-2026)
- [GlobalSecurity – Iran War 2026, Day 258 Update (Nov 12, 2026)](https://www.globalsecurity.org/military/ops/iran-war-oprep.htm)
- [CBS News – Trump says "we don't need a deal with Iran"](https://www.cbsnews.com/live-updates/iran-war-us-nuclear-strait-of-hormuz/)
- [Al Jazeera – Iran says tankers struck in Hormuz amid fears of new US attack (Nov 5, 2026)](https://www.aljazeera.com/news/2026/11/5/iran-says-tankers-struck-in-hormuz-amid-fears-of-new-us-attack)
- [Macrotrends – WTI Crude Oil Prices 10 Year Daily Chart](https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart)
- [Investing.com – Crude Oil WTI Futures Historical Prices](https://www.investing.com/commodities/crude-oil-historical-data)
- [Schaeffer's – Tracking Oil: A Timeline of Crude Prices in 2026 (Nov 12, 2026)](https://www.schaeffersresearch.com/content/education/2026/11/12/tracking-oil-a-timeline-of-crude-prices-in-2026)
- [FutureSearch – How high will oil (WTI) get by Dec 31, 2026?](https://futuresearch.ai/app/p/a/kalshi-kxwtimax-26dec31-jun23)
- [Trading Economics – Oil Set for Record Monthly Surge](https://tradingeconomics.com/commodity/crude-oil/news/537517)
- [NYU V-Lab – OVX Spline-GARCH Volatility Analysis](https://vlab.stern.nyu.edu/volatility/VOL.OVX%3AVIND-R.S0GARCH)
- [SpotGamma – Crude oil rally vs oil options volatility](https://spotgamma.com/crude-oil-rally-vs-oil-options-volatility/)
- [Pepperstone – Have we seen the worst of the oil market volatility?](https://pepperstone.com/en/analysis/navigating-markets/have-we-seen-the-worst-of-the-oil-market-volatility-brent-s-crisis-spike-and-what-comes-next)
- [Commodity-board – WTI and Brent ease from war highs but forward curve stays tight](https://commodity-board.com/wti-and-brent-ease-from-war-highs-but-forward-curve-stays-tight)
- [Wikipedia – 2026 Strait of Hormuz crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis)