import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from  sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score

# Data generation
np.random.seed(42)
n_samples = 500

X,_ = make_moons(n_samples=n_samples, noise=0.05, random_state=42)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# DBSCAN clustering
dbscan=DBSCAN(eps=0.3, min_samples=5)
dbscan_labels=dbscan.fit_predict(X_scaled)

# Agglomerative clustering
agglo = AgglomerativeClustering(n_clusters=2)
agglo_labels = agglo.fit_predict(X_scaled)

# Evaluation
print("Silhouette Score - KMeans:",
      silhouette_score(X_scaled, kmeans_labels))

print("Silhouette Score - DBSCAN:",
      silhouette_score(X_scaled, dbscan_labels))

print("Silhouette Score - Agglomerative:",
      silhouette_score(X_scaled, agglo_labels))

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels)
axes[0].set_title("K-Means")

axes[1].scatter(X[:, 0], X[:, 1], c=dbscan_labels)
axes[1].set_title("DBSCAN")

axes[2].scatter(X[:, 0], X[:, 1], c=agglo_labels)
axes[2].set_title("Agglomerative")

plt.tight_layout()
plt.savefig("result.png",dpi=300)
plt.legend()
plt.show()