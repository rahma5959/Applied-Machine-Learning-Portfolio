# ReadmissionRiskPredictor

## Objective
Predict whether a patient will be readmitted within 30 days after hospital discharge.

## Problem Type
Binary classification (0 = no readmission, 1 = readmission).

## Dataset
Synthetic structured tabular data with 400 samples.

### Input features
- age
- length_of_stay
- num_lab_tests
- num_procedures
- has_chronic_disease
- previous_admissions

### Output
- readmitted (0 or 1)

## Model
Logistic Regression

### Why Logistic Regression?
- Suitable for small structured datasets
- Provides interpretability (coefficients)
- Commonly used in medical decision support
- Easier to explain to clinicians than black-box models

## Training
- Train/Test split: 75% / 25%
- L2 regularization
- Class weighting to handle imbalance

## Evaluation
- Classification report (precision, recall, F1-score)
- Confusion matrix saved as `result.png`

## How to run
```bash
python ReadmissionRiskPredictor.py
