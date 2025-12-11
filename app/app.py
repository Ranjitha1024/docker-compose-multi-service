from flask import Flask
import mysql.connector
import redis
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "App is healthy", 200

@app.route("/")
def index():
    return "Hello from Flask App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
