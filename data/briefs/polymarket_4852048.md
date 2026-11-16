# Research brief: lowest gage height at St. Louis (USGS 07010000), Sept 21 – Nov 30, 2026, in the -1.00 to 0.99 ft bin

**Data caveat:** Every WebFetch call failed (the proxy refused the connection), including the USGS Daily Values URL named in the rules. I could not read the resolution table. The figures below come from search-result snippets. Some of them conflict, and the snippets do not show the full Sept 21 – Nov 15 record. A forecaster should check the USGS DV table directly before trading.

## 1. Resolution mechanics
- **What decides it:** the minimum of the USGS daily values (parameter 00065, gage height; statistic code 30800) for site 07010000, the Mississippi River at St. Louis. The window runs from market creation to Nov 30, 2026. The query URL in the rules starts at **2026-09-21**, so the late-September through mid-November record already counts.
- **YES condition:** that minimum is ≥ -1.00 and ≤ 0.99 ft, using published values with no rounding. Exactly -1.00 counts as YES for this bin. 0.99 is in this bin and 1.00 is in the next one up.
- **What makes this hard to reach:** the lowest value already recorded cannot be undone. For YES, the window minimum has to land between -1.00 and 0.99. If a reading already below 0.99 exists, it must not be below -1.00. If none exists yet, as the evidence suggests, the river has to fall into the bin between now and Nov 30 without going below -1.00.
- **Edge cases:**
  - Provisional ("P") values count as published at resolution.
  - The market can stay open up to 2 days after Nov 30 for unpublished data, or 3 days for clerical-error corrections.
  - If the source is unavailable, it can be extended to Dec 15. If there is still no data then, it resolves to "Below -3.00 ft".
  - I could not confirm what statistic code 30800 means. It may be a daily mean or a daily minimum. A daily minimum would sit slightly below a daily mean. That matters only near the 0.99 boundary.

## 2. Reference classes and base rates
- **Fall low-water years at St. Louis:**
  - 2022 through 2025 each brought fall low water, with draft and tow restrictions.
  - In fall 2025 the Corps listed St. Louis at about 1.27 ft (Farm Bureau, ~Sept 2025).
  - The record low is -6.2 ft (Jan 1940) per media. The USACE table gives -5.2 ft (1989). The NWS page shows -4.49 ft, which may be an early-2026 value; this is unverified.
  - My rough estimate: in about half of recent autumns (2022–2025), the Sept–Nov minimum fell below 1 ft. This is not computed from data.
  - That reference class mostly does not fit 2026. USACE says October 2026 stages were "notably higher than the low-water comparison years" (USACE State of the River, Nov 2026).
- **Recession from a rise:** the stage reportedly rose to about 10–13 ft by Nov 13. To reach ≤0.99 ft by Nov 30, it would need to fall about 9.5–12 ft in roughly 15 days, or 0.6–0.8 ft/day sustained. That is at the fast end of normal St. Louis recessions, and it would have to start right away. USACE says Upper Mississippi stages are **rising** to a mid-to-late-November peak, which argues against it. My judgment is that a fall this large in the last two weeks of November, with no prior low below 1 ft that season, has happened rarely. I have no exact count.
- **Historical November minimums:** the NWS LSX "Monthly Minimum River Stages" page exists but I could not fetch it. Its September record example is -0.2 ft (Sept 7, 1991).

## 3. Current state of the world (most recent first)
- **Nov 13, 2026:** The NWS St. Louis gauge page (EADM7) shows about 10.4–10.6 ft. One snippet gives 390.16 ft NAVD88 minus the 379.58 ft datum, which is about 10.6 ft. A 13.0 ft figure also appears, unlabelled. There are no warnings. Flood stage is 30 ft (NWS EADM7 page, Nov 13, 2026). This is ambiguous but consistent with a rise.
- **Nov 2026:** The USACE State of the River says Upper Mississippi stages are rising and forecast to peak mid-to-late November. It also says the Corps is preparing for a shortened Missouri River navigation season and low-water operations from mid-November. Lower Gavins Point releases would reach St. Louis after about 10 days and push stages down. It lists St. Louis at 3.69 ft on Nov 3, and also mentions 4.7 ft at an unclear date (USACE MVD State of the River, Nov 2026).
- **Nov 5, 2026:** Snoflo reports about 5.20 ft and 142,000 cfs, 103% of normal flow (Snoflo, Nov 5, 2026).
- **Nov 3, 2026:** Severe storms and heavy rain hit the Mississippi Valley, including Missouri and Iowa (weather.com, Nov 3, 2026). USGS instantaneous reading: 3.88 ft and 130,000 cfs (USGS current conditions, Nov 3, 2026).
- **About Nov 1, 2026:** One search snippet says the USGS reading was about 2.8 ft. **This is probably the window minimum so far**, but I could not confirm it.
- **Nov 2, 2026:** The Coast Guard issued MSIB 17-2026 on low-water operations for the Lower Mississippi (IRPT).
- **Oct 22, 2026:** DTN said St. Louis was at its "lowest point thus far this fall" and was forecast to reach the low-water threshold in early November unless significant rain fell. Around Oct 21–22 the stage was about 8.0 ft (USACE/Rivergages). If both are right, the fall minimum through Oct 22 was about 8 ft or higher.
- **Early October 2026:** USACE describes a "significant peak", followed by declines through October.
- **IFCA item:** it reports -1.16 ft on "Nov 7" with a forecast of -2.4 ft by Nov 20. It has no year and conflicts with 2026 readings, so it is probably from 2023. Do not use it.
- **St. Louis low-water threshold:** about -3.0 to -3.2 ft per a hard-to-parse Corps table; unconfirmed.

