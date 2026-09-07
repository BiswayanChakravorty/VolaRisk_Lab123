"""Streamlit interface for VolaRisk Lab."""

from __future__ import annotations

import datetime as dt

import streamlit as st

from src.config import DEFAULT_START, DEFAULT_TICKERS
from src.ingestion import fetch_adjusted_close
from src.analytics.basic_risk import annualized_volatility, log_returns, max_drawdown
from src.analytics.dynamics import garch_11_variance

st.set_page_config(page_title="VolaRisk Lab", layout="wide")
st.title("VolaRisk Lab: Dynamic Portfolio Risk Engine")

tickers = st.text_input("Tickers", ",".join(DEFAULT_TICKERS))
start = st.date_input("Start date", value=dt.date.fromisoformat(DEFAULT_START))

if st.button("Run risk analysis"):
    symbols = [ticker.strip().upper() for ticker in tickers.split(",") if ticker.strip()]
    try:
        if not symbols:
            st.error("Please enter at least one ticker")
        elif start > dt.date.today():
            st.error("Start date cannot be in the future")
        else:
            prices = fetch_adjusted_close(symbols, start=str(start))
            if prices.empty:
                st.error(f"No data found for {symbols} in the given date range")
            else:
                returns = log_returns(prices)
                st.subheader("Adjusted Close")
                st.line_chart(prices)
                st.subheader("Annualized Volatility")
                st.dataframe(annualized_volatility(returns).to_frame("volatility"))
                st.subheader("Maximum Drawdown")
                st.dataframe(prices.apply(max_drawdown).to_frame("max_drawdown"))
                st.subheader("GARCH(1,1) Variance Prototype")
                st.line_chart(garch_11_variance(returns.iloc[:, 0]))
    except ValueError as exc:
        st.error(f"Data error: {exc}")
    except Exception as exc:
        st.error(f"Unexpected error: {exc}")
