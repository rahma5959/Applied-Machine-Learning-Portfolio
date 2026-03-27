import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Data generation
np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    "age": np.random.randint(18, 70, n_samples),
    "monthly_spend": np.random.normal(50, 15, n_samples),  # subscription cost
    "support_calls": np.random.poisson(2, n_samples),
    "data_usage_gb": np.random.normal(10, 5, n_samples),
    "late_payments": np.random.poisson(0.5, n_samples)
})

# Data preprocessing
features = data[["age", "monthly_spend", "support_calls", "data_usage_gb", "late_payments"]]
x=StandardScaler().fit_transform(features)

# K-Means Clustering

k = 4
kmeans = KMeans(n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=42)
kmeans.fit(x)

# Add cluster labels to data
data["cluster"] = kmeans.labels_

# Visualisation of clusters (using first two features for simplicity)
plt.figure(figsize=(8,6))
plt.scatter(x[:,0], x[:,1], c=kmeans.labels_, cmap="tab10", s=50, alpha=0.7)
plt.xlabel("age(scaled)")
plt.ylabel("monthly_spend(scaled)")
plt.title("Customer Segmentation with K-Means")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()