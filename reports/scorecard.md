# Forecaster scorecard

Generated 2026-11-16T05:35:46+00:00. Lower Brier and log loss are better.

Questions collected: 165. Resolved yes/no: 20. Voided: 2.

## Agreement check (no waiting needed)

On 74 liquid markets, v0 sits on average **9.4 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 20 | 0.2161 | 0.614 | |
| v0 (median) | 20 | 0.2128 | 0.599 | -0.0033 (-0.0511 to +0.0503) |
| v0, mean of log-odds | 20 | 0.2138 | 0.601 | -0.0023 (-0.0505 to +0.0513) |
| v0, capped 2-98% | 20 | 0.2128 | 0.599 | -0.0032 (-0.0510 to +0.0503) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 11 | 0.2566 | 0.709 | |
| v0 | 11 | 0.2742 | 0.765 | +0.0176 (-0.0580 to +0.1066) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 9 | 0.1666 | 0.497 | |
| v0 | 9 | 0.1377 | 0.395 | -0.0288 (-0.0747 to +0.0111) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 4 | 3% | 0% |
| 10-30% | 4 | 19% | 50% |
| 30-50% | 6 | 36% | 50% |
| 50-70% | 5 | 57% | 40% |
| 70-90% | 1 | 70% | 100% |
