# Rubric Evidence Package

## Rubric Compliance Audit (Current Status)

1. Repository and version control:
- Status: PASS
- Evidence:
  - Repository initialized and pushed to GitHub.
  - Trained artifacts committed in starter/model/.

2. CI/CD with GitHub Actions:
- Status: PASS
- Evidence:
  - Workflow runs pytest and flake8 on push/PR.
  - Python version aligned to development version family (3.14).
  - File: .github/workflows/ci.yml

3. Data handling:
- Status: PASS
- Evidence:
  - Data loaded from starter/data/census.csv.
  - Whitespace trimming in load_data().
  - File: starter/ml/data.py

4. Model implementation:
- Status: PASS
- Evidence:
  - Training, inference, metrics, and artifact persistence implemented.
  - Slice metrics function implemented for categorical features.
  - Files: starter/ml/model.py, starter/ml/train_model.py

5. Model unit tests (>=3 functions):
- Status: PASS
- Evidence:
  - Three tests in starter/tests/test_model.py.

6. FastAPI implementation:
- Status: PASS
- Evidence:
  - GET / welcome endpoint.
  - POST /predict endpoint.
  - Type hints used.
  - Pydantic model includes examples and hyphenated alias handling.
  - File: starter/main.py

7. API unit tests:
- Status: PASS
- Evidence:
  - GET test validates status and payload.
  - Two POST tests validate each output class (<=50K and >50K).
  - File: starter/tests/test_api.py

8. sanitycheck.py execution:
- Status: PASS
- Evidence:
  - Script present and validates GET/POST test coverage heuristics.
  - File: starter/sanitycheck.py

9. Model card:
- Status: PASS
- Evidence:
  - File: starter/model_card.md

10. Cloud deployment + live POST script:
- Status: PASS
- Evidence:
  - Render blueprint deployed from render.yaml.
  - Deployed URL: https://census-fastapi-bom7.onrender.com
  - POST script present and tested: starter/live_post.py

11. GitHub repo link in README/comments:
- Status: PASS
- Evidence:
  - README contains repository URL.

12. Required screenshots included:
- Status: PENDING USER CAPTURE
- Evidence:
  - Checklist and capture commands provided below.

## Exact Screenshot Checklist

Capture these files into submission/evidence/screenshots/ with the exact names below:

1. 01_local_swagger_docs.png
- Required content:
  - Browser at http://127.0.0.1:8000/docs
  - GET / visible
  - POST /predict expanded
  - Request body example visible with fields like age, capital-gain, education, hours-per-week

2. 02_github_actions_checks_pass.png
- Required content:
  - GitHub Actions run page for this repo
  - Latest run shows pytest and flake8 passing

3. 03_render_service_running.png
- Required content:
  - Render service page for census-fastapi
  - Service URL visible
  - Healthy/running status visible

4. 04_render_post_prediction_output.png
- Required content:
  - Terminal output from running starter/live_post.py
  - URL shown as deployed Render endpoint
  - Status 200 and prediction JSON visible

## Commands to Prepare and Capture Evidence

Run from repository root.

1. Run full local checks and save log:

python run_local_checks.py | Tee-Object submission/evidence/local_checks.log

2. Start local API for Swagger screenshot:

python -m uvicorn starter.main:app --host 127.0.0.1 --port 8000

3. In a second terminal, open local docs page:

Start-Process "http://127.0.0.1:8000/docs"

4. Open GitHub Actions page for screenshot:

Start-Process "https://github.com/Arijit-1988/Udacity-Deploying-a-ML-Model-to-Cloud-Application-Platform-with-FastAPI/actions"

5. Open Render service dashboard for screenshot:

Start-Process "https://dashboard.render.com/web/srv-d8b8run7f7vs73brs6j0"

6. Run live POST test against deployed Render URL and save output:

$env:LIVE_API_URL = "https://census-fastapi-bom7.onrender.com/predict"
python starter/live_post.py | Tee-Object submission/evidence/live_post.log

## Final Submission Gate

Before submission, verify all below are true:
- pytest passes
- flake8 passes
- sanitycheck.py passes
- screenshots captured with required content
- GitHub repository link present in README
