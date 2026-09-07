import numpy as np
import pandas as pd
import pytest

from src.analytics.basic_risk import beta, log_returns, max_drawdown
from src.analytics.dynamics import garch_11_variance
from src.analytics.state_space import kalman_beta


def test_log_returns_matches_numpy():
    prices = pd.Series([100.0, 105.0, 110.0])
    result = log_returns(prices)
    assert np.allclose(result.values, np.log(prices / prices.shift(1)).dropna().values)


def test_log_returns_rejects_non_positive_prices():
    with pytest.raises(ValueError):
        log_returns(pd.Series([100.0, -105.0, 110.0]))


def test_max_drawdown_peak_to_trough():
    prices = pd.Series([100.0, 120.0, 90.0, 110.0])
    assert max_drawdown(prices) == -0.25


def test_beta_for_two_x_asset():
    market = pd.Series([0.01, -0.02, 0.03, -0.01])
    asset = 2 * market
    assert np.isclose(beta(asset, market), 2.0)


def test_beta_rejects_zero_market_variance():
    market = pd.Series([0.01, 0.01, 0.01])
    asset = pd.Series([0.02, 0.02, 0.02])
    with pytest.raises(ValueError):
        beta(asset, market)


def test_garch_variance_positive():
    returns = pd.Series([0.01, -0.02, 0.015, -0.005])
    variance = garch_11_variance(returns)
    assert (variance > 0).all()


def test_kalman_beta_returns_aligned_series():
    market = pd.Series([0.01, -0.02, 0.03])
    asset = 1.5 * market
    estimates = kalman_beta(asset, market)
    assert len(estimates) == 3


def test_kalman_beta_drops_missing_observations():
    market = pd.Series([0.01, np.nan, 0.03])
    asset = pd.Series([0.02, 0.02, np.nan])
    result = kalman_beta(asset, market)
    assert len(result) == 1
