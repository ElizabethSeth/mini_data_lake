DuckDB Data Pipeline – Flask + Streamlit

Small end-to-end data pipeline to ingest, analyze, visualize, and persist datasets with DuckDB, Pandas, and Streamlit.
Optionally includes a Flask app already present in the repo.

✨ Features

Upload CSV / JSON / Excel / Parquet

Quick EDA: uniques / nulls / zeros per column

Auto histograms for first numeric columns

Save data to Parquet and to DuckDB (outputs/output.duckdb)

Optional SQL on the in-memory DataFrame via DuckDB

Dockerized
Schema project



├── app/
│   ├── logic/
│   │   ├── __init__.py
│   │   ├── file_loader.py        # load_file()
│   │   ├── etl_utils.py          # analyze_dataframe()
│   │   ├── save_utils.py         # save_parquet(), save_duckdb()
│   │   └── viz_utils.py          # generate_graphs()
│   ├── templates/                # Flask templates (if you run Flask)
│   └── __init__.py               # Flask factory (optional)
├── app_streamlit.py              # Streamlit UI
├── run.py                        # Flask entrypoint (optional)
├── requirements.txt
├── docker-compose.yml
├── Dockerfile                    # base image (used by both services)
├── Dockerfile.streamlit          # (if you chose separate files)
├── uploads/                      # user uploads  (mounted volume)
├── outputs/                      # parquet/duckdb (mounted volume)
└── app/static/                   # saved charts  (mounted volume)
