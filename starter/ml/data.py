import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder


def load_data(path: str) -> pd.DataFrame:
    """Load census data and strip extra whitespace from headers and object values."""
    data = pd.read_csv(path)
    data.columns = [col.strip() for col in data.columns]

    object_columns = data.select_dtypes(include=["object", "string"]).columns
    for col in object_columns:
        data[col] = data[col].astype(str).str.strip()

    return data


def split_data(data: pd.DataFrame, test_size: float = 0.20, random_state: int = 42):
    """Split the data into train and test partitions."""
    train, test = train_test_split(data, test_size=test_size, random_state=random_state)
    return train, test


def process_data(
    data: pd.DataFrame,
    categorical_features,
    label,
    training: bool = True,
    encoder: OneHotEncoder = None,
    lb: LabelBinarizer = None,
):
    """Process the data for machine learning.

    Returns feature matrix X, label vector y, fitted encoder, and fitted label binarizer.
    """
    X = data.drop([label], axis=1)
    y = data[label].values

    if training:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        lb = LabelBinarizer()

        X_cat = encoder.fit_transform(X[categorical_features])
        y = lb.fit_transform(y).ravel()
    else:
        X_cat = encoder.transform(X[categorical_features])
        y = lb.transform(y).ravel() if lb is not None else y

    X_cont = X.drop(columns=categorical_features)
    X_cat_df = pd.DataFrame(X_cat, index=X_cont.index)
    X = pd.concat([X_cat_df, X_cont], axis=1)

    return X.values, y, encoder, lb
