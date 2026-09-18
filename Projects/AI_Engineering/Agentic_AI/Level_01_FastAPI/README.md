# Level 01 — FastAPI REST API

## Overview

This level introduces the backend foundation of the AI Agent Platform using **FastAPI**.

The goal is to build a simple REST API, understand how HTTP requests are handled, and prepare the backend architecture for the next AI components.

## Objectives

* Understand the basics of FastAPI
* Create a REST API with Python
* Create a GET endpoint
* Return JSON responses
* Run the API with Uvicorn
* Explore the automatic API documentation

## Project Structure

```text
Level_01_FastAPI/
├── README.md
├── requirements.txt
└── src/
    └── app.py
```

## Technologies

* Python
* FastAPI
* Uvicorn

## Implementation

The application exposes a basic endpoint:

```text
GET /
```

Example response:

```json
{
    "message": "AI Agent Platform API is running"
}
```

## Running the Application

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the API:

```bash
python -m uvicorn src.app:app --reload
```

The API is available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## What I Learned

* How FastAPI applications are created
* How REST endpoints work
* How to define GET routes
* How Uvicorn runs a FastAPI application
* How APIs return JSON responses
* How to use automatic API documentation

## Next Step

The next level will integrate an **LLM service** into the FastAPI backend.

```text
FastAPI
   ↓
LLM Service
   ↓
LLM
```
