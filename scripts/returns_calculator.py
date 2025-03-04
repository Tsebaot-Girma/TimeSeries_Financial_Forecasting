import pandas as pd

def calculate_daily_returns(data):
    return data.pct_change().dropna()