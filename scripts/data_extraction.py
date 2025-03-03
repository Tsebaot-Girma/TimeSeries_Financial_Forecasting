import yfinance as yf
import pandas as pd
import os

def fetch_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)
    return data

def save_to_csv(data, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the folder if it doesn't exist
    for ticker, df in data.items():
        file_path = os.path.join(folder_path, f"{ticker}_historical_data.csv")
        df.to_csv(file_path)
        print(f"Saved {ticker} data to {file_path}")

if __name__ == "__main__":
    TICKERS = ['TSLA', 'BND', 'SPY']
    START_DATE = '2015-01-01'
    END_DATE = '2025-01-31'
    historical_data = fetch_data(TICKERS, START_DATE, END_DATE)

    # Save the historical data to CSV files
    save_to_csv(historical_data, 'data')