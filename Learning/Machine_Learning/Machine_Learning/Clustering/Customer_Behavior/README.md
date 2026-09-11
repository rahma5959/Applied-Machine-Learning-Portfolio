# Customer Behavior Clustering (DBSCAN)

## Objective
Segment customers based on behavioral patterns while identifying abnormal or rare users.

## Problem Type
Unsupervised learning – clustering with noise detection.

## Dataset
Synthetic structured customer data with 1000+ samples.

### Input features
- age
- monthly_spend
- support_calls
- data_usage_gb
- late_payments

### Output
- cluster label
- noise points labeled as `-1`

## Model
DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

### Why DBSCAN?
- No need to specify number of clusters
- Detects noise and outliers explicitly
- Handles irregular cluster shapes
- Suitable for real-world behavioral data

## Hyperparameters
- eps = 0.9
- min_samples = 10
- distance metric = Euclidean

## Preprocessing
- Feature scaling using StandardScaler

## Evaluation
- Number of clusters discovered
- Number of noise points
- Visualization saved as `result.png`

## How to run
```bash
python Customer_Behavior.py
