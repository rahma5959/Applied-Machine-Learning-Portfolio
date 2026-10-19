# Level 10 — Docker: Containerizing a FastAPI Application

## Overview

This project demonstrates how to containerize a FastAPI application using Docker and Docker Compose.

The objective is to package the API and its Python dependencies into a reproducible environment that can run consistently across different machines.

## Features

- FastAPI REST API
- Health-check endpoint
- Docker image built from a Dockerfile
- Port mapping between the host and the container
- Docker Compose service configuration
- `.dockerignore` to exclude unnecessary files from the build context

## Project Structure

```text
Level_10_Docker/
├── src/
│   └── app.py
├── .dockerignore
├── compose.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Requirements

- Docker Desktop
- Docker Compose
- A web browser or an HTTP client

Python does not need to be installed separately to run the containerized application.

## Run with Docker

Build the Docker image:

```bash
docker build -t level10-docker-api .
```

Start the container:

```bash
docker run --name level10-api -p 8000:8000 level10-docker-api
```

Open the API:

- Home: http://localhost:8000
- Health check: http://localhost:8000/health
- Interactive API documentation: http://localhost:8000/docs

Stop the container with `Ctrl+C` when running in the foreground.

## Run with Docker Compose

Build and start the service:

```bash
docker compose up --build
```

Stop the service and remove its container and network:

```bash
docker compose down
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/health` | Reports the application's health status |
| GET | `/docs` | Provides interactive Swagger documentation |

## Key Concepts Learned

- **Docker image:** A packaged template containing the application environment and dependencies.
- **Container:** A running instance of a Docker image.
- **Dockerfile:** Instructions used to build the image.
- **Port mapping:** Makes the application accessible from the host machine.
- **Docker Compose:** Defines and manages application services using a YAML file.
- **Build context:** Files made available to Docker during image construction.
- **Layer caching:** Reusing unchanged build layers to make subsequent builds faster.

## Limitations and Future Improvements

This project is a learning demonstration, not a production deployment. Potential improvements include:

- Pinning dependency versions.
- Adding automated container health checks.
- Running the application as a non-root user.
- Adding automated tests to the container workflow.
- Implementing CI/CD for automated builds and validation.

## Author

AI Engineering and Agentic AI Learning Portfolio