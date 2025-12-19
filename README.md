# AutoOps AI

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CI/CD Pipeline](https://github.com/mdsaad360/AutoOps-AI/actions/workflows/build.yaml/badge.svg)](https://github.com/mdsaad360/AutoOps-AI/actions/workflows/build.yaml)

AutoOps AI is a portfolio project demonstrating DevOps + MLOps practices:

- 🚀 **FastAPI** microservice with `/health` and `/predict`
- 🐳 Containerization with **Docker** and Orchestration with **Kubernetes**
- ⚙️ CI/CD with **GitHub Actions** + GitOps via **ArgoCD**
- 📊 Monitoring with **Prometheus** + **Grafana**
- ☁️ Cloud-ready (AWS EKS)

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
  docker compose -f docker-compose.override.yaml up --build
  ```
## Phase 6a - Local Kubernetes Simulation using Minikube

✅ Features implemented:
- Installed and configured Minikube for local Kubernetes.
- Initialized a local single-node Kubernetes cluster.
- Learned and validated Kubernetes core concepts:
  - Pods
  - Deployments
  - Services (NodePort)

- Deployed autoops-ai using Kubernetes manifests.

- Exposed the application locally via NodePort.

- Verified application behavior inside a Kubernetes runtime.

## Phase 6b - Host autoops-ai on AWS EC2 (HTTP)

✅ Features implemented:
- Launched an EC2 Ubuntu instance (default VPC) with a public IP.

- Used SSH key-based authentication.

- Opened Security Group inbound ports: SSH (22) restricted to my IP, HTTP/testing port (8000) open as needed.

- Installed and configured Docker on EC2.

- Pulled autoops-ai image from Docker Hub.

- Ran the container manually on EC2.

- Exposed the application via EC2 public IP over HTTP.

<img src="images/EC2/aws-ec2-autoops-ai-ub.png" alt="AWS EC2 Instance" width="800"/>

## Setup Instructions

### 1. Launch EC2 (Fast-track using default VPC)
- AMI: Ubuntu 22.04

- Instance type: t3.micro

- Key pair: create / download .pem

- Security Group inbound rules:

  - SSH (22) — Source: My IP

  - Custom TCP (8000) — Source: 0.0.0.0/0 (for testing)


### 2. SSH into EC2
```bash
ssh -i ./your_key_name.pem ubuntu@<ec2_public_ip>
```

### 3. Install Docker & Compose
```bash
# 1. Update the package index
sudo apt-get update

# 2. Install necessary packages to allow apt to use a repository over HTTPS
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y

# 3. Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Update the package index again with the new repository data
sudo apt-get update

# 6. Install Docker Engine, CLI, and Containerd
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# 7. Verify the installation
sudo docker run hello-world
```

<img src="images/EC2/verify-docker-install.png" alt="Example verify output" width="800"/>

```bash
# 8. Manage Docker as a non-root user (For this change to take effect, you must log out of your SSH session and log back in. )
sudo usermod -aG docker ${USER}
```

### 4. Deploy app
```bash
docker pull mdsaad360/autoops-ai:latest

docker run -d -p 8000:8000 mdsaad360/autoops-ai:latest

docker ps
```

<img src="images/EC2/docker-run-ec2.png" alt="Docker run on ec2" width="800"/>

### 5. Verify the app
```bash
#Run below outside instance to verfiy the app is running
curl http://<EC2_PUBLIC_IP>:8000/health
```

<img src="images/EC2/verify-app-8000.png" alt="Verify app is running" width="800"/>

## Phase 6c - Host autoops-ai on AWS EKS (HTTP via ALB)

✅ Features implemented:
- Installed and configured AWS CLI.
- Created an EKS cluster via a config file( [cluster.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/cluster.yaml) ).
- Generated and updated kubeconfig using AWS CLI.
- Deployed autoops-ai using Kubernetes manifests( [deployment.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/base/deployment.yaml) ).
- Created Kubernetes LoadBalancer Service( [service-lb.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/service-lb.yaml) ).
- Exposed application publicly via ALB DNS over HTTP.

## Setup Instructions

###  1. Install and configure AWS CLI
```bash
pip install awscli --upgrade --user

aws configure   # set access key, secret, region, default output
```

### 2. Create an EKS Cluster
```bash
eksctl create cluster -f cluster.yaml
```
<img src="images/EKS/ekscktl-create-cluster.png" alt="Create an EKS cluster" width="800"/>

### 3. Create and verify app deployment and load balancer service
```bash
aws eks update-kubeconfig --region us-east-1 --name autoops-ai-eks
```

<img src="images/EKS/verify-cluster-creation.png" alt="Create and Update kubeconfig" width="800"/>

```bash
kubectl apply -f deployment.yaml

kubectl apply -f serivce-lb.yaml
```

<img src="images/EKS/Phase1/create-deployment-alb.png" alt="Apply k8s manifests" width="500"/>

```bash
kubect get deployments

kubectl get pods -o wide

kubectl get svc autoops-ai-lb
```

<img src="images/EKS/Phase1/k-get-deploy-pods.png" alt="Get deployments, pods, lb service" width="800"/>

### 4. Test the app
```bash
curl http://<LB_DNS>/health

curl http://<LB_DNS>/predict -H "Content-Type: application/json" -d '{"text":"I love DragonFruit!"}'
``` 

Bash

<img src="images/EKS/Phase1/test-app-bash.png" alt="Test result from bash" width="800"/>

Postman

<img src="images/EKS/Phase1/test-app-postman-predict.png" alt="Test result from postman" width="800"/>

Web - health endpoint

<img src="images/EKS/Phase1/test-app-web-health.png" alt="Test result from web for health endpoint" width="800"/>

Web - Documentation 

<img src="images/EKS/Phase1/test-app-web-docs.png" alt="Test result from web for documentation" width="800"/>

## Phase 6d - Domain, TLS & HTTPS (Ingress + Route53)

✅ Features implemented:

- Purchased custom domain: autoops-ai.cloud.

- Configured AWS Route53 Hosted Zone( DNS fundamentals - A, CNAME, Alias records).

- Installed Ingress NGINX Controller on EKS.

- Installed cert-manager for certificate automation.

- Configured Let’s Encrypt ClusterIssuer( [cluster-issuer.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/base/cluster-issuer.yaml) ).

- Created Kubernetes Ingress resources( [autoops-ingress.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/base/autoops-ingress.yaml) ).

- Integrated HTTPS using TLS secrets.

- Routed domain traffic to Ingress Load Balancer via Route53.

- Exposed autoops-ai securely over HTTPS.

### 
Domain - GoDaddy

<img src="images/EKS/Phase2/domain-godaddy-autoops-ai.png" alt="Domain ownership record - GoDaddy" width="400"/>

Route53 HZ

<img src="images/EKS/Phase2/route53-hz.png" alt="Route53 configuration" width="800"/>

## Test results

Web - health endpoint

<img src="images/EKS/Phase2/test-web-health.png" alt="Test result from web for health endpoint" width="800"/>

Web - Documentation

<img src="images/EKS/Phase2/test-web-documentation.png" alt="Test result from web for documentation" width="800"/>

Postman - predict endpoint

<img src="images/EKS/Phase2/test-postman-predict.png" alt="Test result from postman for predict" width="800"/>

## Phase 7a - GitOps Repository Creation

✅ Features implemented:

- Created a dedicated GitOps repository( [autoops-ai GitOps repo](https://github.com/mdsaad360/autoops-ai-gitops) ).

- Uploaded Kubernetes manifests to the gitops repo( [K8s manifests](https://github.com/mdsaad360/autoops-ai-gitops/tree/main/base) ).

- Established declarative infrastructure management.

- Enabled version-controlled deployments.

## Phase 7b - Install ArgoCD on EKS & link ArgoCD to the GitOps Repository

✅ Features implemented:

- Installed ArgoCD in EKS cluster.

- Exposed ArgoCD UI securely and retrieved and updated admin credentials.

- Created ArgoCD Application resource and linked ArgoCD to the GitOps repository( [argocd.yaml](https://github.com/mdsaad360/autoops-ai-gitops/blob/main/argocd.yaml) )

- Enabled automatic synchronization.

- Ensured cluster state always matches Git state.

ArgoCD UI

<img src="images/EKS/Phase2/login-argocd.png" alt="ArgoCD UI" width="800"/> 