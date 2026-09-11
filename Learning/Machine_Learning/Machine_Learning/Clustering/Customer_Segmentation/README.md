# Customer Segmentation with K-Means

## Objective
Segment customers into groups based on behavior and usage patterns to target marketing and retention strategies.

## Problem Type
Unsupervised clustering.

## Dataset
Synthetic structured tabular data with 1000 samples.

### Input features
- age
- monthly_spend (subscription cost)
- support_calls
- data_usage_gb
- late_payments

### Output
- cluster label (0, 1, 2, 3)

## Model
**K-Means Clustering**

### Why K-Means?
- Works well for structured numerical data
- Simple and widely used
- Easy to interpret cluster assignments
- Fast for medium-sized datasets
- Strong baseline for customer segmentation

## Training
- Standard scaling applied to features
- Number of clusters: 4
- Initialization: k-means++
- Max iterations: 300
- Random state: 42 for reproducibility

## Evaluation
- Visual inspection of clusters (saved as `result.png`)
- Cluster assignments saved in `customer_clusters.csv`

## How to run
```bash
python Customer_Segmentation.py
