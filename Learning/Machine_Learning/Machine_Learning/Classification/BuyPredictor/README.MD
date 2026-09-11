
## Objective
Predict whether a user will purchase a product (`buy=0/1`) based on features such as age, gender, time on site, pages viewed, and previous purchases.

## Dataset
- Synthetic dataset with 1000 samples
- Features:
  - `age`: user age (numeric)
  - `gender`: 0=female, 1=male
  - `time_on_site`: time spent on website in minutes
  - `pages_viewed`: number of pages visited
  - `previous_purchases`: number of previous purchases
- Target:
  - `buy`: 0=no purchase, 1=purchase

## Model
- Random Forest Classifier
- Train/Test split: 80%/20%
- Hyperparameters:
  - `n_estimators=100`
  - `max_depth=5`

## Results
- Classification report printed in console
- Confusion matrix saved as `result.png`

## How to run
```bash
python BuyPredictor.py
