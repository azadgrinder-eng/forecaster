# Forecaster scorecard

Generated 2026-11-10T04:56:47+00:00. Lower Brier and log loss are better.

Questions collected: 75. Resolved yes/no: 6. Voided: 1.

## Agreement check (no waiting needed)

On 37 liquid markets, v0 sits on average **9.5 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 6 | 0.2612 | 0.727 | |
| v0 (median) | 6 | 0.2379 | 0.636 | -0.0233 (-0.0729 to +0.0259) |
| v0, mean of log-odds | 6 | 0.2387 | 0.637 | -0.0225 (-0.0709 to +0.0252) |
| v0, capped 2-98% | 6 | 0.2379 | 0.636 | -0.0233 (-0.0729 to +0.0259) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 2 | 4% | 0% |
| 10-30% | 1 | 22% | 100% |
| 30-50% | 1 | 30% | 0% |
| 50-70% | 2 | 60% | 0% |
