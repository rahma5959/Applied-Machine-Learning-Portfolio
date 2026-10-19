from fastapi.testclient import TestClient
from src.app import app

Client=TestClient(app)

def test_home_returns_welcome_message():
    response=Client.get("/")
    assert response.status_code==200
    assert response.json()=={
        "message":"hello from fast api running from "
    }

def test_health_returns_healthy_status():
    response=Client.get("/health")
    assert response.status_code==200
    assert response.json()=={
        "status":"healthy"
    }