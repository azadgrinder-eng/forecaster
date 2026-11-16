# Research brief: Will the U.S. government officially attribute the Nov 13, 2026 FAA outage to a hack by Nov 30, 2026?

*Method note: The web-page fetch tool was blocked in this environment, so every fact below comes from search-result summaries of the cited articles, not from reading the full text. Exact quotes and figures should be checked where they matter.*

## 1. Resolution mechanics

- **What counts as YES:** Between market creation and **Nov 30, 2026, 11:59 PM ET**, an authorized U.S. federal official, acting officially and on the record, must say publicly that the Nov 13 outage **was caused by** a hack. The outage in question is the equipment and communications failure behind the nationwide departure ground stop. A federal criminal charge alleging a hack caused it also counts.
- **"Hack" is defined broadly** as "intentional, malicious activity that caused the outage." That probably covers deliberate insider sabotage, such as a malicious misconfiguration by someone with access, not just outside cyber intrusion. This is the main ambiguity in the rules.
- **What does not count:**
  - Statements that a hack is "suspected / likely / probable / not ruled out" or "consistent with" a hack.
  - Anonymous or unnamed officials.
  - Foreign governments.
  - Hacker groups claiming responsibility, unless the U.S. government confirms.
- **Other rules:**
  - A YES cannot be undone by a later retraction.
  - The main source is official U.S. statements, but a "consensus of credible reporting" may also be used. That leaves some room for judgment if reporting gets ahead of official statements.
- **Edge cases:**
  - An official finding of carelessness or negligence (installer error, a wrong configuration, a defective device) resolves **NO**.
  - A politician loosely calling it "sabotage" for political reasons, such as blaming the prior administration's neglect, probably does not qualify unless it is a clear official finding of an intentional malicious cause.
  - Window: only 14 days remain after today (Nov 16).

## 2. Reference classes and base rates

**A. Major U.S. aviation/ATC outages since 2014: how many were malicious?** This list is my own compilation.
- **Malicious, 1 of about 12:** the Sept 2014 fire at the Chicago air traffic control center in Aurora, set deliberately by a contractor.
- **Not malicious:**
  - 2015 FAA computer-system failure at the Leesburg, VA center (software)
  - 2015 United outage (router)
  - 2016 Delta outage (power)
  - 2017 Atlanta airport power fire
  - Sept 2022 United slowdown (software update; "not a cybersecurity issue")
  - Dec 2022 Southwest meltdown
  - Jan 2023 FAA NOTAM outage (a contractor accidentally deleted files; "no evidence of a cyber-attack or malicious intent")
  - July 2024 CrowdStrike/Microsoft outage (not a cyberattack)
  - 2025 Newark radar/radio losses (copper/fiber line failures)
  - Sept 2026 Northeast outage (Amtrak crew accidentally cut a fiber line)
- **Base rate:** about 8% were malicious. In the one malicious case the cause was physical and obvious, and a federal complaint was filed within roughly a day (Brian Howard; ABC7, 2014). **In none of these cases did officials first say "no evidence of cyber" and later attribute the outage to an attack.**

**B. Large network or infrastructure outages where officials quickly said "no sign of cyberattack" and a router or configuration problem was found.**
- Examples: the AT&T outage of Feb 2024 (configuration error), Australia's Optus outage of 2023 (router messages flooding the network after an upgrade), the 2023 NOTAM outage, and CrowdStrike 2024.
- Rate at which these flipped to a confirmed malicious cause: effectively 0 of about 5–10 I can recall. Rough base rate: **under 5%**.

**C. Speed of official attribution when an attack really happened.**
- When an attack is real, U.S. officials usually confirm it within days (Aurora fire; Colonial Pipeline ransomware, 2021).
- Formal government-to-government attributions of state-sponsored attacks often take months.
- So even with a malicious cause, a qualifying statement within 17 days is likely only if the evidence is clear-cut or there is an insider suspect.

## 3. Current state of the world (most recent first)

