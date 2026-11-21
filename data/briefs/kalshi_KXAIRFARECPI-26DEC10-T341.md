# Research brief: CPI-U Airline Fares (SA, CUSR0000SETG01) for November 2026 above 341?

## 1. Resolution mechanics
- **What counts:** The question resolves YES if FRED series CUSR0000SETG01 (CPI-U airline fares, U.S. city average, seasonally adjusted, 1982-84=100) prints **strictly above 341** for November 2026.
- **Release timing:** BLS is scheduled to publish November 2026 CPI on **Thursday, Dec 10, 2026 at 8:30 a.m. ET** (BLS CPI release schedule; FRED lists Dec 10 as the next release). The market closes at 13:29 UTC, which is 8:29 a.m. ET, one minute before the print. Resolution therefore depends on the Dec 10 release, read from FRED.
- **Distance to the threshold:** The latest value is **October 2026 = 328.318**, published Nov 10, 2026 (FRED/finzdata). Reaching 341 takes a **seasonally adjusted month-over-month gain of at least +3.87%** (341 / 328.318 = 1.0386). BLS normally revises seasonal factors only in February, so the October base should stay at 328.318 on Dec 10.
- **Year-over-year view:** November 2025 SA was **253.063** (FRED, current vintage). A print above 341 would mean roughly **+34.8% YoY**.
- **Shutdown risk:** The current stopgap funding runs out **Dec 11**, and agencies would close Dec 12 (Federal News Network, Nov 2026; NerdWallet). That is after the Dec 10 release, so a lapse should not delay the November print. A delayed release would only become an issue if the schedule changes unexpectedly. I found no BLS notice of any change.
- **Data-quality quirks:** October 2025 was never published because of the 2025 shutdown, and November 2025 collection was disrupted. This may make the November seasonal factors less reliable than usual.

## 2. Reference classes and base rates
1. **SA monthly airfare changes of at least +3.9% in any month.** My approximate count of 2023–2025 BLS monthly SA changes, from memory of the releases, is about **6 of ~35 months (~15–17%)**: Feb 2023 +6.4, Aug 2023 +4.9, Dec 2024 +4.7, Jul 2025 +4.0, Aug 2025 +5.9, Dec 2025 +5.2 as first published. Jan 2026 was about +6.5% on the current vintage (262.573 to 279.693). Over 2010–2019 such moves were much rarer, perhaps 3–5% of months. The Apr–May 2022 jumps of +10% to +18% happened during a jet-fuel spike, which is the closest analogue to 2026. These counts are approximate and I did not verify them against BLS tables.
2. **Big moves after a run of slowing gains.** The last three months were +2.7% (Aug), +1.2% (Sep), and +0.4% (Oct) (BLS Sep release; CNBC Nov 10, 2026). In 2022, once jet fuel peaked in June, CPI airfares fell sharply in Jul–Sep 2022 (−1.8%, −4.6%, −8.4% SA, approximate). Gains of 4% or more are uncommon right after momentum stalls and fuel turns lower.
3. **Booking-data YoY as a cross-check.** Hopper's Thanksgiving 2026 domestic round-trip average is **$402, +31% YoY**, and Christmas is **$452, +23%** (Hopper via FOX/KTVU, Oct–Nov 2026). Applying +31% to Nov 2025 SA (253.063) gives about **331.5**, below 341. Hopper's figures come from September searches of lower-priced tickets, so they are not the same thing as the CPI.

