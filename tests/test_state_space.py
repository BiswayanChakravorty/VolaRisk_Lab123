import numpy as np
import pandas as pd
import pytest

from src.analytics.state_space import kalman_beta, kalman_beta_vectorized


def test_kalman_beta_alias_matches_vectorized():
    market = pd.Series([0.01, -0.02, 0.03, 0.015])
    asset = 1.5 * market

    expected = kalman_beta_vectorized(asset, market)
    actual = kalman_beta(asset, market)

    assert np.allclose(actual.to_numpy(), expected.to_numpy())


def test_kalman_rejects_invalid_variances():
    returns = pd.Series([0.01, 0.02])
    with pytest.raises(ValueError, match="variances must be positive"):
        kalman_beta_vectorized(returns, returns, process_variance=0)