- **Nov 15–16:**
  - No root-cause report has been published.
  - FAA Administrator Bryan Bedford: "When we have that root cause analysis complete, we'll share it with you." No date given (CNN, Nov 14; ABC News live blog, Nov 15–16).
  - Flight cancellations continued into Monday.
- **Nov 15, router maker pushes back:** HPE, which owns Juniper, says the routers "did not fail" and that "the device functioned as it was configured to by the installer." This points at configuration or installation, not a hardware defect.
  - L3Harris says only that it is "supporting the FAA in its investigation."
  - FAA technicians turned off the routers' data-broadcast feature across all of the agency's Juniper routers.
  - Sources: Yahoo/Men's Journal, Nov 15; WSJ via SiliconReport.
- **Nov 15, Transportation Secretary Duffy on cyber:**
  - Asked about a cyber or foreign attack: "we don't believe so … we don't believe this was cyber at all" (ANI/Tribune, Nov 15; The Defiant).
  - Asked whether sabotage was ruled out, he did not fully rule it out: "we're looking at a full suite of issues with the router and with the installation."
  - The FAA is "partnering with the FBI and other law enforcement."
  - Sources: Fortune, Nov 15; Yahoo, Nov 15.
- **Nov 14–15, what officials say happened:**
  - The outage began during L3Harris work switching copper lines to fiber at an FAA radio site in **El Dorado, Arkansas**.
  - A newly installed Juniper router flooded the FAA network with more than 1,000 connection attempts every 4–5 seconds.
  - A second router in **Amarillo, Texas**, installed about three weeks earlier, also flooded the network.
  - Communications were disrupted at roughly 17 of the FAA's 22 high-altitude (en route) centers. This figure comes from paraphrase, not a direct quote.
  - Both routers are at an L3Harris lab in Florida.
  - Officials are weighing three possible causes: an installation error, a misconfiguration, or a defective device.
  - Sources: Yahoo/WSJ; KATV; Scripps; Al Jazeera, Nov 15.
- **Nov 14:**
  - Bedford: "zero evidence of anything nefarious, and zero evidence of anything AI-related" (ABC7 Chicago).
  - SecurityWeek: "No Signs of Hacking…as FBI Reportedly Probes Software Update."
  - CBS cited conflicting information, including a Cisco router theory.
  - CNN reported some controllers "don't buy" Duffy's explanation. I could not confirm the details.
- **Nov 13, Homeland Security Secretary Mullin (briefing with Duffy):**
  - The outage "doesn't appear" to be a cyberattack; "nothing certain right now … not going to rule that out."
  - No group had claimed responsibility.
  - He dismissed "conspiracy theories."
  - He said NSA, the Defense Department, CISA and other agencies were involved.
  - The White House said there was no indication of a "nefarious act" (CBS).
  - Officials said it was unrelated to a Microsoft outage earlier that week.
