# Research brief: Karlsruher SC vs VfL Osnabrück, 2. Bundesliga Matchday 12 (22 Nov 2026), outcome "Any Other Score"

**Note on sourcing:** The fetch tool was blocked in this environment, so every fact below comes from search-result snippets. Some of those snippets were summarized and contradicted each other in places. I rebuilt both teams' results match by match and cross-checked the point totals. Before trading, verify the key numbers against bundesliga.com or kicker.

## 1. Resolution mechanics
- **What counts:** The score after 90 minutes plus stoppage time. Extra time and penalties do not apply in a league match.
- **When YES happens:** "Any Other Score" wins only if the final score is not one of the scores the market lists. **I could not see the list of outcomes.** Polymarket exact-score markets usually list every score up to 3-3: 0-0, 1-0, 0-1, 1-1, 2-0, 0-2, 2-1, 1-2, 2-2, 3-0, 0-3, 3-1, 1-3, 3-2, 2-3 and 3-3. If that holds here, **YES means at least one team scores 4 or more goals** (4-0, 4-1, 2-4, 5-3 and so on). If the list is shorter (for example, no 3-3, or nothing beyond 2-2), YES becomes much more likely. Confirm the list first.
- **Kickoff:** Sunday 22 Nov 2026, 13:30 CET (12:30 UTC, 7:30 AM ET), at BBBank Wildpark in Karlsruhe (Hessenschau schedule; Sportschau audio listing). The market closes at kickoff.
- **Cancellation or abandonment:** If the match is cancelled, does not start by 24 Nov 11:59 PM ET, or ends with no official result, the market resolves to "0-0". These rules can only push the market toward "0-0", never toward YES. The one exception is an awarded or abandoned result of 4+ goals, which is very unlikely.
- **Who decides:** Official 2. Bundesliga match data. If that is not published within 2 hours, Flashscore, then Sofascore, then a consensus of credible reporting. Score corrections made after resolution do not count.

## 2. Reference classes and base rates
1. **2. Bundesliga 2025-26 scorelines:** About 308 matches, 2.92 goals per game, 57.5% of matches over 2.5 goals. Home wins 46.4%, draws 24.0%, away wins 29.6%. Shares of specific scores (both directions combined): 4-0 at 1.30% (4 games), 4-1 at 2.92% (9), 5-1 at 0.97% (3), 5-4 at 0.65%. The search did not show the 4-2, 4-3, 5-0, 5-2 or 6+ rows (futbol24 2025-26). Adding a rough estimate for the missing rows gives **about 9–11% of matches with a team scoring 4+**.
2. **Poisson model for a typical 2. Bundesliga match:** With 2.9–3.0 goals per game split about 1.6 home and 1.3 away:
   - P(home team scores 4+) ≈ 7.9%
   - P(away team scores 4+) ≈ 4.3%
   - P(either) ≈ **11–12%**
   
   Real football scores are usually a little less spread out than this, so the observed rate tends to be 1–2 points lower (consistent with item 1).
3. **These two teams in 2026-27 (rebuilt from results):**
   - **Karlsruhe, 11 matches:** 3 wins, 2 draws, 6 losses; 15 scored, 24 conceded; about **3.5 goals per game**. **3 of 11** matches had a team on 4+: 2-5 vs Wolfsburg, 4-0 vs Darmstadt, 1-6 at Magdeburg.
     - KSC at home (6 matches): 2-1, 2-5, 0-3, 0-1, 4-0, 2-1. That is 10 scored, 11 conceded, 3.5 goals per game, and 2 of 6 had a team on 4+.
   - **Osnabrück, 11 matches:** 3 wins, 2 draws, 6 losses; 14 scored, 18 conceded; about **2.9 goals per game**. **1 of 11** had a team on 4+ (3-4 at Heidenheim).
     - Osnabrück away (5 matches): 3-4, 1-0, 1-1, 1-2, 0-2. That is 6 scored, 9 conceded.
   - **Combined:** 4 of 22 team-matches (about 18%). The sample is small and should be pulled strongly back toward the league base rate.

