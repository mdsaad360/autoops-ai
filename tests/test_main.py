from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}

# def test_predict():
#     response = client.post("/predict")
#     assert response.status_code == 200
#     body = response.json()
#     assert "message" in body
#     assert body["message"] == "Prediction endpoint placeholder"

def test_predict_positive():
    response = client.post("/predict", json={"text":"Even"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_predict_negative():
    response = client.post("/predict", json={"text":"Odd"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"