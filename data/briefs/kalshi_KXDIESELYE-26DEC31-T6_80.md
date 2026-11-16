# Research brief: Will the AAA national average diesel price on December 31, 2026 be above $6.80?

Note on method: all 12 searches were used. Every WebFetch call (AAA, Wikipedia, FleetOwner and others) was refused by the environment's proxy. The facts below therefore come from search-result summaries, which were often aggregator pages, not from pages I read in full. Treat specific decimals with some caution.

## 1. Resolution mechanics
- **What counts as YES:** the AAA "Today's National Average" for diesel, as shown on gasprices.aaa.com for December 31, 2026, must be strictly above $6.80. AAA reports to three decimals, so a reading of $6.800 resolves NO.
- **Timing:**
  - AAA updates its daily average once, early each morning (US Eastern), using OPIS data.
  - The market closes at 2026-12-31 04:59 UTC, which is 11:59 pm ET on Dec 30. That is before the Dec 31 figure is published, so the value that resolves the market won't be visible while trading is open.
  - In practice, the Dec 30 reading is the last value traders can see.
- **Who decides:** the market operator, reading AAA. The rules say nothing about how to handle the following:
  - an AAA site outage on Dec 31, or retroactive revisions;
  - a mismatch between AAA and other trackers. These differ a lot: on Nov 14, AAA showed $6.037 while GasBuddy showed $5.998. EIA's weekly survey usually runs about $0.05–0.10 below AAA, and EIA's last survey of the year (likely Dec 28) is not the resolution source.
- **How far the price has to move:**
  - The latest AAA reading is about $6.037 (Nov 14, 2026). YES needs a rise of about **$0.76, or +12.7%, in roughly 45 days.**
  - $6.80 is also about **$0.27 above AAA's all-time record of $6.5276** (Sept 22, 2026). So YES needs a new all-time high.

## 2. Reference classes and base rates
1. **Any 6-week rise of 12% or more in US retail diesel, 1994–2026.** This is my estimate from memory of the EIA/AAA series; I did not compute it from data. Such rises happen only in clear supply shocks:
   - 2005 (Hurricanes Katrina and Rita), 2008, Mar–Apr 2022 (AAA went from about $4.10 on Mar 1 to about $5.13 by late April), and Mar 2026 (+$1.42, or 38%, in a month, per AAA via ABC on Mar 19, 2026).
   - Unconditionally, I'd put this at about 3–5% of 45-day windows.
   - Late-year windows (mid-Nov to Dec 31) almost never show it. Diesel usually drifts sideways or down into late December. In 2022, for example, AAA diesel fell from about $5.30 in mid-November to about $4.60 at year-end.
2. **The 2026 war period alone** (Feb 28 to now), where volatility is far higher:
   - Large rises have happened twice: the March surge (from about $3.76 before the war to $5.45 by Mar 31), and the re-closure in July–September, which climbed to the record $6.53 by Sept 22.
   - Roughly 2 of about 6 non-overlapping 6-week windows since March contained a rise of 12% or more. That is about 30%, but it is a tiny, autocorrelated sample.
   - Both rises started from a calmer state *and* followed an escalation (the war starting; the June MOU collapsing on Jul 8–14).
3. **Setting a new all-time high within about 6 weeks while prices are falling.** Retail diesel is now about 8% below its record and dropping (down about 16¢ week over week). In past cycles (2008, 2022), once retail diesel rolled over from a peak, it rarely made a new high within 2 months unless a fresh shock hit. In 2022, the May/June peak of $5.816 was not exceeded afterwards.

## 3. Current state of the world (most recent first)
- **Nov 16, 2026:** Brent was about $95.4 in early Asian trade, down $0.47 (financefeeds/Reuters).
  - The hormuz.now tracker lists the Strait as "Restricted": about 6.4 transits a day over the past week versus 84.8 before the war, or about 8% of normal. Ships move under US naval coordination, and Iran demands transit permits.
  - Another report says Hormuz shipments are "close to pre-war levels," which contradicts the tracker. I could not resolve this.
