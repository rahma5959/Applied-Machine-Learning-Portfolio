from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_home():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert "running" in response.json()["message"]

def test_predict():
    response = client.post(
        "/v1/predict",
        json={"sample": [5.1, 3.5, 1.4, 0.2]}
    )
    assert response.status_code == 200
    assert "predicted_class" in response.json()