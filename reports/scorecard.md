# Forecaster scorecard

Generated 2026-11-17T05:07:32+00:00. Lower Brier and log loss are better.

Questions collected: 180. Resolved yes/no: 24. Voided: 2.

## Agreement check (no waiting needed)

On 83 liquid markets, v0 sits on average **9.1 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 24 | 0.2478 | 0.708 | |
| v0 (median) | 24 | 0.2223 | 0.628 | -0.0255 (-0.0811 to +0.0294) |
| v0, mean of log-odds | 24 | 0.2233 | 0.632 | -0.0245 (-0.0807 to +0.0305) |
| v0, capped 2-98% | 24 | 0.2224 | 0.629 | -0.0255 (-0.0811 to +0.0294) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 14 | 0.2586 | 0.722 | |
| v0 | 14 | 0.2725 | 0.769 | +0.0139 (-0.0476 to +0.0843) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 10 | 0.2327 | 0.688 | |
| v0 | 10 | 0.1521 | 0.431 | -0.0807 (-0.1820 to -0.0027) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 4 | 3% | 0% |
| 10-30% | 7 | 16% | 43% |
| 30-50% | 6 | 36% | 50% |
| 50-70% | 6 | 57% | 33% |
| 70-90% | 1 | 70% | 100% |
