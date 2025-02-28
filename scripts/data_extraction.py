import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    TICKERS = ['TSLA', 'BND', 'SPY']
    START_DATE = '2015-01-01'
    END_DATE = '2025-01-31'
    historical_data = fetch_data(TICKERS, START_DATE, END_DATE)




