📘 Dockerized Multi-Service Application

This project demonstrates a Docker Compose setup containing an App, MySQL Database, Redis Cache, and Nginx Reverse Proxy.
It shows how to build a simple containerized multi-service architecture with health checks, named volumes, custom networks, and environment variables.

🔧 Services Included
1️⃣ Application (app)

Main backend application
Uses variables from .env
Connected to Redis and MySQL

2️⃣ MySQL Database (db)

Uses named volume for data persistence
Credentials stored in .env
Not exposed publicly

3️⃣ Redis Cache (cache)

Used for storing sessions or caching
Internal service only

4️⃣ Nginx Reverse Proxy

Routes external traffic to the App
Can be extended for SSL

📁 Project Structure
my-docker-app/
│── app/
│── db/
│── cache/
│── reverse-proxy/
│── .env.example
│── docker-compose.yml
│── .gitignore
│── README.md

🔐 Environment Variables

A .env.example file is included.
Before running:
cp .env.example .env

Open .env and replace values such as DB credentials, app port, etc.

➡️ Note:
.env is added to .gitignore and must not be uploaded to GitHub.

🚀 How to Run the Project
docker compose up --build -d

Check running containers:
docker ps

To stop services:
docker compose down

📦 Volumes & Networks

mysql_data → Persistent MySQL storage
Custom Docker network → Ensures secure communication between services

❤️ Why This Project

Helps understand real-time multi-service deployments
Shows container orchestration skills
Interview-friendly and production-ready structure
