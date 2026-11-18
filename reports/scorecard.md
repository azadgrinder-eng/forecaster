# Forecaster scorecard

Generated 2026-11-18T05:02:55+00:00. Lower Brier and log loss are better.

Questions collected: 195. Resolved yes/no: 27. Voided: 2.

## Agreement check (no waiting needed)

On 90 liquid markets, v0 sits on average **8.8 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 27 | 0.2209 | 0.638 | |
| v0 (median) | 27 | 0.1991 | 0.568 | -0.0218 (-0.0720 to +0.0272) |
| v0, mean of log-odds | 27 | 0.2000 | 0.571 | -0.0209 (-0.0717 to +0.0285) |
| v0, capped 2-98% | 27 | 0.1992 | 0.569 | -0.0217 (-0.0720 to +0.0273) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 14 | 0.2586 | 0.722 | |
| v0 | 14 | 0.2725 | 0.769 | +0.0139 (-0.0476 to +0.0843) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 13 | 0.1803 | 0.547 | |
| v0 | 13 | 0.1201 | 0.352 | -0.0602 (-0.1407 to +0.0000) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 6 | 3% | 0% |
| 10-30% | 7 | 16% | 43% |
| 30-50% | 6 | 36% | 50% |
| 50-70% | 6 | 57% | 33% |
| 70-90% | 2 | 75% | 100% |
