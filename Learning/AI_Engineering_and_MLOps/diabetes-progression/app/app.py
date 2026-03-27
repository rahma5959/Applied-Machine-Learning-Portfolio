from fastapi import FastAPI
from pydantic import BaseModel, Field
import sys
import os
from typing import List

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from predict import predict

app = FastAPI(
    title="Diabetes Progression API",
    version="1.0"
)

class PatientData(BaseModel):
    features: List[float] = Field(..., example=[
        0.038, 0.050, 0.061, 0.021,
        -0.044, -0.034, -0.043, -0.002,
        0.019, -0.017
    ])

@app.get("/v1/")
def home():
    return {"message": "Diabetes Progression Prediction API v1"}

@app.post("/v1/predict")
def make_prediction(data: PatientData):
    if len(data.features) != 10:
        return {"error": "Exactly 10 features are required"}

    result = predict(data.features)
    return {"prediction": result}