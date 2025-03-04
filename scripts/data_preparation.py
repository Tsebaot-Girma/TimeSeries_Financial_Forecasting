#scripts/data_preparation
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return data

def plot_time_series(data, title='Time Series Data', xlabel='Date', ylabel='Price'):
    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Prices')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()