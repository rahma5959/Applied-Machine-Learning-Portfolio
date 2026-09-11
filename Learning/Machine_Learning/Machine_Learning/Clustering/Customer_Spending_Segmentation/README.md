# Customer Spending Segmentation using GMM

## Objective
Segment customers based on their spending behavior to support personalized financial products and targeted marketing.

## Problem Type
Unsupervised learning – Clustering.

There are no labels. The goal is to discover natural customer segments.

## Dataset
Synthetic structured tabular data with 1000 samples.

### Input Features
- avg_transaction_amount: Average transaction value (€)
- transactions_per_month: Number of monthly transactions
- monthly_spend: Total monthly spending (€)
- account_age_months: Customer account age

### Output
- cluster: Customer segment assigned by the model

## Model
Gaussian Mixture Model (GMM)

## Why Gaussian Mixture Model?
- Supports soft clustering (probabilistic membership)
- Handles overlapping customer behaviors
- More realistic than K-Means for financial data
- Provides uncertainty information for business decisions

## Training Details
- Features scaled using StandardScaler
- Number of clusters: 3
- Covariance type: full

## Evaluation & Visualization
- Customers visualized in 2D feature space
- Clusters saved as `result.png`

## How to Run
```bash
python Customer_Spending_Segmentation.py

