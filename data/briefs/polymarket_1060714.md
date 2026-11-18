# Research brief: "Nothing Ever Happens: 2026" (Polymarket)

Today is 18 Nov 2026 and about 43 days remain. On the evidence I found, none of the 13 triggers has occurred yet. Most of them can no longer realistically fire in the time left, and the main live risk is the US–Iran conflict.

## 1. Resolution mechanics

- **What the market asks.** It resolves **"No"** if any one of 13 events happens between market creation and 31 Dec 2026, 11:59 ET. If none happens, it resolves **"Yes"**. A single trigger is enough.
- **Close time.** The stated close is 2026-12-31T16:59Z, which is 11:59 **AM** ET. So the window may end at noon ET on 31 Dec, not midnight.
- **The 13 triggers.**
  - Trump out as President
  - China invades Taiwan
  - Xi Jinping out
  - U.S. invades Iran
  - Iranian regime falls
  - BTC reaches $1M or falls to $10k
  - Epstein found alive
  - Republican trifecta with a Senate supermajority
  - Russia invades a NATO country
  - Trump acquires Greenland
  - Earthquake of magnitude 9.0 or more
  - Eruption of VEI 6 or more
  - Meteor strike of 250 kt or more
- **Resolution sources.** The rules PDF is mostly unreadable as text. Its file metadata shows it was created 6 Jan 2026, and it links to these sources:
  - Binance BTC/USDT for the Bitcoin triggers
  - USGS "significant earthquakes" for earthquakes
  - the Smithsonian Global Volcanism Program for VEI
  - the NASA CNEOS fireball database for meteors

  (Polymarket NEH 2026 rules PDF, created 2026-01-06)
- **Who decides.** Polymarket and its resolution process (UMA). I could not read the exact definitions in the PDF.
- **Main ambiguity: what counts as "invades."** In a January 2026 Polymarket market on a US invasion of Venezuela, Polymarket ruled that the capture of Maduro was **not** an invasion. It said a qualifying invasion means "US military operations intended to establish control," and that ruling drew heavy criticism (DeFi Rate / SAN / CasinoBeats, Jan 2026). By the same standard:
  - US air and naval strikes on Iran since Feb 2026 have evidently not counted, since the market is still open.
  - A limited raid also probably would not count.
  - Seizing and holding Iranian territory, such as Kharg, Abu Musa or Larak islands, plausibly would.
- **Other ambiguities.**
  - Iran: the death of Ali Khamenei and the handover to Mojtaba Khamenei apparently did not count as "regime falls." That implies the bar is the end of the Islamic Republic itself.
  - "Senate supermajority" is undefined in what I could read (60 or 67 seats). Either way it cannot be met, because the 2027 Senate is not seated until 3 Jan 2027, and Democrats won the Senate anyway.
- **Precedent for "nothing happening."** Big 2026 events have not triggered resolution so far. These include the US capture of Maduro, the US–Israel war on Iran and Khamenei's death, the Greenland crisis, and Baltic drone incursions.

## 2. Reference classes and base rates

Each per-year rate below is scaled to the remaining ~43 days (about 0.118 of a year) using a constant hazard.

| Trigger | Reference class and how I got it | Annual rate | ~43-day probability |
|---|---|---|---|
| M9.0+ earthquake | About 5 instrumentally recorded since 1900: Kamchatka 1952, Chile 1960, Alaska 1964, Sumatra 2004, Tōhoku 2011. Kamchatka in July 2025 was M8.8. Count is from my own knowledge, not a source checked here. | ~4% | ~0.5% |
| VEI 6+ eruption | Roughly 4–5 since 1880: Krakatau 1883, Santa María 1902, Novarupta 1912, Pinatubo 1991. Hunga Tonga 2022 is generally rated VEI 5–6. | ~1.5–3% | ~0.2–0.35% |
| 250 kt+ fireball | In CNEOS records since 1988, essentially only Chelyabinsk 2013 (~440–500 kt) qualifies. The Bering Sea 2018 event was ~173 kt. | ~2.5–3% | ~0.3% |
| Trump out | Actuarial death rate for an 80-year-old US male is ~5–6% a year. Removal by impeachment needs 67 senators, and the new Congress does not sit until January. Resignation is negligible. | ~6% | ~0.7–0.9% |
| Xi out | Death rate at age 73 is ~2–3% a year, plus a small chance of a political ouster. | ~3% | ~0.3–0.4% |
| Wars | Reference class is great-power invasions of contested or allied territory. China–Taiwan and Russia–NATO have never happened. US ground invasions of a state it is already at war with are the more relevant class (Iraq 2003 followed months of buildup). | — | see §4 |

