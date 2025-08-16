def analyze_dataframe(df):
    stats = {}
    for col in df.columns:
        stats[col] = {
            'unique': df[col].nunique(),
            'nulls': df[col].isnull().sum(),
            'zeros': (df[col] == 0).sum() if df[col].dtype != 'O' else 'N/A'
        }
    return stats