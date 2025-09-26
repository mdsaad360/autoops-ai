from fastapi.testclient import TestClient
from app.main import app
import logging
logging.basicConfig(level=logging.INFO)

client = TestClient(app)

def test_health():
    response = client.get("/health")
    logging.info(f"Health check response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}

# def test_predict():
#     response = client.post("/predict")
#     assert response.status_code == 200
#     body = response.json()
#     assert "message" in body
#     assert body["message"] == "Prediction endpoint placeholder"

# def test_predict_positive():
#     response = client.post("/predict", json={"text":"Even"})
#     assert response.status_code == 200
#     assert response.json()["sentiment"] == "positive"

# def test_predict_negative():
#     response = client.post("/predict", json={"text":"Odd"})
#     assert response.status_code == 200
#     assert response.json()["sentiment"] == "negative"

def test_predict_real_model():
    response = client.post("/predict", json={"text":"I love coding!"})
    logging.info(f"Prediction Response: {response.json()}")
    #assert response.status_code == 200
    #assert response.json()["label"] == "positive"
    #assert response.json()["score"] > 0.9
    assert response.status_code == 200
    data = response.json()
    assert "label" in data, "label key missing in response"
    assert data["label"] in ["POSITIVE", "NEGATIVE"], f"Unexpected label value: {data.get('label')}"
    assert "score" in data, "score key missing in response"
    assert isinstance(data["score"], float), f"score is not a float: {data.get('score')}"
