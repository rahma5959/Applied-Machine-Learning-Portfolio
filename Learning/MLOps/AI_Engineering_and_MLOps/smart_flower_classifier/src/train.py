import os
import pandas as pd
import numpy as np
import yaml
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
import joblib

# Define base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load configuration from YAML
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# Model parameters from config
n_estimators = config["model"]["n_estimators"]
max_depth = config["model"]["max_depth"]

# Data parameters from config
test_size = config["data"]["test_size"]
random_state = config["data"]["random_state"]

# MLflow experiment name from config
experiment_name = config["experiment_name"]
mlflow.set_experiment(experiment_name)

# Define models directory path and create it if it does not exist
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODELS_DIR, exist_ok=True)

# Load Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

# Start MLflow tracking run
with mlflow.start_run():

    # Log hyperparameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("test_size", test_size)
    mlflow.log_param("random_state", random_state)

    # Initialize RandomForest model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )

    # Train the model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Compute training accuracy
    train_accuracy = model.score(X_train, y_train)

    # Compute test accuracy
    test_accuracy = accuracy_score(y_test, y_pred)

    # Perform cross-validation for robust evaluation
    cv_scores = cross_val_score(model, X, y, cv=5)
    cv_mean = np.mean(cv_scores)

    # Log metrics to MLflow
    mlflow.log_metric("train_accuracy", train_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.log_metric("cv_mean_accuracy", cv_mean)

    # Infer model signature for production compatibility
    signature = infer_signature(X_train, model.predict(X_train))

    # Define example input for reproducibility
    input_example = X_train[:5]

    # Log model with signature and input example in MLflow
    mlflow.sklearn.log_model(
        model,
        name="rf_model",
        signature=signature,
        input_example=input_example
    )

    # Save model locally for inference
    model_path = os.path.join(MODELS_DIR, "rf_model.joblib")
    joblib.dump(model, model_path)

# Print final results
print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)
print("Cross validation mean accuracy:", cv_mean)
print("Model saved at:", model_path)