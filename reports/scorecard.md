# Forecaster scorecard

Generated 2026-11-25T05:04:07+00:00. Lower Brier and log loss are better.

Questions collected: 300. Resolved yes/no: 52. Voided: 2.

## Agreement check (no waiting needed)

On 143 liquid markets, v0 sits on average **8.9 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 52 | 0.1855 | 0.559 | |
| v0 (median) | 52 | 0.1974 | 0.580 | +0.0118 (-0.0204 to +0.0441) |
| v0, mean of log-odds | 52 | 0.1981 | 0.584 | +0.0125 (-0.0199 to +0.0447) |
| v0, capped 2-98% | 52 | 0.1974 | 0.581 | +0.0119 (-0.0204 to +0.0441) |
| v0 + Platt scaling (5-fold CV) | 52 | 0.1984 | 0.586 | +0.0129 (-0.0168 to +0.0421) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 25 | 0.2106 | 0.633 | |
| v0 | 25 | 0.2533 | 0.750 | +0.0427 (+0.0017 to +0.0852) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 27 | 0.1623 | 0.489 | |
| v0 | 27 | 0.1456 | 0.423 | -0.0167 (-0.0652 to +0.0286) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 12 | 4% | 8% |
| 10-30% | 13 | 15% | 38% |
| 30-50% | 9 | 39% | 56% |
| 50-70% | 11 | 57% | 55% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
