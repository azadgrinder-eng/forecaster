# Research brief: Will Carbon Arc's Amusement Parks & Attractions Ad Spend index for November 2026 be above 137?

## 1. Resolution mechanics

- **What counts as YES:** Carbon Arc's finalized "Amusement Parks & Tourist Attractions" ad spend index for November 2026 must be **strictly above 137**. That means ad spend at least about 37% higher than in November 2025. The index is year-over-year: 100 means spend equal to the same month last year. A value of exactly 137.00 resolves NO. (Kalshi event KXAMUSEMENTADS-26DEC06 metadata, retrieved 2026-11-19)
- **Who decides:** Kalshi lists the market in series KXAMUSEMENTADS. It also appears on Public.com, which uses Kalshi contracts. The settlement source is Carbon Arc's "Prisms" product for the entity "Amusement Parks & Tourist Attractions". The contract terms are in Kalshi's CARBONARC rulebook PDF, which I could not open. (Kalshi series API, retrieved 2026-11-19)
- **Timing:** The rules say the value is taken from finalized Carbon Arc data at 11:59 p.m. ET on the 5th calendar day after month-end, so 11:59 p.m. ET on December 5, 2026. Trading closes 2026-12-06 04:59 UTC. Expected expiration is 2026-12-13 06:30 UTC. The market "will close and expire early if the economic data is released."
- **Edge cases and ambiguities:**
  - **Release dates slip.** The October 2026 market closed 2026-11-09 04:59 UTC, which is November 8 at 11:59 p.m. ET, not November 5. The November market could also settle later than its nominal date.
  - **"Finalized" is not defined** in what I could see. I could not confirm whether Carbon Arc revises figures or how its panel or methodology handles revisions.
  - **The category definition is unclear.** I don't know which brands are in it (Disney parks, Universal, Six Flags, SeaWorld/United Parks, Merlin, zoos, aquariums?) or which channels are measured (digital only, or also TV). This matters a lot, because a few big advertisers can swing a year-over-year ratio.
  - **Strike ladder.** The November event has 11 strikes: 38, 87.5, 92, 137, 186.5, 216, 247, 280.5, 320.5, 371.5, 506. For comparison, the October event had 105, 120, 155, 195, 280, and the September event ran 103–151 in steps of 2. The very wide range suggests whoever lists the market expects big swings. That is a fact about how the contract was set up, not a price.

## 2. Reference classes and base rates

**A. This index's own history.** Only two settled months exist, both from the Kalshi settled-markets API:
- September 2026: **187.44** (event KXAMUSEMENTADS-26OCT06)
- October 2026: **124.14** (event KXAMUSEMENTADS-26NOV06)

So the index has been above 137 in 1 of 2 months. The most recent value, 124.14, is about 9.4% below 137. The two months differ by 63 points, a change of −0.41 in log terms.

A rough random-walk check from the October level:
- Monthly log standard deviation of about 0.3: P(>137) ≈ 35–40%. This uses ln(137/124.14) ≈ 0.099, so z ≈ 0.33.
- Standard deviation of about 0.15: P(>137) ≈ 25%.
- If you instead assume reversion toward the two-month average of about 156: above 50%.

Two points are far too few to pin down volatility or how persistent the index is.

**B. Other Carbon Arc ad spend indices on Kalshi, September → October 2026 settlements** (Kalshi API):

| Category | September | October | Change |
|---|---|---|---|
| Online Sportsbook | 127.45 | 137.59 | +10 |
| Fitness Centers | 119.37 | 110.25 | −9 |
| Casino | 71.34 | 67.49 | −4 |
| Film & TV Streaming | 84.08 | 97.92 | +14 |
| Amusement Parks | 187.44 | 124.14 | −63 |

- For the other categories, month-to-month moves were about ±4 to ±14 points, and their levels ranged from 67 to 138.
- Amusement parks is clearly the most volatile series, probably because a few large advertisers and seasonal campaigns dominate it.
- Only 1 of the 8 category-months for those four peers was above 137 (Sportsbook, October, at 137.59).

**C. Broad ad market growth.** The IAB 2026 Outlook forecasts US ad spend up 9.5% in 2026, which would mean an index around 110 for an average category. Winterberry projects US advertising, marketing and data spend up 9.4%. A reading above 137 needs category growth roughly four times the market's, which only happens with large campaign or base effects. Amusement parks managed that in September 2026 but not October.

