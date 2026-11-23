# Forecaster scorecard

Generated 2026-11-23T05:03:39+00:00. Lower Brier and log loss are better.

Questions collected: 270. Resolved yes/no: 45. Voided: 2.

## Agreement check (no waiting needed)

On 128 liquid markets, v0 sits on average **9.0 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 45 | 0.1803 | 0.531 | |
| v0 (median) | 45 | 0.1878 | 0.539 | +0.0075 (-0.0284 to +0.0448) |
| v0, mean of log-odds | 45 | 0.1890 | 0.543 | +0.0087 (-0.0273 to +0.0463) |
| v0, capped 2-98% | 45 | 0.1878 | 0.540 | +0.0075 (-0.0283 to +0.0448) |
| v0 + Platt scaling (5-fold CV) | 45 | 0.1889 | 0.549 | +0.0086 (-0.0274 to +0.0453) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 21 | 0.1971 | 0.570 | |
| v0 | 21 | 0.2321 | 0.661 | +0.0350 (-0.0128 to +0.0871) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 24 | 0.1656 | 0.496 | |
| v0 | 24 | 0.1491 | 0.432 | -0.0165 (-0.0702 to +0.0340) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 10 | 4% | 0% |
| 10-30% | 12 | 16% | 42% |
| 30-50% | 8 | 39% | 50% |
| 50-70% | 8 | 56% | 50% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
