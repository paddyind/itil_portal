# syntax=docker/dockerfile:1

# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
ENV http_proxy=http://genproxy.amdocs.com:8080
ENV https_proxy=http://genproxy.amdocs.com:8080
RUN pip install --proxy http://genproxy.amdocs.com:8080 --no-cache-dir -r requirements.txt

# Copy project
COPY . .