Under independence, the natural-hazard and actuarial triggers together give roughly **2–2.5% for "No"** before counting the geopolitical triggers.

## 3. Current state of the world (most recent first)

- **Iran: Nov 16–17.**
  - A third carrier group, USS Roosevelt, entered the region on 15 Nov. US personnel in West Asia are about 53,000, described as the biggest buildup since 2003, and Iran is reportedly rebuilding its missile arsenal (Organiser/JPost, 2026-11-17).
  - Al Jazeera asks whether the war is "about to resume" (Al Jazeera, 2026-11-16).
  - There is unconfirmed reporting that Iraq's prime minister briefed Shiite leaders on a possible US ground plan against southern Iran (Kantan News, Nov 2026).
- **Bitcoin: Nov 13–15.** About $69k on 13 Nov (Fortune, 2026-11-13). Headlines on 15 Nov put it near $62–65k, against an all-time high of about $126k on 6 Oct 2025.
  - $10k would require a fall of about 85%; $1M is not reachable.
  - The Bitcoin triggers are effectively zero.
- **Taiwan: Nov 13.**
  - China held a large unannounced drill: 100+ navy and coast guard ships, three theater commands, and simulated strikes on Taiwanese cities (Star-Advertiser, 2026-11-13; IBTimes).
  - Xi's Sun Yat-sen speech called for *peaceful* reunification and did not mention force.
  - Trump and Xi are due to meet at APEC in Shenzhen the following week, their third meeting this year. That is a de-escalation signal.
- **Russia and NATO: Nov 11.** Stray drones from Ukrainian strikes on Russia crossed Lithuania, Latvia and Estonia, and NATO jets failed to shoot one down (Euronews, 2026-11-11).
  - Incursions in August, September and March followed the same pattern.
  - Nothing in these incidents resembles a Russian ground invasion.
- **Iran: Nov 9–10.**
  - Trump said the war is "militarily effectively over" and that new strikes are "quite unlikely" (CNBC, 2026-11-10; Business Standard, 2026-11-10).
  - The naval blockade of Iranian ports, in place since 13 Apr, continues, and limited US strikes on air defenses resumed in early November.
  - CENTCOM set up Task Force Iron Gate on 8 Nov to interdict Iran's land and Caspian supply routes. It is an interdiction role, not an invasion (Al Jazeera, 2026-11-08).
  - The Secretary of State reportedly saw "no need for military action" (INSS, Nov 8–15 report).
- **US Senate: Nov 3–4.** Democrats won control of the Senate in the midterms. They flipped Iowa, Maine, North Carolina and Ohio, and outlets give their total as at least 51 or 54 seats (Al Jazeera, 2026-11-04; Indiana Capital Chronicle, 2026-11-04).
  - The current Senate is 53–47 Republican, which is no supermajority, and the new Senate is seated in January 2027.
  - This trigger is effectively impossible.
- **Iran: Oct 16.** Trump said he would not use nuclear weapons or send ground troops to Iran (CNBC, 2026-10-16).
- **Greenland: Sep 18–24.**
  - Trump announced a deal to expand the US military presence while Greenland stays under Danish sovereignty. A security pact was signed at the UN on 22 Sep (CSMonitor, 2026-09-19; Chatham House, 2026-09-24).
  - In January at Davos, Trump had ruled out seizing Greenland by force.
  - Acquisition before 31 Dec is effectively nil.
- **Iran war timeline, earlier in 2026.**
  - US–Israeli strikes began in late February.
  - Ali Khamenei was killed. One source has Mojtaba named Supreme Leader on 8 Mar; another gives a June date, so the timeline is inconsistent.
  - The 31st MEU, about 2,500 Marines, arrived on 27 Mar for possible operations to seize Kharg, Abu Musa or Larak islands. I found no evidence any of these took place (The National, 2026-03-31; Quincy Institute).
  - The blockade began 13 Apr. A 14 Jun deal collapsed, and Trump declared the ceasefire over on 8 Jul (Business Standard, 2026-11-10).
