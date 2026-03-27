import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


# Data generation
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "age": np.random.normal(40, 12, n_samples),
    "monthly_spend": np.random.normal(60, 25, n_samples),
    "support_calls": np.random.poisson(2, n_samples),
    "data_usage_gb": np.random.normal(15, 7, n_samples),
    "late_payments": np.random.poisson(1, n_samples)
})

outliers = pd.DataFrame({
    "age": np.random.normal(70, 5, 50),
    "monthly_spend": np.random.normal(100, 30, 50),
    "support_calls": np.random.poisson(5, 50),
    "data_usage_gb": np.random.normal(30, 10, 50),
    "late_payments": np.random.poisson(3, 50)
})

data=pd.concat([data,outliers], ignore_index=True)

# Data preprocessing
features = data.columns
x=StandardScaler().fit_transform(data[features])

# DBSCAN Clustering
dbscan = DBSCAN(eps=0.9, min_samples=10, metric="euclidean")
data["cluster"] = dbscan.fit_predict(x)

# Visualisation of clusters (using first two features for simplicity)
plt.figure(figsize=(8,6))
plt.scatter(data["age"], data["monthly_spend"], c=data["cluster"], cmap="viridis")
plt.xlabel("Age")
plt.ylabel("Monthly Spend")
plt.title("Customer Segments using DBSCAN Clustering")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()