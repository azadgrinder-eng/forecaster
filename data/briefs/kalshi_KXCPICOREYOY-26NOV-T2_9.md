# Research brief: Will US core CPI be above 2.9% for the 12 months ending November 2026?

**Note on sourcing:** Every page fetch failed ("proxy refused the connection"), including bls.gov, FRED, CNBC, EY, StoneX and Continuum. Everything below comes from search-result snippets. The key index levels in section 3 match each other, but I could not check them against the BLS tables directly. A forecaster should treat them as likely correct but unconfirmed.

## 1. Resolution mechanics

- **What counts as YES:** BLS's published 12-month change, Nov 2025 to Nov 2026, in CPI-U All Items Less Food and Energy must be **more than 2.9% at one decimal**. That means the published figure must be **3.0% or higher**. A print of exactly 2.9% resolves NO.
- **Which series:** BLS publishes the 12-month change on the not-seasonally-adjusted (NSA) index. So the calculation is NSA Nov 2026 ÷ NSA Nov 2025 − 1, rounded to one decimal. YES needs an unrounded value of about 2.95% or more.
- **When:** The November 2026 CPI comes out **Thursday, Dec 10, 2026, 8:30 AM ET** (13:30 UTC). That is the day after the Dec 9 FOMC decision. The market closes Dec 10 at 13:25 UTC, five minutes before the release (Fed Rate Calc; Thrive in Markets calendar; Nowflation).
- **Edge cases:**
  - **Shutdown clause:** If a government shutdown delays the data, the deadline extends. I found no sign of a current shutdown or a delay to the Dec 10 release.
  - **The base month is unusual:** November 2025 data were collected only in the second half of the month, after the 43-day 2025 shutdown, and October 2025 was never collected. The Nov 2025 index exists and is the base. BLS publishes 12-month changes for November (it did so for Nov 2025, at 2.6%), but **not for October 2026**, which has no October 2025 comparison (BLS release table, Nov 10 2026).
  - **Revisions:** NSA CPI is not revised, so the first print is final.

## 2. Reference classes and base rates

1. **The size of the November 2026 monthly core print (the deciding variable; see section 3).** YES needs roughly a seasonally adjusted (SA) November core gain of about 0.27–0.28% or more, which usually rounds to 0.3%.
   - The last three monthly prints (Aug, Sep, Oct 2026) were all **0.3%** (stocktitan / Karmactive, Nov 2026).
   - From memory, not checked here: November SA core in recent years was 0.5% (2021), 0.2% (2022), 0.3% (2023) and 0.3% (2024). In 2025 BLS published only a two-month change (0.2% total).
   - So, judged by recent November history and the latest run of prints, about half to two-thirds of comparable months reached about 0.3% unrounded.
2. **Pre-release forecasts versus actual core prints.** Core CPI usually lands within ±0.1pp of consensus. A miss of more than 0.1pp happens in roughly 10–20% of months (general knowledge). For October 2026, core came in at 0.3% against a Reuters-poll range of 0.2–0.3%.
3. **Nowcasts and outside forecasts for November 2026 core, year on year:**
   - Cleveland Fed nowcast (updated 11/23): **2.87%** y/y, with 0.21% m/m.
   - Nowflation model: about **2.95%**.
   - StoneX preview: 0.2% m/m and **2.8%** y/y (this may refer to the October report; the date is unclear).
   - University of Michigan RSQE (May 2026): Q4 2026 core around 3.5%. That is a quarterly average, and the forecast is old.
   - These estimates sit right on the threshold. Cleveland's nowcast has historically been fairly accurate for headline CPI but weaker for core.

## 3. Current state of the world (most recent first)

- **Nov 23, 2026:** Cleveland Fed nowcast for November: core CPI y/y 2.87%, core m/m 0.21%, headline y/y 3.86% (Cleveland Fed Inflation Nowcasting).
- **Mid-Nov 2026:** A StoneX preview said traders priced about 80% odds of a **Fed rate hike** at the December meeting. A stocktitan headline said the October core print reached Fed Governor Waller's threshold for "weighing a half-point hike." So inflation is a live policy concern. Headline CPI is about 3.7–3.9%, apparently pushed up by energy. Oxford Economics (Nov 16) expected headline PCE inflation (the Fed's preferred gauge) of 3.8% y/y for October.
- **Nov 10, 2026 (October CPI):**
  - Headline +0.4% m/m (about 0.35% unrounded); core **+0.3% (about 0.30%)**, the third straight 0.3%.
  - Shelter +0.3%; owners' equivalent rent (OER) +0.3%; rent +0.2%.
  - Outside estimates of the year-on-year rate BLS didn't publish: BofA core about 2.7%; another interpolation and EY/Haver about 2.8%.
  - **NSA core index: Sep 2026 = 339.287; Oct 2026 = 339.921**, a 0.19% NSA rise against 0.30% SA. The October seasonal factor therefore took off about 0.11pp (BLS table via search; FRED CPILFENS).
- **Sep 2026 CPI (released Oct 14):** core y/y **2.6%**. The Sep 2025 core NSA index was 330.804, and 339.287 ÷ 330.804 = +2.56%, which checks out.
- **Base-period levels (BLS Jan 13 2026 release, via search):** **Nov 2025 core NSA = 330.425**; Dec 2025 = 330.506; Dec 2024 = 322.007. The Dec 2025 y/y works out to 2.64%, matching the published 2.6%. Nov 2025 NSA sat *below* Sep 2025 (−0.11% over two months), which reflects the shutdown-depressed November 2025 reading. The New York Fed concluded the November 2025 data were "unusually low," likely because of collection delays (Liberty Street Economics, Feb 2026).

