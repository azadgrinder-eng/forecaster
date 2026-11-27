# Forecaster scorecard

Generated 2026-11-27T05:00:12+00:00. Lower Brier and log loss are better.

Questions collected: 330. Resolved yes/no: 61. Voided: 2.

## Agreement check (no waiting needed)

On 158 liquid markets, v0 sits on average **8.7 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 61 | 0.2164 | 0.634 | |
| v0 (median) | 61 | 0.2317 | 0.686 | +0.0153 (-0.0189 to +0.0519) |
| v0, mean of log-odds | 61 | 0.2318 | 0.688 | +0.0154 (-0.0190 to +0.0522) |
| v0, capped 2-98% | 61 | 0.2317 | 0.686 | +0.0153 (-0.0189 to +0.0519) |
| v0 + Platt scaling (5-fold CV) | 61 | 0.2204 | 0.630 | +0.0040 (-0.0297 to +0.0367) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 27 | 0.2265 | 0.680 | |
| v0 | 27 | 0.2673 | 0.800 | +0.0407 (+0.0015 to +0.0817) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 34 | 0.2084 | 0.596 | |
| v0 | 34 | 0.2035 | 0.596 | -0.0049 (-0.0600 to +0.0495) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 16 | 4% | 19% |
| 10-30% | 14 | 15% | 43% |
| 30-50% | 11 | 38% | 55% |
| 50-70% | 13 | 58% | 46% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
