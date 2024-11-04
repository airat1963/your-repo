# model.py

import joblib

# Загружаем модель
model = joblib.load("sp500_model.joblib")

def predict_price(day: int) -> float:
    prediction = model.predict([[day]])
    return float(prediction[0])