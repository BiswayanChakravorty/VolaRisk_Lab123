"""Shared configuration constants for VolaRisk Lab."""

TRADING_DAYS = 252
DEFAULT_TICKERS = ["AAPL", "MSFT", "SPY"]
DEFAULT_START = "2020-01-01"

# GARCH(1,1) parameters
GARCH_OMEGA = 0.000001
GARCH_ALPHA = 0.08
GARCH_BETA = 0.90

# Kalman filter parameters
KALMAN_PROCESS_VAR = 1e-5
KALMAN_MEASUREMENT_VAR = 1e-3
