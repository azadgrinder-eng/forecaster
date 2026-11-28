# Research brief: Will Josh Shapiro's 2028 Democratic nomination odds on PredictionMarketOdds.com reach 8% by December 31, 2026?

## 1. Resolution mechanics

- **What counts as YES:** Shapiro's hourly "Odds of Happening" value in the "2028 Democratic Nomination" listing on PredictionMarketOdds.com must be **8.0% or higher for 4 consecutive published hourly values**. Every one of those hours must fall between market creation and January 1, 2027, 12:00 AM ET (04:59 UTC close). Values are compared at the site's published precision of 0.1%, so 7.9% does not count and 8.0% does.
- **What ends a run:** any published hour below 8.0%. Hours marked "NO_PRINT" are skipped. They neither count toward a run nor break it, so a run can stretch across data gaps.
- **Time left:** from November 28 to December 31 is about 33 days, roughly 790 hourly values. A single sustained 4-hour excursion is enough. Brief one- or two-hour spikes, for example from one thin trade feeding the aggregate, do not qualify.
- **Who decides:** PredictionMarketOdds.com's listing page and Shapiro's detail-page "Odds History" graph. Prices on individual markets such as Polymarket or Kalshi do not count, even if they show Shapiro above 8%.
- **Edge cases:**
  - Clearly erroneous values (technical errors) can be corrected within 48 hours, and the corrected value is used.
  - If Shapiro is removed from the listing or publishing stops, the market resolves on the data published up to then.
  - If the underlying market is "officially decided" early, the market resolves YES only if Shapiro is the nominee. That cannot realistically happen before 2028.
- **Unknowns about the site:** I could not find any methodology page for PredictionMarketOdds.com. I don't know which venues it aggregates, how it weights them, or whether it uses midpoint or last trade. Those choices decide how noisy the hourly series is, and therefore how likely a 4-hour excursion is.
- **Price not checked:** As instructed, I did not look at Shapiro's current value on the site or on any market. The forecaster needs to establish his current level independently. Markets like this are usually created with a threshold somewhat above the prevailing price, so the gap to 8% is the most important number to pin down.

## 2. Reference classes and base rates

1. **Threshold markets on long-dated nomination odds over about one month.** Odds for a nomination roughly 18 months away usually drift slowly in non-election months. The big moves come at discrete catalysts: formal announcements, dropouts, scandals, viral moments. The relevant quantity is the gap between Shapiro's current value and 8%:
   - Gap of about 1 point or less: a 4-hour touch within 33 days is fairly common, because of normal noise.
   - Gap of 2–3 points or more: it usually takes a real catalyst.
   
   I could not build a quantitative frequency table for this. That is a gap the forecaster should weigh.

2. **The 2020 cycle (comparable post-midterm window, Nov–Dec 2018).** The main early-cycle moves came from announcements and media surges:
   - Beto O'Rourke rose after his November 2018 Senate loss.
   - Kamala Harris rose around her January 2019 launch.
   
   Most second-tier governors and senators moved little in December. That suggests a December catalyst for Shapiro is possible but not the default. Note this is a qualitative comparison, not computed odds.

3. **Shapiro's polling level as an anchor.** He polls 3–6% nationally and is usually about 7th:
   - Emerson: 5%, 7th place (date uncertain, about 4 months old).
   - Strength In Numbers/Verasight, November 2026: 4%.
   - Summer 2026 polls: 5%.
   
   Nomination markets often price electability-signalling swing-state governors above their name-ID-driven primary polling. So polling alone does not pin down where he sits relative to 8%. Polling has also been stable, with no recent surge.

## 3. Current state of the world (most recent first)

