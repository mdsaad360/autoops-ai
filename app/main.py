from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "Ok"}


# @app.post("/predict")
# def predict():
#     logger.info("Predict endpoint called")
#     return {"message": "Prediction endpoint placeholder"}

class PredictRequest(BaseModel):
    text: str

#Dummy predict endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    logger.info("Predict endpoint called")
    #Dummy logic: classsify text length
    if len(request.text) % 2 == 0:
        sentiment = "positive"
    else:
        sentiment = "negative"
    logger.info(f"Predicted sentiment: {sentiment}")
    return {"input": request.text, "sentiment": sentiment}