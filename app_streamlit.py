import streamlit as st
import pandas as pd
from app.logic.file_loader import load_file
from app.logic.etl_utils import analyze_dataframe
from app.logic.save_utils import save_parquet, save_duckdb
from app.logic.viz_utils import generate_graphs
import os

st.set_page_config(page_title="Data Pipeline App", layout="wide")

st.title("🚀 Mini Data Pipeline avec Streamlit")

st.sidebar.header("1. Charger un fichier")
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier (csv, json, xlsx, parquet)", type=["csv", "json", "xlsx", "xls", "parquet"])

if uploaded_file:
    with open(f"uploads/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    filepath = f"uploads/{uploaded_file.name}"

    df = load_file(filepath)

    if df is not None:
        st.success(f"✅ Fichier chargé : {uploaded_file.name}")
        st.write("Aperçu des données :", df.head())

        # --- Analyse exploratoire ---
        st.sidebar.header("2. Analyse exploratoire")
        if st.sidebar.button("Analyser le dataset"):
            stats = analyze_dataframe(df)
            st.subheader("📊 Statistiques de base")
            st.json(stats)

        # --- Visualisation ---
        st.sidebar.header("3. Génération de graphes")
        if st.sidebar.button("Créer des visualisations"):
            os.makedirs("app/static", exist_ok=True)
            graphs = generate_graphs(df)
            st.subheader("📈 Graphiques générés")
            for g in graphs:
                st.image(f"app/{g}")

        # --- Sauvegarde ---
        st.sidebar.header("4. Sauvegarder les données")
        if st.sidebar.button("Enregistrer en Parquet"):
            if save_parquet(df):
                st.success("✅ Données sauvegardées en outputs/output.parquet")
        if st.sidebar.button("Enregistrer en DuckDB"):
            if save_duckdb(df):
                st.success("✅ Données sauvegardées en outputs/output.duckdb")
    else:
        st.error("Erreur de chargement du fichier")
else:
    st.info("⬅️ Chargez un fichier depuis la barre latérale pour commencer")
