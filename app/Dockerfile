FROM python:3.11-slim

WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install flask redis mysql-connector-python

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
