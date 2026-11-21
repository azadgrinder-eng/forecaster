## Research brief: Will there be exactly 2 government shutdowns in 2026 under the GOVTSHUTLENGTH definition?

**Bottom line:** Kalshi says it has already settled two 2026 funding deadlines as shutdowns: January 31 and February 14. If those count toward this market, the question is almost the same as asking whether the government stays open at 10:00 AM ET on every day from December 12 through December 31, 2026. The next deadline is the end of December 11, which is a Friday.

### 1. Resolution mechanics
- **What resolves YES:** The number of distinct federal government shutdowns in calendar year 2026 must be exactly 2. A shutdown is defined by the GOVTSHUTLENGTH contract, and status is checked at 10:00 AM ET each day. The market closes on Jan 1, 2027 at 14:59 UTC. Kalshi decides the outcome.
- **How GOVTSHUTLENGTH defines a shutdown:** The government's "orderly suspension of agency work that is not legally excepted, typically accompanied by furloughing the employees who perform that work." Days are counted on a calendar basis, including weekends and holidays. A holiday does not end a shutdown. A "technical lapse in appropriations" does not count if OMB tells agencies to keep operating normally. Kalshi relies on primary source agencies such as OMB and OPM, and may use secondary sources if those are late or conflict (Kalshi GOVTSHUTLENGTH rules PDF, created 2026-02-06; I could only read fragments of it through search).
- **Partial shutdowns count:** A related Kalshi contract says "at least part of the federal government has to shut down at 10 a.m." A missed deadline alone is not enough (next.io summary of Kalshi rules).
- **Count so far:** Kalshi's own shutdown page says its markets settled two funding deadlines as shutdowns in 2026, January 31 and February 14, and lists the January 31 shutdown as lasting 4 days (Kalshi government-shutdown page, accessed Nov 2026). Wikipedia lists the same two, with the second running Feb 14 to Apr 30 (76 days).
- **Edge cases:**
  - **(a) A short weekend lapse.** The Dec 11 deadline expires at midnight going into Saturday, Dec 12. If a bill is signed before 10 AM ET Saturday, or OMB says no shutdown is needed (as happened in Dec 2024, when the bill was signed about 12:40 AM), the day should not count. The Jan 31, 2026 precedent cuts the other way: OMB began shutdown procedures at midnight on a Saturday and Kalshi counted it.
  - **(b) A shutdown that starts in December and runs into 2027** would still make the 2026 count 3, so the market would resolve NO.
  - **(c) What counts as "distinct."** After April 30, ICE and CBP were left out of the DHS funding bill and were to be funded through reconciliation. I found no evidence that OMB ran shutdown procedures for them afterward or that Kalshi treated this as continuing or new. Because Kalshi reports two settled shutdowns, this appears not to matter.
  - **(d) Recount risk.** There is a small chance Kalshi interprets the "distinct shutdowns" count differently, for example by not counting the 4-day weekend-start lapse. That would make the current count 1 and the market would lose its main path to YES. Kalshi's settlement of both deadlines makes this unlikely.

### 2. Reference classes and base rates
1. **December deadlines in lame-duck sessions since 1980.** Funding lapses happened in Dec 1982 (Dec 17–21, about 3 days) and Dec 2018 (Dec 22 to Jan 25). The 2018 case is closely comparable: Democrats had just won the House and Trump demanded money (then for a border wall). Other year-end lame-duck deadlines were closed with a CR or omnibus without a counted shutdown: 2010, 2014, 2016, 2020, 2022 and 2024. The 2024 lapse lasted minutes and OMB did not shut anything down. My rough count is 2 lapses out of about 10 or 11 such deadlines, roughly 15–20%. This is my own tally from the House History and CRS lists.
2. **All funding gaps.** CRS counts 21 funding gaps from FY1977 to 2025, about 1 for every 4 or 5 CR or appropriations deadlines. About half lasted 3 days or less (CRS RS20348, Dec 18, 2025). Taking 25–40 deadlines as the denominator, the per-deadline lapse rate is around 10–20%.
3. **The current Trump-era regime.** Since late 2025, 3 of about 5 major deadlines produced shutdowns: Oct 1, 2025; Jan 31, 2026; Feb 14, 2026. The Nov 2025 CR and the Sept 2026 CR passed without one. That is about 50–60%, which shows the current environment is much more prone to shutdowns than the historical average.

