# AutoOps AI

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CI/CD Pipeline](https://github.com/mdsaad360/AutoOps-AI/actions/workflows/build.yaml/badge.svg)](https://github.com/mdsaad360/AutoOps-AI/actions/workflows/build.yaml)

AutoOps AI is a portfolio project demonstrating DevOps + MLOps practices:

- 🚀 **FastAPI** microservice with `/health` and `/predict`
- 🐳 Containerization with **Docker**
- ⚙️ CI/CD with **GitHub Actions** + GitOps via **ArgoCD**
- 📊 Monitoring with **Prometheus** + **Grafana**
- ☁️ Cloud-ready (AWS EKS + MWAA)

## Phase 1 – Local FastAPI App

✅ Features implemented:
- `/health` endpoint returning service status
- `/predict` endpoint (placeholder for AI logic)
- Logging enabled
- Swagger UI available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Setup Instructions

### 1. Clone repo & create environment
```powershell
git clone https://github.com/mdsaad360/autoops-ai.git
cd autoops-ai
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install dependencies
```powershell
pip install -r requirements.txt
```

### 3. Run the app
```powershell
uvicorn app.main:app --reload
```

### 4. Test endpoints
Health check: http://127.0.0.1:8000/health

Swagger UI: http://127.0.0.1:8000/docs

## Phase 2 – Dockerized FastAPI App

✅ Features implemented:
- Added `Dockerfile` and `.dockerignore`
- App runs inside a Docker container
- Port mapping allows access from host at `127.0.0.1:8000`
- Ready for future use with Kubernetes and AWS

### Run with Docker

1. **Build the image**
```powershell
docker build -t autoops-ai:1.0 .
```

2. **Run the container**
```powershell
docker run -d -p 8000:8000 autoops-ai:1.0
```

3. **Test endpoints**
```
Health check → http://127.0.0.1:8000/health
Swagger UI → http://127.0.0.1:8000/docs
```

4. **Optional: Run with Docker Compose**
```powershell
docker compose up --build
```

## Phase 3 – CI/CD with GitHub Actions

✅ Features implemented:
- Added workflow file: `.github/workflows/build.yml`
- Configured GitHub Actions to run on:
  - Pull requests → lint + unit tests
  - Push to `main` → lint + unit tests + Docker image build
- Added real unit tests with `pytest`:
  - `/health` endpoint returns `{"status": "ok"}`
  - `/predict` endpoint returns `"Model not implemented yet"`
- Configured linting with `flake8` for code quality checks
- Docker images tagged with both:
  - `autoops-ai:latest` (human-friendly)
  - `autoops-ai:<commit-sha>` (traceable, reproducible)
- Added `pytest.ini` to ensure imports resolve cleanly
- CI/CD status badge added to README

### Test the CI/CD Workflow

1. **Trigger**  
   - Create a Pull request → Runs tests & lint only  
   - Push to main → Runs tests, lint, and builds Docker image  

2. **Check pipeline status**  
   - Go to your repo’s **Actions** tab  
   - Select the workflow **“Test & Build Pipeline”**  
   - View logs for lint, test, and Docker build steps  