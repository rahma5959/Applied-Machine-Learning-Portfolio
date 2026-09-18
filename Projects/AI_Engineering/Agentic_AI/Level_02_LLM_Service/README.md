# Level 02 — LLM Service

## Overview

This level extends the FastAPI backend by integrating a **Large Language Model (LLM)**.

The goal is to separate the API layer from the LLM logic and create a dedicated service responsible for generating responses.

## Objectives

* Integrate an LLM into a Python backend
* Understand the role of an LLM service
* Separate API logic from AI logic
* Create a reusable LLM service
* Handle prompts and generated responses
* Expose the LLM through a REST API

## Project Structure

```text
Level_02_LLM_Service/
├── README.md
├── requirements.txt
└── src/
    ├── app.py
    └── services/
        ├── __init__.py
        └── llm_service.py
```

## Architecture

The application follows a simple service-based architecture:

```text
User
  │
  ▼
FastAPI
  │
  ▼
LLM Service
  │
  ▼
LLM
  │
  ▼
Response
```

The responsibilities are separated:

* `app.py` handles the REST API and HTTP requests.
* `llm_service.py` handles the LLM integration and text generation.

## Technologies

* Python
* FastAPI
* Uvicorn
* LLM / Transformers

## Planned API

The application will expose a chat endpoint:

```text
POST /chat
```

Example request:

```json
{
    "message": "What is machine learning?"
}
```

Example response:

```json
{
    "response": "Machine learning is a field of artificial intelligence..."
}
```

## Development Steps

### Step 1 — LLM Service

Create a dedicated service responsible for communicating with the LLM.

```text
llm_service.py
      ↓
     LLM
```

### Step 2 — Test the LLM

Test the LLM independently before connecting it to FastAPI.

```text
Question
   ↓
LLM Service
   ↓
Response
```

### Step 3 — Connect FastAPI

Connect the LLM service to the FastAPI backend.

```text
POST /chat
      ↓
FastAPI
      ↓
LLM Service
      ↓
LLM
      ↓
Response
```

### Step 4 — Test the API

Use the automatic FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## What I Will Learn

* LLM integration
* Prompt handling
* Service-based architecture
* REST API integration with an LLM
* Separation of concerns
* Backend AI application design

## Next Step

The next level will introduce **LangGraph** and transform the LLM service into an **AI Agent** capable of managing workflows and using tools.

```text
FastAPI
   ↓
LLM Service
   ↓
LangGraph Agent
   ↓
Tools
```
