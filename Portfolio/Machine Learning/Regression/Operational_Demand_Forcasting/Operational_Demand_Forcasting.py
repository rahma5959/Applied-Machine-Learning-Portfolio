import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error

# Data generation
np.random.seed(0)
data=pd.date_range(start="2022-01-01", end="2023-12-31", freq="D")
trend=np.linspace(20,60,len(data))
weekly=np.where(data.weekday<5,1.0,0.7)
noise=np.random.normal(0,3,len(data))

campaign=np.zeros(len(data))
campaign[100:130]=1
campaign[400:430]=1

outage=np.zeros(len(data))
outage[200:210]=1
outage[500:510]=1

tickets=trend*weekly+15*campaign-10*outage+noise

df=pd.DataFrame({
    "ds":data,
    "y":tickets,
    "campaign":campaign,
    "outage":outage
})

# Train / Test
train=df.iloc[:-60]
test=df.iloc[-60:]

# Model
model=Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.add_regressor("campaign")
model.add_regressor("outage")
model.fit(train)

# Prediction
future=model.make_future_dataframe(periods=60)
future=future.merge(df[["ds","campaign","outage"]], on="ds", how="left")
future["campaign"]=future["campaign"].fillna(0)
future["outage"]=future["outage"].fillna(0)
forecast=model.predict(future)
y_true=test["y"].values
y_pred=forecast.iloc[-60:]["yhat"].values
mse=mean_squared_error(y_true, y_pred)
print(f"MSE : {mse:.2f}")

# Visualisation
plt.figure(figsize=(12,6))
plt.plot(test["ds"], y_true, label="Actual")
plt.plot(forecast["ds"][-60:], y_pred, label="Predicted")
plt.legend()
plt.title("Operational Demand Forecasting")
plt.xlabel("Date")
plt.ylabel("Tickets")
plt.tight_layout()
plt.savefig("Result.png", dpi=300)
plt.show()