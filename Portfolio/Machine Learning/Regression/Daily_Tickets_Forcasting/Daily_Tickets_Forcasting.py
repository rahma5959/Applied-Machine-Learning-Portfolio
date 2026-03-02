import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from prophet import Prophet

# Data Generation
np.random.seed(42)
n_samples = 200

date=pd.date_range(start="2023-01-01", periods=n_samples, freq="D")
trend=np.linspace(20,60,n_samples)
weekly=np.where(date.weekday<5,1.0,0.7)
noise=np.random.normal(0,3,n_samples)

compaign=np.zeros(n_samples)
compaign[50:80]=1
compaign[150:180]=1

tickets=trend*weekly+15*compaign+noise

data=pd.DataFrame({
    "ds":date,
    "y":tickets,
    "compaign":compaign
})


# Train / Test
train=data.iloc[:-30]
test=data.iloc[-30:]

# Model
model=Prophet(weekly_seasonality=True)
model.add_regressor("compaign")
model.fit(train)

# Prediction
future=model.make_future_dataframe(periods=30)
future["compaign"]=future.merge(data[["ds","compaign"]], on="ds", how="left")["compaign"].fillna(0)
forecast=model.predict(future)

y_true=test["y"].values
y_pred=forecast.iloc[-30:]["yhat"].values

mse=mean_squared_error(y_true, y_pred)
r2=r2_score(y_true, y_pred)
print(f"MSE : {mse:.2f}")
print(f"R² : {r2:.2f}")

# Visualisation
plt.figure(figsize=(12,6))
plt.plot(test["ds"], test["y"], label="Actual")
forecast_test=forecast.iloc[-30:]
plt.plot(forecast_test["ds"], forecast_test["yhat"], label="Predicted")
plt.xlabel("Date")
plt.ylabel("Tickets")
plt.title("Daily Tickets Forecasting")
plt.legend()

plt.savefig("Daily_Tickets_Forecasting.png", dpi=300, bbox_inches='tight')
plt.show()

