# Forecaster scorecard

Generated 2026-11-22T05:01:59+00:00. Lower Brier and log loss are better.

Questions collected: 255. Resolved yes/no: 37. Voided: 2.

## Agreement check (no waiting needed)

On 121 liquid markets, v0 sits on average **9.1 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 37 | 0.2022 | 0.586 | |
| v0 (median) | 37 | 0.2119 | 0.596 | +0.0098 (-0.0347 to +0.0539) |
| v0, mean of log-odds | 37 | 0.2134 | 0.602 | +0.0112 (-0.0335 to +0.0556) |
| v0, capped 2-98% | 37 | 0.2120 | 0.597 | +0.0098 (-0.0347 to +0.0539) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 18 | 0.2223 | 0.633 | |
| v0 | 18 | 0.2569 | 0.726 | +0.0346 (-0.0203 to +0.0947) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 19 | 0.1831 | 0.541 | |
| v0 | 19 | 0.1693 | 0.474 | -0.0137 (-0.0781 to +0.0485) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 8 | 3% | 0% |
| 10-30% | 10 | 16% | 50% |
| 30-50% | 7 | 38% | 57% |
| 50-70% | 7 | 57% | 43% |
| 70-90% | 4 | 78% | 75% |
| 90-100% | 1 | 97% | 100% |
