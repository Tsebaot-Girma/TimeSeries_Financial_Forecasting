import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    for ticker in data.keys():
        # Plot closing prices
        plt.figure(figsize=(10, 5))
        plt.plot(data[ticker]['Close'], label=f'{ticker} Closing Price')
        plt.title(f'{ticker} Closing Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

def calculate_daily_change(data):
    for ticker in data.keys():
        data[ticker]['Daily Change'] = data[ticker]['Close'].pct_change()
        plt.figure(figsize=(10, 5))
        plt.plot(data[ticker]['Daily Change'], label=f'{ticker} Daily Change')
        plt.title(f'{ticker} Daily Percentage Change')
        plt.xlabel('Date')
        plt.ylabel('Daily Change')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    from data_cleaning import cleaned_data
    visualize_data(cleaned_data)
    calculate_daily_change(cleaned_data)