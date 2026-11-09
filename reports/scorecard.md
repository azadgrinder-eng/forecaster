# Forecaster scorecard

Generated 2026-11-09T04:56:52+00:00. Lower Brier and log loss are better.

Questions collected: 60. Resolved yes/no: 4. Voided: 0.

## Agreement check (no waiting needed)

On 30 liquid markets, v0 sits on average **10.1 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 4 | 0.1632 | 0.454 | |
| v0 (median) | 4 | 0.1823 | 0.486 | +0.0192 (-0.0045 to +0.0428) |
| v0, mean of log-odds | 4 | 0.1817 | 0.484 | +0.0186 (-0.0085 to +0.0456) |
| v0, capped 2-98% | 4 | 0.1823 | 0.486 | +0.0192 (-0.0045 to +0.0428) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 2 | 4% | 0% |
| 50-70% | 2 | 60% | 0% |
