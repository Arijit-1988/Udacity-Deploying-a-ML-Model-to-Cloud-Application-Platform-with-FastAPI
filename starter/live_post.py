import os

import requests

URL = os.getenv("LIVE_API_URL", "https://your-deployed-api-url/predict")

payload = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 284582,
    "education": "Masters",
    "education-num": 14,
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Wife",
    "race": "White",
    "sex": "Female",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

if "your-deployed-api-url" in URL:
    raise SystemExit(
        "Set LIVE_API_URL to your deployed endpoint, for example: "
        "https://your-service.onrender.com/predict"
    )

response = requests.post(URL, json=payload, timeout=30)
print("URL:", URL)
print("Status:", response.status_code)
print("Body:", response.json())
