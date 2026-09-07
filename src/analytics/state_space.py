"""State-space estimators for dynamic market exposure."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.config import KALMAN_MEASUREMENT_VAR, KALMAN_PROCESS_VAR


def kalman_beta_vectorized(
    asset_returns: pd.Series,
    market_returns: pd.Series,
    process_variance: float = KALMAN_PROCESS_VAR,
    measurement_variance: float = KALMAN_MEASUREMENT_VAR,
    initial_beta: float = 1.0,
    initial_covariance: float = 1.0,
) -> pd.Series:
    """Estimate time-varying beta using an efficient NumPy-backed filter."""
    if process_variance <= 0 or measurement_variance <= 0:
        raise ValueError("Kalman variances must be positive")
    if initial_covariance < 0:
        raise ValueError("initial covariance must be non-negative")

    data = pd.concat([asset_returns, market_returns], axis=1).dropna()
    data.columns = ["asset", "market"]
    if data.empty:
        return pd.Series(dtype=float, index=data.index, name="kalman_beta")

    market = data["market"].to_numpy(dtype=float)
    asset = data["asset"].to_numpy(dtype=float)
    estimates = np.empty(len(data), dtype=float)
    covariance = float(initial_covariance)
    beta_state = float(initial_beta)

    for i, (asset_observation, market_observation) in enumerate(zip(asset, market)):
        covariance += process_variance
        innovation = asset_observation - market_observation * beta_state
        innovation_variance = market_observation**2 * covariance + measurement_variance
        kalman_gain = covariance * market_observation / innovation_variance
        beta_state += kalman_gain * innovation
        covariance = (1 - kalman_gain * market_observation) * covariance
        estimates[i] = beta_state

    return pd.Series(estimates, index=data.index, name="kalman_beta")


def kalman_beta(
    asset_returns: pd.Series,
    market_returns: pd.Series,
    process_variance: float = KALMAN_PROCESS_VAR,
    measurement_variance: float = KALMAN_MEASUREMENT_VAR,
    initial_beta: float = 1.0,
    initial_covariance: float = 1.0,
) -> pd.Series:
    """Backward-compatible alias for :func:`kalman_beta_vectorized`."""
    return kalman_beta_vectorized(
        asset_returns, market_returns, process_variance, measurement_variance,
        initial_beta, initial_covariance,
    )