## 4. Drivers and scenarios
- **NO, most likely:**
  - The window minimum stays around 2.5–3.7 ft, set around Nov 1–3, which falls in the 1.00–2.99 bin.
  - The mid-November rise and the Upper Mississippi crest late in the month keep stages well above 1 ft through Nov 30.
- **YES, unlikely:**
  - (a) The early-November trough was actually ≤0.99 ft. This depends on the snippet figures being wrong.
  - (b) The Upper Mississippi crest is small or early, then a fast recession, a dry late November, and Missouri River release cuts together drive St. Louis below 1 ft by Nov 30, without going below -1.00.
- **NO, other bins:** a crash below -1.00 would need a recession even faster than (b), which is extremely unlikely in this window.

## 5. Signposts
- **The USGS DV table itself:** if any value from Sept 21 to Nov 15 is ≤0.99, the probability moves sharply. If none is below about 2.5 ft, it stays low.
- **NWS/NCRFC St. Louis forecasts:** daily forecasts and the 28-day extended outlook. A forecast below about 3 ft by late November would raise YES. Forecasts holding at 8 ft or more would all but close it.
- **Missouri River:** the Gavins Point release-cut schedule and Missouri River flows at Hermann.
- **Upstream:** the size and timing of the Upper Mississippi crest at Grafton and Alton.
- **Weather:** precipitation over the Midwest for Nov 15–30.

## 6. Uncertainties
- I could not read the USGS daily-value record. The exact window minimum and its date are unconfirmed (about 2.8 ft around Nov 1 is my best estimate).
- The mid-November stage could be 10.4, 10.6 or 13 ft; the snippets are ambiguous.
- I do not know what statistic 30800 measures.
- I could not see the current NWS forecast trajectory after Nov 13.
- The St. Louis low-water threshold is unconfirmed.

## Sources
- [Mississippi River at St. Louis – NWS/NWPS](https://water.noaa.gov/gauges/eadm7)
- [USGS Current Conditions 07010000](https://waterdata.usgs.gov/nwis/uv?site_no=07010000&legacy=1)
- [USGS 7-day gage height 07010000](https://waterdata.usgs.gov/mo/nwis/uv?cb_00065=on&format=html&period=7&site_no=07010000)
- [Water Levels on Lower Mississippi River Starting to Run Low Again – DTN, Oct 22, 2026](https://www.dtnpf.com/agriculture/web/ag/blogs/ag-weather-forum/blog-post/2026/10/22/water-levels-lower-mississippi-river)
- [State of the River – USACE MVD](https://www.mvk-wc.usace.army.mil/mvd/stateoftheriver.pdf)
- [Event Summary – Mississippi River Low Water, Sept 3, 2026 – USACE](https://www.mvk-wc.usace.army.mil/mvd/lowwaterupdate.pdf)
- [Mississippi River @ St Louis – USACE Water Data](https://water.usace.army.mil/overview/mvs/locations/st%20louis)
- [Rivergages – St. Louis station info](https://rivergages.mvr.usace.army.mil/WaterControl/stationinfo2.cfm?dt=S&sid=CE40010E&fid=EADM7)
- [Snoflo – Mississippi River flow](https://snoflo.org/river-levels/mississippi-river)
- [Severe storms and heavy rain for the Mississippi River Valley – weather.com, Nov 3, 2026](https://weather.com/2026/11/03/storms/severe/video/severe-storms-texas-louisiana-arkansas-missouri-iowa-memphis)
- [MSIB 17-2026 – LMR for Nov 2 – IRPT](https://www.irpt.net/msib-17-2026-lmr-for-nov-2/)
- [IFCA – Mississippi River Water Levels Remain Low (undated)](https://www.ifca.com/resource_display/?id=7193&title=Mississippi+River+Water+Levels+Remain+Low%2C+But+So+Do+Barge+Rates)
- [Low Mississippi River Levels Again Jeopardize Farm Income – AFBF](https://www.fb.org/intel/markets/low-mississippi-river-levels-again-jeopardize-farm-income)
- [American Currents – ACBL](https://bargeacbl.com/american-currents/)
- [Monthly Minimum River Stages for St. Louis – NWS LSX](https://www.weather.gov/lsx/stl_river_mins)