import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_graphs(df):
    graphs = []
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    for col in numeric_cols[:3]:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        path = f'static/{col}_hist.png'
        plt.savefig(f'app/{path}')
        graphs.append(path)
    return graphs