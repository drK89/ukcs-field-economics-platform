from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "processed" / "field_month_economics.csv"
SUMMARY = ROOT / "outputs" / "tables" / "field_summary.csv"
OPERATORS = ROOT / "outputs" / "tables" / "operator_summary.csv"

st.set_page_config(page_title="UKCS Field Economics L1", layout="wide")
st.title("UKCS Field Economics and Operational Transparency")
st.caption("Official field production plus EIA Brent benchmark, 2021-2025")

if not DATA.exists():
    st.error("Run `python run_analysis.py` before opening the dashboard.")
    st.stop()

data = pd.read_csv(DATA, parse_dates=["date"])
summary = pd.read_csv(SUMMARY)
operators = pd.read_csv(OPERATORS)

field_options = sorted(data["field_name"].dropna().unique())
selected_fields = st.sidebar.multiselect("Fields", field_options, default=field_options[:5])
year_range = st.sidebar.slider("Years", 2021, 2025, (2021, 2025))

filtered = data[data["year"].between(*year_range)]
if selected_fields:
    filtered = filtered[filtered["field_name"].isin(selected_fields)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Field-month records", f"{len(filtered):,}")
c2.metric("Oil production", f"{filtered['oil_bbl'].sum()/1e6:,.1f} MMbbl")
c3.metric("Gross revenue proxy", f"${filtered['gross_revenue_proxy_usd'].sum()/1e9:,.2f} bn")
c4.metric("Average Brent", f"${filtered['brent_usd_per_bbl'].mean():,.2f}/bbl")

st.subheader("Monthly oil production")
monthly = filtered.groupby("date", as_index=False)["oil_bbl"].sum().set_index("date")
st.line_chart(monthly / 1e6, y_label="Million bbl")

st.subheader("Field comparison")
comparison = (
    filtered.groupby("field_name", as_index=False)
    .agg(
        oil_bbl=("oil_bbl", "sum"),
        gross_revenue_proxy_usd=("gross_revenue_proxy_usd", "sum"),
        gas_flared_ksm3=("gas_flared_ksm3", "sum"),
        water_produced_m3=("water_produced_m3", "sum"),
    )
    .sort_values("oil_bbl", ascending=False)
)
st.dataframe(comparison, use_container_width=True, hide_index=True)

st.subheader("Portfolio reference table")
st.dataframe(summary.head(30), use_container_width=True, hide_index=True)

st.subheader("Operator comparison")
st.dataframe(operators, use_container_width=True, hide_index=True)

st.info(
    "The revenue figure is a transparent benchmark proxy: monthly oil volume multiplied by "
    "the monthly Brent spot price. It excludes realised price differentials, gas revenue, "
    "tax, royalties, transport, capital expenditure and operating expenditure."
)
