## Research brief: Will Waymo run public, paid, driverless ride-hailing in Las Vegas, NV before Jan 1, 2027?

**Bottom line:** Waymo already runs paid, fully driverless rides in Las Vegas, but only for invited riders. As of Nov 24, 2026 the service is still invite-only. The question turns almost entirely on one thing: does Waymo open Las Vegas to everyone in the next ~37 days?

### 1. Resolution mechanics

- **What YES needs:** Before Jan 1, 2027, any member of the public must be able to download the Waymo app (or a partner app), request a paid ride with pickup and dropoff inside Las Vegas, NV, and get a fully driverless ride at least some of the time.
- **What rules it out:** Invite codes, waitlist approval, testing programs, safety-driver-only service, or only an announcement.
- **Already met today:**
  - Rides are paid and fully driverless (Ojai minivans) since Sep 14, 2026 (TechCrunch, Sep 14, 2026; 8 News Now, Sep 2026).
  - Coverage may be limited to part of the city.
- **Not met as of the latest sources (late Oct to mid Nov 2026):** open access.
  - Waymo said at launch it would "steadily give access to more Waymo riders in Clark County, as we work toward opening our service to everyone" (Waymo blog "Vegas, Deal Us In!", Sep 14, 2026).
  - Its Oct 21 airport post says it will "gradually welcome more riders over time before opening to everyone" (Waymo blog, Oct 21, 2026).
  - KSNV reports riders need approval, with a waitlist of about 100,000 (News 3 LV, Sep 2026).
- **Who decides:** The question doesn't name a resolver. In practice, look for a Waymo blog or Help Center post saying "now available to everyone in Las Vegas." That is how Waymo announced it in other cities (Waymo Help, Oct 14, 2026).
- **Edge cases:**
  1. **City limits.** The launch area (the Strip south of Sahara Ave/SR-589, Allegiant Stadium, Chinatown, UNLV, Spring Valley) is almost entirely in unincorporated Clark County (Paradise/Spring Valley), not the City of Las Vegas. Waymo also describes the market as "Clark County." A tracker reports a Nov 6 expansion to about 47 sq mi that includes Downtown/Fremont Street and the Arts District, which are inside city limits (Robotaxi Tracker/X, Nov 2026; Cybercab Collective, Nov 6, 2026). That isn't confirmed by Waymo. A strict reader would need the downtown area to be included, but most resolvers will probably treat "Las Vegas" as the metro area.
  2. **Partial opening.** Waymo might open the core area to all while keeping the airport or new zones limited. The rules allow geographic limits, so a general opening should count.
  3. **No partner app.** No Uber or Lyft deal has been reported for Las Vegas, so the Waymo app is the only route.

### 2. Reference classes and base rates

**A. Waymo's 2026 launches: days from first invited riders to "open to everyone."** I built this from dated reports. Las Vegas reaches Dec 31 at day 108 and is at day 71 today with no opening.

| City | Invites began | Opened to all | Days |
|---|---|---|---|
| Tampa | Sep 1 | Oct 14 | 43 |
| San Diego | Sep 1 | Oct 14 | 43 |
| Orlando | Feb 24 | Apr 15 | ~50 |
| Nashville | Apr 7 | Jun 25 | 79 |
| Miami | Jan 22 | Apr 15 | 83 |
| Dallas | Feb 24 | Aug 4 | ~161 |
| Houston | Feb 24 | Aug 20 | ~177 |
| San Antonio | Feb 24 | Oct 14 | ~232 |
| Denver | Sep 1 | unclear | ≥84 if still waitlisted |

Sources: Electrive, Apr 16, 2026; WSVN; Waymo Nashville blog, Jun 2026; Axios Nashville, Apr 7, 2026; Robotaxi Atlas; Waymo Help "available to everyone in Tampa, San Diego, and San Antonio," Oct 14, 2026.

- **Unconditional rate:** 5 of 8 cities with known dates opened within 108 days (~60%).
- **Conditional rate (more relevant):** Of the cities still closed at day 71, 2 opened by day 108 (Nashville, Miami) and 3 did not (Dallas, Houston, San Antonio). That is ~40%, from a very small sample.

**B. Earlier Waymo markets (Phoenix, SF, LA).** Waitlists in these cities lasted many months to years (SF ended its waitlist in mid-2024; LA took about 8 months). That points toward NO, but these predate the much faster 2026 playbook, so they deserve little weight.

**C. Waymo's announcement rhythm.** Waymo tends to open several cities at once: Miami and Orlando on Apr 15, then Tampa, San Diego and San Antonio on Oct 14. Las Vegas and Denver, both launched in September, look like natural candidates for the next batch. The gap between the April and October batches was 6 months, though Dallas and Houston opened on their own in August. Batch timing could fall either side of Dec 31.