- **Trump's health: May 2026.** A Walter Reed exam found him "excellent," with 30/30 on the MoCA cognitive test, mild leg swelling and statin use (Fox4/NBC, 2026-05-26). He turned 80 on 14 Jun 2026.
- **Earthquakes.** The largest 2026 event I found was M7.2 in Venezuela on 24 Jun (earthquaketracker.org, from USGS data). I found no M9.
- **Volcanoes and meteors.** I found nothing indicating a VEI 6+ eruption or a 250 kt+ fireball in 2026.

**Scheduled before the close:**
- APEC Shenzhen and the Trump–Xi meeting, late November
- Possible US–Iran talks; Qatar is mediating
- Congress stays at 53–47 Republican until 3 Jan 2027
- Nothing else scheduled bears on the triggers

## 4. Drivers and scenarios

**Paths to NO** (my rough 43-day estimates, for the forecasters to adjust):

1. **US "invades" Iran (~1–3%).** This is the largest single risk.
   - For: renewed buildup (3 carriers, about 53k troops), an Iranian missile rebuild, Hormuz still closed, and Iraq-basing rumors.
   - Against: Trump's repeated statements against ground troops (16 Oct, 9 Nov) and his "effectively over" framing.
   - Even if escalation comes, airstrikes probably would not count under the Venezuela precedent. A seizure of an island or the coast likely would.
2. **Iranian regime falls (~0.5–1%).** The regime is under severe economic strain (inflation, blockade) and repression-based stability is fragile, but it survived the decapitation strike. Collapse within six weeks is unlikely.
3. **Trump out (~0.7–1%).** Mostly the actuarial risk of death or incapacity. 25th Amendment and impeachment routes are negligible.
4. **Natural hazards combined (~1–1.2%).** Earthquake, volcano and meteor together.
5. **Xi out (~0.3%), China invades Taiwan (~0.2%), Russia invades NATO (~0.2%).**
   - Taiwan: December 2025 and November 2026 drills show capability, but the diplomatic calendar points to de-escalation. A blockade may not count as an "invasion."
   - Russia/NATO: drone incursions are not an invasion.
6. **Greenland, Bitcoin, Epstein, Senate supermajority (~0%).**

Taken together and treated as independent, these give roughly **3–6% total for NO**.

**Path to YES:** the status quo holds through noon ET on 31 Dec. That has been the pattern all year despite very large events.

## 5. Signposts

- **Toward NO, in rough order of impact:**
  - US forces landing on Iranian soil or islands
  - Reports of a 82nd Airborne or MEU tasking
  - Iraqi basing agreements
  - Collapse of Qatar-mediated talks
  - Major Iranian attacks on US assets
  - IRGC fracture or mass defections, or Mojtaba's incapacitation
  - Any credible report of a serious Trump health event (hospitalization)
  - PLA drills turning into a quarantine or blockade with a landing
  - Any M8.5+ foreshock-type activity (very weak signal)
- **Toward YES:**
  - A signed US–Iran deal or reopening of Hormuz
  - A cordial outcome from the Trump–Xi APEC meeting
  - Calm news through early December, since the hazard falls as the window closes

## 6. Uncertainties

