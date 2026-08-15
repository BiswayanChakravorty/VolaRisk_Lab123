# GitHub Deployment Guide

Use this checklist to publish VolaRisk Lab to your own GitHub repository and make it visible on your LinkedIn profile.

## 1. Create the GitHub repository

1. Go to GitHub and create a new public repository named `VolaRisk_Lab123` or `vola-risk-lab`.
2. Do not initialize it with a README, because this project already includes one.
3. Copy the repository URL. It will look like one of these:
   - `https://github.com/<your-user>/VolaRisk_Lab123.git`
   - `git@github.com:<your-user>/VolaRisk_Lab123.git`

## 2. Connect this local project to GitHub

```bash
git remote add origin https://github.com/<your-user>/VolaRisk_Lab123.git
git branch -M main
git push -u origin main
```

If `origin` already exists, update it instead:

```bash
git remote set-url origin https://github.com/<your-user>/VolaRisk_Lab123.git
git push -u origin main
```

## 3. Verify the GitHub showcase quality

Before sharing the project, confirm that:

```bash
make compile
make test
```

Then check that GitHub Actions passes on the repository page.

## 4. Optional Streamlit Community Cloud deployment

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Select this repository.
4. Set the app entry point to:

```text
src/dashboard.py
```

5. Deploy the app and copy the public URL into the GitHub repository description and your LinkedIn Featured section.

## 5. LinkedIn headline / featured description

```text
VolaRisk Lab — Python quantitative finance risk engine with GARCH(1,1) volatility, Kalman-filter beta tracking, vectorized drawdown analytics, tests, CI, and Streamlit dashboard.
```
