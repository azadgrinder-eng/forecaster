# Forecaster scorecard

Generated 2026-11-20T05:04:04+00:00. Lower Brier and log loss are better.

Questions collected: 225. Resolved yes/no: 34. Voided: 2.

## Agreement check (no waiting needed)

On 105 liquid markets, v0 sits on average **8.9 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 34 | 0.2163 | 0.621 | |
| v0 (median) | 34 | 0.2249 | 0.628 | +0.0086 (-0.0391 to +0.0575) |
| v0, mean of log-odds | 34 | 0.2264 | 0.634 | +0.0101 (-0.0383 to +0.0594) |
| v0, capped 2-98% | 34 | 0.2249 | 0.629 | +0.0086 (-0.0391 to +0.0575) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 17 | 0.2294 | 0.648 | |
| v0 | 17 | 0.2611 | 0.736 | +0.0318 (-0.0242 to +0.0953) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 17 | 0.2032 | 0.593 | |
| v0 | 17 | 0.1886 | 0.521 | -0.0147 (-0.0918 to +0.0552) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 7 | 3% | 0% |
| 10-30% | 9 | 16% | 56% |
| 30-50% | 7 | 38% | 57% |
| 50-70% | 6 | 57% | 33% |
| 70-90% | 4 | 78% | 75% |
| 90-100% | 1 | 97% | 100% |
