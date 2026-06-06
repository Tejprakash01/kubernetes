# Flask + MongoDB + Docker + Kubernetes

Simple Flask application that saves names into MongoDB.

## Project Structure

```text
flask-mongo-app/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/index.html
├── Dockerfile
├── docker-compose.yml
└── k8s/
    ├── mongo-deployment.yaml
    ├── mongo-service.yaml
    ├── flask-deployment.yaml
    └── flask-service.yaml
```

---

## Local Run

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac

# Windows
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r app/requirements.txt
```

### Run Flask

```bash
cd app
python app.py
```

Open:

```text
http://localhost:5000
```

---

## Docker

### Build Image

```bash
docker build -t flask-mongo .
```

### Run with Docker Compose

```bash
docker compose up --build
```

Background:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Application:

```text
http://localhost:5000
```

---

## Kubernetes

### Apply Resources

```bash
kubectl apply -f k8s/
```

### Check Resources

```bash
kubectl get pods
kubectl get svc
```

### Access Application

```bash
kubectl port-forward svc/flask-service 5000:5000
```

Open:

```text
http://localhost:5000
```

### Delete Resources

```bash
kubectl delete -f k8s/
```

---

## Useful Commands

### Docker

```bash
docker ps
docker logs <container>
```

### Kubernetes

```bash
kubectl get all
kubectl logs deployment/flask-app
kubectl describe pod <pod-name>
```
