# Forecaster scorecard

Generated 2026-11-13T04:58:26+00:00. Lower Brier and log loss are better.

Questions collected: 120. Resolved yes/no: 11. Voided: 1.

## Agreement check (no waiting needed)

On 57 liquid markets, v0 sits on average **9.6 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 11 | 0.1873 | 0.555 | |
| v0 (median) | 11 | 0.2234 | 0.601 | +0.0361 (-0.0277 to +0.1142) |
| v0, mean of log-odds | 11 | 0.2249 | 0.605 | +0.0377 (-0.0262 to +0.1154) |
| v0, capped 2-98% | 11 | 0.2234 | 0.603 | +0.0362 (-0.0276 to +0.1142) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 7 | 0.1825 | 0.544 | |
| v0 | 7 | 0.1700 | 0.467 | -0.0125 (-0.0536 to +0.0253) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 3 | 3% | 0% |
| 10-30% | 2 | 19% | 50% |
| 30-50% | 3 | 35% | 67% |
| 50-70% | 3 | 58% | 33% |
