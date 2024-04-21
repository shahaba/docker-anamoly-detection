from typing import List
from fastapi import FastAPI
from joblib import load
from prometheus_client import Histogram, make_asgi_app, Counter
import time

# create different metrics for prometheus
pred_count = Counter(
    "prediction_count", "Total number of requests to prediction service"
)
info_count = Counter(
    "model_info_count", "Total number of requests to model information service"
)
h_pred = Histogram("prediction_output", "Histogram of model.predict()")
h_score = Histogram("prediction_score", "Histogram of prediction scores")
h_latency = Histogram("prediction_latency", "Histogram of predection latency")

# create FastAPI app
app = FastAPI()

# create prometheus_client middleware
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# load Isolation Forest model
model = load("models/model.joblib")


@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.post("/prediction")
async def predict(feature_vector: List[float], score: bool = False):
    pred_count.inc()  # increment counter
    start_time = time.time()  # track latency of prediction

    prediction = int(model.predict([feature_vector])[0])
    h_pred.observe(prediction)

    response = {"is_inliner": prediction}

    if score:
        val = model.score_samples([feature_vector])
        h_score.observe(val)
        response["anomaly_score"] = val[0]

    h_latency.observe(time.time() - start_time)  # total observed time

    return response


@app.get("/model_information")
async def get_hyperparams():
    info_count.inc()
    return model.get_params()
