"""State-space estimators for dynamic market exposure."""

from __future__ import annotations

import pandas as pd


def kalman_beta(
    asset_returns: pd.Series,
    market_returns: pd.Series,
    process_variance: float = 1e-5,
    measurement_variance: float = 1e-3,
    initial_beta: float = 1.0,
    initial_covariance: float = 1.0,
) -> pd.Series:
    """Estimate time-varying beta with a one-state Kalman filter."""
    if process_variance <= 0 or measurement_variance <= 0:
        raise ValueError("Kalman variances must be positive")

    data = pd.concat([asset_returns, market_returns], axis=1).dropna()
    data.columns = ["asset", "market"]
    beta_state = initial_beta
    covariance = initial_covariance
    estimates: list[float] = []

    for _, row in data.iterrows():
        covariance += process_variance
        observation_matrix = row["market"]
        innovation = row["asset"] - observation_matrix * beta_state
        innovation_variance = observation_matrix**2 * covariance + measurement_variance
        kalman_gain = covariance * observation_matrix / innovation_variance
        beta_state += kalman_gain * innovation
        covariance = (1 - kalman_gain * observation_matrix) * covariance
        estimates.append(float(beta_state))

    return pd.Series(estimates, index=data.index, name="kalman_beta")
