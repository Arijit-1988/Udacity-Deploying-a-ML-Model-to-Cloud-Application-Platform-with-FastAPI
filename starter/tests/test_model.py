import pandas as pd

from starter.ml.data import process_data
from starter.ml.model import compute_model_metrics, inference, train_model


def test_compute_model_metrics_returns_valid_scores():
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1


def test_inference_returns_expected_length():
    X = [[0, 1], [1, 0], [0, 0], [1, 1]]
    y = [0, 1, 0, 1]

    model = train_model(X, y)
    preds = inference(model, X)

    assert len(preds) == len(X)


def test_process_data_training_and_inference_shapes():
    df = pd.DataFrame(
        {
            "age": [25, 50, 31, 44],
            "workclass": ["Private", "Private", "State-gov", "Private"],
            "education": ["Bachelors", "Masters", "HS-grad", "Masters"],
            "marital-status": [
                "Never-married",
                "Married-civ-spouse",
                "Never-married",
                "Married-civ-spouse",
            ],
            "occupation": ["Sales", "Exec-managerial", "Adm-clerical", "Prof-specialty"],
            "relationship": ["Not-in-family", "Husband", "Not-in-family", "Husband"],
            "race": ["White", "White", "Black", "White"],
            "sex": ["Female", "Male", "Female", "Male"],
            "native-country": ["United-States", "United-States", "United-States", "India"],
            "fnlgt": [10000, 20000, 30000, 40000],
            "education-num": [13, 14, 9, 14],
            "capital-gain": [0, 10000, 0, 5000],
            "capital-loss": [0, 0, 0, 0],
            "hours-per-week": [35, 50, 40, 60],
            "salary": ["<=50K", ">50K", "<=50K", ">50K"],
        }
    )

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_train, y_train, encoder, lb = process_data(
        df,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    X_infer, y_infer, _, _ = process_data(
        df,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    assert X_train.shape[0] == 4
    assert X_infer.shape[0] == 4
    assert y_train.shape == y_infer.shape
