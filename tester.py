import requests
import csv
import random

TEST_DATA = "./data/test.csv"
URL = "http://localhost:8000/prediction?"

with open(TEST_DATA, "r") as csvfile:
    data = csv.reader(csvfile)
    next(data, None)  # skip the header
    for row in data:
        mean, sd = map(float, row)
        payload = [mean, sd]
        if random.randint(1, 4) % 4 == 0:
            url = URL + "score=true"
        else:
            url = URL + "score=false"

        response = requests.post(url, json=payload)
        print(response.json())
