## 1. Resolution mechanics
- **What counts as YES:** Cristiano Ronaldo must score his 1,000th official career goal (club plus Portugal senior team, competitive matches only) in a match played on or before **Sunday, November 29, 2026, 11:59 PM ET**. The match date in ET decides it, not the day the tracker updates.
- **Who decides:** ESPN's Cristiano Ronaldo goal tracker (the "Road to 1,000" story). If it is unavailable or out of date, a consensus of credible reporting is used. I could not open the tracker directly because fetches to it were refused. ESPN's articles have followed the mainstream count: 977 at the start of the season, 979 against Abha, 980/981 in October, and ESPN reported Ronaldo "claims disputed goal" against Al Faisaly (ESPN, Oct 2026).
- **Edge cases:**
  - **The disputed Al Faisaly goal (Oct 23, 2026).** The Saudi Pro League and the referee's report credited it to Ronaldo. Opta, SofaScore, FotMob, Flashscore and Transfermarkt record it as an own goal by Andrei Girotto. One Yahoo report says the league later reclassified it. So his total after the Oct 29 hat-trick is **984 or 985**, depending on the source (Yahoo Sports, Oct–Nov 2026; World Soccer Talk; Archyde).
  - **An outlier figure.** One search snippet of Wikipedia's "List of world association football records" said "1,003 official goals as of 2 November 2026." Every dated news source puts him at about 983–985, so this is probably a different counting basis or a bad edit. It only matters if someone resolves the market off Wikipedia instead of ESPN, which the rules do not allow.
  - **Gap needed:** 15 or 16 more goals, depending on how the disputed goal is treated.

## 2. Reference classes and base rates
1. **Ronaldo's recent scoring rate.** About 27 goals in calendar 2026 by Oct 30, including World Cup and club matches (beIN Sports, Oct 30, 2026). That is very roughly 0.8–1.0 goals per appearance. He went from 976 (Jul 3, World Cup knockout goal against Croatia) to 985 (Oct 29), so about 9 goals in about 4 months of club play (beIN, Jul 3 and Oct 29, 2026).
   - With 3–4 games left and about 0.9 goals per game, expected goals are about 3–4. Under a Poisson model, the chance of 15 or more is on the order of 10⁻⁵ to 10⁻⁴.
2. **Ronaldo's most goals in one match or a short run (my own approximation from memory of his record; not verified this session).**
   - His career best is 5 goals in a match, done about twice (Granada and Espanyol, 2015).
   - He has had roughly a dozen 4-goal games, and about one since joining Al Nassr (Al Wehda, 2023).
   - His 67 hat-tricks are spread over more than 1,300 matches (World Soccer Talk, Oct 29, 2026).
   - I know of no case where he scored 15 or more in any 4-match run, or anywhere near it. His best short bursts were around 8–10 goals in 3–4 games, at his 2015 peak.
3. **Elite players in general scoring 15 or more in 4 consecutive official matches.** This is practically unheard of in modern top-level football. The base rate is close to zero.

## 3. Current state of the world (most recent first)
- **Nov 16, 2026 (today):** He has not played since Oct 29, so the total stays at **984 (Opta-style count) or 985 (league and most media count)** (messixronaldo.com tracker, about Nov 12; ronaldogoalscore.com says 983 as of Nov 14, with its last goal dated Oct 30).
- **Al Nassr matches left before the deadline (sources disagree on some opponents and dates):**
  - **Nov 20:** Saudi Pro League. ESPN and FotMob list away at Al Ahli in Jeddah; other listings say Al Qadsiah.
  - **Nov 24:** AFC Champions League Elite, home against Al Sadd in Riyadh.
  - **Nov 26:** Al Shabab appears on some listings (ESPN alternate page, OddsCalendar). Not confirmed.
  - **Nov 28:** Saudi Pro League, away at Al Hazem (ESPN lists a 7:15 AM ET kickoff). This fits inside the window.
  - So he has **3 or at most 4 matches** (World Soccer Talk "seven matches before 2026 end"; ESPN fixtures).
