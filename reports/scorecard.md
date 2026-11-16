# Forecaster scorecard

Generated 2026-11-15T05:02:27+00:00. Lower Brier and log loss are better.

Questions collected: 150. Resolved yes/no: 17. Voided: 2.

## Agreement check (no waiting needed)

On 67 liquid markets, v0 sits on average **9.6 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 17 | 0.2174 | 0.615 | |
| v0 (median) | 17 | 0.2220 | 0.615 | +0.0046 (-0.0505 to +0.0661) |
| v0, mean of log-odds | 17 | 0.2234 | 0.618 | +0.0060 (-0.0498 to +0.0674) |
| v0, capped 2-98% | 17 | 0.2220 | 0.615 | +0.0046 (-0.0505 to +0.0662) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 8 | 0.2746 | 0.748 | |
| v0 | 8 | 0.3168 | 0.862 | +0.0422 (-0.0610 to +0.1655) |

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
| 30-50% | 4 | 37% | 75% |
| 50-70% | 4 | 59% | 50% |
| 70-90% | 1 | 70% | 100% |
