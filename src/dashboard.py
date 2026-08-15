"""Streamlit interface for VolaRisk Lab."""

from __future__ import annotations

import streamlit as st

from ingestion import fetch_adjusted_close
from analytics.basic_risk import annualized_volatility, log_returns, max_drawdown
from analytics.dynamics import garch_11_variance

st.set_page_config(page_title="VolaRisk Lab", layout="wide")
st.title("VolaRisk Lab: Dynamic Portfolio Risk Engine")

tickers = st.text_input("Tickers", "AAPL,MSFT,SPY")
start = st.date_input("Start date")

if st.button("Run risk analysis"):
    symbols = [ticker.strip().upper() for ticker in tickers.split(",") if ticker.strip()]
    prices = fetch_adjusted_close(symbols, start=str(start))
    returns = log_returns(prices)
    st.subheader("Adjusted Close")
    st.line_chart(prices)
    st.subheader("Annualized Volatility")
    st.dataframe(annualized_volatility(returns).to_frame("volatility"))
    st.subheader("Maximum Drawdown")
    st.dataframe(prices.apply(max_drawdown).to_frame("max_drawdown"))
    st.subheader("GARCH(1,1) Variance Prototype")
    st.line_chart(garch_11_variance(returns.iloc[:, 0]))