- **Nov 6:** The Al Hazem league match was called off. On Nov 3 the Saudi Pro League postponed all of Matchweek 13 after changes to the 2027 Asian Cup schedule (beIN, Nov 6; World Soccer Talk).
- **Nov 5:** Ronaldo **retired from international football** after a rift with Portugal coach Jorge Jesus. He finished with 234 caps and 146 goals. Portugal's Nations League games against Denmark and Wales in November are therefore out (CNN, Nov 5; Sky Sports).
- **Nov 2:** He was left out of Al Nassr's 6-2 Champions League Elite win at Pakhtakor. The coach said he was rested for travel and workload; some outlets blamed security concerns, which SI disputes. Separately, a Champions League Elite game against Al Wasl was postponed after Al Wasl refused to travel to Riyadh, and an earlier home match was delayed over reported Houthi missile attacks (ESPN; Daily Star; SI).
- **Oct 29:** Hat-trick in 15 minutes in a 5-3 win over Al Kholood, his 67th career hat-trick, reaching 984 or 985 (beIN, Oct 29; Yahoo).
- **Oct 23:** The disputed goal against Al Faisaly (Vanguard; Yahoo).
- **Oct 12:** Goal 981 against Neftchi Fergana in the Champions League Elite. **Oct 9–10:** Goal 980 against Al Diriyah. The Portugal federation provisionally suspended him on Oct 9 and later gave him a 30-day ban (beIN; ESPN; Sky Sports).
- **Contract:** He is under contract with Al Nassr until June 2027 (World Soccer Talk).

## 4. Drivers and scenarios
- **Path to YES:** He would need about 15–16 goals in 3–4 matches, roughly 4–5 per game in every game. That has never happened in his career. A tiny extra path exists if a postponed match (Matchweek 13, or the Al Wasl game) is moved into Nov 20–29, giving one more appearance. That still leaves the requirement close to impossible.
- **Path to NO (overwhelmingly likely):**
  - Normal scoring of about 0–2 goals per match.
  - Rest or rotation, as on Nov 2.
  - More security-related postponements in Riyadh.
  - Injury, at age 41.
- **Resolution-risk tail:** The main way YES could happen without the goals is a resolver wrongly using an inflated count, such as the Wikipedia "1,003" figure. The rules name ESPN as the source, and ESPN follows the roughly 984–985 count, so this risk looks small.

## 5. Signposts
- **Would move toward YES (each only slightly):**
  - A confirmed ESPN tracker figure far above 985, which would show the counting basis differs from what I found.
  - Extra matches added before Nov 29.
  - A 5-plus goal game on Nov 20.
- **Would move further toward NO:**
  - Ronaldo rested or injured for the Nov 20 or Nov 24 games.
  - More postponements.
  - Scoring 0–1 on Nov 20. After that match, 1,000 by Nov 29 becomes arithmetically almost impossible: he would need 14 or more in 2–3 games.

## 6. Uncertainties
- I could not read ESPN's tracker directly because fetches were blocked. Its exact current figure (984 or 985) is therefore unconfirmed.
- The source of the Wikipedia "1,003 as of Nov 2, 2026" snippet is unexplained.
- The exact fixture list for Nov 20–29 is unclear: whether the Nov 20 opponent is Al Ahli or Al Qadsiah, and whether the Nov 26 Al Shabab game exists. Rescheduling of the postponed Matchweek 13 games is also unknown.
- I did not verify his historical maximum over short runs of games against a source. Those figures come from my own background knowledge.

