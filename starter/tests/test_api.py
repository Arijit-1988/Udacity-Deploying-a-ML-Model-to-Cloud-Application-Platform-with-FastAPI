from fastapi.testclient import TestClient

from starter.main import app

client = TestClient(app)


def test_get_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Census Income Prediction API"}


def test_post_predict_returns_less_equal_50k():
    payload = {
        "age": 23,
        "workclass": "Private",
        "fnlgt": 122272,
        "education": "Some-college",
        "education-num": 10,
        "marital-status": "Never-married",
        "occupation": "Sales",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 20,
        "native-country": "United-States",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json()["prediction"] == "<=50K"


def test_post_predict_returns_greater_50k():
    payload = {
        "age": 54,
        "workclass": "Private",
        "fnlgt": 300000,
        "education": "Doctorate",
        "education-num": 16,
        "marital-status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 20051,
        "capital-loss": 0,
        "hours-per-week": 55,
        "native-country": "United-States",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json()["prediction"] == ">50K"