- **Nov 14–15:** Iran said 3–4 tankers hit mines in the Strait; the US military disputes this. The Houthis claimed strikes on Saudi oil sites. Trump said the US "doesn't need a deal" with Iran (New Arab; CBS live updates).
  - Iran's terms for reopening the Strait: sanctions relief, an end to the US blockade of Iranian ports, and compensation. A separate report says an "$8 billion Hormuz deal" is heading to Trump (oilprice.com, mid-Nov).
- **Nov 14:** AAA diesel was **$6.0366**, against $3.769 a year earlier. AAA regular gasoline was $3.979, below $4 for the first time since July. GasBuddy diesel was $5.998 (EconoTimes).
- **Nov 13:**
  - Brent settled at $95.84 and WTI at $88.56, each down about 2.5% for the week, the second straight weekly loss.
  - NYMEX ULSD futures closed at about **$4.259/gal**. The diesel crack was about $83/bbl, down from more than $100 on Sept 1. The one-year range for the crack is $26–115 (worldoilmonitor).
  - The IRGC said a gas carrier hit a mine in the eastern Strait.
  - A trucking outlet put AAA diesel at $6.09, down 16¢ week over week.
- **Nov 12 (EIA weekly data, week ending Nov 6):** distillate stocks rose 4.1M bbl to 103.3M bbl. Analysts had expected a 1M bbl draw. Stocks are about 8% below the 5-year average. Four-week distillate demand was 4.2M b/d, up 3.9% y/y.
- **Nov 10:** EIA weekly diesel was $6.127, down 17¢ (FleetOwner).
  - EIA's November Short-Term Energy Outlook (STEO), with inputs frozen Nov 5, forecasts **Q4 2026 retail diesel at about $6.05** and Brent near $100 through year-end. It raised its 2027 diesel forecast to $5.03 because refined-fuel markets stay tight. The IEA sees a crude surplus in Q4.
- **Nov 9:** AAA diesel was $6.1723. **Nov 2:** EIA weekly diesel was $6.292.
- **Oct 26:** the IRGC declared Hormuz closed again.
- **Sept 22:** AAA diesel hit its record of **$6.5276**, with Brent at about $103–106 and the Gulf Coast crack above $100/bbl on Sept 1. Other drivers: a Russian diesel-export ban and Ukrainian strikes on Russian refineries (American Action Forum; ABC7; Upside).
- **Background:** the US/Israel–Iran war began Feb 28, 2026. Other milestones:
  - a ceasefire on Apr 8;
  - a US blockade from Apr 13;
  - the Islamabad MOU on Jun 17, under which the Strait reopened only nominally;
  - collapse of the MOU and re-closure on Jul 8–14.

  Brent peaked at about $118 in late March. AAA diesel was $3.76 before the war.

**Scheduled events before Dec 31:**
- EIA weekly petroleum status reports (Wednesdays) and on-highway diesel prices (Mondays: Nov 23, Nov 30, Dec 7, 14, 21, 28).
- The EIA STEO on about Dec 8–9.
- An OPEC+ meeting, typically around late November or early December.
- Onset of Northeast heating-oil season.
- US–Iran negotiations, which have no fixed date.

**Rough price arithmetic** (my calculation, not sourced):
- Today's retail-minus-ULSD-futures spread is about $6.04 − $4.26 = **$1.78**. That is wide; the normal level, including about $0.55–0.60 of taxes, is about $1.20–1.50. Retail is still lagging the drop in wholesale prices, which argues for **further retail declines** if futures stay flat.
- For AAA to exceed $6.80 by Dec 31, ULSD futures would probably need to hold at about **$5.10–5.50/gal** through mid-to-late December. That is a rise of about 20–30%. At today's crack, it implies Brent around $120–135. Alternatively, Brent could sit around $110 with the crack back above $100.

## 4. Drivers and scenarios
**Paths to YES (all need a new shock soon, by about mid-December, because retail lags wholesale by 1–3 weeks):**
- **Major escalation:**
  - verified mine or missile damage that halts the remaining Hormuz traffic;
  - large Houthi or Iranian strikes on Saudi or UAE export or refining assets (such as Abqaiq or Ras Tanura);
  - US strikes that widen the war.

  This would need Brent to move into the $115–130+ range and stay there.
