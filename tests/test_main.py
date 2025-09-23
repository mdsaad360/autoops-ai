from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}

def test_predict():
    response = client.post("/predict")
    assert response.status_code == 200
    body = response.json()
    assert "message" in body
    assert body["message"] == "Prediction endpoint placeholder"