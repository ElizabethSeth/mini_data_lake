import os

def save_parquet(df):
    try:
        df.to_parquet(os.path.join('outputs', 'output.parquet'))
        return True
    except:
        return False

def save_duckdb(df):
    try:
        import duckdb
        con = duckdb.connect(database='outputs/output.duckdb', read_only=False)
        con.execute("CREATE TABLE IF NOT EXISTS data AS SELECT * FROM df")
        con.close()
        return True
    except:
        return False