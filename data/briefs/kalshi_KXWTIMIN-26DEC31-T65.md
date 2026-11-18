# Research brief: Will the WTI front-month settle fall to $64.99 or below by Dec 31, 2026?

**Bottom line:** WTI's front month settled at about $86 on Nov 17. To resolve YES it has to settle below $65 in the next 30 or so trading days, a drop of roughly 22–25%. That level is also below the market's own price for oil in 2027–28 and below the pre-war price of about $67. The one big caveat is the Issuance date (section 1). If the market was issued in January or February 2026, YES may already have happened.

**Sourcing note:** Every attempt to open a full article (WebFetch) was refused by the network proxy. All facts below come from search-result summaries, which sometimes disagreed with each other. Treat exact settle prices as ±$1 and check them against CME/ICE data if precision matters.

---

## 1. Resolution mechanics

- **What counts as YES:** any daily WTI front-month settlement price below $65.00 ("64.99 or below"), counted from the market's Issuance date through Dec 31, 2026, as reported by ICE.
- **Settlements only:** only official daily settles count. A dip below $65 during the trading day that recovers by the settle does not count.
- **Front-month rolls:** under the standard rule, a CL contract stops trading 3 business days before the 25th of the month before delivery. The dates below are my calculation, not checked against an exchange calendar:
  - The December 2026 contract (CLZ26), whose settles were about $85–86 on Nov 16–17, should expire around Fri **Nov 20, 2026**.
  - The January 2027 contract (about $83.83 on Nov 16) then becomes the front month until about **Dec 21**, because Dec 25 is a Friday holiday.
  - The February 2027 contract is the front month for roughly the last week of December.
  - The curve is in backwardation (later months cheaper), so each roll mechanically lowers the front-month price by about $1–1.5. That slightly helps YES.
- **Ambiguity: the Issuance date is not given.**
  - WTI settled at $67 on Feb 27, 2026, just before the war (CNN, Apr 7, 2026).
  - From memory, and not confirmed by search, WTI traded around the high $50s to low $60s in late 2025 and early 2026.
  - So if Issuance was in early 2026, the condition may already be met. If the market is still open and unresolved, Issuance was probably after the war began (about Mar 1, 2026). WTI has not settled below $65 at any point since then. The June 2026 low was around $80 (see section 3).
- **Ambiguity: "ICE reports" vs NYMEX.** The standard front-month contract is NYMEX CL, run by CME. ICE also lists a WTI contract that settles almost identically, so the difference should not matter.
- **Timing:** the market closes Dec 31, 2026 at 19:30 UTC. The Dec 31 settle comes at about 14:30 ET (19:30 UTC), so it should count.

## 2. Reference classes and base rates

**A. Big drops in WTI over about 6 weeks (unconditional).** A fall of at least 22–25% in about 30 trading days is rare. Episodes I know of:
- late 1985–86 (Saudi price war)
- Jan 17, 1991: Desert Storm, a one-day drop of about 33% as the war premium collapsed
- Oct–Nov 2008
- Nov–Dec 2014: the OPEC decision not to cut, roughly $75 to $55
- Mar–Apr 2020 (COVID)
- Jun–Jul 2022: roughly $120 to $90

That is about 6–8 episodes in 40 years. Taking each episode's overlapping windows into account, a rough estimate is that **about 2–5% of all 30-trading-day windows** saw a peak-to-trough fall of 25% or more. This is my estimate, not a computed statistic.

**B. Collapse of a war premium when the conflict ends.**
- 1991: crude gave up most of its war premium within days once the outcome was clear.
- 2026 precedents in this conflict:
  - The Apr 7 ceasefire cut WTI 16.4% in one day, but only to $94.41 (CNN, Apr 7, 2026).
  - The June interim deal took WTI to its lowest since Mar 4, around $80 (Yahoo/Business Standard, ~Jun 18, 2026).

  So even the two biggest de-escalation events of 2026 left WTI $13–15 above $65. They did not push it below the pre-war $67. In this class, a de-escalation shock is needed but has not historically been enough on its own to reach $65 in one step.

