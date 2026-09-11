# ApartementPricePredictor

## Objective
Predict the selling price of a house based on its physical characteristics and location quality.

## Problem Type
Regression (continuous target variable: house price).

## Dataset
Synthetic structured tabular data with 200 samples.

### Input features
- size (house size in square feet)
- bedrooms (number of bedrooms)
- age (age of the house in years)
- location_score (location quality score from 0 to 10)

### Output
- price (house price)

## Model
Linear Regression

### Why Linear Regression?
- Simple and interpretable baseline model
- Well-suited for numerical, structured data
- Allows understanding the influence of each feature on price
- Commonly used as a first approach in price prediction tasks

## Training
- Train/Test split: 80% / 20%
- Random state fixed for reproducibility
- Ordinary Least Squares optimization

## Evaluation
- Mean Squared Error (MSE)
- R² Score (coefficient of determination)

## Visualization
- Bar chart comparing **actual vs predicted prices** for a sample of 10 houses
- Figure saved as `result.png`

## How to run
```bash
python HousePricePredictor.py