### 3. Current state of the world (most recent first)

- **Nov 6, 2026:** Waymo's Help Center map reportedly now shades Downtown Las Vegas. Trackers say the area roughly doubled from about 23–24 to about 47 sq mi, including the Arts District. The Help Center still describes gradual rider access and gives no date to open to all. I couldn't find a Waymo press release (Cybercab Collective, Nov 6, 2026; Robotaxi Tracker/X).
- **Oct 2026 (third-party trackers):** Las Vegas and Denver are listed as the only Waymo metros still on waitlist or rolling invites; the other 13 are open to all (Robotaxi Atlas, checked about Oct 13; Codeload, Nov 2026; Driverless Rider, Oct 2026). Driverless Rider says Denver is now open to everyone, but this conflicts with the other trackers.
- **Oct 21, 2026:** Airport rides began at Harry Reid International (Terminals 1 and 3), for existing Las Vegas riders only, "before opening to everyone." There is no freeway service (TechCrunch, Oct 21, 2026; Las Vegas Review-Journal; Motorbiscuit).
- **Oct 14, 2026:** Tampa, San Diego and San Antonio opened to all. Tampa and San Diego took 43 days from launch (Waymo Help, Oct 14, 2026).
- **Sep 14, 2026:** Las Vegas launch with "dozens" of Ojai minivans, about 24 sq mi, paid rides, rolling invites. More than 100,000 people had expressed interest beforehand (TechCrunch, Sep 14, 2026; Fox5, Sep 14, 2026; News 3 LV).
- **Aug 2026:** The Nevada Transportation Authority approved a fleet of up to 1,000 vehicles (Fox5/Review-Journal, Sep 2026). Fleet size is not a regulatory constraint.
- **Competitors:**
  - Zoox already runs a public service in Las Vegas and has expanded to Downtown.
  - Tesla and Motional are preparing launches; a commentator expects Tesla by year-end (Robotaxi Radar/X).
  - Competition could push Waymo to open sooner.
- **No adverse events found:** I found no reported Waymo crash, pause or regulatory action in Las Vegas. Some Las Vegas Sun complaints concerned other companies' robotaxis (Las Vegas Sun, Sep 21, 2026).
- **Scheduled events:**
  - Holiday travel season through December.
  - New Year's Eve on the Strip (heavy road closures).
  - CES 2027 in Las Vegas, about Jan 5–8, 2027, which is **just after** the deadline.

### 4. Drivers and scenarios

**Paths to YES (open to all by Dec 31):**
1. **The expansion signals scale-up.** Doubling the area on Nov 6 suggests the fleet has grown. In Tampa and San Diego, opening to all came about 6 weeks after launch, and Miami opened alongside an expansion.
2. **A batch announcement in December** opens Las Vegas (and Denver) together. This depends on fleet size against demand: with more than 100,000 interested in a tourist city, Waymo needs enough cars to keep wait times acceptable.
3. **Competition with Zoox and an expected Tesla launch** pushes Waymo to open before peak holiday and CES traffic.

**Paths to NO:**
1. **Demand is far above supply.** Tourist demand from millions of visitors, plus a large waitlist, means a "dozens to low hundreds" fleet could be overwhelmed. This looks like the slower Texas pattern (161–232 days).
2. **Timing around CES.** Waymo may prefer to open publicly to coincide with CES (Jan 5–8, 2027), just after the deadline. This is speculative but plausible.
3. **Operational caution.** Waymo may avoid opening up during New Year's Eve and peak events, or a safety incident could slow the rollout.
4. **Strict city-limits reading.** If downtown coverage isn't real or isn't counted, the core area isn't legally "Las Vegas." This is a low-probability risk.

### 5. Signposts

**Toward YES:**
- A Waymo blog or Help Center post saying "now available to everyone in Las Vegas." This would be decisive.
- Denver opening to all, which would signal a batch.
- Trackers relabeling Las Vegas as "open."
- Reports of freeway rides or airport rides opened to all.
- Fleet-size announcements (hundreds of vehicles).

**Toward NO:**
- Waymo statements pointing to "early 2027" or CES for opening.
- Reports of long waits or limited supply.
- Any safety incident, recall or NTA scrutiny.
- No announcement by about Dec 20. Waymo announcements often fall mid-week, and holiday weeks are less likely.

### 6. Uncertainties

- I couldn't open Waymo's Help Center or blog directly (fetches were blocked). Status after about Nov 6 rests on search snippets and third-party trackers.
- Denver's status conflicts across sources, which affects both the batch inference and the base rate.
- The Nov 6 expansion to Downtown and about 47 sq mi comes from trackers, not an official Waymo statement.
- Current Las Vegas fleet size and invite pace are unknown.
- How the resolver treats "within Las Vegas, NV" versus unincorporated Clark County is unknown.
- Waymo's internal criteria for opening to all (wait-time thresholds, fleet ratios) aren't public.

