# Research brief: Will Spain's 29 Nov 2026 general election end in a tie between the left and right blocs?

Note on method: every page fetch was refused by the network proxy. All figures below come from search-result snippets and summaries, not from reading the full articles. Treat exact numbers as approximate, and the forecaster may want to check the key polls directly.

## 1. Resolution mechanics

**What counts as YES ("Tie").** The two blocs must win exactly the same number of seats in the 350-seat Congress of Deputies:
- **Right bloc:** PP and Vox. A joint UPN–PP list in Navarre counts as PP.
- **Left bloc:** PSOE (including PSC), Frente Amplio (FA, including Comuns, Compromís–Front Valencià and Canarian UPC), Podemos (only lists it runs on its own), ERC (including joint ERC–Podem lists), EH Bildu and BNG.
- **Counted for neither bloc:** Junts, PNV, CC, Adelante Andalucía, SALF and any other list.

**Parity rule.** A tie is only arithmetically possible if the seats won by uncounted parties add up to an even number, because the two blocs together must hold an even total.

**Timing and who decides.** The election is on 29 Nov 2026. Results are reported on election night, but votes from Spaniards abroad (the CERA vote) are counted a few days later and can move a seat. In 2023 that count moved a Madrid seat from PSOE to PP. Resolution follows a consensus of credible reporting, with the Interior Ministry's results as the tiebreaker. If results aren't definitively known by 30 Nov 2027, the market resolves "Other". The market closes 30 Nov 04:59 UTC, which is before the overseas count, but resolution can wait for it.

**Edge cases and ambiguities:**
- **Which list is "Podemos alone".** Pollsters show both "ERC-Podemos" lists in Catalonia (these count as ERC) and some separate Podemos lists.
- **Adelante Andalucía.** Polls give it about 2 seats. It is not in the left bloc, so its seats count for neither side.
- **UPN.** If UPN runs alone rather than jointly with PP, its seats count for neither bloc. One poll mentions UPN winning 2 seats (Hamalgama/Vozpópuli). I could not confirm whether UPN and PP have a joint list in 2026.
- **Senate coalition.** PSOE and FA run together in the Senate as "Senado de Progreso". That is irrelevant here, since only the Congress counts.
- **Frente Amplio.** FA is led by Ada Colau and groups Movimiento Sumar, IU, Más Madrid and Comuns (Público/Infobae, 2 Nov 2026). Candidacies were proclaimed 2 Nov and published in the BOE (534 Congress lists). Appeals ran until about 9 Nov.

## 2. Reference classes and base rates

**A. Past Spanish elections, re-scored with this market's bloc definitions** (my calculation from official results; the 2019 and 2015–16 predecessor parties are mapped to the left bloc):

