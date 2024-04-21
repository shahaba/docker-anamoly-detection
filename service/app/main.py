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
    }

    if score:
        val = model.score_samples([feature_vector])
        response["anomaly_score"] = val[0]

    return response


@app.get("/model_information")
async def get_hyperparams():
    return model.get_params()
