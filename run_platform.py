from pathlib import Path
from src.data import load_production,load_brent_prices,build_economic_dataset
from src.economics import EconomicAssumptions,evaluate_cash_flow,field_economic_summary,monte_carlo_portfolio,scenario_comparison
from src.database import save_run
ROOT=Path(__file__).resolve().parent; OUT=ROOT/"outputs"/"advanced"
def main():
    OUT.mkdir(parents=True,exist_ok=True); data=build_economic_dataset(load_production(),load_brent_prices()); a=EconomicAssumptions(); evaluated=evaluate_cash_flow(data,a); fields=field_economic_summary(evaluated)
    evaluated.to_csv(OUT/"monthly_cash_flow.csv",index=False); fields.to_csv(OUT/"field_economic_summary.csv",index=False); scenario_comparison(data).to_csv(OUT/"scenario_comparison.csv",index=False); monte_carlo_portfolio(data,a,1000).to_csv(OUT/"monte_carlo_portfolio.csv",index=False)
    run=save_run(OUT/"economic_runs.sqlite","base",a,fields.discounted_cash_flow_usd.sum(),len(fields)); print(f"Completed economic run {run}: {len(fields):,} fields")
if __name__=="__main__": main()
