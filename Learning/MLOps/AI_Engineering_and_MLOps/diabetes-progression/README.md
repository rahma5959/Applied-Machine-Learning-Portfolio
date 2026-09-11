# Explainable Diabetes Progression ML Ops

This project is a Machine Learning pipeline for predicting diabetes progression. It demonstrates a full ML workflow including data preprocessing, model training, evaluation, interpretability, and deployment readiness.

## Project Structure

diabetes-progression/
│
├── config/ Configuration files
│ └── config.yaml
│
├── data/ Input datasets (CSV)
│
├── src/ Python scripts
│ ├── train.py Train models
│ ├── predict.py Make predictions
│ ├── preprocessing.py Preprocessing functions
│ └── config.py Load configuration
│
├── app/ API or application entry point
│ └── main.py
│
├── models/ Saved trained models and scalers
│
├── tests/ Unit tests
│ └── test_api.py
│
├── requirements.txt Python dependencies
├── Dockerfile Containerization
├── README.md Project documentation
└── .gitignore Files to ignore in git

## Installation

# Create virtual environment:

python -m venv venv
venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt
Train the Model
python src/train.py

This will create:

models/model.pkl
models/scaler.pkl

## Run the API
uvicorn app.app:app --reload

Open in browser:

http://127.0.0.1:8000/docs

## API Usage

# GET /v1/ 

Returns API status.

# POST /v1/predict

Example request:

{
  "features": [0.038, 0.050, 0.061, 0.021,
               -0.044, -0.034, -0.043, -0.002,
               0.019, -0.017]
}

Example response:

{
  "prediction": 208.06
}

## Run with Docker

# Build image:

docker build -t diabetes-api .

# Run container:

docker run -p 8000:8000 diabetes-api

Access:

http://localhost:8000/docs