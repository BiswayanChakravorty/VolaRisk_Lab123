# GitHub Pages Demo

The `github-pages-demo` branch contains a self-contained browser demo of VolaRisk Lab. It is intentionally separate from the Python/Streamlit `main` branch because GitHub Pages serves static files and cannot run a Python backend.

## What works in the demo

The page runs the risk calculations locally in the browser: log returns, annualized volatility, maximum drawdown, CAPM beta, GARCH(1,1) variance, and a one-state Kalman beta estimate. It includes scenario controls, responsive charts, asset-level risk breakdown, CSV upload, and CSV report download. The default scenarios use deterministic synthetic data so the public demo is reproducible and does not depend on Yahoo Finance, a server, or an API key.

## Enable Pages once

1. Open the repository **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Push to `github-pages-demo` or manually run the **Deploy browser demo to GitHub Pages** workflow.
4. GitHub will publish the site at `https://biswayanchakravorty.github.io/VolaRisk_Lab123/`.

The workflow runs the browser analytics tests before deployment. The Python Streamlit application remains available from `main` for a full data-connected deployment through Streamlit Community Cloud.

## CSV format

Upload a CSV with at least three rows and these columns:

```csv
Date,Asset,Market
2025-01-01,100,100
2025-01-02,101,100.5
2025-01-03,99,101
```

`Date` is optional for calculation but is accepted for readability. Prices must be positive.
