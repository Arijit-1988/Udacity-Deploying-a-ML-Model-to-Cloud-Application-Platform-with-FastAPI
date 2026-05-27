from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

from starter.ml.train_model import CAT_FEATURES, train_and_save_model

APP_DIR = Path(__file__).resolve().parent
MODEL_DIR = APP_DIR / "model"

app = FastAPI(title="Census Income Classifier")


class CensusInput(BaseModel):
    """Pydantic schema for census inference payload."""

    age: int = Field(..., examples=[37])
    workclass: str = Field(..., examples=["Private"])
    fnlgt: int = Field(..., examples=[284582])
    education: str = Field(..., examples=["Masters"])
    education_num: int = Field(..., alias="education-num", examples=[14])
    marital_status: str = Field(..., alias="marital-status", examples=["Married-civ-spouse"])
    occupation: str = Field(..., examples=["Exec-managerial"])
    relationship: str = Field(..., examples=["Wife"])
    race: str = Field(..., examples=["White"])
    sex: str = Field(..., examples=["Female"])
    capital_gain: int = Field(..., alias="capital-gain", examples=[0])
    capital_loss: int = Field(..., alias="capital-loss", examples=[0])
    hours_per_week: int = Field(..., alias="hours-per-week", examples=[40])
    native_country: str = Field(..., alias="native-country", examples=["United-States"])

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
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
        },
    )


def _ensure_artifacts():
    model_path = MODEL_DIR / "model.joblib"
    encoder_path = MODEL_DIR / "encoder.joblib"
    lb_path = MODEL_DIR / "lb.joblib"

    if model_path.exists() and encoder_path.exists() and lb_path.exists():
        return

    train_and_save_model(str(APP_DIR / "data" / "census.csv"), str(MODEL_DIR))


def _load_artifacts():
    _ensure_artifacts()
    model = joblib.load(MODEL_DIR / "model.joblib")
    encoder = joblib.load(MODEL_DIR / "encoder.joblib")
    lb = joblib.load(MODEL_DIR / "lb.joblib")
    return model, encoder, lb


@app.get("/")
def get_welcome_message():
    """Return a welcome message."""
    return {"message": "Welcome to the Census Income Prediction API"}


@app.post("/predict")
def predict_income(data: CensusInput):
    """Return income class prediction for a single payload."""
    model, encoder, lb = _load_artifacts()

    payload = data.model_dump(by_alias=True)
    frame = pd.DataFrame([payload])

    encoded = encoder.transform(frame[CAT_FEATURES])
    numeric = frame.drop(columns=CAT_FEATURES)

    X = pd.concat(
        [
            pd.DataFrame(encoded, index=numeric.index),
            numeric.reset_index(drop=True),
        ],
        axis=1,
    )

    pred = model.predict(X.values)
    label = lb.inverse_transform(pred)[0]

    return {"prediction": label}
