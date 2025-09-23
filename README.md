# AutoOps AI

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
<!-- [![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]() -->

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