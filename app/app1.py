"""

Application

"""
import os
from fastapi import FastAPI
from pydantic import BaseModel
#import joblib
MODEL_PATH=os.path.join("models","model.joblib")

app = FastAPI()



@app.get("/status")
def health_check() -> dict:
    """
    Health check
    """
    return {"status": "ok"}