## 3. Current state of the world (most recent first)
- **Nov 18, 2026:** Oil fell more than 2% after larger-than-expected U.S. inventory builds. Ongoing U.S.–Iran attacks and Hormuz disruptions limited the decline (CNBC, Nov 18, 2026).
- **Nov 17, 2026:** U.S. Gulf Coast jet fuel spot was about **$3.76/gal** (EIA via Flycraft), down from about $4.84–4.90 in October (EUROCONTROL, Argus). Trading Economics shows a November figure of about $4.04, possibly a monthly average. Either way, fuel is roughly **15–25% below the October peak**.
- **Nov 12, 2026:** EUROCONTROL reported European jet fuel averaging $4.84/gal in October, easing to $4.42 in the week to Nov 8.
- **Nov 10, 2026:** October CPI showed airline fares **+0.4% SA** (about +3.8% NSA), index 328.318. Headline CPI was +0.4%. No YoY figure was published because October 2025 is missing; U.S. Travel estimates about +26% (CNBC; U.S. Travel TPI). Brent fell about 6.7% to about $105.87 in early November on peace hopes (UPI, Nov 10; Mansfield Energy, Nov 6). Goldman raised its December Brent forecast to $105.
- **Oct 22–27, 2026:** Jet fuel was near a record and roughly double year-earlier levels. Airlines were cutting capacity, with about 3% of domestic seats cut for late Nov–Dec per Cirium as cited by secondary sources. Fares were about 23% higher with emptier planes (NPR Oct 23; Axios Oct 22; Fortune Oct 27). Executives signalled that fare increases would stick even if fuel eases (CNBC Oct 5).
- **Sep 2026 CPI:** Airfares rose +1.2% SA and +22.4% YoY, the 10th straight monthly increase. August was +2.7% SA.
- **Index path (SA, FRED):** Nov 2025 253.063; Dec 262.573; Jan 2026 279.693; Jun 307.963; Jul 314.803; Aug 323.244; Sep 326.991; Oct 328.318. I could not confirm the Feb–May values. In April, airfares were about +20.7% YoY.
- **Background:** The 2026 Iran war fuel shock began around March, with jet fuel at about $209/bbl in early April. Spirit Airlines shut down, which removed low-fare capacity. IATA expects fuel to be about 31% of airline costs in 2026, up from 25% in 2025.
- **Scheduled before close:** Thanksgiving falls on Nov 26. The November CPI is released Dec 10. The PPI (which includes airline passenger services) comes Dec 15, after the close.

## 4. Drivers and scenarios
**Paths to YES (Nov SA gain of at least +3.9%):**
- Delayed pass-through of October's record fuel prices into November fares, together with holiday capacity cuts.
- A seasonal-adjustment artifact. November 2025 was depressed by the shutdown and fell about 5% over two months, so the November seasonal factor may be low, which would inflate the SA reading.
- Large moves in this series are not unusual. A one-month jump of 4–6% happened in Dec 2025 and Jan 2026.

**Paths to NO:**
- Momentum has been fading for three months in a row (+2.7, +1.2, +0.4).
- Jet fuel fell about 15–25% from October to mid-November.
- High fares may be reducing demand ("emptier planes").
- The Hopper YoY cross-check implies about 330–335.
- Even if fares stay flat or rise 1–3%, the index ends up well below 341.

## 5. Signposts
- **Toward YES:**
  - Analyst CPI previews (Goldman, BofA, Citi, Barclays, Continuum) forecasting airfares up 3% or more in November.
  - Secondary-source fare trackers (Hopper, Kayak, ARC/Adobe) showing November domestic fares rising sharply from October.
  - Jet fuel spiking back above $4.50 in late November, for example on Hormuz escalation. This would matter more for December than November.
- **Toward NO:**
  - Previews calling for flat or negative airfares in November, or citing lower fuel.
  - Airline commentary on softer demand or fare sales.
  - A U.S.–Iran peace deal pushing crude down further.
  - Commentary that the PPI or import-price airfare components softened in October.

## 6. Uncertainties
- I could not read the BLS tables or the FRED text data directly because the proxy refused those fetches. All index levels come from search-result summaries of FRED and finzdata pages, so the exact 328.318 base should be checked.
- I could not confirm the monthly values for Feb–May 2026, and the 2023–2025 base-rate counts are approximate recollections.
- I don't know how BLS's secondary-source airfare data relates timing-wise to booking versus travel date, so the lag from fuel to CPI fares is uncertain. It is typically 1–3 months.
- The November seasonal factor's quality is uncertain after the 2025 shutdown disruptions.
- I found no 2026-specific economist forecast for November airfares. The current status of the U.S.–Iran conflict and talks in mid-November is unclear, apart from "ongoing attacks" with peace hopes.