## 3. Current state of the world (latest first)
- **22 Nov 2026 (scheduled):** KSC vs Osnabrück, Matchday 12. Both teams' next matches are on 28 Nov: KSC at Hertha, Osnabrück at home to Hannover (FotMob; vfl.de).
- **8 Nov 2026:** Bochum 3-2 KSC. KSC are 16th, the relegation play-off place, with 11 points from 11 matches (news.de; search summaries). One source puts them 17th.
- **7 Nov 2026:** Osnabrück 0-1 Kaiserslautern; Tazemeta scored in the 55th minute in front of a sell-out crowd of 15,741. Osnabrück are 13th–14th with 11 points (Sportschau; bundesliga.com; osradio).
- **31 Oct:** Wolfsburg 2-0 Osnabrück.
- **27 Oct:** KSC lost 0-2 at Gladbach in the DFB-Pokal.
- **25 Oct:** Osnabrück 3-0 Greuther Fürth. KSC won 2-1 at home to Heidenheim (Matchday 10).
- **Earlier KSC results:**
  - Home: 4-0 Darmstadt
  - Away: 6-1 loss at Magdeburg (Matchday 9)
- **Earlier Osnabrück results:**
  - Home: 3-1 Braunschweig, 1-3 Hertha (13 Sep)
  - Away: 1-1 at Kiel, 1-2 at Bielefeld
- **Table:** The bottom of the table is tightly bunched, with several clubs on 11–12 points. Both teams are in a relegation fight and have lost 4 of their last 5 between them.
- **Coaching:** KSC are led by **Maximilian Senft**, who started on 21 May 2026 after Christian Eichner left by mutual consent (Wikipedia 2026-27 2. Bundesliga page, via snippet). I did not establish Osnabrück's coach or any current injury news.
- **Osnabrück's status:** They appear to have been promoted from the 3. Liga in 2025-26, but I did not confirm this.

## 4. Drivers and scenarios
**Paths to YES (a team scores 4+):**
- **KSC's leaky defence collapses** (2.2 goals conceded per game; 5 and 6 conceded to strong sides) and Osnabrück reach 4. This is less likely: Osnabrück's attack is modest (1.2 goals per away game) and has scored 3+ only twice.
- **KSC run up a big home win**, as in the 4-0 against Darmstadt. Osnabrück have conceded 3+ three times (Heidenheim, Magdeburg, Hertha), but always to stronger attacks.
- **An open, chaotic game** in the 4-3 or 4-2 style, made more likely by a red card or early goals.

**Paths to NO:** A cagey relegation six-pointer between two sides on 11 points, both short of confidence. Osnabrück's away matches have been low-scoring (four of five had 3 goals or fewer). A tight game makes a 1-1, 1-0 or 2-1 type score most likely.

**Rough expected goals:** KSC about 1.5–1.6, Osnabrück about 1.2–1.35, total about 2.8–3.0. Poisson then gives roughly 10–12% that either team scores 4+. Discounting for the usual over-spread of Poisson gives about 8–11%.

## 5. Signposts
- **The list of outcomes** (most important). If any score with both teams on 3 or fewer is missing, YES gets a big boost.
- **Team news:** KSC defensive absences or Osnabrück attacking injuries could push the probability up a point or two. Starting line-ups appear about an hour before kickoff, after the market closes.
- **A coaching change at KSC** before the match (16th place after a 2-3 loss could prompt one). The direction is ambiguous; a new coach usually tightens the defence at first.
- **Weather in late November:** heavy rain or snow slightly lowers expected goals.

## 6. Uncertainties
- The exact list of outcomes in this market.
- Exact goal totals: one source gave KSC's goal difference as −5, but my match-by-match count gives −9. Treat the per-team goals as approximate.
- I could not get a 2. Bundesliga goals-per-game figure for 2026-27, or the full 2025-26 scoreline table (the 4-2, 4-3, 5-0 and 6+ rows are missing).
- Head-to-head history, the Osnabrück coach, and injury or suspension lists were not established.

