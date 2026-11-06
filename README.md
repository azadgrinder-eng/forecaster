# harness-data

Data branch for the forecaster's daily harness runs. Code lives on `main`.

- `data/`: append-only logs (questions, forecasts, resolutions, research briefs)
- `reports/scorecard.md`: the latest scorecard

A scheduled cloud task commits here once a day. Don't edit the .jsonl files by hand.
