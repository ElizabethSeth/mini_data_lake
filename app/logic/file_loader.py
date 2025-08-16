import pandas as pd
import os

def load_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    try:
        if ext in ['.csv', '.txt']:
            return pd.read_csv(filepath)
        elif ext == '.json':
            return pd.read_json(filepath)
        elif ext in ['.xls', '.xlsx']:
            return pd.read_excel(filepath)
        elif ext == '.parquet':
            return pd.read_parquet(filepath)
        else:
            return None
    except Exception as e:
        print(f"Load error: {e}")
        return None