## Sources
- [Can Cristiano Ronaldo Reach 1,000 Career Goals Before the End of 2026? (beIN Sports, Oct 30, 2026)](https://www.beinsports.com/en-us/soccer/articles/can-cristiano-ronaldo-reach-1-000-career-goals-before-the-end-of-2026-2026-10-30)
- [Cristiano Ronaldo Scores Hat-Trick in 15 Minutes to Reach 985 Career Goals (beIN Sports, Oct 29, 2026)](https://www.beinsports.com/en-us/soccer/articles/cristiano-ronaldo-scores-hat-trick-in-15-minutes-to-reach-985-career-goals-2026-10-29)
- [How many World Cup and career goals does Cristiano Ronaldo have? 976 (beIN Sports, Jul 3, 2026)](https://www.beinsports.com/en-us/soccer/fifa-world-cup-2026/articles/cristiano-ronaldo-breaks-another-record-with-his-first-world-cup-knockout-goal-reaches-976-career-goals-2026-07-03)
- [Why Will Cristiano Ronaldo Have to Wait Longer to Play Again for Al Nassr? (beIN Sports, Nov 6, 2026)](https://www.beinsports.com/en-us/soccer/articles/why-will-cristiano-ronaldo-have-to-wait-longer-before-playing-again-2026-11-06)
- [Ronaldo Total Goals (Nov 2026): 985 (messixronaldo.com)](https://messixronaldo.com/cristiano-ronaldo-total-career-goals/)
- [How Many Goals Has Ronaldo Scored? — Live Goal Tracker (ronaldogoalscore.com)](https://www.ronaldogoalscore.com/en/)
- [List of world association football records (Wikipedia)](https://en.wikipedia.org/wiki/List_of_world_association_football_records)
- [Cristiano Ronaldo's disputed goal is reclassified (Yahoo Sports)](https://sports.yahoo.com/articles/cristiano-ronaldo-disputed-goal-reclassified-193000402.html)
- [Cristiano Ronaldo's 985-goal count sparks furious reaction (World Soccer Talk)](https://worldsoccertalk.com/news/cristiano-ronaldos-985-goal-count-sparks-furious-reaction-as-saudi-pro-league-statistics-row-escalates/)
- [Cristiano Ronaldo's Goal Count Disputed at 984 or 985 (Archyde)](https://www.archyde.com/cristiano-ronaldos-goal-count-disputed-at-984-or-985/)
- [Ronaldo scores 982nd career goal as Al Nassr beat Al Faisaly 3-1 (Vanguard, Oct 2026)](https://www.vanguardngr.com/2026/10/ronaldo-scores-982nd-career-goal-as-al-nassr-beat-al-faisaly-3-1/)
- [Cristiano Ronaldo claims disputed goal in Al Nassr win over Al Faisaly (ESPN)](https://www.espn.com/soccer/story/_/id/50258631/cristiano-ronaldo-portugal-al-nassr-goal-saudi-pro-league)
- [Cristiano Ronaldo Reaches 981 Career Goals in ACL Victory (beIN Sports, Oct 12, 2026)](https://www.beinsports.com/en-us/soccer/articles/cristiano-ronaldo-reaches-981-career-goals-in-al-nassr-s-afc-champions-league-victory-2026-10-12)
- [Cristiano Ronaldo hits 980th career goal (The National, Oct 10, 2026)](https://www.thenationalnews.com/sport/football/2026/10/10/cristiano-ronaldo-hits-980th-career-goal-as-he-puts-portugal-row-behind-him-in-al-nassr-win/)
- [Cristiano Ronaldo suspended by Portugal after national team walkout (ESPN)](https://www.espn.com/soccer/story/_/id/50146841/cristiano-ronaldo-suspended-portugal-national-team-walkout-jorge-jesus-disciplinary)
- [Cristiano Ronaldo retires from international soccer (CNN, Nov 5, 2026)](https://www.cnn.com/2026/11/05/sport/cristiano-ronaldo-retires-portuguese-national-team)
- [Cristiano Ronaldo retires from international football (Sky Sports)](https://www.skysports.com/football/news/13593800/cristiano-ronaldo-retires-from-international-football-after-glittering-portugal-career-that-spanned-23-years)
- [Ronaldo off Al Nassr's ACL squad due to security concerns (ESPN)](https://www.espn.com/soccer/story/_/id/50353917/ronaldo-al-nassr-acl-squad-saudi-security-concerns)
- [Ronaldo rested for Al Nassr trip amid security fears (Daily Star)](https://www.thedailystar.net/sports/football/news/ronaldo-rested-al-nassr-trip-amid-security-fears-4313506)
- [Why Security Concerns Were Not to Blame for Ronaldo's Al Nassr Absence (SI)](https://www.si.com/soccer/why-security-concerns-cristiano-ronaldo-al-nassr-absence)
- [Seven matches confirmed before 2026 end after SPL fixture changes (World Soccer Talk)](https://worldsoccertalk.com/news/cristiano-ronaldo-handed-new-brutal-al-nassr-schedule-as-seven-matches-confirmed-before-2026-end-after-saudi-pro-leagues-major-fixture-changes/)
- [Why Al-Nassr won't play today against Al-Hazem (World Soccer Talk)](https://worldsoccertalk.com/news/why-cristiano-ronaldos-al-nassr-wont-play-today-against-al-hazem-in-2026-27-saudi-pro-league/)
- [Al Nassr 2026-27 Schedule (ESPN)](https://www.espn.com/soccer/team/fixtures/_/id/817/al-nassr)
- [Al Nassr 2026 Results (ESPN)](https://www.espn.com/soccer/team/results/_/id/817/al-nassr)
- [Al Nassr FC fixtures (FotMob)](https://www.fotmob.com/teams/101918/overview/al-nassr-fc)
- [Ronaldo scores 67th career hat-trick (World Soccer Talk)](https://worldsoccertalk.com/news/cristiano-ronaldo-scores-67th-career-hat-trick-how-his-record-compares-to-lionel-messi/)
- [ESPN Ronaldo goal tracker (primary resolution source; could not be accessed)](https://www.espn.com/soccer/story/_/id/46751020/cristiano-ronaldo-goal-tracker-road-1000-career-goals)