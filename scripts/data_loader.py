import pandas as pd

def load_data(file_path, column_name):
    data = pd.read_csv(file_path, parse_dates=True, index_col='Date')
    return data[column_name]

def load_all_data(tsla_file, bnd_file, spy_file):
    tsla_data = load_data(tsla_file, 'Close')
    bnd_data = load_data(bnd_file, 'Close')
    spy_data = load_data(spy_file, 'Close')
    return tsla_data, bnd_data, spy_data