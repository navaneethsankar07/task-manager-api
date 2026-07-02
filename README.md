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

