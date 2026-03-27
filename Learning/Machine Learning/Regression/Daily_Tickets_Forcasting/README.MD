# DailyTicketsForecasting

## Objective
Forecast the daily number of customer support tickets while accounting for weekly patterns and marketing campaigns.

## Problem Type
Time series forecasting (regression on temporal data).

## Dataset
Synthetic time series data with 200 daily observations.

### Input features
- ds (date)
- compaign (binary indicator of marketing campaign: 0 = no campaign, 1 = active campaign)

### Output
- y (number of daily tickets)

## Model
Prophet (Facebook Prophet) with external regressor

### Why Prophet?
- Designed for time series forecasting
- Automatically handles trend and seasonality
- Robust to missing data and noise
- Allows inclusion of external regressors (campaign effect)
- Easy to interpret and visualize

## Training
- Train/Test split: last 30 days used for testing
- Weekly seasonality enabled
- External regressor: marketing campaign indicator

## Evaluation
- Mean Squared Error (MSE)
- R² Score
- Forecast evaluated only on the test period

## Visualization
- Line plot showing:
  - Actual daily ticket counts (test period)
  - Predicted ticket counts (forecast)
- Figure saved as `Daily_Tickets_Forecasting.png`

## How to run
```bash
python DailyTicketsForecasting.py
