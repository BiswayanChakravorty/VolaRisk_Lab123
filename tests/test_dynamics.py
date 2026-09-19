import pandas as pd
import pytest

from src.analytics.dynamics import garch_11_variance


def test_garch_variance_is_positive_and_indexed():
    returns = pd.Series([0.01, -0.02, 0.015], index=pd.date_range("2026-01-01", periods=3))
    variance = garch_11_variance(returns, omega=1e-6, alpha=0.1, beta=0.8)

    assert len(variance) == len(returns)
    assert variance.index.equals(returns.index)
    assert (variance > 0).all()


def test_garch_rejects_unstable_parameters():
    returns = pd.Series([0.01, 0.02])
    with pytest.raises(ValueError, match="alpha \+ beta < 1"):
        garch_11_variance(returns, alpha=0.6, beta=0.4)
