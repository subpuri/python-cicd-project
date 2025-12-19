# InfraOps Automator 🚀

InfraOps Automator is an end-to-end **Python-based infrastructure operations automation platform** built to demonstrate **real-world DevOps and Cloud-Native practices**.

The project showcases how a Python application can be:
- containerized with Docker
- tested automatically
- pushed to AWS ECR
- deployed on a self-managed Kubernetes (k3s) cluster on AWS EC2
- fully automated using Jenkins CI/CD
- provisioned using Terraform

This repository is designed as a **learning-focused but production-aligned project**.

---

## 🧩 High-Level Architecture

Developer (Git Push)
|
v
GitHub Repository
|
v
Jenkins CI/CD
(WSL-based Jenkins)
|
|-- Run tests (pytest)
|-- Build Docker image
|-- Push image to AWS ECR
|-- Deploy manifests via kubectl
v
AWS EC2 (Free Tier)
|
k3s Cluster
|
FastAPI Application
(NodePort Service)





---

## ✨ Features

- ✅ Python automation & scripting
- ✅ FastAPI-based REST API
- ✅ CLI tool for system operations
- ✅ Dockerized application
- ✅ Private AWS ECR image registry
- ✅ Kubernetes (k3s) deployment
- ✅ Jenkins-based CI/CD pipeline
- ✅ Infrastructure provisioned using Terraform
- ✅ Free-tier friendly AWS setup

---

## 🛠️ Tech Stack

### Application
- **Python 3.10**
- **FastAPI**
- **psutil**
- **pytest**

### DevOps & Cloud
- **Docker**
- **Kubernetes (k3s)**
- **AWS EC2**
- **AWS ECR**
- **Terraform**
- **Jenkins**

---

## 📂 Project Structure

python-cicd-project/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── core/ # Config & logging
│ ├── system/ # CPU, memory, disk metrics
│ ├── cli/ # CLI automation
│ ├── tests/ # Pytest test cases
│ └── requirements.txt
│
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ └── service.yaml # NodePort Service
│
├── terraform/
│ ├── main.tf # EC2 & IAM provisioning
│ ├── variables.tf
│ ├── outputs.tf
│ └── versions.tf
│
├── Dockerfile
├── Jenkinsfile
├── pytest.ini
├── .gitignore
└── README.md




---

## 🚀 Application Capabilities

### REST API (FastAPI)

Available endpoints:

| Endpoint | Description |
|--------|-------------|
| `/health` | Health check |
| `/system/cpu` | CPU usage metrics |
| `/system/memory` | Memory usage metrics |
| `/system/disk` | Disk usage metrics |

Swagger UI:

http://<EC2_PUBLIC_IP>:30080/docs


---

### CLI Tool

The same functionality is available via CLI:

```bash
python3 -m app.cli.ops_cli cpu
python3 -m app.cli.ops_cli memory
python3 -m app.cli.ops_cli disk --path /


---

🧪 Testing

Tests are written using pytest and executed automatically in CI.

pytest

The pipeline ensures:

Tests run before image build

Failures stop deployment




---
🐳 Docker

Build locally:

docker build -t infraops-automator .
docker run -p 8000:8000 infraops-automator




---
☸️ Kubernetes Deployment (k3s)

The app is deployed using:

Deployment (single replica, free-tier safe)

NodePort Service

Apply manually:

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml



---

🔐 AWS ECR Integration

Images are pushed to private AWS ECR

Kubernetes pulls images using imagePullSecret

No credentials stored in repo



---

🤖 Jenkins CI/CD Pipeline

On every push to main, Jenkins:

Clones the repository

Runs pytest

Builds Docker image

Pushes image to AWS ECR

Deploys updated image to Kubernetes

This ensures fully automated, repeatable deployments.



---

🌍 Infrastructure as Code (Terraform)

Terraform provisions:

EC2 instance (free tier)

IAM role with ECR permissions

Security groups

State files and secrets are intentionally excluded from Git.

🔒 Security & Best Practices

❌ No secrets in repository

❌ No Terraform state in Git

❌ No private keys committed

✅ IAM roles used for AWS access

✅ Reproducible CI/CD pipeline

✅ Container-based testing



---

📈 Learning Outcomes

This project demonstrates hands-on experience with:

Python automation & backend development

Docker & container workflows

Kubernetes fundamentals

AWS ECR & EC2

Jenkins CI/CD pipelines

Terraform infrastructure provisioning

Debugging real-world DevOps issues



---

🏁 Future Enhancements

Helm chart support

Ingress controller (NGINX)

Prometheus & Grafana monitoring

Horizontal Pod Autoscaling

Remote Terraform backend (S3 + DynamoDB)





---

👤 Author

Subhash Puri

This project was built as a hands-on learning initiative to gain deep, practical understanding of backend development and cloud-native DevOps workflows.



