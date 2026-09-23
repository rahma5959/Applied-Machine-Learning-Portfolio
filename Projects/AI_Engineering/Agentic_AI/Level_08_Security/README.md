# Level 08 – Security

## Overview

This level introduces the basic security concepts required for an AI Agent platform.

The objective is to understand and implement:

* User authentication
* OAuth2 password flow
* Bearer tokens
* Protected API endpoints
* Role-based authorization
* HTTP `401 Unauthorized` and `403 Forbidden` responses

The implementation uses **FastAPI** and its built-in security utilities.

---

## Learning Objectives

By completing this level, I learned how to:

* Authenticate users through an API endpoint.
* Generate an access token after successful authentication.
* Protect API routes using Bearer authentication.
* Distinguish authentication from authorization.
* Implement role-based access control.
* Restrict administrative endpoints to users with the required role.
* Test authentication and authorization through Swagger UI.

---

## Project Structure

```text
Level_08_Security/
│
├── README.md
├── requirements.txt
│
└── src/
    ├── __init__.py
    └── app.py
```

---

## Technologies

* Python
* FastAPI
* OAuth2
* Bearer Authentication
* Uvicorn
* Swagger UI

---

## Authentication vs Authorization

### Authentication

Authentication answers:

> **Who are you?**

The application verifies the username and password provided by the user.

In this learning project, a simple in-memory user is used:

```python
fake_user = {
    "username": "rahma",
    "password": "1234",
    "role": "admin"
}
```

After successful authentication, the API returns an access token.

### Authorization

Authorization answers:

> **What are you allowed to do?**

After authentication, the application checks the user's role before allowing access to specific resources.

For example:

* `user` → access to regular protected resources
* `admin` → access to administrative resources

---

## API Endpoints

### 1. Health Check

```http
GET /
```

Returns a simple message confirming that the security API is running.

Example response:

```json
{
  "message": "AI Agent Platform Security API is running"
}
```

---

### 2. Login and Token Generation

```http
POST /token
```

The user sends their username and password.

If the credentials are valid, the API returns a Bearer access token.

Example:

```json
{
  "access_token": "my-secret-token",
  "token_type": "bearer",
  "role": "admin"
}
```

Invalid credentials return:

```http
401 Unauthorized
```

---

### 3. Protected Endpoint

```http
GET /protected
```

This endpoint requires a valid Bearer token.

Without authentication:

```http
401 Unauthorized
```

With a valid token:

```json
{
  "message": "You have access to the protected route",
  "token": "my-secret-token"
}
```

---

### 4. Admin Endpoint

```http
GET /admin
```

This endpoint demonstrates role-based authorization.

If the authenticated user has the `admin` role, access is granted.

Otherwise:

```http
403 Forbidden
```

Example successful response:

```json
{
  "message": "Welcome to the admin area"
}
```

---

## HTTP Security Responses

This project demonstrates the difference between two common HTTP security responses.

### 401 Unauthorized

The user has not been properly authenticated.

Example:

```text
No Bearer token provided
```

The API returns:

```http
401 Unauthorized
```

### 403 Forbidden

The user is authenticated but does not have the required permission.

Example:

```text
Authenticated user with role = user
Attempting to access /admin
```

The API returns:

```http
403 Forbidden
```

---

## Testing with Swagger UI

FastAPI automatically provides an interactive API documentation interface.

Start the application with:

```bash
python -m uvicorn src.app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

The security flow can be tested directly from Swagger UI.

### Authentication Test

1. Open `/docs`.
2. Click **Authorize**.
3. Enter the username.
4. Enter the password.
5. Authorize the application.
6. Call `/protected`.

### Authorization Test

The `/admin` endpoint can be tested with different roles.

For example:

```text
role = user
→ 403 Forbidden
```

and:

```text
role = admin
→ 200 OK
```

---

## Security Flow

The implemented flow is:

```text
User
  │
  │ username + password
  ▼
POST /token
  │
  │ authentication
  ▼
Access Token
  │
  │ Bearer token
  ▼
Protected API
  │
  │ authorization
  ▼
Role Check
  │
  ├── user  → regular access
  │
  └── admin → administrative access
```

---

## Relevance to AI Agent Systems

Authentication and authorization become particularly important when an AI Agent can access tools and external resources.

For example:

```text
User
  ↓
Authentication
  ↓
AI Agent
  ↓
Authorization
  ├── Calculator Tool
  ├── RAG Tool
  ├── Database Tool
  └── Administrative Tools
```

Different roles can be used to control which tools or resources an agent is allowed to access.

For example:

```text
Regular User
→ Ask questions
→ Use RAG
→ Use calculator

Administrator
→ All regular permissions
→ Database administration
→ System management
```

This provides a foundation for securing more advanced agentic AI systems.

---

## Current Implementation Scope

This level is intentionally designed as a learning implementation.

It demonstrates the concepts of authentication and authorization without introducing unnecessary infrastructure.

The current implementation uses:

* An in-memory user
* A simple access token
* A static role
* FastAPI OAuth2 utilities

It is **not intended as a production authentication system**.

A production implementation could later introduce:

* Password hashing
* JWT access tokens
* Database-backed users
* Token expiration and refresh tokens
* OAuth2/OpenID Connect providers
* More granular permissions
* Secure secret management
* Audit logging

These concepts can be introduced progressively in future levels.

---

## Key Takeaways

This level demonstrates the security foundations required before exposing an AI Agent platform through an API.

The main concepts learned are:

```text
Authentication
      ↓
Access Token
      ↓
Protected Endpoint
      ↓
Authorization
      ↓
Role-Based Access
```

These concepts will later be integrated with the AI Agent architecture to control access to tools, data, and administrative operations.

---

## Next Step

**Level 09 – Observability**

The next level will focus on monitoring and tracing the AI Agent system, including:

* Agent execution
* Tool calls
* Errors
* Execution traces
* Performance monitoring
* LLM/agent observability
