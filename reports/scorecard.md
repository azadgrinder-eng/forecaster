# Forecaster scorecard

Generated 2026-11-26T05:00:22+00:00. Lower Brier and log loss are better.

Questions collected: 315. Resolved yes/no: 58. Voided: 2.

## Agreement check (no waiting needed)

On 150 liquid markets, v0 sits on average **9.0 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 58 | 0.1971 | 0.586 | |
| v0 (median) | 58 | 0.2077 | 0.616 | +0.0106 (-0.0253 to +0.0476) |
| v0, mean of log-odds | 58 | 0.2082 | 0.619 | +0.0112 (-0.0250 to +0.0484) |
| v0, capped 2-98% | 58 | 0.2077 | 0.617 | +0.0106 (-0.0253 to +0.0476) |
| v0 + Platt scaling (5-fold CV) | 58 | 0.2088 | 0.606 | +0.0117 (-0.0224 to +0.0447) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 26 | 0.2039 | 0.617 | |
| v0 | 26 | 0.2436 | 0.722 | +0.0396 (-0.0002 to +0.0824) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 32 | 0.1915 | 0.560 | |
| v0 | 32 | 0.1785 | 0.530 | -0.0130 (-0.0680 to +0.0406) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 15 | 4% | 13% |
| 10-30% | 13 | 15% | 38% |
| 30-50% | 11 | 38% | 55% |
| 50-70% | 12 | 57% | 50% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
