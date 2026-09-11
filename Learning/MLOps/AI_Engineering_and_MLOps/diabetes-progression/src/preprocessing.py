import os
import sys
import joblib
import numpy as np
import pandas as pd


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import load_config

config = load_config()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALER_PATH = os.path.join(BASE_DIR, config["paths"]["scaler_path"])
scaler = joblib.load(SCALER_PATH)

def preprocess_input(input_data):
    """
    Scale the input data using the saved scaler
    input_data: list or array of features (length must match training features)
    returns: scaled numpy array ready for prediction
    """
    # Convert input to DataFrame to preserve feature names
    arr = pd.DataFrame([input_data], columns=scaler.feature_names_in_)
    return scaler.transform(arr)