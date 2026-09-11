import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from prophet import Prophet
# Data Generation
np.random.seed(42)
n_samples = 200

date = pd.date_range(start="2023-01-01", periods=n_samples, freq="M")
trend = np.linspace(1000, 5000, n_samples)
seasonality = 500 * np.sin(np.arange(n_samples) / 12 * 2 * np.pi)
noise = np.random.normal(0, 200, n_samples)
sales = trend + seasonality + noise

data = pd.DataFrame({
    "ds": date,
    "y": sales
})

# Train/Test Split
train = data.iloc[:-12]
test = data.iloc[-12:]

# Model Training
model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
model.fit(train)

# Forecasting
future = model.make_future_dataframe(periods=12,freq="M")
forecast = model.predict(future)

# Evaluation
y_true = test["y"].values
y_pred = forecast.iloc[-12:]["yhat"].values
mse = mean_squared_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(train["ds"], train["y"], label="Training Data")
plt.plot(test["ds"], test["y"], label="Test Data")
forecast_test = forecast.iloc[-12:]

plt.plot(
    forecast_test["ds"],
    forecast_test["yhat"],
    label="Forecast (Test Period)",
    linestyle="--"
)

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Monthly Sales Forecasting (Train / Test / Forecast)")
plt.legend()

plt.savefig("result.png", dpi=300, bbox_inches="tight")
plt.show()