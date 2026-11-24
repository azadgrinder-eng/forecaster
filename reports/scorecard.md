# Forecaster scorecard

Generated 2026-11-24T05:01:01+00:00. Lower Brier and log loss are better.

Questions collected: 285. Resolved yes/no: 50. Voided: 2.

## Agreement check (no waiting needed)

On 136 liquid markets, v0 sits on average **9.1 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 50 | 0.1861 | 0.560 | |
| v0 (median) | 50 | 0.1950 | 0.575 | +0.0089 (-0.0244 to +0.0424) |
| v0, mean of log-odds | 50 | 0.1958 | 0.580 | +0.0097 (-0.0240 to +0.0437) |
| v0, capped 2-98% | 50 | 0.1950 | 0.576 | +0.0089 (-0.0243 to +0.0424) |
| v0 + Platt scaling (5-fold CV) | 50 | 0.2013 | 0.595 | +0.0152 (-0.0162 to +0.0458) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 24 | 0.2176 | 0.650 | |
| v0 | 24 | 0.2565 | 0.758 | +0.0389 (-0.0031 to +0.0831) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 26 | 0.1570 | 0.478 | |
| v0 | 26 | 0.1383 | 0.406 | -0.0188 (-0.0670 to +0.0281) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 12 | 4% | 8% |
| 10-30% | 13 | 15% | 38% |
| 30-50% | 8 | 39% | 50% |
| 50-70% | 10 | 57% | 50% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
