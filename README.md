# AutoOps AI

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
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

## Phase 4 – Docker Hub Integration

✅ Features implemented:
- Updated CI/CD pipeline (`.github/workflows/build.yaml`) to build and push Docker images to **Docker Hub**.  
- Added GitHub repository **Secrets** and **Variables**:
  - `DOCKERHUB_USERNAME` (variable) → Docker Hub account name.  
  - `DOCKERHUB_TOKEN` (secret) → Docker Hub personal access token.  
- Used **official GitHub Actions (`docker/login-action` + `docker/build-push-action`)** for a clean, production-grade setup.  
- Images are pushed with **two tags** for traceability:
  - `latest` → always the most recent build.  
  - `<commit-sha>` → uniquely tied to the exact commit (traceable + reproducible).

### How to Verify
1. Go to **Docker Hub** → [https://hub.docker.com/repositories/mdsaad360](https://hub.docker.com/repositories/mdsaad360)  
2. Confirm `autoops-ai` repo exists and contains both `latest` and commit-specific tags.  
3. Check GitHub Actions logs under the **“Build and Push Docker image”** step.

### Run the Image
```bash
# Pull the latest image from Docker Hub
docker pull mdsaad360/autoops-ai:latest

# Run the container locally
docker run -d -p 8000:8000 mdsaad360/autoops-ai:latest

# Test the health endpoint
curl http://localhost:8000/health
```

## Phase 5a – Dummy Predict Logic & Unit Testing

✅ Features implemented:
- Added a dummy sentiment analysis predict logic.
- Added test case for predict endpoint for:
  - `/predict` endpoint with mock sentiment analysis (positive/negative inputs).

## How to Run Locally

```bash
# Pull docker image
docker pull mdsaad360/autoops-ai:latest

# Start the container
docker run -d -p 8000:8000 mdsaad360/autoops-ai:latest

# Test predict endpoint
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text":"Even"}'

curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text":"Odd"}'
```

## Phase 5b – Add AI Inference (Sentiment Analysis)

✅ Features implemented:
- Integrated  Hugging Face Transformers `pipeline("sentiment-analysis")`.
- Installed additional dependencies: `transformers` and `torch`(CPU-only).
- Updated FastAPI `/predict` endpoint to:
  - Accept text input.
  - Run it through `distilbert-base-uncased-finetuned-sst-2-english`.
  - Return sentiment label (POSITIVE/NEGATIVE) and confidence score.
- Extended test cases to verify model predictions (positive/negative).
- Improved app logging for better observability during tests.

## How to Run Locally

```bash
# Pull docker image
docker pull mdsaad360/autoops-ai:latest

# Start the container
docker run -d -p 8000:8000 mdsaad360/autoops-ai:latest

# Test predict endpoint
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text":"I love coding!"}'

curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text":"I hate dragon fruit"}'
```
## Expected Ouput
```json
{
  "input": "I love coding",
  "label": "POSITIVE",
  "score": 0.9996923208236694
}

{
  "input": "I hate dragon fruit",
  "label": "NEGATIVE",
  "score": 0.9971433281898499
}
```

## Phase 5c –  Add pip Dependency and Docker Build Caching in CI/CD

✅ Features implemented:
- Optimized our CI/CD pipeline by caching Python dependencies. This prevents reinstalling the same packages on every run, reducing pipeline execution time.
- Enabled **`Docker build caching`**. This reduces build times by reusing unchanged layers instead of rebuilding everything from scratch.

## Phase 5d –  Add Dockerfile dev setup

✅ Features implemented:
- Added a separate **`Dockerfile.dev`** for local development:
  - Uses `uvicorn --reload` for auto-restart on code changes
  - Mounts source code into the container (`volumes`) so edits reflect immediately

- Added **`docker-compose.override.yml`**:
  - Overrides the default compose configuration only in local dev
  - Automatically uses `Dockerfile.dev` instead of the production Dockerfile
  - Runs the app in hot-reload mode

-  Run in DEV mode:
  ```bash
  docker compose -f docker-compose.override.yml up --build
  ```
