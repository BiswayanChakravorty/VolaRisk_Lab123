.PHONY: install test compile run

install:
	python -m pip install -r requirements.txt

test:
	pytest

compile:
	python -m py_compile src/analytics/basic_risk.py src/analytics/dynamics.py src/analytics/state_space.py src/ingestion.py src/dashboard.py

run:
	streamlit run src/dashboard.py