- **Nov 25–27, 2026:** In a Wall Street Journal interview, Shapiro called Netanyahu a "failed leader" and faulted both Biden and Trump for not restraining him on Gaza. Reports say he backed ending US military aid to Israel in a separate PBS interview. Coverage frames this as 2028 groundwork, and in particular as repairing his standing with the progressive base on his main vulnerability (Israel Hayom, Nov 25; Haaretz, Nov 26; JPost; Wisevoter, Nov 27). This is a shift from April 2026, when he supported aid but wanted it used as leverage (Jewish Insider, Apr 2026). How progressives and pro-Israel donors react is still unclear.
- **Nov 27, 2026:** He signed a prevailing-wage expansion bill (SB 908). This is routine governance (Bradford Era, Nov 27).
- **Mid-to-late November 2026:** He told Politico he is open to the National Popular Vote Interstate Compact (Spotlight PA, Nov 2026).
- **Nov 19–20, 2026, post-midterm polls:** The field has no clear leader, and Shapiro is in the bottom of the named tier.
  - Emerson (Nov 14–16): Ossoff 17%, Harris 16%, AOC 15%, Buttigieg 14%. A second report of the same poll gave conflicting numbers.
  - Verasight: Harris 18%, AOC 17%, Buttigieg 15%, Ossoff 12%, Newsom 10%, Shapiro 4%.
  - Echelon (Nov 12–16): Harris 19%, Buttigieg 15%, Newsom 11%.
  - Economist/YouGov (Nov 9–11): Harris 18%, Ossoff 15%, Newsom 14%.
  - PollCheck average (Nov 17): Harris 20.6%, AOC 13.8%, Buttigieg 13.4%, Newsom 13.2%. Shapiro's individual poll results range from about 3% to 6%.
  
  Sources: Political Wire, Nov 19; Yahoo/AOL; National Pulse, Nov 20; PollCheck.
- **Nov 12–14, 2026:** Shapiro spoke at the Majority Democrats "What's Next" conference in Denver. Asked about 2028, he said it is a family decision and "we'll let people know when we're ready". He also argued the nominee should "know how to run something" (Inquirer, Nov 13; NPR affiliates, Nov 14).
- **Nov 3, 2026:** He won re-election in a landslide over Stacy Garrity, about 60.1% to 38.6% with 93% counted. AP called the race one minute after polls closed. Democrats won a Pennsylvania trifecta by flipping the state Senate. PhillyVoice framed his "iron is hot" for 2028 (Penn Capital-Star; Spotlight PA; PhillyVoice). I did not find certified final figures.
- **Oct 16, 2026:** He launched a federal PAC, New Path PAC, described as the strongest signal yet of a 2028 run (Inquirer, Oct 16; Jewish Insider, Oct 2026).
- **August 2026:** The DNC approved the early 2028 calendar: South Carolina Jan 22, Nevada Feb 1, New Hampshire Feb 8, New Mexico Feb 15. I found no debate dates (Al Jazeera, Aug 15; Ballotpedia).
- **Field context:** Ossoff won re-election in Georgia and has become a media and market favourite despite earlier denials that he would run. Harris, AOC, Buttigieg and Newsom lead the polls. No major Democrat has formally declared, as of the latest reports I found.

**Scheduled events before Dec 31:** I found none that are specific to Shapiro. December is typically slow:
- Pennsylvania's new legislative session and his second inauguration come after the close. By the constitutional third-Tuesday rule, the inauguration should be January 19, 2027.
- A formal Shapiro announcement before he is sworn in seems unlikely.
- Possible December items: New Path PAC activity or FEC filings, year-end "2028 power rankings" pieces, more national interviews, and announcements or rule-outs by rivals.

## 4. Drivers and scenarios

**Paths to YES:**
- **Already close to the line.** If his aggregated value is within about 1 point of 8%, ordinary noise or small drift could produce 4 consecutive hours at or above 8.0%. This is the most important factor.
- **Rivals exit.** A top-tier rival rules out a run, for example Ossoff reaffirming his denial, or Newsom, Buttigieg or Harris stepping back. Probability would redistribute, and his moderate "governing" lane would benefit.
- **Repositioning on Israel goes over well.** If the late-November shift is read as removing his main primary liability with the progressive base, and if he gets elite or media buzz from the landslide and trifecta, "Shapiro is a frontrunner" stories could follow.
- **Escalating 2028 signals.** A major staff hire, early-state travel (South Carolina, Nevada), a book or tour announcement, or an exploratory step.
- **Aggregator quirks.** If one source venue is thin and the aggregate overweights it, one large buy held for several hours could cross the threshold.