**C. Simple option-style calculation (my own arithmetic).** I treated the chance of touching $65 as the probability that a random-walk price path crosses a fixed level. Inputs: effective start of about $84 (the January contract), barrier $65, about 0.12 years left, and an assumed annualised volatility (OVX). The most recent OVX reading I found for this period is a model estimate of about 90–100 (V-Lab, Nov 5, 2026); I found no published November close.

| Assumed volatility | Chance of touching $65 |
|---|---|
| 40% | ~7% |
| 50% | ~14% |
| 60% | ~22% |

These numbers probably **overstate** the chance, for three reasons:
- Volatility during a supply crisis is skewed upward (spikes up, not down).
- Daily settles cross less often than a continuous price path would.
- $65 is below the entire forward curve out to 2028 (see section 3).

## 3. Current state of the world (most recent first)

- **Nov 18, 2026:** oil slipped in Asian trading; one report puts WTI around $85 (Gulf News, Nov 18, 2026).
- **Nov 17:**
  - WTI settled at about **$86.01**, up $0.29.
  - It had traded as low as about $83.50 during the day, its lowest since Nov 10, before tanker attacks in the Gulf lifted it.
  - WTI is down about 16% so far in November (FXStreet, Nov 17; settlement reports, Nov 17).
  - US emergency crude reserves (SPR) are at 276.4M bbl, the lowest since 1982.
- **Nov 16–17, tankers:**
  - Iran's IRGC says two tankers hit mines on a southern route it deems "unauthorised", and a third caught fire.
  - UKMTO, the UK maritime agency, logged two attacks.
  - Trackers say the Strait of Hormuz has been "closed" for about day 257–261 (Al Jazeera, Nov 17; straits.live, Nov 18).
  - One analyst says US Navy escorts have brought exports close to pre-war levels. This is disputed.
- **Nov 16:**
  - The December contract settled at **$85.06** (−$3.50, −4.1%) and January 2027 at **$83.83**.
  - The curve is in firm backwardation into early 2027. The market is moving from worries about shortage to worries about surplus (CMB News, Nov 17).
  - Late September data had January 2028 at about $73.
- **Nov 15–16, Goldman Sachs:**
  - Sees a "sizeable" 2027 surplus of about 2 mb/d.
  - WTI forecast to average $78 in 2027 and reach about $70 by end-2027; Brent $78 by end-2027.
  - Flags near-term **upside** risk from shipping attacks (Bloomberg, Nov 16; Zawya/EnergyNow, Nov 2026).
  - An earlier Goldman forecast had December 2026 WTI at about $80–81.
- **Nov 13, IEA November Oil Market Report:**
  - Supply exceeded demand for the first time since the war began.
  - October supply was 105.4 mb/d (+2.3 mb/d month on month), and inventories rose by 52M bbl.
  - The market returns to surplus in Q4 2026, with a larger build in 2027.
  - 2026 demand is about 102.3 mb/d, down 2.7 mb/d (Times of Oman / Egypt Oil & Gas, Nov 13, 2026).
- **Nov 9–10:**
  - Trump said the Iran war was "effectively over" militarily but forces were "locked and loaded."
  - Qatar relayed an Iranian two-day plan that would reopen Hormuz on day 2.
  - Iran denied talks and listed 7 conditions for reopening.
  - The December contract settled at $86.85, then the lowest since Aug 31 (Al Jazeera Nov 9; Euronews/CNBC Nov 10; 24/7 Wall St, Nov 10).
  - Republicans lost both chambers in the midterms, and the administration's war rhetoric has softened.
- **Nov 1:** OPEC+ kept December targets unchanged. It will set its 2027 production framework at a meeting around **Nov 29** (Star-Advertiser/Reuters, Nov 1, 2026). The war has delayed its capacity review.
- **Earlier 2026 path:**
  - Feb 27 settle $67, then the war began.
  - April ceasefire: WTI $94.41.
  - June interim deal: about $80, the low since the war began.
  - Late July: $82.61.
  - October peak: Brent above $100.

