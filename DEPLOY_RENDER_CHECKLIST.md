# Render Deployment: Ready Command Checklist

## 1) Local Validation (before push)
Run from repository root:

python run_local_checks.py

## 2) Commit and Push

git add .
git commit -m "chore: prepare render deployment and automation"
git push origin main

## 3) Create Render Service (Blueprint)
Option A (recommended):
- In Render dashboard, choose New + > Blueprint.
- Connect GitHub repo.
- Select this repository.
- Render reads render.yaml and creates service automatically.

Option B (manual web service):
- New + > Web Service > connect repo.
- Build command: pip install -r requirements.txt
- Start command: uvicorn starter.main:app --host 0.0.0.0 --port $PORT
- Health check path: /
- Environment variable: PYTHON_VERSION=3.14.2

## 4) Verify Deployment
After deployment:
- Open: https://<your-service>.onrender.com/
- Open Swagger: https://<your-service>.onrender.com/docs

Test POST using script:
1. Edit starter/live_post.py and set URL.
2. Run:

python starter/live_post.py

## 5) Auto-deploy and CI Gate
- Keep autoDeploy enabled in Render.
- In GitHub, require CI checks for protected branch merges:
  - pytest
  - flake8
