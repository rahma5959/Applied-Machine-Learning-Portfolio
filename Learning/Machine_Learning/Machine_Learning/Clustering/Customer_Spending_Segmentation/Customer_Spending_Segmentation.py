import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

# Data generation
np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    "avg_transaction_amount": np.random.normal(60, 20, n_samples),
    "transactions_per_month": np.random.normal(25, 8, n_samples),
    "monthly_spend": np.random.normal(1500, 500, n_samples),
    "account_age_months": np.random.normal(36, 15, n_samples)
})
features = data.columns
x=StandardScaler().fit_transform(data[features])

# Clustering with Gaussian Mixture Models
gmm = GaussianMixture(n_components=4, random_state=42)
gmm.fit(x)
data["cluster"] = gmm.predict(x)

# Visualize clusters

plt.figure(figsize=(10, 6))
plt.scatter(data["avg_transaction_amount"], data["transactions_per_month"], c=data["cluster"], cmap="viridis")
plt.xlabel("Average Transaction Amount")
plt.ylabel("Transactions Per Month")
plt.title("Customer Segments Based on Spending Behavior")
plt.legend()
plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()