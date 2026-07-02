# Task Manager API

A RESTful Task Management API built with Django REST Framework to demonstrate backend development, containerization, continuous integration, and Kubernetes deployment.

The project follows modern development practices including JWT authentication, automated testing, Docker-based containerization, GitHub Actions CI, and Kubernetes deployment with PostgreSQL.

---

## Features

### Authentication

* User Registration
* JWT-based Authentication
* Protected API Endpoints

### Task Management

* Create Task
* Retrieve All Tasks
* Retrieve a Single Task
* Update Task
* Delete Task
* User-specific Task Isolation

### Testing

* Registration API Tests
* Login API Tests
* Task CRUD Tests
* Authentication & Authorization Tests

### DevOps

* Dockerized Application
* Docker Compose for Local Development
* GitHub Actions CI Pipeline
* PostgreSQL Integration
* Kubernetes Deployment
* ConfigMaps and Secrets
* Persistent Volume Claims

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* Simple JWT

### Database

* PostgreSQL

### DevOps

* GitHub Actions
* Docker
* Docker Compose
* Kubernetes

---

## Project Structure

```text
task-manager-api/
│
├── accounts/
├── tasks/
├── config/
├── k8s/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Authentication

| Method | Endpoint         | Description                             |
| ------ | ---------------- | --------------------------------------- |
| POST   | `/api/register/` | Register a new user                     |
| POST   | `/api/login/`    | Authenticate user and obtain JWT tokens |

### Tasks

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| GET    | `/api/tasks/`      | Retrieve all tasks      |
| POST   | `/api/tasks/`      | Create a new task       |
| GET    | `/api/tasks/{id}/` | Retrieve a task         |
| PUT    | `/api/tasks/{id}/` | Update a task           |
| PATCH  | `/api/tasks/{id}/` | Partially update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task           |

---

## Running the Project

### Clone the Repository

```bash
git clone <repository-url>
cd task-manager-api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start the Development Server

```bash
python manage.py runserver
```

---

## Running Tests

```bash
python manage.py test
```

---

## Docker

Build the image

```bash
docker build -t task-manager-api .
```

Run the container

```bash
docker run -p 8000:8000 task-manager-api
```

---

## Docker Compose

Start the application

```bash
docker compose up --build
```

Stop the application

```bash
docker compose down
```

---

## Kubernetes Deployment

Deploy all Kubernetes resources

```bash
kubectl apply -f k8s/
```

Verify the deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get pvc
kubectl get ingress
```

---

## Continuous Integration

The project uses GitHub Actions for Continuous Integration.

The pipeline performs the following steps:

1. Checkout Repository
2. Set Up Python Environment
3. Install Dependencies
4. Execute Automated Tests
5. Build Docker Image
6. Push Docker Image to Docker Hub

---

## Kubernetes Resources

The Kubernetes configuration includes:

* Deployment
* Service
* ConfigMap
* Secret
* Persistent Volume
* Persistent Volume Claim
* Ingress

---

## Concepts Demonstrated

* REST API Development
* JWT Authentication
* Django REST Framework
* API Testing
* Docker
* Docker Compose
* PostgreSQL
* GitHub Actions
* Continuous Integration
* Kubernetes Deployments
* ConfigMaps
* Secrets
* Persistent Storage
* Service Discovery

---

## Future Enhancements

* Gunicorn for Production
* Nginx Reverse Proxy
* Health and Readiness Probes
* Horizontal Pod Autoscaler
* Continuous Deployment Pipeline
* API Documentation (Swagger/OpenAPI)
* Role-Based Access Control
* Logging and Monitoring
* Redis Caching
* Celery Background Tasks

---

## License

This project is intended for educational and learning purposes.


