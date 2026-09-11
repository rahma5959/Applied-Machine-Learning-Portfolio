# CustomerChurnPredictor

## Objective
Predict whether a telecom customer will leave (churn) or stay with the company.

## Problem Type
Binary classification (0 = stays, 1 = churn).

## Dataset
Synthetic structured tabular data representing customer behavior.

### Input features
- contract_length (months with company)
- monthly_cost (subscription cost per month)
- support_calls (number of support calls made)
- data_usage (GB per month)
- late_payments (number of late payments)
- has_premium (0 = no premium, 1 = premium)

### Output
- churn (0 or 1)

## Model
Logistic Regression

### Why Logistic Regression?
- Provides probabilistic output (chance of churn)
- Coefficients are interpretable → easy to explain to business
- Strong baseline for small/medium structured datasets
- Preferred for situations where interpretability matters more than non-linear modeling

## Training
- Train/Test split: 80% / 20%
- L2 regularization
- Can include class weighting if target imbalance exists

## Evaluation
- Classification report (precision, recall, F1-score)
- Confusion matrix saved as `result.png`

## How to run
```bash
python Customer Churn Prediction.py