## Sources
- [KSC vs Osnabrück 12. Spieltag – fussballtransfers](https://www.fussballtransfers.com/spiel/805444332339292771-karlsruher-sc-vs-vfl-osnabrueck)
- [Live hören: Karlsruher SC gegen VfL Osnabrück – Sportschau](https://www.sportschau.de/fussball/bundesliga2/karlsruher-sc-gegen-vfl-osnabrueck,audiostream-karlsruher-sc-gegen-vfl-osnabrueck-102.html)
- [Karlsruher SC – FotMob](https://www.fotmob.com/teams/8295/overview/karlsruher-sc)
- [Spielplan – vfl.de](https://www.vfl.de/teams/spielplan)
- [2. Bundesliga Tabelle 11. Spieltag – Sportschau](https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-2-bundesliga/blitztabelle)
- [Karlsruher SC: Spielplan & Ergebnisse 2026/27 – Hessenschau](https://www.hessenschau.de/sport/ergebnisse-tabellen/fussball-2bl100~team_id-85.html)
- [Spielplan Karlsruher SC 2026/27 – liga-spielplan.de](https://www.liga-spielplan.de/spielplan/Karlsruher+SC)
- [Karlsruher SC: Platz 16 nach Niederlage gegen VfL Bochum – news.de](https://www.news.de/sport/860171512/karlsruher-sc-ergebnis-aktuell-3-2-gegen-vfl-bochum-tabelle-und-statistik/1/)
- [Karlsruher SC results 2026/27 – VAVEL](https://www.vavel.com/en-us/data/karlsruher-sc/results/)
- [VfL Osnabrück: Spielplan & Ergebnisse 2026/27 – Hessenschau](https://www.hessenschau.de/sport/ergebnisse-tabellen/fussball-2bl100~team_id-109.html)
- [VfL Osnabrück 2026/27 alle Spiele – weltfussball](https://www.weltfussball.de/teams/te2083/vfl-osnabrueck/alle-spiele/)
- [Osnabrück vs Kaiserslautern Liveticker – Sportschau](https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-2-bundesliga/ma12194935/vfl-osnabrueck_1-fc-kaiserslautern/liveticker)
- [VfL Osnabrück – 1. FC Kaiserslautern Spielbericht – bundesliga.com](https://www.bundesliga.com/de/2bundesliga/news/vfl-osnabrueck-1-fc-kaiserslautern-spieltag-11-spielbericht-highlights-39912)
- [VfL Osnabrück verliert gegen Kaiserslautern – osradio](https://osradio.de/vfl-osnabrueck-verliert-gegen-kaiserslautern/)
- [Osnabrück vs Braunschweig Liveticker – bundesliga.com](https://www.bundesliga.com/de/2bundesliga/spieltag/2026-2027/4/vfl-osnabrueck-vs-eintracht-braunschweig/liveticker)
- [VfL Osnabrück – FotMob](https://www.fotmob.com/uk/teams/9775/overview)
- [3:1 in Osnabrück – Hertha bleibt verlustpunktfrei – ZDFheute](https://www.zdfheute.de/sport/osnabrueck-hertha-2-bundesliga-3-spieltag-100.html)
- [Hertha BSC nicht zu stoppen: 3:1 beim VfL Osnabrück – Nordkurier](https://www.nordkurier.de/regional/brandenburg/hertha-bsc-nicht-zu-stoppen-31-beim-vfl-osnabrueck-4862087)
- [2026–27 2. Bundesliga – Wikipedia](https://en.wikipedia.org/wiki/2026%E2%80%9327_2._Bundesliga)
- [futbol24 2. Bundesliga 2025-26 statistics](https://www.futbol24.com/national/Germany/2-Bundesliga/2025-2026/statistics)
- [futbol24 2. Bundesliga 2025-26 statistieken (NL)](https://www.futbol24.com/nl/nationaal/Germany/2-Bundesliga/2025-2026/statistieken)
- [futbol24 2. Bundesliga 2024-25 statistics](https://www.futbol24.com/national/Germany/2-Bundesliga/2024-2025/statistics)
- [2. Bundesliga Most Common Full-Time Scores – WinDrawWin](https://www.windrawwin.com/statistics/full-time-scores/germany-2-bundesliga/)