**Scheduled before Dec 31:**
- Dec contract expiry about Nov 20
- OPEC+ ministerial about Nov 29–30
- Weekly EIA inventory reports
- IEA December report (about Dec 11), plus OPEC and EIA monthly outlooks
- January contract expiry about Dec 21
- Thin holiday trading in the last week of December

## 4. Drivers and scenarios

**Paths to YES (front month below $65):**
1. **A full, verified peace deal with Hormuz reopened quickly, plus a visible glut.** Tankers move freely, insurance normalises, and Iranian barrels return. Add the IEA's Q4 surplus and rising inventories, and the remaining war premium (WTI vs pre-war ≈ +$19) could collapse. Even so, the June precedent stalled at about $80. Reaching below $65 needs an overshoot below the pre-war price and below the 2028 forward price.
2. **An OPEC+ price war or market-share push at the Nov 29 meeting.** For example, Gulf producers ramp up to recapture share once Hormuz reopens, a 2014-style shock.
3. **A macro demand shock.** A sharp recession or risk-off move, worsened by surplus headlines and thin December liquidity.
4. **Roll effects.** About $2–3 of backwardation over two rolls lowers the bar a little.

**Paths to NO:**
- The Hormuz standoff continues, with mines and tanker strikes adding risk premium.
- A deal is reached but reopening is gradual.
- SPR refill demand: the SPR is at a 1982 low, which gives a policy buyer on dips.
- Diesel tightness.
- The forward curve sits above $70 through 2028.
- Goldman's base case has WTI around $78–80 in December.
- Simply too little time: about 6 weeks.

## 5. Signposts

**Would raise the chance of YES (large moves):**
- A signed US–Iran agreement with a firm Hormuz reopening date, or mine-clearing and escorts confirmed with traffic back at about 20 mb/d.
- WTI settling below about $78, then below $72. Each step greatly raises the odds of reaching $65.
- An OPEC+ decision on about Nov 29 to unwind cuts or raise 2027 quotas sharply.
- EIA weekly inventory builds plus a steepening contango in the front spreads (front month cheaper than later months).
- Bank forecast cuts to the $60s.
- OVX staying above 60 while prices fall.

**Would lower the chance of YES:**
- More tanker or mine strikes.
- Collapse of the Qatar-mediated talks, or renewed US strikes.
- Announcements of SPR refill purchases.
- OPEC+ holding output flat or cutting.
- WTI rebounding above $90.

## 6. Uncertainties

- **Issuance date (the most important unknown).** If it was before about March 2026, early-2026 settles may already resolve YES; I could not verify WTI's January–February 2026 settles.
- **Exact recent settles.** Sources conflict (for example, Gulf News quoted $85.06 on Nov 18, which matches the Nov 16 settle). I could not read primary CME/ICE data.
- **Current implied volatility.** I found no published November 2026 OVX close.
- **Actual Hormuz flows.** Accounts range from "effectively closed" to "near pre-war levels via US escort."
- **The full forward curve.** I don't have the current Dec 2027 or 2028 levels as of mid-November; the latest Jan 2028 figure is about $73 from late September.
- **OPEC+.** Whether the meeting is on Nov 29 or 30, and what members want on 2027 quotas.

