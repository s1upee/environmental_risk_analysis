import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from neuralprophet import NeuralProphet

def process_and_forecast(filename, pollutant_name):
    df = pd.read_csv(filename)
    print(df.info())
    print(df.head())
    
    df['Date Local'] = pd.to_datetime(df['Date Local'])
    df = df.sort_values(by='Date Local')
    
    daily_avg = df.groupby('Date Local')['Arithmetic Mean'].mean()
    
    plt.figure(figsize=(12,6))
    plt.plot(daily_avg, label=f'Daily {pollutant_name} Level (avg)')
    plt.title(f"Daily {pollutant_name} Levels - 2024")
    plt.xlabel("Date")
    plt.ylabel(f"{pollutant_name} Level")
    plt.legend()
    plt.show()
    
    # ARIMA Model
    model = ARIMA(daily_avg, order=(1,1,1))
    results = model.fit()
    forecast = results.forecast(steps=30)
    
    plt.figure(figsize=(12,6))
    plt.plot(daily_avg, label="Observed")
    plt.plot(forecast.index, forecast, label="ARIMA Forecast", linestyle="--")
    plt.title(f"ARIMA Forecast - {pollutant_name} Levels")
    plt.legend()
    plt.show()
    
    # Linear Regression
    X = daily_avg.index.map(lambda x: x.toordinal()).values.reshape(-1, 1)
    y = daily_avg.values
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_dates = pd.date_range(daily_avg.index[-1] + pd.Timedelta(days=1), periods=30)
    X_future = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
    y_pred = model.predict(X_future)
    
    plt.figure(figsize=(12,6))
    plt.plot(daily_avg, label="Observed")
    plt.plot(future_dates, y_pred, label="Linear Regression Forecast", linestyle="--")
    plt.title(f"Linear Regression Forecast - {pollutant_name} Levels")
    plt.legend()
    plt.show()
    
    # NeuralProphet Forecasting
    df_prophet = daily_avg.reset_index()
    df_prophet.columns = ['ds', 'y']
    
    model = NeuralProphet()
    model.fit(df_prophet, freq='D')
    
    daily_avg = daily_avg.asfreq('D')
    future = model.make_future_dataframe(df_prophet, periods=30)
    forecast = model.predict(future)
    
    fig_forecast = model.plot(forecast)
    fig_forecast.suptitle(f"NeuralProphet Forecast - {pollutant_name} Levels")
    plt.show()

# Process Ozone
daily_ozone_file = "daily_44201_2024.csv"
process_and_forecast(daily_ozone_file, "Ozone")

# Process PM2.5
daily_pm25_file = "daily_88101_2024.csv"
process_and_forecast(daily_pm25_file, "PM2.5")

# Process Temperature
daily_temp_file = "daily_TEMP_2024.csv"
process_and_forecast(daily_temp_file, "Temperature")