- **A diesel-specific squeeze on top of escalation:**
  - a cold December in the Northeast or Europe;
  - more Ukrainian strikes on Russian refineries, or a longer Russian export ban;
  - unplanned outages at US Gulf refineries.

  These could push the crack back above $100.
- Both would probably be needed together. The September record took Brent at about $103–106 *plus* a crack above $100 to reach $6.53.

**Paths to NO:**
- **Status quo or slow easing (the most likely path):** Brent stays at $90–100, the crack stays at $80–90, and retail keeps sliding toward $5.70–6.00 as the wide retail margin compresses. EIA's Q4 average of $6.05 is consistent with this.
- **De-escalation:** an Iran deal or Hormuz reopening (talks are reportedly active) drives Brent and the crack sharply lower, toward diesel in the $5s.
- **Global demand weakness** and the IEA's projected crude surplus.

## 5. Signposts
**Toward YES (strongly):**
- Brent closing above $110, or ULSD futures above $4.80–5.00/gal, at any point before about Dec 15.
- Independent confirmation of tanker mine strikes and insurers or US Navy convoy suspending Hormuz transits.
- Strikes on Gulf export or refining infrastructure.
- AAA diesel turning up week over week by more than 10¢.
- Distillate stocks falling below about 95M bbl.
- A major cold snap in the Northeast.

**Toward NO:**
- A signed US–Iran reopening deal.
- Hormuz transit counts rising toward 30 or more a day.
- Brent below $90.
- The crack below $70.
- AAA diesel below $5.90 by early December.
- The December STEO cutting its Q4 diesel forecast.

**Timing:** if AAA is still at or below about $6.20 on Dec 15, reaching above $6.80 by Dec 31 would need a March-2026-scale jump (about 96¢ in one EIA week). That has happened only once in this war.

## 6. Uncertainties
- **Hormuz traffic:** I could not reconcile the tracker's "8% of normal" with reports of shipments "close to pre-war levels."
- **The Iranian mine claims of Nov 14–15** are unverified.
- **The US–Iran deal** (the reported "$8B Hormuz deal") has unclear status and timing.
- **Exact records:** AAA's daily peak is cited as $6.5276 (Sept 22), but another outlet gives $6.52. Sources conflict on EIA's weekly peak ($6.285 vs. higher), and on whether the $5.85 "record" was set in April or Sept 4.
- **I could not see AAA directly** (fetch was blocked). There is no verified AAA figure after Nov 14, and no futures curve for HO January 2027 contracts (which would show expected wholesale prices around Dec 31).
- **Base rates for 6-week diesel moves** are estimated from memory of historical series, not computed from data.

