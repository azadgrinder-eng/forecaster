# Research brief: Will it snow (trace or more) at Detroit Metro Airport (KDTW) on Thursday, Nov 26, 2026?

*Prepared Nov 17, 2026, 9 days before the event. Direct page fetches were blocked in this environment, including weather.gov and cpc.ncep.noaa.gov. Everything below comes from search-result excerpts, and figures that need checking are marked.*

## 1. Resolution mechanics

- **What counts as YES:** the official new-snowfall total at Detroit Metro Airport (KDTW) for Nov 26, 2026 is above 0. A reported trace ("T") counts. In practice the source will be the NWS Detroit/Pontiac (DTX) daily climate report (CLI) or the monthly CF6 for DTW.
- **Reporting day:** the station's local day. NWS climate days run midnight to midnight local standard time, which in November is the same as EST clock time. Snow that falls late on Wednesday Nov 25 or after midnight into Friday Nov 27 does not count.
- **What does not count:** snow already on the ground or snow depth. Snow at other Detroit-area sites, such as Detroit City Airport or White Lake, also does not count.
- **Edge cases:**
  - A few flurries or a brief rain-to-snow changeover at the end of a cold front is usually logged as T. That makes YES easier than the phrase "snow on Thanksgiving" suggests.
  - Mixed precipitation such as sleet is normally recorded in the snowfall column. Freezing rain is not.
  - The preliminary CLI can be corrected later in the CF6 or final data. The rules don't say which version governs.
  - The market closes at 04:59 UTC on Nov 27, which is 23:59 EST on Nov 26, so it closes at the end of the climate day. Late-evening flakes would still count if reported.

## 2. Reference classes and base rates

1. **Detroit Thanksgivings, 1959 onward (NWS DTX count):** NWS Detroit reported "only 11 times since 1959" with snow on Thanksgiving, as of late 2024 (WWJ/Audacy, ~Nov 2024).
   - The definition seems to mix new snowfall and snow on the ground. NWS lists new snowfall with nothing on the ground in 2013, 2004, 1980, 1976 and 1969. It lists 1–3 inches on the ground in 2005, 1996, 1985, 1974 and 1971. 1975 had 4.6 inches, the record (NWS DTX Thanksgiving Climate, 1874–2025). 1959 appears as a trace.
   - The NWS table seems to show a trace to 0.1 inch of snowfall on Nov 27, 2025, with a high of 34°F and low of 28°F during lake-effect and wind-driven snow showers. The column headers were cut off, so I can't confirm this reading.
   - That gives roughly **11–12 of 66–67 Thanksgivings, or about 16–18%**. The true trace-inclusive rate may be a little higher if some trace days were left out of the NWS count, or a little lower if some years were counted only for snow on the ground.
   - Long-run average Thanksgiving snowfall is 0.2 inches (1874–2025). Average high/low is 42°F/29°F.
2. **Calendar date Nov 26 in Detroit:** a third-party site (weatheronthisday) says precipitation fell on 22% of recorded Nov 26ths and snow on 2%. The 2% figure is probably measurable snow only and probably from a patchy dataset, so it is not reliable for a trace-inclusive question. Its 22% precipitation figure does put a rough ceiling on how often any precipitation falls on one late-November day.
3. **Late-November seasonality:** the average first measurable (0.1 inch) snow at Detroit is about Nov 16, and the first 1-inch snowfall is about Nov 30 (Fox 2 Detroit, citing NWS). By Nov 26 the season is cold enough for flakes on most days with precipitation behind cold fronts, but rain is still common. My own rough estimate, not sourced: about 20–30% of late-November days at DTW record a trace or more. This fits reference class 1.

**Base rate to anchor on:** about 15–25% unconditionally.

## 3. Current state of the world (most recent first)

