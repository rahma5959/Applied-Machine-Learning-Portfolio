import os
import joblib
import pandas as pd
import numpy as np

# Define base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define model path
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.joblib")

# Define CSV path for new data (can contain multiple rows)
CSV_PATH = os.path.join(BASE_DIR, "data", "new_samples.csv")

# Load trained model
model = joblib.load(MODEL_PATH)
print("Model loaded from:", MODEL_PATH)

# Load new samples from CSV
if os.path.exists(CSV_PATH):
    new_data = pd.read_csv(CSV_PATH)
    print("New samples to predict:\n", new_data)
else:
    # If CSV does not exist, use a default example
    print("CSV file not found, using default example")
    new_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]],
                            columns=['sepal_length','sepal_width','petal_length','petal_width'])

# Convert DataFrame to numpy array
X_new = new_data.values

# Predict classes
predictions = model.predict(X_new)

# Print prediction results
for i, pred in enumerate(predictions):
    print(f"Sample {i+1} predicted as class: {pred}")