**The key arithmetic (if the index levels are right):**
- The Oct 2026 index is already 339.921 ÷ 330.425 = **+2.87%** above the November 2025 base.
- YES needs Nov 2026 NSA ≥ 330.425 × 1.0295 ≈ **340.17**. That is an **NSA November gain of about 0.074% or more**.
- Seasonal factors usually push the November NSA reading below the SA one. Sep→Nov 2025 showed −0.11% NSA against about +0.2% SA, and October 2026 removed 0.11pp, which implies November removes something like 0.15–0.25pp.
- So YES needs roughly **SA core of about 0.23–0.33%, central estimate about 0.27–0.28%**.
- The Cleveland Fed's figures (0.21% SA giving 2.87% y/y) imply November takes off about 0.2pp. Under that model, YES needs an SA print of about 0.28% or more.

## 4. Drivers and scenarios

**Paths to YES (core 3.0%+):**
- Core momentum holds at about 0.3% SA, as in Aug–Oct.
- Energy costs pass through into core services (airfares, transport) and goods prices (tariffs).
- Shelter stays at about 0.3%.
- The November seasonal factor takes off less than about 0.2pp.

**Paths to NO (core 2.9% or lower):**
- Core cools to about 0.2% SA, the Cleveland nowcast's estimate (0.21%).
- Holiday discounting is heavy in apparel, lodging, airfares or used cars.
- OER/rent keep softening (rent was +0.2% in October).
- The November seasonal adjustment is large.
- Because the 2.9% threshold is just above where the October index already stands (2.87%), even a flat-to-small NSA November keeps the result at 2.9% or below.

## 5. Signposts

- **Consensus for November core m/m in previews (about Dec 3–9):** 0.3% favors YES; 0.2% favors NO. Any previews that state a y/y consensus of 3.0% versus 2.9% would be directly informative.
- **Daily Cleveland Fed nowcast updates:** a move to 2.95% or higher favors YES.
- **Inputs to used-car and airfare estimates:** Manheim used-vehicle index for November, airline fares, and any holiday-discount evidence.
- **Nov 2026 PPI (if released before Dec 10)** and import prices.
- **Confirming the Nov 2025 NSA core index (330.425)** on BLS series CUUR0000SA0L1E. If it is wrong, the threshold arithmetic moves one-for-one.

## 6. Uncertainties

- I could not open BLS or FRED pages, so the index levels (330.425, 339.921) rest on search snippets. They agree with the published y/y rates, but I did not confirm them directly.
- I don't know the exact November seasonal factor for 2026. It decides whether an "SA 0.2%" or only an "SA 0.3%" print clears the bar.
- The StoneX "2.8% y/y" may refer to the October report rather than November.
- I found no published Street consensus for November core yet.
- Unrounded October core was about 0.30%, and its subcomponent detail beyond shelter, OER and rent is unclear.

## Sources
- [Consumer Price Index News Release – 2026 M10 (BLS)](https://www.bls.gov/news.release/cpi.htm)
- [Consumer Price Index Summary – 2026 M10 (BLS)](https://www.bls.gov/news.release/cpi.nr0.htm)
- [CPI News Release – 2025 M12, Jan 13 2026 (BLS archive)](https://www.bls.gov/news.release/archives/cpi_01132026.htm)
- [CPI News Release – 2026 M09, Oct 14 2026 (BLS archive)](https://www.bls.gov/news.release/archives/cpi_10142026.htm)
- [CPI News Release – 2025 M11, Dec 18 2025 (BLS archive)](https://www.bls.gov/news.release/archives/cpi_12182025.htm)
- [FRED CPILFENS](https://fred.stlouisfed.org/series/CPILFENS)
- [Cleveland Fed Inflation Nowcasting](https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting)
- [Seeing Through the Shutdown's Missing Inflation Data – Liberty Street Economics](https://libertystreeteconomics.newyorkfed.org/2026/02/seeing-through-the-shutdowns-missing-inflation-data/)
- [CNBC – October CPI preview, Nov 9 2026](https://www.cnbc.com/2026/11/09/october-cpi-report-2026-inflation.html)
- [Stocktitan – October 2026 CPI report](https://www.stocktitan.net/articles/october-2026-cpi-inflation-report)
- [Karmactive – October 2026 CPI breakdown](https://www.karmactive.com/october-2026-cpi-inflation-breakdown-fed-rate/)
- [Verified Investing – CPI October 2026](https://verifiedinvesting.com/blogs/us-economic-metrics/cpi-mom-october-2026)
- [EY – Consumer Price Index October 2026](https://www.ey.com/en_us/insights/strategy/macroeconomics/cpi-report)
- [StoneX – US CPI preview, Nov 9 2026](https://www.stonex.com/en-gb/news-and-analysis/us-cpi-preview-will-inflation-fall-enough-to-put-a-fed-hike-in-doubt-2026-11-09/)
- [Nowflation – CPI forecast November 2026](https://nowflation.com/forecast)
- [Fed Rate Calc – CPI release dates](https://fedratecalc.com/cpi-release-date/)
- [Thrive in Markets – CPI calendar](https://thriveinmarkets.com/calendar/indicator/cpi/)
- [University of Michigan RSQE US Outlook, May 2026](https://lsa.umich.edu/content/dam/econ-assets/Econdocs/RSQE%20PDFs/RSQE_May26_US_Forecast.pdf)
- [Oxford Economics – US PCE nowcast, Nov 2026](https://www.oxfordeconomics.com/resource/us-pce-nowcast-broadening-pressures-lock-in-december-rate-hike/)
- [Payney – US inflation rate](https://payney.com/inflation-rate/)
- [Trading Economics – US core inflation, Nov 2025](https://tradingeconomics.com/united-states/core-inflation-rate/news/511088)