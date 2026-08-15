# VolaRisk Lab: Dynamic Portfolio Risk & State-Space Engine

**VolaRisk Lab** is an intermediate quantitative risk analytics framework that upgrades simple historical stock dashboards into a modular, testable Python project. It combines traditional market-risk reporting with forward-looking volatility modeling and an Electrical Engineering-inspired state-space approach for dynamic beta tracking.

## Why this project stands out

Entry-level finance projects usually stop at price charts, daily returns, and static volatility. VolaRisk Lab is structured as a recruiter-friendly quant repository with:

- vectorized risk metrics for volatility, beta, and maximum drawdown;
- a transparent GARCH(1,1) conditional variance engine;
- a one-state Kalman filter for time-varying systematic risk;
- a Streamlit dashboard for interactive analysis;
- unit tests and CI to show software-engineering discipline.

## Repository structure

```text
vola-risk-lab/
├── .github/workflows/       # CI pipeline for automated tests
├── data/                    # Optional local cache or sample market data
├── notebooks/               # Research notebooks and experiments
├── src/                     # Core application source code
│   ├── __init__.py
│   ├── ingestion.py         # Market data fetching helpers
│   ├── dashboard.py         # Streamlit interface
│   └── analytics/           # Mathematical/statistical engines
│       ├── __init__.py
│       ├── basic_risk.py    # Log returns, volatility, beta, drawdown
│       ├── dynamics.py      # GARCH(1,1) conditional variance
│       └── state_space.py   # Kalman filter beta estimator
├── tests/                   # Unit tests for analytics engines
├── requirements.txt         # Runtime and test dependencies
└── README.md
```

## Mathematical foundations

### 1. GARCH(1,1) volatility clustering

Financial returns often display volatility clustering: large shocks tend to be followed by large shocks. VolaRisk Lab models the conditional variance path as:

```math
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
```

where `omega` is the long-run variance baseline, `alpha` controls sensitivity to recent shocks, and `beta` controls persistence.

### 2. Kalman filter for time-varying beta

Instead of assuming one fixed CAPM beta, the project treats beta as a hidden state that evolves over time:

```math
R_{i,t} = \beta_t R_{m,t} + v_t
```

```math
\beta_t = \beta_{t-1} + w_t
```

This creates a clean bridge between Electrical Engineering signal processing and quantitative finance.

### 3. Maximum drawdown

Maximum drawdown measures the worst historical peak-to-trough capital loss:

```math
MDD = \min_t \left(\frac{P_t}{\max_{s \le t} P_s} - 1\right)
```

## System architecture

```text
[Yahoo Finance / CSV Data]
          |
          v
[Data Ingestion + Cleaning]
          |
          v
[Log Return Transformation]
          |
          +--> [Basic Risk Metrics: Volatility, Beta, Drawdown]
          |
          +--> [Dynamic Volatility: GARCH(1,1)]
          |
          +--> [State-Space Risk: Kalman Beta]
          |
          v
[Streamlit Dashboard + Tables + Charts]
```

## Quick start

```bash
git clone <your-repository-url>
cd vola-risk-lab
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
streamlit run src/dashboard.py
```

## Suggested LinkedIn positioning

> Built VolaRisk Lab, a Python-based quantitative risk engine implementing vectorized drawdown analytics, GARCH(1,1) volatility modeling, and Kalman-filter beta estimation, with tests and CI for reproducible finance research.

## Roadmap

- Add maximum-likelihood estimation for GARCH parameters.
- Add portfolio-level risk attribution and marginal contribution to risk.
- Add CSV upload support to the dashboard.
- Add a research notebook comparing static rolling beta vs. Kalman beta.
