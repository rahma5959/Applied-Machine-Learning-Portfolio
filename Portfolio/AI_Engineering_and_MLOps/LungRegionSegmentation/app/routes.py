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

mlflow.set_tracking_uri("mlruns")  # dossier local
mlflow.set_experiment("LungRegionSegmentation")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_web", methods=["POST"])
def predict_web():
    file = request.files["image"]

    # Lire image originale
    file_bytes = file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    original_img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Sauvegarder original
    timestamp = int(time.time())
    original_filename = f"original_{timestamp}.png"
    original_path = os.path.join(STATIC_FOLDER, original_filename)
    cv2.imwrite(original_path, original_img)

    # Reset stream pour overlay
    file.stream = BytesIO(file_bytes)
    overlay_img = predict_overlay(file)

    # Sauvegarder overlay
    overlay_filename = f"overlay_{timestamp}.png"
    overlay_path = os.path.join(STATIC_FOLDER, overlay_filename)
    cv2.imwrite(overlay_path, overlay_img)

    # --- Step: MLflow logging ---
    with mlflow.start_run():
        mlflow.log_param("kernel_size", 5)  # exemple si tu as un paramètre
        mlflow.log_artifact(original_path, artifact_path="input")
        mlflow.log_artifact(overlay_path, artifact_path="output")
    # --- End MLflow logging ---

    # Retourner template avec chemins relatifs pour url_for
    return render_template("index.html", original=original_filename, result=overlay_filename)