# Deploying a ML Model to Cloud Application Platform with FastAPI

GitHub repository: https://github.com/Arijit-1988/Udacity-Deploying-a-ML-Model-to-Cloud-Application-Platform-with-FastAPI

## Project Summary
This project trains a census-income classification model, validates slice performance,
serves predictions with FastAPI, and includes CI checks with pytest and flake8.

## Quickstart
1. Install dependencies:
   pip install -r requirements.txt
2. Train model artifacts:
   python -m starter.ml.train_model
3. Run tests:
   pytest -q
4. Run lint:
   flake8
5. Run API sanity checks:
   python -m starter.sanitycheck
6. Start API:
   uvicorn starter.main:app --reload

## One-command Local Checklist
- Run all required local checks in one command:
  python run_local_checks.py

## Deployment Notes
- App start command: `uvicorn starter.main:app --host 0.0.0.0 --port $PORT`
- Make sure deployment uses the same Python major/minor version used in development.
- Enable auto deploy only after CI checks pass.

## Render Files
- `render.yaml` contains Render Blueprint service config.
- `DEPLOY_RENDER_CHECKLIST.md` contains a ready command checklist.