## Sources
- [Oil Prices Drop as Crude Benchmarks Slide on November 18, 2026 (Gulf News)](https://gulfnews.com/business/energy/oil-slips-in-asia-led-by-murban-brent-wti-what-to-know-on-nov-18-2026-1.500751476)
- [Gulf attacks lift Crude Oil, but most of Monday's drop stays (FXStreet, Nov 17, 2026)](https://www.fxstreet.com/news/gulf-attacks-lift-crude-oil-but-most-of-mondays-drop-stays-202611171916)
- [Crude Oil Market Analysis: Futures Curve, Surplus Signals and Diesel Weakness (CMB News)](https://commodity-board.com/crude-oil-futures-slide-as-market-shifts-from-tightness-to-emerging-surplus)
- [Oil Prices Fall for Second Straight Week… WTI Closes at $88.56 (EnergyNow, Nov 2026)](https://energynow.com/2026/11/oil-prices-fall-for-second-straight-week-as-global-supply-surplus-emerges-wti-closes-at-88-56-brent-at-95-84/)
- [Goldman Sachs Predicts 'Sizeable Surplus' for Oil Market in 2027 (Bloomberg, Nov 16, 2026)](https://www.bloomberg.com/news/articles/2026-11-16/goldman-sachs-predicts-sizeable-surplus-for-oil-market-in-2027?srnd=phx-india)
- [Goldman sees Brent easing to $78 a barrel by end-2027 (Zawya)](https://www.zawya.com/en/business/goldman-sees-brent-easing-to-78-a-barrel-by-end-2027-as-markets-adapt-2277950)
- [Goldman warns of sizable 2027 oil surplus (Crypto Briefing)](https://cryptobriefing.com/goldman-warns-of-sizable-2027-oil-surplus-prices-may-fall/)
- [Global oil market to return to surplus in Q4 2026 (Times of Oman)](https://timesofoman.com/article/179134-global-oil-market-to-return-to-surplus-in-q4-2026-larger-supply-build-expected-in-2027-iea)
- [IEA Sees Global Oil Market Returning to Surplus in 4Q26 (Egypt Oil & Gas)](https://egyptoil-gas.com/news/iea-sees-global-oil-market-returning-to-surplus-in-4q-26-as-supply-recovers/)
- [Oil Market Report – November 2026 (IEA)](https://iea.org/reports/oil-market-report-november-2026)
- [Tankers hit in Strait of Hormuz… (Al Jazeera, Nov 17, 2026)](https://www.aljazeera.com/news/2026/11/17/tankers-hit-in-strait-of-hormuz-as-drone-raises-alarm-at-iraq-gas-field)
- [Strait of Hormuz News, November 18, 2026 (straits.live)](https://straits.live/briefs/2026-11-18)
- [Trump calls Iran war 'effectively over' after talks with Qatar PM (Al Jazeera, Nov 9, 2026)](https://www.aljazeera.com/news/2026/11/9/trump-calls-iran-war-effectively-over-after-talks-with-qatar-pm)
- [Trump says Iran war 'effectively over' as Tehran denies planned talks (Euronews, Nov 10, 2026)](https://www.euronews.com/2026/11/10/trump-says-iran-war-effectively-over-as-tehran-denies-planned-talks)
- [Trump says Iran war to end 'fairly soon' (CNBC, Nov 10, 2026)](https://www.cnbc.com/2026/11/10/trump-iran-war-hormuz-.html)
- [Iran Denies US Talks, Hormuz Closed Until 7 Conditions Met (House of Saud)](https://houseofsaud.com/iran-rejects-trump-war-over-hormuz)
- [Oil Prices Just Fell to Their Lowest Since August… (24/7 Wall St, Nov 10, 2026)](https://247wallst.com/investing/2026/11/10/oil-prices-just-fell-to-their-lowest-since-august-as-trump-says-the-iran-war-is-effectively-over/)
- [Oil plunges… after US-Iran ceasefire (CNN, Apr 7, 2026)](https://www.cnn.com/2026/04/07/markets/us-stocks-oil-trump-iran-ceasefire)
- [Oil prices fall to lowest after ceasefire deal, touch pre-Iran war level (Business Standard, ~Jun 18, 2026)](https://www.business-standard.com/world-news/oil-fall-to-lowest-after-ceasefire-deal-touches-pre-iran-war-prices-126061801403_1.html)
- [Oil prices settle at lowest in over a week, as US pauses attacks on Iran (Yahoo Finance)](https://finance.yahoo.com/energy/articles/oil-slips-more-5-us-221044741.html)
- [OPEC+ keeps December oil output targets steady amid Iran war (Star-Advertiser, Nov 1, 2026)](https://www.staradvertiser.com/2026/11/01/breaking-news/opec-keeps-december-oil-output-targets-steady-as-iran-war-disrupt-flows/)
- [CBOE Crude Oil Volatility Index GARCH analysis (NYU V-Lab)](https://vlab.stern.nyu.edu/volatility/VOL.OVX%3AVIND-R.S0GARCH)