- I could not read the exact rule text. Definitions of "invades," "regime falls," "out," "supermajority," and the exact market creation date are unconfirmed, and so is whether the window ends at 11:59 AM or PM ET.
- I could not confirm whether any trigger has been flagged or disputed, though the market appears open.
- The Iran war timeline is inconsistent across sources (date of Khamenei's death, the June deal), and I could not confirm whether any brief US ground raid has already happened and been ruled not to count.
- Senate seat totals vary between reports. This does not matter for resolution.
- The Bitcoin price on 18 Nov is not confirmed; the last data points are 13–15 Nov.
- Several of the fetched pages were blocked, so some details come from search summaries rather than full articles.

## Sources
- [Polymarket NEH 2026 rules PDF](https://polymarket-upload.s3.us-east-2.amazonaws.com/market_products/NEH/NEH+2026.pdf)
- [Polymarket Sparks Outrage, Settling $10.5M Venezuela Invasion Market as 'No' (DeFi Rate)](https://defirate.com/news/polymarket-sparks-outrage-settling-10-5m-venezuela-invasion-market-as-no/)
- [What's an invasion? (SAN)](https://san.com/cc/whats-an-invasion-gambling-sites-definition-costs-gamblers-millions/)
- [Polymarket backlash: Venezuela wasn't invaded (CasinoBeats)](https://casinobeats.com/2026/01/07/polymarket-backlash-venezuela-wasnt-invaded/)
- [US deploys 3 aircraft carriers, 53,000 troops (Organiser)](https://organiser.org/2026/11/17/426958/international/us-deploys-3-aircraft-carriers-53000-troops-amid-iran-rebuilds-missile-arsenal-gulf-sees-biggest-buildup-since-2003/)
- [USS Roosevelt arrives in Middle East (Al Jazeera)](https://www.aljazeera.com/news/2026/11/16/uss-roosevelt-arrives-in-middle-east-is-the-us-iran-war-about-to-resume)
- [INSS US Force Posture Nov 8–15, 2026](https://www.inss.org.il/publication/us-forces-november-8-15/)
- [INSS US Force Posture Nov 1–7, 2026](https://www.inss.org.il/publication/us-forces-november-1-7/)
- [US launches task force to disrupt Iran's land-based supply routes (Al Jazeera)](https://www.aljazeera.com/news/2026/11/8/us-launches-task-force-to-disrupt-irans-land-based-supply-routes)
- [Trump says Iran war to end 'fairly soon' (CNBC)](https://www.cnbc.com/2026/11/10/trump-iran-war-hormuz-.html)
- [Trump says Iran war is 'effectively over': How the conflict unfolded (Business Standard)](https://www.business-standard.com/world-news/trump-says-iran-war-is-effectively-over-how-the-conflict-unfolded-126111000144_1.html)
- [Trump says he won't use nuclear weapons or send ground troops to Iran (CNBC)](https://www.cnbc.com/2026/10/16/us-iran-war-trump-hormuz.html)
- [Blinken Warns on Iran (Kantan News)](https://kantan.news/news/blinken-warns-on-iran-us-ground-operation-would-be-a-total-disaster)
- [Live updates: Pentagon options for Kharg Island (The National)](https://www.thenationalnews.com/news/mena/2026/03/31/pentagon-options-for-kharg-island-and-unlocking-hormuz)
- [Limited US ground operations in Iran (Quincy Institute)](https://quincyinst.org/research/limited-us-ground-operations-in-iran-will-not-shift-the-wars-balance)
- [Iran Regime Change 2026 – Scenarios (GlobalSecurity)](https://www.globalsecurity.org/military/world/iran/regime-change-2026-03.htm)
- [Iran's uncertain transition (Stimson)](https://www.stimson.org/2026/irans-uncertain-transition-from-the-streets-to-a-strongman-2/)
- [Democratic Party wins US Senate in 2026 midterms (Al Jazeera)](https://aljazeera.com/news/2026/11/4/democratic-party-flips-us-senate-in-2026-midterm-elections)
- [Democrats score control of US Senate (Indiana Capital Chronicle)](https://indianacapitalchronicle.com/2026/11/04/repub/democrats-score-control-of-us-senate-in-stunning-midterm-victory/)
- [Price of bitcoin 11/13/2026 (Fortune)](https://fortune.com/article/price-of-bitcoin-11-13-2026/)
- [Why bitcoin is falling today (Motley Fool)](https://www.fool.com/investing/2026/11/13/why-bitcoin-is-falling-today/)
- [Earthquakes on June 24, 2026 (earthquaketracker.org)](https://www.earthquaketracker.org/earthquakes/today/2026-06-24)
- [Trump in 'excellent health' after annual physical (Fox4)](https://www.fox4news.com/news/trump-excellent-health-annual-physical)
- [China stages unannounced Pacific drills (Star-Advertiser)](https://www.staradvertiser.com/2026/11/13/breaking-news/china-stages-unannounced-pacific-drills-in-intimidation-of-taiwan/)
- [China quietly mobilizes over 100 warships (IBTimes)](https://www.ibtimes.com/china-unannounced-naval-deployment-taiwan-blockade-3809720)
- [A restless night in the Baltics (Euronews)](https://www.euronews.com/2026/11/11/a-restless-and-difficult-night-in-the-baltics-as-nato-fighter-jets-fail-to-shoot-down-dron)
- [Denmark's leaders cautiously optimistic on Trump's Greenland deal (CSMonitor)](https://www.csmonitor.com/World/2026/0919/Denmark-s-leaders-express-cautious-optimism-on-Trump-s-Greenland-deal)
- [Denmark's Greenland deal with Trump (Chatham House)](https://www.chathamhouse.org/2026/09/denmarks-greenland-deal-trump-victory-diplomacy-over-bullying)