# Forecaster scorecard

Generated 2026-11-28T05:00:30+00:00. Lower Brier and log loss are better.

Questions collected: 345. Resolved yes/no: 63. Voided: 2.

## Agreement check (no waiting needed)

On 165 liquid markets, v0 sits on average **9.0 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 63 | 0.2103 | 0.619 | |
| v0 (median) | 63 | 0.2267 | 0.674 | +0.0163 (-0.0170 to +0.0523) |
| v0, mean of log-odds | 63 | 0.2268 | 0.675 | +0.0165 (-0.0171 to +0.0527) |
| v0, capped 2-98% | 63 | 0.2267 | 0.674 | +0.0164 (-0.0170 to +0.0523) |
| v0 + Platt scaling (5-fold CV) | 63 | 0.2210 | 0.636 | +0.0107 (-0.0220 to +0.0409) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 27 | 0.2265 | 0.680 | |
| v0 | 27 | 0.2673 | 0.800 | +0.0407 (+0.0015 to +0.0817) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 36 | 0.1982 | 0.572 | |
| v0 | 36 | 0.1962 | 0.579 | -0.0020 (-0.0543 to +0.0496) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 16 | 4% | 19% |
| 10-30% | 15 | 15% | 40% |
| 30-50% | 11 | 38% | 55% |
| 50-70% | 14 | 58% | 50% |
| 70-90% | 6 | 78% | 83% |
| 90-100% | 1 | 97% | 100% |