## 3. Current state of the world (most recent first)

- **Nov 16, 2026:** Theme park Black Friday sales are already running:
  - LEGOLAND Florida: $49 day ticket
  - SeaWorld Orlando: from $61.99
  - Six Flags: 2027 Silver Pass for the price of one day ticket ($69 at Six Flags Over Texas and Carowinds)
  - Universal Studios Hollywood: $50 off the Platinum annual pass

  (Haunted Attraction Network roundup, as summarized in search results, Nov 16, 2026). Universal Orlando's Black Friday promotions lean toward multi-day tickets that include Epic Universe (Oct 2026 article). This is normal November promotion and in itself does not show spending up year-over-year.
- **Nov 13, 2026:** The November 2026 market's strikes were finalized. Markets opened between Nov 3 and Nov 13 (Kalshi API).
- **Nov 8–9, 2026:** The October index settled at 124.14, down from 187.44 in September (Kalshi API).
- **Early Nov 2026 – Six Flags Q3 2026 results and call:**
  - Same-park SG&A fell $41.1M, mainly from lower full-time wages and **reduced advertising costs** (Benzinga/press release, Nov 2026).
  - Management said it sees "an opportunity to lean in… including with paid marketing support" and highlighted CMO-led customer acquisition (StatementDog transcript; Attractions Magazine).
  - The 2027 season pass launch was **deliberately delayed**. If pass advertising moved later in the year than in 2025, November 2026 could get a year-over-year boost; this is my inference.
  - In Q3 2025, Six Flags had already cut advertising by about $26M after moving spend earlier in the year (Barchart/Quantisnow, Nov 2025). That makes its late-2025 base relatively low.
- **Early Nov 2026 – United Parks (SeaWorld/Busch Gardens) Q3 2026:**
  - SG&A rose 13.1% to $68.6M.
  - Attendance fell 4.7%; revenue fell 1.1% to $506.5M.
  - Management called its marketing execution "frustrating" (247WallSt, TipRanks, StatementDog, Nov 2026).
  - Weak attendance could push it to spend more on promotions, or to cut costs. The direction is unclear.
- **2026 background:** Universal's Epic Universe opened in May 2025, so the big launch-year spending is in the 2025 base for spring and summer, less so for November. I could not confirm any major new park launches with heavy November 2026 campaigns.

**Scheduled before close:** Black Friday (Nov 27) and Cyber Monday (Nov 30) pass and ticket sales, which are the peak promotional window. The data should be released and the market settled around Dec 5–8.

## 4. Drivers and scenarios

**Paths to YES (above 137):**
- **Low November 2025 base.** Six Flags in particular was cutting advertising in the second half of 2025. A weak base plus normal 2026 spending could inflate the ratio.
- **Six Flags "leans in"** on paid marketing alongside its delayed 2027 pass launch, concentrating spend in the Black Friday window.
- **Whatever drove September's 187 comes back.** It might have been a large advertiser's campaign, a base effect, or a change in the data panel.
- **A noisy, concentrated category.** The October-to-September swing of more than 60 points shows the index can easily jump 15+ points in a month.

**Paths to NO (137 or below):**
- **October's 124 reflects the real trend.** September looks like a one-off spike, and November continues at roughly 105–130.
- **Cost cutting.** Six Flags reported lower advertising costs in Q3 2026, and United Parks faces margin pressure.
- **The broad market only supports about 10% growth.** A reading above 137 needs an unusual base or campaign effect.
- **November 2025 was itself a strong promotional month** (pass sales, holiday events), which would make the base hard to beat.

## 5. Signposts

- **Carbon Arc's own data** (the settlement Prism page) showing partial-month or weekly November values. This is the most decisive input; I could not access it.
- **The finalized October figure being revised** after settlement. That would indicate how much the data moves.
- **Evidence of heavy Black Friday or holiday TV, CTV and social campaigns** from Disney, Universal, Six Flags or United Parks in late November 2026 → pushes toward YES. Reports of trimmed marketing budgets → toward NO.
- **November 2025 context.** If Six Flags or others went quiet in Nov 2025 (CEO transition, cost cuts), that favors YES. If 2025 had heavy pass-launch spending, that favors NO.
- **Other Carbon Arc categories' November readings** when they settle. These could reveal panel-wide shifts.

