# Forecaster scorecard

Generated 2026-11-14T04:56:39+00:00. Lower Brier and log loss are better.

Questions collected: 135. Resolved yes/no: 12. Voided: 1.

## Agreement check (no waiting needed)

On 63 liquid markets, v0 sits on average **10.0 points** from the market price recorded at collection. This catches broken changes; it is not a reason to ship one.

## v0: all resolved questions

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 12 | 0.1729 | 0.520 | |
| v0 (median) | 12 | 0.2156 | 0.588 | +0.0427 (-0.0172 to +0.1152) |
| v0, mean of log-odds | 12 | 0.2175 | 0.592 | +0.0446 (-0.0153 to +0.1172) |
| v0, capped 2-98% | 12 | 0.2156 | 0.590 | +0.0428 (-0.0171 to +0.1152) |

### v0: liquid markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 5 | 0.1594 | 0.486 | |
| v0 | 5 | 0.2795 | 0.759 | +0.1200 (+0.0038 to +0.2792) |

### v0: thin markets

| Forecaster | n | Brier | Log loss | Brier minus market (90% CI) |
| --- | --- | --- | --- | --- |
| Market price at collection | 7 | 0.1825 | 0.544 | |
| v0 | 7 | 0.1700 | 0.467 | -0.0125 (-0.0536 to +0.0253) |

### v0: calibration

| Forecast range | n | Avg forecast | Actually happened |
| --- | --- | --- | --- |
| 0-10% | 3 | 3% | 0% |
| 10-30% | 2 | 19% | 50% |
| 30-50% | 3 | 35% | 67% |
| 50-70% | 4 | 59% | 50% |
