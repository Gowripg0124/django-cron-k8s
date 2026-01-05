## Prerequisites

The following tools must be installed before running this project:

- Python 3.10+
- Docker
- Kubernetes (Docker Desktop Kubernetes or Minikube)
- kubectl
- Git

---

## Python Dependencies

Installed via `requirements.txt`:

- Django
- django-crontab

---
## Project Structure

django-cron-k8s/
├── config/
│ └── settings.py # Django settings (cron configuration)
├── core/
│ └── cron.py # Cron job logic
├── docker/
│ └── Dockerfile # Docker configuration
├── k8s/
│ └── deployment.yaml # Kubernetes Deployment
├── manage.py
├── requirements.txt
└── README.md

---

## Setup and Run

### Build Docker Image

```bash
docker build -t django-cron-app:latest -f docker/Dockerfile .
```
Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
```

Verify Pod Status

```bash
kubectl get pods
```
View Cron Logs
```bash
kubectl logs -f <pod-name>
```
---
Important Notes
Cron runs automatically after the Kubernetes pod starts

Do not run cron commands on the local machine

Keep replicas set to 1 to avoid duplicate cron executions

Kubernetes logs show only stdout and stderr output

---