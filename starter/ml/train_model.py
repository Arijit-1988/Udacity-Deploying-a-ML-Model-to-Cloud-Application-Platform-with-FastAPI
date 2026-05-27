from pathlib import Path

import joblib

from starter.ml.data import load_data, process_data, split_data
from starter.ml.model import compute_model_metrics, inference, train_model

CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
LABEL = "salary"


def compute_slice_metrics(test_data, cat_features, model, encoder, lb, output_file):
    """Compute model metrics for each value of each categorical feature."""
    lines = []
    for feature in cat_features:
        for value in sorted(test_data[feature].unique()):
            df_slice = test_data[test_data[feature] == value]
            X_slice, y_slice, _, _ = process_data(
                df_slice,
                categorical_features=cat_features,
                label=LABEL,
                training=False,
                encoder=encoder,
                lb=lb,
            )
            preds = inference(model, X_slice)
            precision, recall, fbeta = compute_model_metrics(y_slice, preds)
            lines.append(
                f"feature={feature}, value={value}, "
                f"precision={precision:.3f}, recall={recall:.3f}, fbeta={fbeta:.3f}"
            )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(lines), encoding="utf-8")


def train_and_save_model(data_path: str, model_dir: str = "starter/model"):
    """Train a model from census data and persist model artifacts."""
    data = load_data(data_path)
    train, test = split_data(data)

    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=CAT_FEATURES,
        label=LABEL,
        training=True,
    )
    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=CAT_FEATURES,
        label=LABEL,
        training=False,
        encoder=encoder,
        lb=lb,
    )

    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

    model_path = Path(model_dir)
    model_path.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_path / "model.joblib")
    joblib.dump(encoder, model_path / "encoder.joblib")
    joblib.dump(lb, model_path / "lb.joblib")

    compute_slice_metrics(
        test_data=test,
        cat_features=CAT_FEATURES,
        model=model,
        encoder=encoder,
        lb=lb,
        output_file=model_path / "slice_output.txt",
    )

    return {
        "precision": precision,
        "recall": recall,
        "fbeta": fbeta,
    }


if __name__ == "__main__":
    metrics = train_and_save_model("starter/data/census.csv")
    print("Training completed with metrics:", metrics)
