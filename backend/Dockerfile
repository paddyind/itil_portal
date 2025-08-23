# syntax=docker/dockerfile:1

# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Define build-time arguments for proxy
ARG http_proxy
ARG https_proxy

# Set proxy environment variables. Pip will use these automatically.
ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
