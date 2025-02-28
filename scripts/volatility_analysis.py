import matplotlib.pyplot as plt
import seaborn as sns



def analyze_volatility(data):
    for ticker in data.keys():
        data[ticker]['Rolling Mean'] = data[ticker]['Close'].rolling(window=30).mean()
        data[ticker]['Rolling Std'] = data[ticker]['Close'].rolling(window=30).std()

        plt.figure(figsize=(10, 5))
        plt.plot(data[ticker]['Rolling Mean'], label='30-Day Rolling Mean')
        plt.plot(data[ticker]['Rolling Std'], label='30-Day Rolling Std')
        plt.title(f'Volatility Analysis for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        # Outlier detection
        outliers = data[ticker][(data[ticker]['Daily Change'] > 0.1) | (data[ticker]['Daily Change'] < -0.1)]
        print(f'Outliers for {ticker}:\n{outliers}')

if __name__ == "__main__":
    from data_cleaning import cleaned_data
    analyze_volatility(cleaned_data)