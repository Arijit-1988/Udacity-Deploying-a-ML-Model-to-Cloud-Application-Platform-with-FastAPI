import requests

URL = "https://your-deployed-api-url/predict"

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

response = requests.post(URL, json=payload, timeout=30)
print("Status:", response.status_code)
print("Body:", response.json())
