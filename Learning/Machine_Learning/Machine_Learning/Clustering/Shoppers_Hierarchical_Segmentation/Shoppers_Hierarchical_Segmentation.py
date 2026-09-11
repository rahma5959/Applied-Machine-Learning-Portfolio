import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering


# Data generation
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "session_time": np.random.normal(10, 2, n_samples),
    "pages_visited": np.random.normal(5, 1.5, n_samples),
    "cart_additions": np.random.randint(0, 10, n_samples),
    "total_spent": np.random.normal(200, 50, n_samples),
    "discount_usage": np.random.uniform(0, 1, n_samples),
    "newsletter_click_rate": np.random.uniform(0, 1, n_samples)
})

# Data preprocessing
features = data.columns
x = StandardScaler().fit_transform(data[features])

# Hierarchical Clustering
n_clusters = 4
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage="ward")
data["cluster"] = agg_clustering.fit_predict(x)

# Visualisation of clusters (using first two features for simplicity)
plt.figure(figsize=(8,6))
plt.scatter(data["session_time"], data["pages_visited"], c=data["cluster"], cmap="tab10", s=50, alpha=0.7)
plt.xlabel("Session Time (scaled)")
plt.ylabel("Pages Visited (scaled)")
plt.title("Customer Segmentation with Hierarchical Clustering")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()