**Paths to NO:**
- **Static holiday period.** His value stays below 8% through a low-news December, which is the default if the gap is meaningful.
- **Backlash to the Israel shift.** Criticism of flip-flopping, or pro-Israel donor and moderate reaction, combined with Ossoff, AOC and Harris drawing post-midterm attention.
- **Rivals gain.** A rival in his lane (Beshear, Ossoff, Buttigieg) gains momentum or makes a formal move first.
- **Negative Pennsylvania news.** An unfavourable story from state governance, such as budget fights or controversies.

## 5. Signposts

| Signpost | Direction |
|---|---|
| His current value and recent range on the site, especially any recent hours at or above 7.5% | Strongest determinant; close to 8% means YES is much more likely |
| A top-tier Democrat (Ossoff, Newsom, Harris, Buttigieg) ruling out 2028 | ↑ |
| Shapiro hiring national staff, going to SC/NV/NH, or giving a clear "I'm considering it" signal | ↑ |
| Favourable elite coverage of the Israel pivot, or the landslide driving "most electable" narratives | ↑ |
| A new poll with Shapiro at 8% or higher nationally, or leading a key early state | ↑ |
| Sustained progressive or pro-Israel backlash, or a Pennsylvania scandal or budget fight | ↓ |
| Ossoff or AOC formally signalling a run and consolidating attention | ↓ (mild) |
| The site adding or removing venues, or NO_PRINT gaps | Ambiguous; affects noise |

## 6. Uncertainties

- **Current and recent site values:** Shapiro's current value and recent range on PredictionMarketOdds.com were deliberately not checked. That is the key quantity the forecaster must get.
- **Site methodology:** which venues it uses, how it weights them, whether values are midpoint or last trade, and how often NO_PRINT appears. This determines how noisy the series is.
- **Market creation date:** I don't know when the market opened, so I can't say whether any qualifying hours have already passed.
- **Final certified margin:** I did not confirm the final certified result of the November 3 election.
- **Reaction to the Israel shift:** I did not find measured reaction to the November 25–27 interviews.
- **December schedule:** I couldn't confirm any December 2026 plans for Shapiro, rival announcements, or DNC debate dates.
- **Emerson poll figures:** the two reports of the November Emerson poll conflict.

