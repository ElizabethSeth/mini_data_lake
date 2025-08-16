### DuckDB Data Pipeline — Flask + Streamlit

Small end-to-end data pipeline to ingest, analyze, visualize, and persist datasets with DuckDB, Pandas, and Streamlit.
The repo also includes a (optional) Flask app.

✨ Features

Upload CSV / JSON / Excel / Parquet

Quick EDA: uniques / nulls / zeros per column

Auto histograms for first numeric columns

Save to Parquet and DuckDB (outputs/output.duckdb)

Optional SQL on the in-memory DataFrame via DuckDB

Dockerized, with persistent volumes for uploads/outputs/static

### 🗂️ Project structure
<img width="587" height="407" alt="image" src="https://github.com/user-attachments/assets/82538765-7c69-433f-906d-f64a464f941a" />


#### 🚀 Quickstart (Docker)

Note: Modern Compose ignores the version: key. Remove it if you see a warning.

### Streamlit only
docker compose build --no-cache
docker compose up


Open: http://localhost:8501

Streamlit + Flask (if enabled in compose)

Streamlit → http://localhost:8501

Flask → http://localhost:5000
