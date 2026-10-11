import streamlit as st
from src.data import load_production,load_brent_prices,build_economic_dataset
from src.economics import EconomicAssumptions,evaluate_cash_flow,field_economic_summary,monte_carlo_portfolio
st.set_page_config(page_title="UKCS Field Economics",layout="wide"); st.title("UKCS Field Economics Platform"); st.caption("Public-data screening model — not a reserves report or investment valuation")
p=st.sidebar.slider("Price multiplier",.5,1.5,1.,.05); o=st.sidebar.slider("Variable OPEX (USD/bbl)",5,60,25); t=st.sidebar.slider("Tax proxy",0.,.8,.4,.05); a=EconomicAssumptions(price_multiplier=p,variable_opex_usd_per_bbl=float(o),tax_rate=t)
data=build_economic_dataset(load_production(),load_brent_prices()); s=field_economic_summary(evaluate_cash_flow(data,a)); c=st.columns(3); c[0].metric("Fields",len(s)); c[1].metric("Value proxy",f"${s.discounted_cash_flow_usd.sum()/1e9:,.1f}bn"); c[2].metric("Flagged",int((s.risk_flag!="screen-positive").sum())); st.dataframe(s,use_container_width=True); st.bar_chart(s.head(20).set_index("field_name").discounted_cash_flow_usd)
if st.button("Run stress test"):
    mc=monte_carlo_portfolio(data,a,500); st.line_chart(mc.set_index("simulation").portfolio_value_usd); st.download_button("Download",mc.to_csv(index=False),"monte_carlo.csv")