## Sources
- [Consumer Price Index for All Urban Consumers: Airline Fares (CUSR0000SETG01) – FRED](https://fred.stlouisfed.org/series/CUSR0000SETG01)
- [CUSR0000SETG01: 328.318 (Oct 2026) – finzdata](https://data.finzdata.com/macro/cusr0000setg01)
- [CPI inflation report: October 2026 – CNBC](https://www.cnbc.com/2026/11/10/cpi-inflation-report-october-2026.html)
- [Consumer Price Index News Release – BLS](https://www.bls.gov/news.release/cpi.htm)
- [BLS CPI September 2026 release archive](https://www.bls.gov/news.release/archives/cpi_10142026.htm)
- [US airline fares September 2026 inflation – Airways](https://airwaysmag.com/new-post/us-airline-fares-september-2026-inflation)
- [BLS CPI release schedule](https://www.bls.gov/schedule/news_release/cpi.htm)
- [BLS December 2026 release schedule](https://www.bls.gov/schedule/2026/12_sched_list.htm)
- [Airline fares decreased 5.4 percent over the year, November 2025 – BLS TED](https://www.bls.gov/opub/ted/2025/airline-fares-decreased-5-4-percent-over-the-year-november-2025.htm)
- [Travel Price Index – U.S. Travel Association](https://www.ustravel.org/research/travel-price-index)
- [Jet fuel prices hit a record and holiday airfares soar higher – NPR, Oct 23, 2026](https://www.npr.org/2026/10/23/nx-s1-6009506/jet-fuel-price-holiday-airfare)
- [Airlines trading ~23% higher prices for emptier planes – Fortune, Oct 27, 2026](https://fortune.com/2026/10/27/airlines-nearly-23-prices-empty-jet-fuel-90-iran-war/)
- [Soaring jet fuel costs mean higher fares, fewer flights – Axios, Oct 22, 2026](https://www.axios.com/2026/10/22/airline-prices-fuel-costs)
- [Why airfares could rise even more – CNBC, Oct 5, 2026](https://www.cnbc.com/2026/10/05/airfare-prices-airline-profits.html)
- [High airfares may become new norm – PBS NewsHour](https://www.pbs.org/newshour/world/high-airfares-may-become-new-norm-as-jet-fuel-costs-soar-says-asia-pacific-airline-industry-chief)
- [2026 holiday travel: airfares highest in a decade – KTVU/FOX](https://www.ktvu.com/news/2026-holiday-travel-thanksgiving-christmas-airfares-reach-highest-prices-decade)
- [Jet Fuel Price Today – Flycraft](https://www.flycraft.com/jet-fuel-price)
- [Kerosene-Type Jet Fuel Prices: U.S. Gulf Coast – Trading Economics](https://tradingeconomics.com/united-states/kerosene-type-jet-fuel-prices-u-s-gulf-coast-dollar-per-gallon-fed-data.html)
- [Oil prices tumble as traders weigh surplus – CNBC, Nov 18, 2026](https://www.cnbc.com/2026/11/18/oil-prices-fall-as-higher-us-crude-stocks-temper-supply-risks.html)
- [Gas, oil prices fall amid hopes war ending – UPI, Nov 10, 2026](https://www.upi.com/Top_News/US/2026/11/10/gas-oil-prices-fall-amid-hopes-war-ending/9211794315954/)
- [Week in Review – Mansfield Energy, Nov 6, 2026](https://mansfield.energy/2026/11/06/week-in-review-oil-prices-retreat-on-iran-peace-hopes-and-weaker-global-demand/)
- [US Airfare Surges Over 21% In 4 Months – Simple Flying](https://simpleflying.com/us-airfare-surges-21-percent-4-months-worse/)
- [Another looming funding deadline – Federal News Network, Nov 2026](https://federalnewsnetwork.com/congress/2026/11/another-looming-funding-deadline-for-federal-agencies-what-happens-when-the-current-cr-expires/)
- [Lame-Duck Congress Faced With Averting Another Shutdown – NerdWallet](https://www.nerdwallet.com/finance/news/government-shutdown-news)
- [US Holiday Airfare 2026: Capacity Cuts – nomadlawyer (low quality)](https://www.nomadlawyer.org/us-holiday-airfare-2026-capacity-cuts-jet-fuel-inflation)