## Sources
- [U.S. diesel and gas prices decline, but trucking fuel costs remain elevated year over year (FleetOwner)](https://www.fleetowner.com/emissions-efficiency/news/55416288/us-diesel-and-gas-prices-decline-but-trucking-fuel-costs-remain-elevated-year-over-year)
- [Diesel prices retreat across all U.S. regions as gasoline slips below $4 (FleetOwner)](https://www.fleetowner.com/emissions-efficiency/news/55417900/us-diesel-prices-fall-nationwide-as-trucking-fuel-costs-remain-37-higher-year-over-year)
- [U.S. Diesel Reading Falls Below $6, While AAA Average Stays Higher (EconoTimes)](https://econotimes.com/U-S-Diesel-Reading-Falls-Below-6-While-AAA-Average-Stays-Higher-1777170)
- [Gas Prices Jump 28% in a Year; Diesel Soars 64% (LendingTree)](https://www.lendingtree.com/credit-cards/study/us-gas-prices/)
- [Diesel Prices Today (gas-price-today.com)](https://gas-price-today.com/diesel/)
- [Diesel Prices by State Today (OilPriceAPI)](https://www.oilpriceapi.com/diesel-prices)
- [Why Diesel Prices Hit A Record $6.53 Per Gallon (Upside)](https://www.upside.com/business/retailer-blog/fuel-trends-september-2026)
- [Diesel prices at record highs amid Strait of Hormuz disruption (ABC7)](https://abc7ny.com/story/diesel-prices-record-highs-amid-strait-hormuz-disruption-russia-ukraine-war/19846378/)
- [U.S. Diesel Prices Hit Record High: Factors and Implications (AAF)](https://www.americanactionforum.org/insight/u-s-diesel-prices-hit-record-high-factors-and-implications/)
- [Diesel drops 15¢ nationally to $6.38 as crude hovers above $106 (FleetOwner)](https://www.fleetowner.com/emissions-efficiency/news/55408459/us-diesel-prices-fall-to-638-but-iran-oil-volatility-rages-on)
- [EIA Raises Its 2027 Diesel Forecast to $5.03 a Gallon (Gain Consulting)](https://www.gain.consulting/post/eia-raises-its-2027-diesel-forecast-to-5-03-a-gallon)
- [November 2026 Short-Term Energy Outlook (EIA)](https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf)
- [Oil Swings Back to Surplus, Diesel Doesn't (Energy News Beat)](https://energynewsbeat.co/crude-oil/oil-swings-back-to-surplus-diesel-doesnt/)
- [Brent Crude Oil Price: $95.84 Sunday Before the Futures Open (FinanceFeeds)](https://financefeeds.com/brent-crude-oil-price-95-84-sunday-futures-open-week-ahead-iran-mine-claims-bull-98-bear-91/)
- [Oil Sinks to $94 as Iran's $8 Billion Hormuz Deal Heads to Trump (OilPrice.com)](https://oilprice.com/Latest-Energy-News/World-News/Oil-Sinks-to-94-as-Irans-8-Billion-Hormuz-Deal-Heads-to-Trump.html)
- [Crude Oil Price Slips as IEA Flags Surplus, Hormuz Attacks (Pomegra)](https://pomegra.io/news/crude-oil-price-slips-as-iea-flags-surplus-hormuz-attacks)
- [Trump says no need for Iran deal as four tankers hit in Hormuz (New Arab)](https://www.newarab.com/news/trump-says-no-need-iran-deal-four-tankers-hit-hormuz)
- [Trump says "we don't need a deal with Iran" (CBS News live updates)](https://www.cbsnews.com/live-updates/iran-war-us-nuclear-strait-of-hormuz/)
- [Strait of Hormuz FAQ (hormuz.now)](https://hormuz.now/faq)
- [Strait of Hormuz Timeline (hormuz.now)](https://hormuz.now/timeline)
- [Crisis Timeline: The Strait of Hormuz War 2026](https://hormuzstraitmonitor.com/crisis-timeline/)
- [IRGC Says Gas Carrier Hit Mine in Eastern Strait of Hormuz](https://houseofsaud.com/irgc-gas-carrier-mine-explosion-hormuz-nov13/)
- [2026 Iran war fuel crisis (Wikipedia)](https://en.wikipedia.org/wiki/2026_Iran_war_fuel_crisis)
- [US crude stocks, gasoline and distillate inventories rise (BOE Report, Nov 12, 2026)](https://boereport.com/2026/11/12/us-crude-stocks-gasoline-and-distillate-inventories-rise-eia-3/)
- [Diesel Market Dashboard: Futures, Crack Spread, Stocks (World Oil Monitor)](https://worldoilmonitor.com/diesel-market)
- [Heating oil price (Trading Economics)](https://tradingeconomics.com/commodity/heating-oil)
- [Diesel prices skyrocket: U.S. average jumps nearly $1 (FleetOwner)](https://www.fleetowner.com/emissions-efficiency/news/55362945/iran-impact-us-diesel-prices-jump-96-cents-gas-up-49-cents)
- [Soaring diesel costs amid war with Iran (ABC News, Mar 19, 2026)](https://www.goodmorningamerica.com/amp/news/story/soaring-diesel-costs-amid-war-iran-meat-vegetable-131143752)
- [US gas prices highest level since 2023 (Fortune, Mar 18, 2026)](https://fortune.com/2026/03/18/us-gas-prices-highest-level-since-2023-iran-war-diesel-aaa/)