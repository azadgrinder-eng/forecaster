# Forecaster scorecard

Generated 2026-11-11T04:57:28+00:00. Lower Brier and log loss are better.

Questions collected: 90. Resolved yes/no: 9. Voided: 1.

## Agreement check (no waiting needed)

On 44 liquid markets, v0 sits on average **10.0 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 9 | 0.1853 | 0.550 | |
| v0 (median) | 9 | 0.2159 | 0.578 | +0.0306 (-0.0450 to +0.1260) |
| v0, mean of log-odds | 9 | 0.2167 | 0.580 | +0.0314 (-0.0442 to +0.1270) |
| v0, capped 2-98% | 9 | 0.2160 | 0.579 | +0.0306 (-0.0450 to +0.1260) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 6 | 0.1652 | 0.507 | |
| v0 | 6 | 0.1479 | 0.411 | -0.0173 (-0.0625 to +0.0260) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 3 | 3% | 0% |
| 10-30% | 2 | 19% | 50% |
| 30-50% | 2 | 30% | 50% |
| 50-70% | 2 | 60% | 0% |
