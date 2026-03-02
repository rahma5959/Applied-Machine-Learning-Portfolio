import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Data Generation

np.random.seed(42)
n_samples = 200

data = pd.DataFrame({
    "size": np.random.randint(500, 2000, n_samples),  # square feet
    "bedrooms": np.random.randint(1, 5, n_samples),
    "age": np.random.randint(0, 30, n_samples),  # years
    "location_score": np.random.uniform(0, 10, n_samples)  # 0=bad, 10=excellent
})

data["price"] = (
    150 * data["size"] +
    10000 * data["bedrooms"] -
    500 * data["age"] +
    20000 * data["location_score"] +
    np.random.normal(0, 20000, n_samples)  # noise
)

# Train/Test Split
X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")


#visualisation
# Select a small number of samples for clarity
n = 10
y_test_sample = y_test.iloc[:n]
y_pred_sample = y_pred[:n]

x = np.arange(n)
width = 0.35

plt.figure(figsize=(10, 5))

plt.bar(x - width/2, y_test_sample, width, label="Actual Price")
plt.bar(x + width/2, y_pred_sample, width, label="Predicted Price")

plt.xlabel("House")
plt.ylabel("Price")
plt.title("Actual vs Predicted House Prices (Sample)")

plt.xticks(x, [f"House {i+1}" for i in range(n)])
plt.legend()

plt.savefig("result.png", dpi=300, bbox_inches="tight")
plt.show()
