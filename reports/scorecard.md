# Forecaster scorecard

Generated 2026-11-19T05:03:27+00:00. Lower Brier and log loss are better.

Questions collected: 210. Resolved yes/no: 29. Voided: 2.

## Agreement check (no waiting needed)

On 97 liquid markets, v0 sits on average **8.4 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 29 | 0.2166 | 0.626 | |
| v0 (median) | 29 | 0.2089 | 0.592 | -0.0077 (-0.0591 to +0.0419) |
| v0, mean of log-odds | 29 | 0.2092 | 0.593 | -0.0074 (-0.0587 to +0.0422) |
| v0, capped 2-98% | 29 | 0.2089 | 0.593 | -0.0077 (-0.0590 to +0.0419) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 15 | 0.2423 | 0.682 | |
| v0 | 15 | 0.2570 | 0.733 | +0.0147 (-0.0437 to +0.0816) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 14 | 0.1890 | 0.565 | |
| v0 | 14 | 0.1572 | 0.441 | -0.0318 (-0.1185 to +0.0447) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 6 | 3% | 0% |
| 10-30% | 7 | 16% | 43% |
| 30-50% | 6 | 36% | 50% |
| 50-70% | 6 | 57% | 33% |
| 70-90% | 4 | 78% | 75% |
