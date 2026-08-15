"""Market data ingestion helpers."""

from __future__ import annotations

import pandas as pd
import yfinance as yf


def fetch_adjusted_close(tickers: list[str], start: str, end: str | None = None) -> pd.DataFrame:
    """Fetch adjusted close prices for one or more tickers from Yahoo Finance."""
    if not tickers:
        raise ValueError("provide at least one ticker")
    data = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
    closes = data["Close"] if "Close" in data else data
    if isinstance(closes, pd.Series):
        closes = closes.to_frame(tickers[0])
    return closes.dropna(how="all")
