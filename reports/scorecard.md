# Forecaster scorecard

Generated 2026-11-21T05:02:38+00:00. Lower Brier and log loss are better.

Questions collected: 240. Resolved yes/no: 35. Voided: 2.

## Agreement check (no waiting needed)

On 113 liquid markets, v0 sits on average **8.9 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 35 | 0.2101 | 0.604 | |
| v0 (median) | 35 | 0.2185 | 0.611 | +0.0083 (-0.0378 to +0.0566) |
| v0, mean of log-odds | 35 | 0.2200 | 0.617 | +0.0099 (-0.0370 to +0.0584) |
| v0, capped 2-98% | 35 | 0.2185 | 0.612 | +0.0083 (-0.0378 to +0.0566) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 17 | 0.2294 | 0.648 | |
| v0 | 17 | 0.2611 | 0.736 | +0.0318 (-0.0242 to +0.0953) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 18 | 0.1920 | 0.562 | |
| v0 | 18 | 0.1781 | 0.494 | -0.0139 (-0.0860 to +0.0504) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 8 | 3% | 0% |
| 10-30% | 9 | 16% | 56% |
| 30-50% | 7 | 38% | 57% |
| 50-70% | 6 | 57% | 33% |
| 70-90% | 4 | 78% | 75% |
| 90-100% | 1 | 97% | 100% |
