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

