def clean_data(data):
    for ticker in data.keys():
        # Check data types and missing values
        print(f"Data types for {ticker}:\n{data[ticker].dtypes}")
        print(f"Missing values for {ticker}:\n{data[ticker].isnull().sum()}")
        
        # Handle missing values
        data[ticker].fillna(method='ffill', inplace=True)

        # Normalize data if needed
        data[ticker]['Close'] = (data[ticker]['Close'] - data[ticker]['Close'].mean()) / data[ticker]['Close'].std()

    return data



if __name__ == "__main__":
    # Assume data is imported from the previous script
    from data_extraction import historical_data
    cleaned_data = clean_data(historical_data)