- **Nov 16, 2026 – CPC 6–10 day outlook updated, valid Nov 22–26.** I could not read the map's details for Michigan (CPC 6–10 Day page, Nov 16, 2026).
- **Nov 16, 2026 – Weather.com:** says it is too early for specifics on Thanksgiving week. It expects above-average temperatures across most of the country and above-average precipitation in the Southeast, West Coast, I-95/Northeast and Central Plains. The Great Lakes were not singled out for wet conditions (weather.com, Nov 16, 2026).
- **Nov 15, 2026 – CPC 6–10 day (Nov 21–25) and 8–14 day (Nov 23–29) discussion:**
  - The Michigan rows read "A / N" for both periods. That most likely means above-normal temperature and near-normal precipitation, but the column labels were cut off, so this needs checking.
  - A fragment mentions a precipitation probability below 33% for the Great Lakes, in an unknown category.
  - 8–14 day confidence was rated 3 out of 5 (CPC Prognostic Discussion, Nov 15, 2026).
- **Mid-November 2026 – Country Herald:** says the NOAA outlook for Nov 14–27 "continues to favor above normal temperatures across much of Michigan, including Detroit." It notes Detroit could reach about 71°F on a Tuesday before rain on Wednesday, probably the week of Nov 16–18; the exact date is uncertain. It says snowfall for Detroit is uncertain and no significant accumulation is indicated (Country Herald, Nov 2026).
- **Almanacs (forecast made months in advance, low value):**
  - Old Farmer's Almanac: chance of rain and snow in the Lower Lakes during Thanksgiving week, but relatively mild on Thanksgiving Day itself.
  - Farmers' Almanac: colder, with scattered snow showers or flurries in the Great Lakes.
- **Larger climate pattern:** a strong to very strong El Niño is under way. CPC put the odds of it lasting through Jan–Mar 2027 above 83%, and gave a meaningful chance it becomes the strongest since 1950 (CPC ENSO discussion, Oct 8, 2026). Strong El Niño autumns and winters usually favor a milder northern tier and a weaker supply of cold air into the Great Lakes. This is general climatology, not a confirmed forecast for this week.
- **Scheduled before close:**
  - Daily CPC 6–10 and 8–14 day updates.
  - NWS DTX forecast discussions, issued about four times a day. Day 7 comes into view around Nov 19, and better detail around Nov 22–24.
  - DTX's 7-day point forecast for DTW.
  - Final answer from the DTW CLI after midnight on Nov 27.

## 4. Drivers and scenarios

**Paths to YES:**
- **Cold front with lake-effect or wraparound flurries (most common route):** a front passes Wednesday into Thursday and northwest flow brings flurries or snow showers to DTW. That only needs 850 hPa temperatures around −8°C or colder and some moisture. Even a few flakes give a T. This is how 2025 and 2013 happened.
- **Synoptic low:** a low passing south of Detroit, along the Ohio Valley track, brings rain changing to snow or all snow.
- **Changeover at the tail of a rain event:** rain on Thanksgiving with a changeover before midnight.

**Paths to NO:**
- **Mild, dry pattern:** a ridge or zonal flow over the region, which fits the CPC lean toward above-normal temperatures and El Niño. Temperatures are in the 40s–50s and there is no precipitation, or only rain.
- **Bad timing:** a cold front passes Friday or later, or passes Tuesday and dries out by Thursday. A "cold Thanksgiving" without any precipitation also gives NO.

**What the outcome depends on:**
- Timing of the next trough relative to the Thursday calendar day.
- Whether air cold enough for snow (surface below about 36°F with a cold column above) reaches southeast Michigan.
- Whether NW-flow lake moisture reaches DTW, which is downwind of Lake Michigan only in a weak, distant way.

## 5. Signposts

- **Towards YES, strongly:** a DTX forecast discussion or point forecast from Nov 22 onward mentioning "flurries," "snow showers," or "rain/snow mix" for Thursday. CPC 6–10 day (issued about Nov 19–21) turning to near- or below-normal temperatures for the Great Lakes. Model agreement on a trough or cold front Wednesday night into Thursday.
- **Towards YES, moderately:** precipitation chance of 30% or more on Thursday with highs in the upper 30s or below.
- **Towards NO:** forecast Thanksgiving highs in the upper 40s or 50s. A surface high centred over the Great Lakes on Thursday. Front timing shifting to Friday or Saturday. CPC holding "above normal" temperatures for the Great Lakes through Nov 23–29.
- **Calibration note:** at 2–4 days out, a forecast of "slight chance of flurries" still converts to a reported T fairly often. At about 9 days out, the current lean only modestly adjusts the base rate.

