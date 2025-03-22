import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

wind = pd.read_csv("data/daily_WIND_2024/daily_WIND_2024.csv", low_memory=False)
temp = pd.read_csv("data/daily_TEMP_2024/daily_TEMP_2024.csv", low_memory=False)
press = pd.read_csv("data/daily_PRESS_2024/daily_PRESS_2024.csv", low_memory=False)
humidity = pd.read_csv("data/daily_RH_DP_2024/daily_RH_DP_2024.csv", low_memory=False)
ozone = pd.read_csv("data/daily_44201_2024/daily_44201_2024.csv", low_memory=False)

print(ozone.columns)
print(temp.columns)

ozone = ozone.rename(columns={"Arithmetic Mean": "Ozone"})
temp = temp.rename(columns={"Arithmetic Mean": "Temperature"})

ozone['Date'] = pd.to_datetime(ozone['Date Local'])
temp['Date'] = pd.to_datetime(temp['Date Local'])

wind = wind.rename(columns={"Arithmetic Mean": "Wind Speed"})
press = press.rename(columns={"Arithmetic Mean": "Pressure"})
humidity = humidity.rename(columns={"Arithmetic Mean": "Relative Humidity"})

wind['Date'] = pd.to_datetime(wind['Date Local'])
press['Date'] = pd.to_datetime(press['Date Local'])
humidity['Date'] = pd.to_datetime(humidity['Date Local'])

ozone = ozone[['Date', 'State Code', 'County Code', 'Site Num', 'Ozone']]
temp = temp[['Date', 'State Code', 'County Code', 'Site Num', 'Temperature']]
wind = wind[['Date', 'State Code', 'County Code', 'Site Num', 'Wind Speed']]
press = press[['Date', 'State Code', 'County Code', 'Site Num', 'Pressure']]
humidity = humidity[['Date', 'State Code', 'County Code', 'Site Num', 'Relative Humidity']]

merged = ozone.merge(temp, on=['Date', 'State Code', 'County Code', 'Site Num'])
merged = merged.merge(wind, on=['Date', 'State Code', 'County Code', 'Site Num'])
merged = merged.merge(press, on=['Date', 'State Code', 'County Code', 'Site Num'])
merged = merged.merge(humidity, on=['Date', 'State Code', 'County Code', 'Site Num'])

sns.heatmap(merged.corr(), annot=True)
plt.title("Correlation Matrix: Meteorology vs Ozone")
plt.show()

# Features and target
X = merged[['Temperature', 'Wind Speed', 'Pressure', 'Relative Humidity']]
y = merged['Ozone']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Ozone Levels")
plt.ylabel("Predicted Ozone Levels")
plt.title("Regression Model: Weather vs Ozone")
plt.show()