### 3. Current state of the world (most recent first)
- **Nov 20, 2026:** Reuters (via US News) and NPR report that Congress is struggling to avoid a shutdown. Splits over the Iran war and Trump's demand for $350B in new Pentagon spending threaten a deal. Thune said "The American people don't need another government shutdown" and called another one a "colossal mistake." The administration is considering a stopgap running through March. Senate Republicans are pursuing bipartisan talks on a $1.1T defense appropriations bill that includes only $69B of the request, but reconciliation for the Pentagon money is still possible (Reuters/US News, Nov 20; mlq.ai, Nov 20; Spectrum, Nov 20).
- **Nov 19:** Democrats have not decided whether to make their votes conditional on blocking Iran war funds. Shaheen said nobody she has talked to thinks a shutdown makes sense, and Booker said Democrats "need to avoid a government shutdown." Schumer has not tied war limits to the funding bill. Van Hollen says he will not vote for a funding bill that doesn't defund the war, but reportedly did not argue for risking a shutdown. The dispute is tangled up with Van Hollen's challenge to Schumer for leader (The Hill; HNGN, Nov 19; Washington Sun).
- **Nov 12:** Bennet, Van Hollen, Duckworth and Sanders issued a joint statement saying any short-term package must bar spending on the war. Duckworth and Gillibrand want to cut off funds for offensive operations while keeping defensive funding. Republican senators warned that the $350B defense reconciliation push risks a December shutdown (The Hill, Nov 12).
- **Nov 3–4:** In the midterms, Democrats won both chambers starting in January 2027: roughly 228 House seats and a Senate with at least 54 seats. The current lame-duck Congress still has Republican majorities, and stopgaps need 60 Senate votes (OPB/NPR, Nov 4; AP via WSB, Nov 4).
- **Sept 2, 2026:** Trump signed the Continuing Appropriations and Extensions Act, 2027, a clean CR through Dec 11. It passed 90–6 in the Senate and 370–48 in the House, so there was no shutdown on Oct 1 (Fox News, iHeart, Sept 2–3; Breaking Defense, Sept 2026).
- **Apr 30, 2026:** Trump signed DHS funding, ending the shutdown that began Feb 14 (75 or 76 days depending on the source). The bill left out ICE and CBP, which are to be funded by reconciliation (PBS, CBS, OPB, Apr 30–May 1).
- **Feb 3, 2026:** The House passed H.R. 7148 217–214 and Trump signed it, ending the partial shutdown that began Jan 31. It funded most agencies through Sept 30 but gave DHS money only through Feb 13 (OPB, Feb 3; GovExec/Defense One, Feb 2026).
- **Scheduled before close:** The Dec 11 deadline, with a lapse beginning 12:01 AM Saturday Dec 12. Congress usually adjourns before Christmas. The new Congress convenes Jan 3, 2027, after this market closes.

### 4. Drivers and scenarios
**YES (no new shutdown counted at 10 AM ET from Dec 12 to Dec 31):**
- The most likely route is a CR into early 2027, possibly through March as the White House is considering. Republicans may prefer pushing the fight to the new Congress, and Democrats may prefer to wait until they hold both chambers in January. If Democrats wait, they get more leverage over Iran war funding by holding out a few weeks, which lowers their incentive to force a shutdown now.
- Shutdown fatigue after three shutdowns in 13 months, including the record 76-day DHS shutdown, plus leadership on both sides (Thune, Schumer, Shaheen, Booker) signaling they want to avoid one.
- A lapse that is fixed before 10 AM Saturday, or a weekend lapse where OMB does not direct a shutdown.

**NO (a third shutdown, or a recount):**
- At least 8 Democratic senators would be needed to pass a stopgap. If Democrats insist on war-funding limits, or Trump insists on $350B in Pentagon money or attaches policy riders, Democrats could block it.
- Trump might refuse to sign a CR that restricts the war, which mirrors December 2018 when he refused to sign a CR without wall money after the midterm loss.
- A short CR (for example to Dec 18 or 19) followed by a lapse before Christmas.
- Very unlikely: Kalshi revising the count to 1.

### 5. Signposts
- **Toward NO:** Schumer or the Democratic caucus formally conditioning votes on war-funding limits; Trump publicly rejecting a "clean" CR or demanding the $350B in it; a failed Senate cloture vote on a CR in the week of Dec 7; the White House not sending its requested adjustments; OMB telling agencies to update shutdown plans.
- **Toward YES:** A bipartisan announcement of a CR into 2027; a scheduled House vote on a CR around Dec 9–10; Senate passage with 60 or more votes before Dec 11; the leadership race settled in Schumer's favor; a separate Iran war vote, such as a War Powers resolution, giving Democrats another outlet.
- **On Dec 12 itself:** whether OMB or OPM issues shutdown notices by 10 AM ET Saturday.

### 6. Uncertainties
- I could not read the full GOVTSHUTLENGTH PDF (its text was compressed). The exact wording on start and end, and on what makes shutdowns "distinct," is not confirmed. I am relying on Kalshi's public page saying two deadlines were settled as shutdowns.
- I don't know the status of ICE and CBP funding after April 30, or whether the September CR covers them. A lapse limited to ICE and CBP is a minor tail risk.
- I don't know House Speaker Johnson's or Jeffries's stated positions for December, or how unified House Republicans are on a clean CR.
- I don't know whether Congress plans a single deadline or a series of short CRs, which would mean more chances to lapse.
- Several pages failed to load, so some recent details come from search summaries rather than full articles.