## 6. Uncertainties

- I could not open Carbon Arc's methodology (data source, channel coverage, brand list, panel changes) or the Kalshi CARBONARC rulebook PDF. The proxy refused carbonarc.ai and assets.kalshi.com.
- There are only two historical data points. I don't know how volatile or persistent the index really is, or whether September's 187 was an outlier or a data artifact.
- I don't know the actual size of the November 2025 base or what happened in this category that month.
- I don't know whether Carbon Arc revises "finalized" values, or how much release dates slip. October's value was recorded about 3 days after the nominal date.
- I did not find company-level November 2026 ad budgets for Disney or Universal.

## Sources
- [Kalshi API – KXAMUSEMENTADS settled markets](https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXAMUSEMENTADS&status=settled&limit=200)
- [Kalshi API – KXAMUSEMENTADS series info](https://api.elections.kalshi.com/trade-api/v2/series/KXAMUSEMENTADS)
- [Kalshi API – Event KXAMUSEMENTADS-26DEC06 (rules/strikes)](https://api.elections.kalshi.com/trade-api/v2/events/KXAMUSEMENTADS-26DEC06)
- [Kalshi API – Series search (Carbon Arc ad spend series list)](https://api.elections.kalshi.com/v1/search/series?query=amusement%20parks%20ad%20spend)
- [Kalshi API – KXCASINOADS settled](https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXCASINOADS&status=settled&limit=200)
- [Kalshi API – KXSPORTSBOOKADS settled](https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXSPORTSBOOKADS&status=settled&limit=200)
- [Kalshi API – KXFITNESSADS settled](https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFITNESSADS&status=settled&limit=200)
- [Kalshi API – KXSTREAMINGADS settled](https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXSTREAMINGADS&status=settled&limit=200)
- [Public.com – Amusement Parks & Attractions Ad Spend in November 2026 (rules summary only)](https://public.com/prediction-markets/amusement-parks-attractions-ad-spend-in-november-2026-nuukpwp)
- [Markets Media – Kalshi Launches Sector KPI Contracts With Carbon Arc](https://www.marketsmedia.com/kalshi-launches-sector-kpi-contracts-with-carbon-arc/)
- [Six Flags Entertainment Corporation Reports 2026 Third Quarter Results (Benzinga)](https://www.benzinga.com/node/62907042)
- [Six Flags Q3 2026 earnings call transcript (StatementDog)](https://statementdog.com/analysis/FUN/earnings_calls/320679)
- [Attractions Magazine – Six Flags doubles down on turnaround strategy (Oct/Nov 2026)](https://attractionsmagazine.com/six-flags-earnings-turnaround-strategy-october-2026/)
- [Six Flags 2025 Q3 results (Barchart)](https://www.barchart.com/story/news/35980653/six-flags-entertainment-corporation-reports-2025-third-quarter-results-and-provides-october-update)
- [United Parks & Resorts Q3 2026 (247WallSt)](https://247wallst.com/cards/united-parks-resorts-q3-2026-earnings-prks-01m6nr0qz79ex9sgc6ngs4gsqb)
- [United Parks Q3 2026 earnings call (StatementDog)](https://statementdog.com/analysis/PRKS/earnings_calls/320858)
- [United Parks earnings call highlights (TipRanks)](https://www.tipranks.com/news/company-announcements/united-parks-resorts-inc-earnings-call-highlights-mixed-results)
- [Theme park Black Friday deals (Haunted Attraction Network)](https://hauntedattractionnetwork.com/theme-park-black-friday-deals/)
- [2026 Black Friday deals across theme parks and attractions (Attractions Magazine)](https://attractionsmagazine.com/2026-black-friday-deals-across-theme-parks-and-attractions/)
- [IAB – Outlook study forecasts 9.5% growth in U.S. ad spend](https://www.iab.com/news/outlook-study-forecasts-9-5-growth-in-u-s-ad-spend/)
- [TV Technology – IAB: U.S. Ad Spend to Spike by 9.5% in 2026](https://www.tvtechnology.com/business/iab-u-s-ad-spent-to-grow-9-5-percent-growth-in-2026-as-ai-powers-marketing-efforts-and-linear-tv-declines)