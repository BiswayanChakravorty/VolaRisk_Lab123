"""Core vectorized risk metrics for VolaRisk Lab."""

from __future__ import annotations

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def log_returns(prices: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Compute continuously compounded returns from price levels."""
    if (prices <= 0).any().any() if isinstance(prices, pd.DataFrame) else (prices <= 0).any():
        raise ValueError("prices must be strictly positive to compute log returns")
    return np.log(prices / prices.shift(1)).dropna()


def annualized_volatility(returns: pd.Series | pd.DataFrame, periods: int = TRADING_DAYS):
    """Annualize return volatility using the square-root-of-time convention."""
    return returns.std(ddof=1) * np.sqrt(periods)


def max_drawdown(prices: pd.Series) -> float:
    """Return the maximum peak-to-trough drawdown as a negative percentage."""
    running_peak = prices.cummax()
    drawdown = prices / running_peak - 1.0
    return float(drawdown.min())


def beta(asset_returns: pd.Series, market_returns: pd.Series) -> float:
    """Estimate static CAPM beta via covariance(asset, market) / variance(market)."""
    aligned = pd.concat([asset_returns, market_returns], axis=1).dropna()
    if aligned.shape[0] < 2:
        raise ValueError("at least two aligned observations are required")
    asset = aligned.iloc[:, 0]
    market = aligned.iloc[:, 1]
    market_variance = market.var(ddof=1)
    if market_variance == 0:
        raise ValueError("market return variance cannot be zero")
    return float(asset.cov(market) / market_variance)
