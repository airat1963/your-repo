from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Загружаем модель
model = joblib.load("sp500_model.joblib")

class PredictionRequest(BaseModel):
    day: int  # Прогнозируемая дата в днях от последней даты

@app.post("/predict")                               #predict
def predict(request: PredictionRequest):
    day = request.day
    prediction =model.predict([[day]])
    return {"predicted_close": prediction[0]}
