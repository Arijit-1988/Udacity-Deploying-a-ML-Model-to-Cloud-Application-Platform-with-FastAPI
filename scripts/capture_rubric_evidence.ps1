$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
Set-Location $repoRoot

$python = "c:/Users/arijit.h.roy/OneDrive - Accenture/Desktop/FastAPI/.venv/Scripts/python.exe"
$evidenceDir = Join-Path $repoRoot "submission/evidence"
$screenshotsDir = Join-Path $evidenceDir "screenshots"

New-Item -ItemType Directory -Force -Path $evidenceDir | Out-Null
New-Item -ItemType Directory -Force -Path $screenshotsDir | Out-Null

Write-Host "[1/5] Running full local checks..."
& $python run_local_checks.py | Tee-Object (Join-Path $evidenceDir "local_checks.log")

Write-Host "[2/5] Running sanitycheck directly..."
& $python -m starter.sanitycheck | Tee-Object (Join-Path $evidenceDir "sanitycheck.log")

Write-Host "[3/5] Running deployed live POST test..."
$env:LIVE_API_URL = "https://census-fastapi-bom7.onrender.com/predict"
& $python starter/live_post.py | Tee-Object (Join-Path $evidenceDir "live_post.log")

Write-Host "[4/5] Opening pages for screenshot capture..."
Start-Process "http://127.0.0.1:8000/docs"
Start-Process "https://github.com/Arijit-1988/Udacity-Deploying-a-ML-Model-to-Cloud-Application-Platform-with-FastAPI/actions"
Start-Process "https://dashboard.render.com/web/srv-d8b8run7f7vs73brs6j0"

Write-Host "[5/5] Next manual step: capture screenshots with these exact names in submission/evidence/screenshots/"
Write-Host "- 01_local_swagger_docs.png"
Write-Host "- 02_github_actions_checks_pass.png"
Write-Host "- 03_render_service_running.png"
Write-Host "- 04_render_post_prediction_output.png"
