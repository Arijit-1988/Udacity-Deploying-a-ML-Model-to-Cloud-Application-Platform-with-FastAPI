# Model Card: Census Income Classifier

## Model Details
- Model type: RandomForestClassifier
- Framework: scikit-learn
- Intended task: Binary classification of salary bracket (`<=50K` vs `>50K`)

## Intended Use
- Educational demonstration for end-to-end ML deployment with FastAPI.
- Should not be used for high-stakes decisions.

## Training Data
- Source: `starter/data/census.csv`
- Dataset includes demographic and work-related features.
- Label: `salary`

## Metrics
- Metrics used: precision, recall, fbeta.
- Slice metrics are exported to `starter/model/slice_output.txt`.

## Ethical Considerations
- Dataset contains sensitive demographic attributes.
- Predictions can reflect societal and sampling biases.
- Additional fairness auditing is required before real-world use.

## Caveats and Recommendations
- Model quality depends on data quality and representativeness.
- Retrain with larger and better-curated data for production scenarios.