- **Nov 13, the event:**
  - The FAA "experienced a technical problem" and ordered a nationwide ground stop at about 3:30 p.m. ET, lifted at about 8:15 p.m. ET.
  - Roughly 8,000–12,000+ flights were cancelled (the FAA's Q&A says about 12,462).
  - Duffy and Mullin asked Congress for $50B to overhaul air traffic control; Trump blamed Biden.
- **Political framing:** Officials are clearly blaming old, overloaded technology and the contractor. Calling it a hack would undercut that story and the funding pitch. Partisan incentives are mixed but do not obviously favor a "hack" finding.
- **Scheduled before Nov 30:** The root-cause analysis has no date. There may be congressional oversight hearings or letters, which I could not confirm. Thanksgiving travel peaks Nov 25–29, which adds pressure for a quick explanation. No hearing date was found.

## 4. Drivers and scenarios

**Paths to NO (dominant):**
1. The root-cause analysis finds the installer configured the router wrongly (for example, the broadcast feature left on) or used poor procedures.
2. It finds a hardware or firmware defect.
3. The investigation is still open on Nov 30 with officials still saying "no evidence." Root-cause reports often take weeks.

The physical facts already known all point toward a non-malicious network flood: a new router at a site where a contractor was actively working, a second router behaving the same way, and the maker saying the devices did what they were configured to do. The 2023 Optus outage followed the same pattern and was not an attack.

**Paths to YES (tail):**
1. The FBI or forensic work on the Florida routers finds tampering: a malicious configuration, an implanted firmware change, or unauthorized remote access. Officials then announce it, or prosecutors file charges.
2. **Insider sabotage:** a contractor employee deliberately misconfigures equipment (like the Aurora fire, but digital) and is charged by federal complaint. This could move fast.
3. A foreign actor, such as a group exploiting a Juniper vulnerability, is publicly named. State-attribution timelines make this unlikely before Nov 30.

What YES depends on: forensic findings, the FBI's role changing from "assisting" to a criminal investigation, and a named official being willing to state it as fact rather than "suspected."

## 5. Signposts

- **Toward YES (strong):**
  - The FBI opens a criminal case or names a subject.
  - A federal complaint or arrest tied to the El Dorado or Amarillo work.
  - Duffy, Bedford, Mullin, CISA or the FBI using words like "intentional," "unauthorized access," "tampered" or "malicious."
  - A CISA advisory on Juniper devices tied to this incident.
  - Officials turning from blaming L3Harris to protecting it.
- **Toward YES (weak):** Credible reporting from named sources about unexplained configuration changes, or a credible group claiming responsibility.
- **Toward NO:**
  - The root-cause report pins it on installation or configuration error or a defect.
  - L3Harris accepts fault.
  - The FAA blames the broadcast feature or a "broadcast storm."
  - Congressional discussion focused on modernization funding.
  - Silence through Thanksgiving.

## 6. Uncertainties

- I could not read the full texts (fetch was blocked), so the exact wording of Duffy's and Mullin's caveats is from summaries.
- Who changed the router configuration, when, and whether the change was authorized is not public.
- Why the Amarillo router, installed about three weeks earlier, started flooding only when Arkansas came online is unexplained. That could be ordinary network behavior or an anomaly.
- The FBI's exact role and whether any criminal investigation is open is unclear.
- There is no timetable for the root-cause analysis.
- The CBS Cisco router theory conflicts with the Juniper reporting.
- I could not verify the details of the CNN report that controllers are skeptical.
- It is unclear whether a market resolver would count deliberate insider misconfiguration as a "hack." The definition suggests yes.

## Sources
- [2026 FAA nationwide ground stop – Wikipedia](https://en.wikipedia.org/wiki/2026_FAA_nationwide_ground_stop)
- [Nationwide Ground Stop: Questions and Answers – FAA](https://www.faa.gov/newsroom/faa-statement-nationwide-ground-stop)
- [CNN live, Nov 13, 2026](https://www.cnn.com/2026/11/13/us/live-news/flights-ground-stop-faa)
- [What we know about the cause of the nationwide FAA ground stop – CNN, Nov 14](https://www.cnn.com/2026/11/14/politics/faa-ground-stop-what-we-know)
- [ABC News – ground stop lifted, Trump admin blames old tech](https://abcnews.com/US/nationwide-ground-stop-ordered-airports-faa/story?id=138121848)
- [CNBC – FAA lifts ground stop, Nov 13](https://www.cnbc.com/2026/11/13/faa-ground-stop.html)
- ["Don't believe so": Duffy rules out cyberattack – ANI, Nov 15](https://www.aninews.in/news/world/us/dont-believe-so-us-transportation-secy-rules-out-cyberattack-in-faa-outage-aviation-chief-says-no-ai-link20261115023354/)
- [Duffy Sees No Sign of Foreign Cyberattack – The Defiant](https://thedefiant.io/frontier/technology/duffy-sees-no-sign-of-foreign-cyberattack-in-faa-outage)
- [Transportation secretary still doesn't totally rule out cyberattack; FBI assisting – Fortune, Nov 15](https://fortune.com/2026/11/15/cyberattack-hack-faa-air-traffic-control-communications-router-fbi-probe-sean-duffy-ground-stop/)
- [FAA ground stop latest updates (Duffy blames L3Harris; maker says 'did not fail') – Yahoo News](https://www.yahoo.com/news/us/live/faa-ground-stop-latest-updates-duffy-blames-contractor-l3harris-thousands-more-flights-canceled-saturday-no-sign-of-cyberattack-161329174.html)
- [What forced the US to ground all planes? A router switch – Al Jazeera, Nov 15](https://www.aljazeera.com/news/2026/11/15/what-forced-the-us-to-ground-all-planes-a-router-switch-we-now-know)
- [What caused the FAA ground stop? – Scripps News](https://www.scrippsnews.com/life/travel/what-caused-the-faa-ground-stop-officials-point-to-router-failure)
- [FAA router overload in Arkansas – WSJ via Yahoo](https://www.yahoo.com/news/us/articles/faa-router-overload-arkansas-triggered-053809546.html)
- [El Dorado, Arkansas at center of FAA breakdown – KATV](https://katv.com/news/local/el-dorado-arkansas-at-center-of-nationwide-faa-communications-breakdown-controllers-ground-stop-delays-cancellatoin-radar-installation-investigation-flights)
- [Router Maker HPE Pushes Back: 'They Did Not Fail' – Yahoo](https://www.yahoo.com/news/us/articles/router-maker-hpe-pushes-back-155040506.html)
- [HPE Says Devices 'Did Not Fail' – Men's Journal](https://www.mensjournal.com/news/hpe-juniper-router-faa-ground-stop-did-not-fail)
- [FAA disables Juniper router feature – SiliconReport](https://www.siliconreport.com/faa-disables-juniper-router-feature-after-overload-wsj-reports)
- ['Zero evidence of anything nefarious' – ABC7 Chicago](https://abc7chicago.com/live-updates/faa-ground-stop-live-updates-what-know-nationwide-flights-are-grounded/20038887/entry/20040360/)
- ['Nothing completely certain' on cyberattack, Mullin says – ABC7 SF](https://abc7news.com/live-updates/faa-ground-stop-live-updates-what-know-nationwide-flights-are-grounded/20038887/entry/20039387/)
- [No Signs of Hacking in FAA Ground Stop – SecurityWeek](https://www.securityweek.com/no-signs-of-hacking-in-faa-ground-stop-as-fbi-reportedly-probes-software-update/)
- [Legacy tech issue led to FAA's nationwide ground stop – Nextgov/FCW](https://www.nextgov.com/modernization/2026/11/legacy-tech-issue-led-faas-nationwide-ground-stop/417232/)
- [FAA lifts ground stop; White House says no indication of "nefarious act" – CBS News](https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/)
- [Mullin Dismisses 'Conspiracy Theories' – Trending Politics](https://trendingpoliticsnews.com/video-mullin-dismisses-conspiracy-theories-surrounding-nationwide-ground-stop-cmc/)
- [ABC News live updates – cancellations into Monday](https://abcnews.com/US/live-updates/faa-ground-stop-live-updates-hundreds-flights-canceled/?id=138125140)
- [2023 FAA system outage – Wikipedia](https://en.wikipedia.org/wiki/2023_FAA_system_outage)
- [FAA says unintentionally deleted files to blame (2023) – WHDH](https://whdh.com/news/faa-says-unintentionally-deleted-files-are-to-blame-for-nationwide-ground-stop/)
- [United Airlines says outage not a cybersecurity issue (2022) – SecurityWeek](https://www.securityweek.com/united-airlines-says-the-outage-that-held-up-departing-flights-was-not-a-cybersecurity-issue/)
- [Telecom Failure Disrupts Northeast Air Traffic (Sept 2026) – AVweb](https://avweb.com/aviation-news/telecom-failure-disrupts-ne-air-traffic/)
- [Brian Howard charged with starting fire at FAA facility in Aurora (2014) – ABC7](https://abc7.com/post/man-charged-with-starting-fire-at-faa-facility-in-aurora/326351/)
- [Naperville man pleads guilty to setting fire at Chicago ARTCC – DOJ](https://www.justice.gov/usao-ndil/pr/naperville-man-pleads-guilty-setting-fire-chicago-air-route-traffic-control-center)