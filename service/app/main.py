from typing import List
from fastapi import FastAPI
from joblib import load

app = FastAPI()
model = load("../data/models/model.joblib")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/prediction")
async def predict(feature_vector: List[float], score: bool = False):
    response = {
        "is_inliner": int(model.predict([feature_vector])[0]),
        "anomaly_score": float(model.predict([feature_vector])),
    }

    return response if score else response["is_inliner"]


@app.get("/model_information")
async def get_hyperparams():
    return model.get_params()
