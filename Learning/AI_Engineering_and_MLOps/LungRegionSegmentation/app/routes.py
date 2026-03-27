from flask import Flask, request, render_template
from app.inference import predict_overlay
import cv2
import numpy as np
import os
import time
from io import BytesIO
import mlflow

app = Flask(__name__)
STATIC_FOLDER = os.path.join(app.root_path, 'static')
os.makedirs(STATIC_FOLDER, exist_ok=True)
app.static_folder = STATIC_FOLDER

# Set MLflow tracking URI and experiment
mlflow.set_tracking_uri("mlruns")  
mlflow.set_experiment("LungRegionSegmentation")

@app.route("/")
def home():
    # Render the home page
    return render_template("index.html")

@app.route("/predict_web", methods=["POST"])
def predict_web():
    # Get the uploaded image from the request
    file = request.files["image"]

    # Read the original image as grayscale
    file_bytes = file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    original_img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Save the original image with a timestamp
    timestamp = int(time.time())
    original_filename = f"original_{timestamp}.png"
    original_path = os.path.join(STATIC_FOLDER, original_filename)
    cv2.imwrite(original_path, original_img)

    # Reset the file stream to pass it to the overlay prediction
    file.stream = BytesIO(file_bytes)
    overlay_img = predict_overlay(file)

    # Save the overlay (segmented) image
    overlay_filename = f"overlay_{timestamp}.png"
    overlay_path = os.path.join(STATIC_FOLDER, overlay_filename)
    cv2.imwrite(overlay_path, overlay_img)

    # --- MLflow logging ---
    # Track parameters and artifacts (images) for MLOps
    with mlflow.start_run():
        mlflow.log_param("kernel_size", 5)  # Example parameter
        mlflow.log_artifact(original_path, artifact_path="input")  # Original image
        mlflow.log_artifact(overlay_path, artifact_path="output")  # Segmented overlay image
    # --- End MLflow logging ---

    # Render the template and pass image filenames for display
    return render_template("index.html", original=original_filename, result=overlay_filename)