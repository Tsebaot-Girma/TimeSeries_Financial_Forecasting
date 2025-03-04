#scripts/model_training.py

from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA




def train_arima_model(train_data):
    model = auto_arima(train_data, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
    return ARIMA(train_data, order=model.order).fit()

def train_sarima_model(train_data, seasonal_order=(1, 1, 1, 12)):
    model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=seasonal_order)
    return model.fit(disp=False)

def train_lstm_model(train_data, time_step=10):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(train_data.values.reshape(-1, 1))

    X, y = [], []
    for i in range(len(scaled_data) - time_step - 1):
        X.append(scaled_data[i:(i + time_step), 0])
        y.append(scaled_data[i + time_step, 0])
    X, y = np.array(X), np.array(y)

    X = X.reshape(X.shape[0], X.shape[1], 1)

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X, y, epochs=100, batch_size=32)

    return model, scaler