| Election | Right (PP+Vox) | Left | Margin |
|---|---|---|---|
| 2023 | 137 + 33 = 170 (UPN's 1 seat sat outside) | 121 + 31 + 7 + 6 + 1 = 166 | Right +4 |
| Nov 2019 | 89 + 52 = 141 | about 177 (PSOE 120, UP 35, Más País 3, ERC 13, Bildu 5, BNG 1) | Left +36 |
| Apr 2019 | 90 | about 184 (PSOE 123, UP 42, ERC 15, Bildu 4) | Left +94 |
| 2016 | 137 | about 167 | Left +30 |
| 2015 | 123 | about 172 | Left +49 |

- Ties: 0 of 5. Only one margin was 5 seats or fewer (2023), and the median absolute margin was about 36 seats.

**B. How close is "exactly 0" under a normal error model?**
- The bloc margin moves in 1–2 seat steps, so the chance of landing on exactly 0 is roughly the density of the margin distribution at 0.
- If the expected margin were near 0, with a standard deviation of about 15–20 seats, P(tie) would be about 2–2.5%. That is the ceiling for a genuinely close race.
- With current polls centred around Right +55 and a standard deviation of about 20–25, P(tie) comes out well under 1%. Fat tails or systematic poll error raise it modestly.

**C. Spanish polling error.**
- In 2023, private polls overstated PP. Sigma Dos had PP at 145–150 and got 136–137; GAD3 had 151. The PP+Vox total ended at 169–170, against polls that pointed to roughly 176 or more.
- PSOE was underestimated. Sigma Dos had it at 113–118 and it won 121–122.
- Net error on the bloc margin was about 15–25 seats, in the left's favour (Ara; El Independiente, 25 Jul 2023).
- Only the CIS was roughly close, using very wide ranges.

## 3. Current state of the world (most recent first)

- **6 Nov 2026.** A polling average puts PP at 31.2%, PSOE 26.8%, Vox 19.3% and FA 6.3%. Leads range from 0.7 points (More in Common) to more than 7 points (Periodista Digital, 6 Nov).
- **5–6 Nov.** SW Demoscopia (for La Séptima) is the most left-friendly private poll: PSOE 126, PP 117, Vox 62, FA 13, others 32. PP+Vox = 179.
  - My estimate of the left bloc here is about 155–158, which gives a margin of roughly Right +21 to +24.
  - A 6 Nov table on the same site shows PSOE 127 / PP 115 / Vox 63 (Electomanía, 5–6 Nov).
- **2 Nov.** Electomanía's ElectoPromedio: PP 136, PSOE 104, Vox 65; Right = 201. That implies a left bloc of about 135–140 and a margin of about Right +60.
- **1 Nov.** ElectoPanel: PP 133, PSOE 108, Vox 64, FA 12, ERC-Podemos 8, Bildu 7, PNV 6, Junts 5, Compromís-FV 2, Adelante 2, BNG 2, Podemos 1.
  - Right 197, Left 140 (Compromís counted in FA), uncounted 13.
  - Margin: **Right +57**.
- **28 Oct.** A collision between an AVE and an Iryo train at Urda (Toledo) killed at least 69 people. PP is attacking Transport Minister Óscar Puente. Some outlets report Feijóo widening his lead in the polls taken after the crash; this is unconfirmed (Democrata; Vozpópuli). Unions have called a general strike for 11 Nov.
- **26–27 Oct.** Polls by outlet:
  - SocioMétrica: PP 135, PSOE 108, Vox 63
  - NC Report: PP 141–143, PSOE 100–102, Vox 64–66; Right ≥205
  - Sigma Dos: PP 125–131, PSOE 103–109, Vox 66–69
  - GAD3: PP 133
  - El Independiente reported that the PP+Vox average fell below 200 for the first time in months (Infobae 27 Oct; El Independiente 26 Oct).
- **25 Oct.** El Debate's median of 12 pollsters has PP+Vox at 203 seats (range 198–212), PP at 129–147 and PSOE at 100–112. None gives PP a majority on its own.
- **14 Oct.** CIS barometer: PSOE 34.0%, PP 22.2%, Vox 17.1%, Sumar-FA 6.1%, Podemos 3.1%.
  - At those vote shares the left bloc would plausibly lead the seat count. The CIS has a long-standing pro-PSOE house effect.
  - Ateneo del Dato re-weighted the same data to PSOE 28.6% vs PP 28.2%.
- **9 Oct.** 40dB poll for El País: PP 31.9% (123–140 seats), PSOE 28.1% (105–117), Vox 18.9% (63–74); central estimate Right 198. Sumar gets 5–7 seats and Podemos 2 if they run separately. My implied margin is about Right +60.
- **5 Oct.** Sánchez called the snap election after Congress rejected two housing decrees, with PP, Vox and Junts voting against.

**Scheduled before the vote:** general strike on 11 Nov; official campaign runs about 13–27 Nov; likely TV debates; the legal ban on publishing polls starts about 24 Nov; election 29 Nov; overseas vote count around 2 Dec.

## 4. Drivers and scenarios

- **Base case (NO, Right well ahead):** the private-poll consensus holds, Right gets 190–205 and Left 135–150, a margin of +40 to +70. A tie is impossible here.
- **Left rally (NO, but closer):** a repeat of the 2023 pattern, where the left was underestimated and mobilised late, plus a possible PSOE recovery like the one SW Demoscopia shows. This gives a margin of Right +10 to +30.
- **Path to a tie:** both a large systematic miss in the left's favour (bigger than 2023) and a late campaign swing would be needed, so that each bloc lands around 167–170. It also needs the uncounted seats (Junts about 5–7, PNV 4–6, CC about 1, Adelante about 2, UPN 0–2, SALF 0–?) to total an even number.
- **Left ahead (NO):** CIS-style numbers would put the left in front, which overshoots a tie.
- **What a tie depends on:** vote shares for the two big parties, Vox's strength, Vox–PP competition for marginal seats in small provinces, and whether the fragmented left (FA, Podemos and Compromís running separately) wastes votes below thresholds.

## 5. Signposts

**Would raise P(tie):**
- Polls in the final week showing the PP+Vox lead in seats shrinking toward 175–180 and the left bloc reaching 160 or more.
- Several private pollsters converging on SW Demoscopia or More in Common numbers.
- A clear left-mobilisation story (a debate win, the strike, a PP or Vox scandal).

**Would lower it:**
- Post-crash polls confirming Right at 200 or more.
- Exit polls or the election-night count showing a margin above about 15. Once the count passes about 90%, a margin of 10 or more is essentially decisive, apart from the overseas vote shifting about 1 seat.

**Mechanical check:** on election night, verify whether the uncounted seats total an odd number. If they do, a tie is impossible.

## 6. Uncertainties

- I could not read the full poll tables because page fetches failed. Left-bloc totals are my own reconstructions from snippets, and SW Demoscopia's "others 32" is not broken out.
- I could not confirm whether UPN runs jointly with PP or alone, or whether Podemos runs on its own lists outside Catalonia and how widely.
- The exact composition of FA's lists (whether Compromís and UPC are inside FA everywhere) is unconfirmed; pollsters show "Compromís-FV" separately.
- I found no polls conducted entirely after the Urda crash with full seat tables. The net effect of the crash and the 11 Nov strike is unclear.
- How large polling error will be in 2026: the 2023 error favoured the left, but the direction isn't guaranteed to repeat.

## Sources
- [Pedro Sánchez convoca elecciones generales para el 29 de noviembre – Diario de Avisos](https://diariodeavisos.elespanol.com/2026/10/pedro-sanchez-convoca-elecciones-generales/)
- [Sánchez convoca elecciones generales el 29 de noviembre – EcoAvant](https://www.ecoavant.com/politica/sanchez-convoca-elecciones-generales-29-noviembre_17546_102.html)
- [¿Qué dicen las últimas encuestas…? – El Debate, 25 Oct 2026](https://www.eldebate.com/espana/20261025/dicen-ultimas-encuestas-sobre-elecciones-generales-29-noviembre-cns_472138.html)
- [Así están los sondeos para el 29 de noviembre – Infobae, 27 Oct 2026](https://www.infobae.com/espana/2026/10/27/asi-estan-las-encuestas-para-el-29-de-noviembre-pp-y-vox-mantienen-la-mayoria-absoluta-el-psoe-gana-terreno-y-la-izquierda-fragmentada-no-logra-remontar/)
- [Encuestas elecciones generales 2026 – ElNacional.cat](https://www.elnacional.cat/es/elecciones/generales-2026/encuestas-elecciones-generales-2026-sondeos-29-n_1710013_102.html)
- [Feijóo a la cabeza… qué dicen las encuestas del 29-N – Periodista Digital, 6 Nov 2026](https://periodistadigital.com/periodismo/20261106/feijoo-pp-cabeza-abascal-vox-acelera-sanchez-psoe-hunde-dicen-encuestas-29-n-noticia-689405264292)
- [Elecciones España 2026: el PSOE gana el sondeo, pero PP y Vox son mayoría – Urgente24](https://urgente24.com/mundo/elecciones-espana-2026-el-psoe-sanchez-gana-el-sondeo-pero-pp-y-vox-son-mayoria-n636280)
- [ElectoPanel (1 nov) – Electomanía](https://electomania.es/electopanel-1-nov-el-psoe-baja-y-vuelve-a-minimos/)
- [ElectoPromedio: PP y Vox recuperan los 201 – Electomanía](https://electomania.es/electopromedio-pp-y-vox-recuperan-los-201-escanos-y-el-psoe-baja-del-26/)
- [Encuesta SW Demoscopia (5 nov) – Electomanía](https://electomania.es/encuesta-sw-demoscopia-5-nov-mayoria-de-pp-y-vox-con-el-psoe-primero/)
- [Tracking SW Demoscopia (6 nov) – Electomanía](https://electomania.es/tracking-sw-demoscopia-6-nov-el-psoe-se-afianza-en-primera-posicion/)
- [Encuesta CIS 14/10/2026 – Electográfica](https://www.electografica.com/2026/10/encuesta-cis-261014.html)
- [Encuesta 40dB 09/10/2026 – Electográfica](https://www.electografica.com/2026/10/encuesta-40db-261009.html)
- [Encuesta elecciones generales 40dB da a PP y Vox 198 escaños – Bilbao Hiria](https://bilbaohiria.com/actualidad/encuesta-elecciones-generales-40db-pp-vox-198-escanos-29n)
- [Encuestas 29-N: Sánchez recorta distancias – El Independiente, 26 Oct 2026](https://www.elindependiente.com/espana/2026/10/26/encuestas-29-n-generales-sanchez-recorta-pp-vox-debajo-200-escanos/)
- [Feijóo regains momentum after Urda – Democrata](https://www.democrata.es/en/center-of-surveys-and-electoral-polls/general-elections/feijoo-regains-momentum-after-urda-the-polls-widen-his-victory-in-the-general-elections-of-29n/)
- [El PP ve imposible que Sánchez pueda remontar tras la crisis ferroviaria – Vozpópuli](https://www.vozpopuli.com/espana/politica/el-pp-ve-imposible-que-sanchez-pueda-remontar-en-las-encuestas-tras-la-crisis-ferroviaria.html)
- [PP y Vox suman ya un techo histórico… 205 escaños (Hamalgama) – Vozpópuli](https://www.vozpopuli.com/espana/politica/pp-y-vox-suman-ya-un-techo-historico-de-127-millones-de-votos-y-lograrian-205-escanos.html)
- [Quién gana y quién pierde en cada comunidad autónoma el 29N – Democrata](https://www.democrata.es/encuestas/elecciones-generales/encuesta-elecciones-generales-29n-escanos-por-comunidades-autonomas/)
- [El BOE publica las 895 candidaturas para el 29N – Público](https://www.publico.es/politica/boe-publica-895-candidaturas-29n-consulta-aqui-todas-listas.html)
- [Las Juntas Electorales proclaman las candidaturas del 29N – Infobae, 2 Nov 2026](https://www.infobae.com/espana/agencias/2026/11/02/las-juntas-electorales-proclaman-este-lunes-las-candidaturas-para-las-elecciones-del-29n/)
- [¿Por qué fallaron tanto las encuestas del 23-J? – Ara](https://es.ara.cat/politica/elecciones-generales/fallaron-encuestas-23-j_1_4765199.html)
- [Así fallaron las encuestas del 23-J – El Independiente, 25 Jul 2023](https://www.elindependiente.com/espana/2023/07/25/asi-fallaron-las-encuestas-del-23-j/amp/)
- [Simulaciones: Sánchez solo tiene opciones si la derecha no consigue mayoría absoluta – El Español, 20 Oct 2026](https://www.elespanol.com/espana/20261020/simulaciones-sanchez-solo-opciones-derecha-no-consiga-mayoria-absoluta/1003744426927_0.html)