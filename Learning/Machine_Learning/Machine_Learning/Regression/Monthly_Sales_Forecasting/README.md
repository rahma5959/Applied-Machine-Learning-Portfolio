# MonthlySalesForecasting

## Objective
Forecast monthly sales based on historical data with trend and yearly seasonality.

## Problem Type
Time series forecasting (regression on temporal data).

## Dataset
Synthetic time series data with 200 monthly observations.

### Input features
- ds (date)

### Output
- y (monthly sales)

## Model
Prophet (Facebook Prophet)

### Why Prophet?
- Designed for time series forecasting
- Automatically captures trend and yearly seasonality
- Robust to noise and missing data
- Easy to configure and interpret
- Well-suited for business time series such as sales data

## Training
- Train/Test split: last 12 months used for testing
- Yearly seasonality enabled
- Weekly and daily seasonality disabled

## Evaluation
- Mean Squared Error (MSE)
- R² Score
- Evaluation performed on the test period only

## Visualization
- Line plot showing:
  - Training data (historical sales)
  - Test data (true future values)
  - Forecasted sales over the test period
- Figure saved as `result.png`

## How to run
```bash
python MonthlySalesForecasting.py