## 6. Uncertainties

- I could not read the CPC maps or text directly. The "A/N" reading for Michigan and the meaning of "<33%" are unconfirmed.
- I could not see the current NWS DTX forecast discussion or point forecast for Nov 26.
- I lack an exact count of Thanksgivings with a trace or more since 1959. NWS's count of 11 mixes new snowfall and snow depth. The 2025 row (T or 0.1 inch) needs confirming.
- I don't know the exact date of the Country Herald "71°F Tuesday" item or how recent it is.
- I lack a clean daily frequency of trace-or-more snow for Nov 20–30 at DTW, for example from xmACIS. The forecaster should pull the 1991–2020 record for Nov 26 if possible.
- The effect of El Niño on a single late-November day is weak and noisy.

## Sources
- [Detroit Thanksgiving Climate Averages (1874-2025) – NWS DTX](https://www.weather.gov/dtx/thanksgivingclimate)
- [Thanksgiving Stats – NWS DTX](https://www.weather.gov/dtx/thanksgiving_stats)
- [We may see snow on Thanksgiving Day in Detroit — WWJ/Audacy (~Nov 2024)](https://www.audacy.com/wwjnewsradio/news/local/we-may-see-snow-on-thanksgiving-day-in-detroit-this-year)
- [Same article via NewsBreak](https://www.newsbreak.com/wwj-news-radio-560923/3686178745774-we-may-see-snow-on-thanksgiving-day-in-detroit-and-that-s-not-as-common-as-you-may-think)
- [Post-Thanksgiving Snow 2025 – NWS DTX](https://www.weather.gov/dtx/PostThanksgivingSnow2025)
- [CPC 6-10 and 8-14 Day Prognostic Discussion (Nov 15, 2026)](https://www.cpc.ncep.noaa.gov/products/predictions/610day/fxus06.html)
- [CPC 6 to 10 Day Outlook (updated Nov 16, 2026)](https://www.cpc.ncep.noaa.gov/products/predictions/610day/index.new.php)
- [Thanksgiving travel forecast 2026: early weather outlook – weather.com (Nov 16, 2026)](https://weather.com/2026/11/16/holiday/thanksgiving/thanksgiving-getaway-weekend-weather-outlook-west-central-us)
- [Michigan Weather: Detroit Thanksgiving Holiday Travel Rain or Snow Chances Nov. 14-27? – Country Herald](https://countryherald.com/michigan/detroit/michigan-weather-detroit-thanksgiving-holiday-travel-rain-or-snow-chances-nov-14-27)
- [Michigan Winter 2026-27: Detroit, Grand Rapids Snow by Thanksgiving? – Country Herald](https://countryherald.com/michigan/detroit/michigan-winter-2026-27-detroit-grand-rapids-snow-by-thanksgiving)
- [Thanksgiving Weather Forecast 2026 – Old Farmer's Almanac](https://www.almanac.com/november-weather-forecast)
- [Great Lakes, Ohio Valley & Midwest Thanksgiving Weather Forecast 2026 – Farmers' Almanac](https://www.farmersalmanac.com/?p=444098)
- [Weather on November 26 (Detroit) – weatheronthisday](https://weatheronthisday.com/48201/11/26)
- [When is the first average snowfall across the Midwest? – Fox 2 Detroit](https://www.fox2detroit.com/news/when-first-average-snowfall-midwest-detroit-minneapolis-milwaukee-chicago)
- [CPC ENSO Diagnostic Discussion](https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml)
- [WMO ENSO Update August 2026](https://wmo.int/sites/default/files/2026-08/Factsheet-ENSO-Update-August-2026-en.pdf)