DuckDB Data Pipeline — Flask + Streamlit

Small end-to-end data pipeline to ingest, analyze, visualize, and persist datasets with DuckDB, Pandas, and Streamlit.
The repo also includes a (optional) Flask app.

✨ Features

Upload CSV / JSON / Excel / Parquet

Quick EDA: uniques / nulls / zeros per column

Auto histograms for first numeric columns

Save to Parquet and DuckDB (outputs/output.duckdb)

Optional SQL on the in-memory DataFrame via DuckDB

Dockerized, with persistent volumes for uploads/outputs/static

🗂️ Project structure
.
├─ app/
│  ├─ logic/
│  │  ├─ __init__.py
│  │  ├─ file_loader.py      # load_file()
│  │  ├─ etl_utils.py        # analyze_dataframe()
│  │  ├─ save_utils.py       # save_parquet(), save_duckdb()
│  │  └─ viz_utils.py        # generate_graphs()
│  ├─ templates/             # Flask templates (optional)
│  └─ __init__.py            # Flask factory (optional)
├─ app_streamlit.py          # Streamlit UI
├─ run.py                    # Flask entrypoint (optional)
├─ requirements.txt
├─ docker-compose.yml
├─ Dockerfile                # base image (can be used by both services)
├─ Dockerfile.streamlit      # optional separate Dockerfile for Streamlit
├─ uploads/                  # user uploads  (mounted volume)
├─ outputs/                  # parquet/duckdb (mounted volume)
└─ app/static/               # saved charts  (mounted volume)

🚀 Quickstart (Docker)

Note: Modern Compose ignores the version: key. Remove it if you see a warning.

Streamlit only
docker compose build --no-cache
docker compose up


Open: http://localhost:8501

Streamlit + Flask (if enabled in compose)

Streamlit → http://localhost:8501

Flask → http://localhost:5000