## Sources
- [Kalshi GOVTSHUTLENGTH contract terms](https://kalshi-public-docs.s3.amazonaws.com/contract_terms/GOVTSHUTLENGTH.pdf)
- [Kalshi government shutdown page (settlement history)](https://kalshi.com/politics/government-shutdown-odds)
- [Will There Be a Government Shutdown on December 12, 2026? (next.io)](https://next.io/prediction-markets/trending/will-there-be-a-government-shutdown-on-december-12-2026/)
- [2026 United States federal government shutdowns (Wikipedia)](https://en.wikipedia.org/wiki/2026_United_States_federal_government_shutdowns)
- [Congress Struggles to Avert US Shutdown as Iran War Divides Lawmakers (US News/Reuters, Nov 20, 2026)](https://www.usnews.com/news/politics/articles/2026-11-20/congress-struggles-to-avert-us-shutdown-as-iran-war-divides-lawmakers)
- [Fight over funding for Iran war could put the government at risk of a shutdown (NPR, Nov 20, 2026)](https://npr.org/2026/11/20/nx-s1-6043190/fight-over-funding-for-iran-war-could-put-the-government-at-risk-of-a-shutdown)
- [Congress struggles to avert a government shutdown as the Iran war splits lawmakers (mlq.ai, Nov 20, 2026)](https://mlq.ai/news/congress-struggles-to-avert-a-government-shutdown-as-the-iran-war-splits-lawmakers/)
- [Democrats push to cut Iran war funding, setting up possible shutdown fight (Spectrum, Nov 20, 2026)](https://spectrumlocalnews.com/us/snplus/politics/2026/11/20/democrats-iran-war-funding-possible-government-shutdown)
- [Democrats worry Chris Van Hollen's hardline Iran stance could trigger shutdown (The Hill)](https://thehill.com/homenews/senate/6228970-senate-democrats-avoid-shutdown/)
- [GOP senators warn Trump push for Pentagon funding risks shutdown (The Hill, Nov 12, 2026)](https://thehill.com/homenews/senate/6217691-republican-reconciliation-threatens-government-funding/)
- [Democrats Split on Using Dec. 11 Deadline to End Iran War (HNGN, Nov 19, 2026)](https://www.hngn.com/articles/273891/20261119/democrats-split-using-dec-11-deadline-end-iran-war.htm)
- [Lawmakers Eye Path to Avoid a Government Shutdown in Iran War Funding Fight (Washington Sun)](https://www.washingtonsun.com/congress/iran-war-funding-government-shutdown-van-hollen-senate)
- [Democrats win full control of Congress (OPB/NPR, Nov 4, 2026)](https://www.opb.org/article/2026/11/04/2026-midterms-democrats-win-the-senate/)
- [Election 2026: Democrats capture both chambers of Congress (WSB-TV/AP)](https://www.wsbtv.com/news/trending/election-2026-democrats-capture-both-houses-congress/5ILOWTVABVDPZFYP7VBBCX4EWE/?outputType=amp)
- [Trump signs government funding bill, avoiding a shutdown ahead of midterms (Fox News, Sept 2026)](https://www.foxnews.com/politics/trump-signs-government-funding-bill-avoiding-shutdown-ahead-midterms.amp)
- [Trump Signs Stopgap Bill To Avert Government Shutdown (iHeart, Sept 3, 2026)](https://www.iheart.com/content/2026-09-03-trump-signs-stopgap-bill-to-avert-government-shutdown/)
- [House passes funding stopgap averting government shutdown in October (Breaking Defense, Sept 2026)](https://breakingdefense.com/2026/09/house-passes-funding-stopgap-averting-government-shutdown-in-october/)
- [Trump signs bill funding DHS, ending record-breaking 76-day shutdown (CBS News, Apr 30, 2026)](https://www.cbsnews.com/amp/news/dhs-shutdown-house-vote/)
- [Trump signs bill funding the Department of Homeland Security, ending record shutdown (OPB, May 1, 2026)](https://www.opb.org/article/2026/05/01/trump-signs-bill-funding-the-department-of-homeland-security-ending-record-shutdown/)
- [Trump signs government funding legislation, ending the partial shutdown (OPB, Feb 3, 2026)](https://www.opb.org/article/2026/02/03/trump-signs-government-funding-legislation-ending-the-partial-shutdown-that-began-over-the-weekend)
- [Partial shutdown ends less than four days after it began (GovExec, Feb 2026)](https://www.govexec.com/management/2026/02/partial-shutdown-ends-less-four-days-after-it-began/411160/?oref=ge-next-story)
- [How Prediction Markets Polymarket and Kalshi Are Gamifying Truth (Bloomberg, 2026)](https://www.bloomberg.com/features/2026-prediction-markets-polymarket-kalshi/)
- [Federal Funding Gaps: A Brief Overview (CRS RS20348, Dec 18, 2025)](https://www.everycrsreport.com/files/2025-12-18_RS20348_5a6d658a2c85f7cce62d05d4655dc13bf3c5031f.html)
- [Funding Gaps and Shutdowns in the Federal Government (House History)](https://history.house.gov/Institution/Shutdown/Government-Shutdowns/)