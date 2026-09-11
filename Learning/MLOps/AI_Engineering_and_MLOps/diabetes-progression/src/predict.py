import joblib
import sys
import os

sys.path.append(os.path.dirname(__file__))  # Add src folder to Python path

from config import load_config
from preprocessing import preprocess_input

config = load_config()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, config["paths"]["model_path"])

model = joblib.load(MODEL_PATH)

def predict(input_data):
    """
    Make prediction
    """
    processed = preprocess_input(input_data)
    prediction = model.predict(processed)
    return float(prediction[0])


if __name__ == "__main__":
    sample_patient = [
        0.038, 0.050, 0.061, 0.021,
        -0.044, -0.034, -0.043, -0.002,
        0.019, -0.017
    ]

    result = predict(sample_patient)
    print(f"Prediction: {result:.2f}")