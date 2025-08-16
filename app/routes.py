from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from .logic import file_loader, etl_utils, save_utils, viz_utils

main = Blueprint('main', __name__)

df = pd.DataFrame()

@main.route('/', methods=['GET', 'POST'])
def index():
    global df
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            df = file_loader.load_file(filepath)
            if df is not None:
                flash('File uploaded successfully!', 'success')
                return redirect(url_for('main.preview'))
            else:
                flash('Unsupported or invalid file format.', 'danger')
    return render_template('index.html')

@main.route('/preview')
def preview():
    global df
    rows, cols = df.shape
    preview_data = df.iloc[:10, :15].to_html(classes='table table-striped', index=False)
    return render_template('table.html', rows=rows, cols=cols, table=preview_data)

@main.route('/etl', methods=['GET', 'POST'])
def etl():
    global df
    stats = etl_utils.analyze_dataframe(df)
    if request.method == 'POST':
        drop_cols = request.form.getlist('drop')
        df.drop(columns=drop_cols, inplace=True)
        flash('Selected columns dropped.', 'success')
    return render_template('etl.html', stats=stats)

@main.route('/save/<fmt>')
def save(fmt):
    global df
    if fmt == 'parquet':
        result = save_utils.save_parquet(df)
    elif fmt == 'duckdb':
        result = save_utils.save_duckdb(df)
    else:
        result = False
    flash('Saved successfully!' if result else 'Save failed.', 'success' if result else 'danger')
    return redirect(url_for('main.preview'))

@main.route('/analytics')
def analytics():
    global df
    graphs = viz_utils.generate_graphs(df)
    return render_template('result.html', graphs=graphs)