import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

def forecast_prices(model_fit, steps):
    return model_fit.forecast(steps=steps)

def forecast_sarima(model_fit, steps):
    return model_fit.forecast(steps=steps)

def forecast_lstm(model, scaler, test_data, time_step=10):
    test_scaled = scaler.transform(test_data.values.reshape(-1, 1))
    X_test = []
    for i in range(len(test_scaled) - time_step):
        X_test.append(test_scaled[i:(i + time_step), 0])
    X_test = np.array(X_test)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    lstm_predictions = model.predict(X_test)
    return scaler.inverse_transform(lstm_predictions)

def evaluate_model(test, forecast):
    mae = np.mean(np.abs(test - forecast))
    rmse = np.sqrt(np.mean((test - forecast) ** 2))
    
    if np.any(test == 0):
        mape = np.nan
    else:
        mape = np.mean(np.abs((test - forecast) / test)) * 100

    return mae, rmse, mape