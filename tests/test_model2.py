# test_model2.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"day": 1})
    assert response.status_code == 200
    assert "predicted_close" in response.json()

def test_predict_invalid_input():
    response = client.post("/predict", json={"day": "invalid"})
    assert response.status_code == 422  # Ожидаем ошибку валидации