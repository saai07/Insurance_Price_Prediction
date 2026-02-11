from schema.user_input import PredictionRequest
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle 
import pandas as pd
from typing import Annotated , Literal
from schema.prediction_response import PredictionResponse
from model.predict import predict_output , MODEL_VERSION , model


app = FastAPI()


@app.get("/")
def home():
    return JSONResponse(status_code=200, content={"message": "Welcome to the Insurance Premium Prediction API!"})


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_version": MODEL_VERSION,
        "model_loaded": model is not None}


@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: PredictionRequest):
    
    user_input = {
        "bmi" : data.bmi,
        "lifestyle_risk" : data.lifestyle_risk,
        "age_group" : data.age_group,
        "city_tier" : data.city_tier,
        "income_lpa" : data.income_lpa,
        "occupation" : data.occupation
    }
    try:
        
        prediction = predict_output(user_input)
    
        return JSONResponse(status_code=200, content={"predicted_premium": prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