## Sources
- [Josh Shapiro's 'iron is hot' for 2028 presidential run as Pa. Democrats take control in Harrisburg (PhillyVoice)](https://www.phillyvoice.com/josh-shapiro-2028-presidential-run-pennsylvania-democrats-midterms-trifecta/)
- [Gov. Josh Shapiro launches a federal PAC (Inquirer, Oct 16, 2026)](https://www.inquirer.com/politics/pennsylvania/josh-shapiro-federal-pac-presidential-run-20261016.html)
- [Josh Shapiro launches federal PAC in potential signal of 2028 plans (Jewish Insider, Oct 2026)](https://jewishinsider.com/2026/10/josh-shapiro-federal-pac-2028-signals/)
- [Gov. Josh Shapiro joins other potential 2028 hopefuls in Denver (Inquirer, Nov 13, 2026)](https://www.inquirer.com/politics/pennsylvania/josh-shapiro-democrats-conference-presidential-candidates-20261113.html)
- ['We can't let them down' — After midterm wins, Democrats turn to charting path ahead (GPB/NPR, Nov 14, 2026)](https://www.gpb.org/news/2026/11/14/we-cant-let-them-down-after-midterm-wins-democrats-turn-charting-path-ahead)
- [Netanyahu 'a failed leader,' potential Democratic 2028 nominee says (Israel Hayom, Nov 25, 2026)](https://www.israelhayom.com/2026/11/25/shapiro-faults-biden-trump-netanyahu)
- [Josh Shapiro Ramps up Criticism of Israel Ahead of Possible 2028 Run (Haaretz, Nov 26, 2026)](https://www.haaretz.com/us-news/2026-11-26/ty-article/.premium/josh-shapiro-ramps-up-criticism-of-israel-ahead-of-possible-2028-run/000001a2-14bf-d62f-a5ff-dfff53fa0000)
- [Josh Shapiro slams Biden, Trump for failing to rein in Netanyahu (JPost)](https://www.jpost.com/american-politics/article-916104)
- [Shapiro Says Biden, Trump Failed to Restrain Netanyahu (Wisevoter, Nov 27, 2026)](https://wisevoter.com/world/us/2026/11/27/shapiro-biden-trump-failed-restrain-netanyahu)
- [Shapiro signs bill expanding prevailing wage requirements (Bradford Era, Nov 27, 2026)](https://www.bradfordera.com/2026/11/27/shapiro-signs-bill-expanding-prevailing-wage-requirements/)
- [PA, other states could make the Electoral College irrelevant (Spotlight PA, Nov 2026)](https://spotlightpa.org/news/2026/11/national-popular-vote-interstate-compact-electoral-college-2028-election-pennsylvania-elections)
- [Gov. Josh Shapiro cruises to a second term in Pennsylvania (Penn Capital-Star, Nov 2026)](https://penncapital-star.com/election-2026/gov-josh-shapiro-cruises-to-a-second-term-in-pennsylvania/)
- [Election results: Pennsylvania governor (Spotlight PA, Nov 2026)](https://www.spotlightpa.org/news/2026/11/election-results-pennsylvania-governor-josh-shapiro-stacy-garrity-elections/)
- [No Clear Leaders in 2028 Field (Political Wire, Nov 19, 2026)](https://politicalwire.com/2026/11/19/no-clear-leaders-in-2028-field/)
- [Ossoff and Rubio Lead the 2028 Hopefuls (Political Wire, Nov 19, 2026)](https://politicalwire.com/2026/11/19/ossoff-and-rubio-lead-the-2028-hopefuls/)
- [DNC announces 2028 primary debates: who's leading the polls? (Yahoo)](https://www.yahoo.com/news/politics/articles/dnc-announces-2028-primary-debates-181133869.html)
- [DATA: Harris and Ossoff Lead Pack for Dems' 2028 Nomination (National Pulse, Nov 20, 2026)](https://thenationalpulse.com/2026/11/20/data-harris-and-ossoff-lead-pack-for-dems-2028-nomination-aoc-and-buttigieg-close-behind/)
- [2028 Democratic Primary Polls: National Average (PollCheck)](https://www.pollcheck.com/primaries/democratic/)
- [Gov. Josh Shapiro ranks 7th among Democrats (WJAC)](https://wjactv.com/news/local/gov-josh-shapiro-ranks-7th-among-democrats-ahead-of-2028-presidential-election-poll-united-states-pennsylvania-pa-vice-president-kamala-harris)
- [Is Josh Shapiro Running for President in 2028? (2028tracker)](https://2028tracker.com/candidates/shapiro)
- [US Democrats finalise major shakeup to 2028 presidential primary calendar (Al Jazeera, Aug 15, 2026)](https://www.aljazeera.com/news/2026/8/15/us-democrats-finalise-major-shakeup-to-2028-presidential-primary-calendar)
- [Is Jon Ossoff the Democrats' best hope for 2028? (The Week)](https://theweek.com/politics/jon-ossoff-georgia-senate-race-democrats-2028)
- [Josh Shapiro Yom Haatzmaut / U.S. aid to Israel (Jewish Insider, Apr 2026)](https://jewishinsider.com/2026/04/josh-shapiro-yom-haatzmaut-u-s-aid-israel-hasan-piker/)
- [The 2028 Democratic field is coming into view (Northeastern)](https://cssh.northeastern.edu/the-2028-democratic-field-is-coming-into-view/)