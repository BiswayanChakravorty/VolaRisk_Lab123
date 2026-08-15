"""Forward-looking volatility models."""

from __future__ import annotations

import numpy as np
import pandas as pd


def garch_11_variance(
    returns: pd.Series,
    omega: float = 0.000001,
    alpha: float = 0.08,
    beta: float = 0.90,
) -> pd.Series:
    """Compute a transparent GARCH(1,1) conditional variance path.

    This deterministic implementation is designed for education and dashboards;
    production calibration can replace the default parameters with MLE estimates.
    """
    if alpha < 0 or beta < 0 or omega <= 0 or alpha + beta >= 1:
        raise ValueError("require omega > 0, alpha >= 0, beta >= 0, and alpha + beta < 1")

    clean_returns = returns.dropna()
    if clean_returns.empty:
        raise ValueError("returns cannot be empty")

    variances = np.empty(len(clean_returns))
    variances[0] = clean_returns.var(ddof=1) if len(clean_returns) > 1 else omega / (1 - alpha - beta)

    for idx in range(1, len(clean_returns)):
        shock = clean_returns.iloc[idx - 1] ** 2
        variances[idx] = omega + alpha * shock + beta * variances[idx - 1]

    return pd.Series(variances, index=clean_returns.index, name="garch_variance")
