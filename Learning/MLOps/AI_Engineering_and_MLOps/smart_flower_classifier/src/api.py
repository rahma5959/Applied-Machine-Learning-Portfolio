from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import os

# Create FastAPI app instance
app = FastAPI()

# Define the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the full path to the trained model
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.joblib")

# Load the trained Random Forest model
model = joblib.load(MODEL_PATH)

# Define a Pydantic model for the input data
# This will ensure that the input is a list of floats
class InputData(BaseModel):
    sample: List[float]

# Define a simple GET endpoint for testing if API is running
@app.get("/v1/")
def home():
    return {"message": "Iris Classification API is running"}

# Define a POST endpoint for making predictions
@app.post("/v1/predict")
def predict(data: InputData):

    sample_array = np.array(data.sample).reshape(1, -1)
    prediction = model.predict(sample_array)
    return {"predicted_class": int(prediction[0])}