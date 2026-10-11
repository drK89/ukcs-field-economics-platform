# UKCS Field Economics Platform

An advanced, transparent portfolio-screening application built from official UK Continental Shelf production data and public Brent price data.

## Portfolio highlights

- Validated ingestion and aggregation of 2021–2025 public production records
- Monthly field economics and discounted cash-flow proxies
- Field/operator rankings, margin and breakeven indicators
- Downside, base and upside scenario comparison
- Monte Carlo price and OPEX uncertainty analysis
- Interactive Streamlit dashboard and SQLite audit trail
- Automated tests, CI and reproducible CSV outputs

This is an engineering analytics portfolio project, not a reserves report, tax model, fairness opinion or investment recommendation. Costs and fiscal assumptions are configurable demonstration proxies—not confidential field values.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run_platform.py
streamlit run advanced_dashboard.py
```

Run tests with `python -m unittest discover -s tests -v`.

## Data

Production: North Sea Transition Authority public UKCS production data. Price reference: U.S. Energy Information Administration public Brent series. See `DATA_SOURCE.md` and `DATA_DICTIONARY.md` for attribution and limitations.

## Repository structure

- `src/data.py` — validation, cleaning and feature engineering
- `src/economics.py` — cash flow, breakeven, scenarios and Monte Carlo
- `src/database.py` — reproducible run audit trail
- `run_platform.py` — full analytical pipeline
- `advanced_dashboard.py` — interactive interface
- `tests/` — unit and integration tests

## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  
[GitHub Portfolio](https://github.com/drK89)

## Licence

Copyright (c) 2026 Khaldoun Shaker. All rights reserved. See [LICENSE](LICENSE).
