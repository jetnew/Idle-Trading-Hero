from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error


class LSTM_Forecast:
    def __init__(self, timesteps, n_features=1):
        self.timesteps = timesteps
        self.n_features = n_features
        self.model = self.build()

    def build(self):
        model = Sequential()
        model.add(LSTM(64, activation='relu', input_shape=(self.timesteps, self.n_features), return_sequences=True))
        model.add(LSTM(64, activation='relu'))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mae')
        return model

    def fit(self, X_train, y_train, X_test, y_test, epochs=30, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
        y_pred = self.model.predict(X_test)
        self.score = mean_squared_error(y_test, y_pred)
        print("MSE:", self.score)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
