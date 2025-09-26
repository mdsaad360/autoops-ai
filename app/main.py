from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
#Load sentiment analysis model at startup
#sentiment_pipeline = pipeline("sentiment-analysis")

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="714eb0f")

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
# @app.post("/predict")
# def predict(request: PredictRequest):
#     logger.info("Predict endpoint called")
#     #Dummy logic: classsify text length
#     if len(request.text) % 2 == 0:
#         sentiment = "positive"
#     else:
#         sentiment = "negative"
#     logger.info(f"Predicted sentiment: {sentiment}")
#     return {"input": request.text, "sentiment": sentiment}

@app.post("/predict")
def predict(request: PredictRequest):
    logger.info("Predict endpoint called")
    try:
        #results = sentiment_pipeline(request.text)
        #sentiment = results[0]['label'].lower()
        results = sentiment_pipeline(request.text)[0]
        logger.info(f"Predicted sentiment: {results['label']} with score {results['score']  }")
        return {
            "input": request.text,
            "label": results['label'],
            "score": results['score']
        }
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return {"error": "Prediction failed"}