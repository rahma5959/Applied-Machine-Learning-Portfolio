# OperationalDemandForecasting

## Objective
Forecast daily operational demand (tickets) considering trend, weekly seasonality, and special events such as campaigns and outages.

## Problem Type
Time series forecasting with exogenous regressors (campaigns and outages).

## Dataset
Synthetic daily time series data from 2022-01-01 to 2023-12-31.

### Input features
- `ds` (date)  
- `campaign` (binary flag for marketing campaigns)  
- `outage` (binary flag for system outages)  

### Output
- `y` (number of tickets / daily operational demand)

## Model
**Prophet (Facebook Prophet) with external regressors**

### Why Prophet?
- Handles trend, yearly and weekly seasonality  
- Supports external regressors (campaigns, outages)  
- Robust to noise and missing data  
- Easy to interpret and visualize  
- Well-suited for business operations and ticket forecasting

## Training
- Train/Test split: last 60 days used for testing  
- Yearly and weekly seasonality enabled  
- External regressors: `campaign` and `outage`

## Evaluation
- Mean Squared Error (MSE)  
- Evaluation performed on the test period only  

## Visualization
- Line plot showing:  
  - Actual tickets (test period)  
  - Predicted tickets  
- Figure saved as `Result.png`

## How to run
```bash
python OperationalDemandForecasting.py