## Sources
- [Waymo opens robotaxi service in Las Vegas (TechCrunch, Sep 14, 2026)](https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/)
- [Waymo launches robotaxi service in Las Vegas (Fox5, Sep 14, 2026)](https://www.fox5vegas.com/2026/09/14/waymo-launches-robotaxi-service-las-vegas/)
- [Waymo officially launches fully autonomous rides in Las Vegas (8 News Now)](https://www.8newsnow.com/news/local-news/waymo-officially-launches-fully-autonomous-rides-in-las-vegas/)
- [Waymo launches self-driving rides in Las Vegas, covering 24 square miles (News 3 LV)](https://news3lv.com/news/local/waymo-launches-self-driving-rides-in-las-vegas-covering-24-square-miles)
- [Vegas, Deal Us In! We're welcoming riders today (Waymo blog, Sep 2026)](https://community.waymo.com/blog/2026/09/ride-in-las-vegas/)
- [October 21, 2026 – Las Vegas airport (Waymo blog)](https://waymo.com/blog/shorts/las-airport/)
- [Waymo starts offering rides at the Las Vegas airport (TechCrunch, Oct 21, 2026)](https://techcrunch.com/2026/10/21/waymo-starts-offering-rides-at-the-las-vegas-airport/)
- [Waymo robotaxis greenlighted to provide rides at Reid airport (Review-Journal)](https://www.reviewjournal.com/local/traffic/waymo-begins-reid-airport-rides-in-las-vegas-3903138/)
- [Waymo Robotaxis Now Pick Up at the Las Vegas Airport—but Not Everyone Can Ride Yet (Motorbiscuit)](https://www.motorbiscuit.com/waymo-robotaxis-now-pick-up-at-the-las-vegas-airport-but-not-everyone-can-ride-yet/)
- [Waymo's Las Vegas Service Map Now Includes Downtown (Cybercab Collective, Nov 6, 2026)](https://cybercabcollective.com/news/waymo-las-vegas-service-map-downtown-expansion)
- [Robotaxi Radar on X – 47 sq mi Waymo Vegas area](https://x.com/RobotaxiRadar/status/2118841249138643258)
- [Waymo's driverless cars learn to navigate Las Vegas traffic (Las Vegas Sun, Sep 21, 2026)](https://lasvegassun.com/news/2026/sep/21/the-machine-at-the-wheel-learns-to-maneuver-las-ve/)
- [Waymo: every city, status and how to ride (Robotaxi Atlas)](https://www.robotaxiatlas.com/operators/waymo/)
- [Waymo Cities List (Oct 2026) (Driverless Rider)](https://www.driverlessrider.com/waymo-cities/)
- [Waymo Promo & Invite Code November 2026 (Codeload)](https://codeload.com/for/waymo)
- [Waymo is now available to everyone in Tampa, San Diego, and San Antonio (Waymo Help, Oct 14, 2026)](https://support.google.com/waymo/answer/18765688?hl=en)
- [Waymo Help announcements](https://support.google.com/waymo/announcements/12766613?hl=en)
- [Waymo opens in Miami and Orlando for all customers (Electrive, Apr 16, 2026)](https://www.electrive.com/2026/04/16/waymo-opens-in-miami-and-orlando-for-all-customers/)
- [Waymo opens driverless rides to everyone in Miami (WSVN)](https://wsvn.com/news/local/miami-dade/waymo-opens-driverless-rides-to-everyone-in-miami-adds-highway-access/)
- [Waymo launches driverless car service in Dallas (Axios, Feb 24, 2026)](https://www.axios.com/local/dallas/2026/02/24/waymo-driverless-cars-dallas)
- [Waymo launches autonomous car rides in Nashville (Axios, Apr 7, 2026)](https://www.axios.com/local/nashville/2026/04/07/waymo-launches-autonomous-car-rides-nashville)
- [Nashville June 2026 (Waymo blog)](https://blog.waymo.com/blog/shorts/nashville-june2026/)
- [Waymo officially launches in Denver (Axios, Sep 1, 2026)](https://www.axios.com/local/denver/2026/09/01/waymo-launches-denver)
- [Waymo self-driving taxis are open to the Denver public ... kind of (Westword)](https://www.westword.com/news/waymo-self-driving-taxis-launch-denver-kind-of-40929588/)
- [Waymo in Denver: Everything to know (Denver Gazette, Sep 1, 2026)](https://www.denvergazette.com/2026/09/01/waymo-in-denver-everything-you-need-to-know-about-the-self-driving-car-service/)