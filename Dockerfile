# Use the official Python image as a base
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    default-mysql-client \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

# Copy the current directory to the working directory
COPY . /app/
