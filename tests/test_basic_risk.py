import numpy as np
import pandas as pd
import pytest

from src.analytics.basic_risk import annualized_volatility, beta, log_returns, max_drawdown


def test_log_returns_and_volatility():
    prices = pd.Series([100.0, 110.0, 121.0], index=pd.date_range("2026-01-01", periods=3))
    returns = log_returns(prices)

    assert np.allclose(returns.to_numpy(), [np.log(1.1), np.log(1.1)])
    assert annualized_volatility(returns, periods=1) == pytest.approx(returns.std())


def test_log_returns_rejects_non_positive_prices():
    with pytest.raises(ValueError, match="strictly positive"):
        log_returns(pd.Series([100.0, 0.0, 110.0]))


def test_max_drawdown():
    prices = pd.Series([100.0, 120.0, 90.0, 95.0])
    assert max_drawdown(prices) == pytest.approx(-0.25)


def test_beta():
    market = pd.Series([0.01, -0.02, 0.03, 0.01])
    asset = 2.0 * market
    assert beta(asset, market) == pytest.approx(2.0)
