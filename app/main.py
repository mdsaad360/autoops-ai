from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "Ok"}

@app.post("/predict")
def predict():
    logger.info("Predict endpoint called")
    return {"message": "Prediction endpoint placeholder"}