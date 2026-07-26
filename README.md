# 🛍️ TailStore – E-Commerce DevOps Project

TailStore is a containerized e-commerce web application built with **Flask, MySQL, Docker, Jenkins, and Kubernetes**. The project demonstrates a complete DevOps workflow, from application development and database integration to CI/CD automation and Kubernetes deployment.

---

## 🚀 Project Overview

TailStore provides an online shopping interface where users can:

* 🛒 Browse products
* 🛍️ Add products to the cart
* 💳 Proceed through the checkout process
* 📋 Submit billing details
* 🗄️ Store billing information in MySQL
* 💰 Continue to the payment page

The application is containerized using Docker and can be deployed using Kubernetes.

---

## 🏗️ Architecture

```text
                    👤 User
                       │
                       │ HTTPS
                       ▼
              🌐 TailStore Frontend
                       │
                       ▼
               🐍 Flask Backend
                       │
                       ▼
                🗄️ MySQL Database
                billing_details
```

### DevOps Pipeline

```text
👨‍💻 Developer
      │
      ▼
   GitHub
      │
      ▼
   Jenkins
   CI/CD
      │
      ▼
 Docker Image
      │
      ▼
 Docker Hub
      │
      ▼
 Kubernetes Cluster
      │
      ├── TailStore Application Pods
      │
      ├── Kubernetes Service
      │
      └── MySQL Database Pod
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| 🌐 HTML           | Frontend structure           |
| 🎨 CSS            | Frontend styling             |
| ⚡ JavaScript      | Frontend functionality       |
| 🐍 Python Flask   | Backend application          |
| 🗄️ MySQL 8.0     | Database                     |
| 🐳 Docker         | Application containerization |
| 🔗 Docker Compose | Local multi-container setup  |
| 🔄 Jenkins        | CI/CD automation             |
| ☸️ Kubernetes     | Container orchestration      |
| 📦 Docker Hub     | Container image registry     |
| 🐙 GitHub         | Source code management       |

---

## 📁 Project Structure

```text
tailstore/
│
├── assets/                 # CSS, JavaScript, images and frontend assets
│
├── k8s/                    # Kubernetes configuration files
│
├── 404.html                # 404 error page
├── cart.html               # Shopping cart page
├── checkout.html           # Checkout and billing page
├── index.html              # Homepage
├── payment.html            # Payment page
├── register.html           # Registration/Login page
├── shop.html               # Product listing page
├── single-product-page.html # Product details page
│
├── app.py                  # Flask backend application
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── Jenkinsfile             # Jenkins CI/CD pipeline
├── package.json            # Frontend dependencies
├── package-lock.json       # Dependency lock file
├── .env                    # Environment variables
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

---

## 🐍 Flask Backend

The Flask backend handles:

* Serving the frontend pages
* MySQL database connectivity
* Creating the `billing_details` table
* Receiving checkout billing information
* Saving billing details into MySQL
* Redirecting users to the payment page

### Billing Data Stored

```text
Full Name
Email
Address
City
State
ZIP Code
Phone
Different Address
Created At
```

---

## 🗄️ MySQL Database

The application uses **MySQL 8.0**.

Database configuration is managed using environment variables:

```env
MYSQL_HOST=database
MYSQL_USER=root
MYSQL_PASSWORD=kali
MYSQL_DATABASE=tailstore
```

The Flask application automatically creates the required table:

```text
billing_details
```

---

## 🐳 Run with Docker Compose

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd tailstore
```

Create the `.env` file:

```bash
nano .env
```

Add:

```env
MYSQL_HOST=database
MYSQL_USER=root
MYSQL_PASSWORD=kali
MYSQL_DATABASE=tailstore
```

Build and start the application:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker ps
```

Check application logs:

```bash
docker logs -f tailstore
```

Access the application:

```text
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

The project uses **Jenkins** to automate the CI/CD workflow.

```text
Developer Push
      │
      ▼
    GitHub
      │
      ▼
    Jenkins
      │
      ├── Checkout Code
      │
      ├── Build Docker Image
      │
      ├── Push Image to Docker Hub
      │
      └── Deploy Application
             │
             ▼
        Kubernetes
```

---

## ☸️ Kubernetes Deployment

The `k8s` directory contains Kubernetes configuration files for deploying TailStore.

Typical resources include:

* TailStore Deployment
* TailStore Service
* MySQL Deployment
* MySQL Service
* ConfigMaps/Secrets where required

Check the Kubernetes resources:

```bash
kubectl get all -n tailstore
```

Check application pods:

```bash
kubectl get pods -n tailstore
```

Check services:

```bash
kubectl get svc -n tailstore
```

---

## 🔐 Security Note

For production deployments, avoid storing sensitive credentials directly in `.env` files or source code.

Use:

* Kubernetes Secrets
* AWS Secrets Manager
* HashiCorp Vault
* Other secure secret-management solutions

Also, configure **HTTPS/TLS** for production traffic.

---

## 📌 Project Highlights

* ✅ Flask-based backend
* ✅ MySQL database integration
* ✅ Customer billing data storage
* ✅ Docker containerization
* ✅ Docker Compose environment
* ✅ Jenkins CI/CD pipeline
* ✅ Docker Hub image management
* ✅ Kubernetes deployment
* ✅ Scalable application architecture
* ✅ DevOps automation workflow

---

## 👨‍💻 Author

**Bakhtawar Khan**

DevOps Engineer | Cloud | Docker | Kubernetes | Jenkins | AWS

---

## ⭐ Project Goal

The main goal of this project is to demonstrate a practical **end-to-end DevOps workflow** by combining application development, database integration, containerization, CI/CD automation, container registry management, and Kubernetes deployment into a single e-commerce project.
