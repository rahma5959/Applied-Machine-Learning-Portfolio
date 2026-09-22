# Level 06 — PostgreSQL

## Overview

This level introduces **PostgreSQL database integration** into the AI Agent Platform.

The goal is to allow the Agent to interact with a relational database through a dedicated database tool.

The Agent can:

* Perform calculations using a Calculator tool
* Retrieve documents from PostgreSQL using a Database tool
* Route the user request to the appropriate tool

---

## Learning Objectives

This level focuses on:

* Understanding PostgreSQL integration with Python
* Connecting a Python application to PostgreSQL
* Creating database tables
* Inserting and retrieving data
* Creating a database tool for the AI Agent
* Using LangChain tools
* Integrating database operations into a LangGraph Agent

---

## Project Structure

```text id="6uw0a9"
Level_06_PostgreSQL/
│
├── README.md
├── requirements.txt
│
└── src/
    ├── Agent.py
    │
    ├── database/
    │   ├── __init__.py
    │   ├── connection.py
    │   ├── init_db.py
    │   └── read_document.py
    │
    └── tools/
        ├── __init__.py
        ├── calculator.py
        └── database_tool.py
```

---

## Architecture

```text id="b9h0vz"
                    USER
                      │
                      ▼
                ┌───────────┐
                │ AI AGENT  │
                └─────┬─────┘
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       Calculator Tool   Database Tool
             │                 │
             ▼                 ▼
        Calculation        PostgreSQL
                               │
                               ▼
                           Documents
```

The Agent analyzes the user's request and routes it to the appropriate tool.

---

## PostgreSQL Database

A PostgreSQL database named `ai_agent` is used for this level.

The main table is:

```sql id="4d8t6f"
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);
```

The table stores simple text documents.

Example:

```text id="7l6h0v"
ID: 1
Title: Machine Learning
Content: Machine learning is a branch of artificial intelligence
that allows computers to learn patterns from data.
```

---

## Database Connection

The project uses the `psycopg` library to connect Python to PostgreSQL.

The connection is handled by:

```text id="1g9l1h"
src/database/connection.py
```

Example:

```python id="k9e4yz"
import psycopg

def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="ai_agent",
        user="postgres",
        password="YOUR_PASSWORD"
    )
    return connection
```

> For a production application, database credentials should be stored in environment variables rather than directly in the source code.

---

## Database Initialization

The database initialization script creates the `documents` table.

Run it from the `Level_06_PostgreSQL` directory:

```bash id="l3q3zj"
python -m src.database.init_db
```

---

## Reading Documents

Documents can be retrieved directly from PostgreSQL using:

```bash id="w1j7x8"
python -m src.database.read_document
```

This verifies that Python can successfully communicate with the PostgreSQL database.

---

## Database Tool

The database functionality is exposed to the Agent through a LangChain tool.

The tool retrieves documents from PostgreSQL:

```python id="g8q0r2"
@tool
def get_documents() -> list:
    """Retrieve all documents stored in the PostgreSQL database."""
```

This creates a separation between:

```text id="9j7z0k"
Agent
  ↓
Database Tool
  ↓
PostgreSQL
```

The Agent does not directly manage SQL connections.

---

## Calculator Tool

The project also contains a simple Calculator tool.

Example:

```python id="v4p7cs"
@tool
def calculate(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

The Agent can route mathematical questions to this tool.

For example:

```text id="9q9l8r"
"What is 2 + 2?"
        ↓
Calculator
        ↓
4
```

---

## Agent Routing

The Agent uses LangGraph to route requests.

A simplified workflow is:

```text id="f6j4zq"
START
  │
  ▼
Analyze Question
  │
  ├── Mathematical question
  │        ↓
  │   Calculator
  │
  └── Other question
           ↓
      PostgreSQL
```

The Agent uses the appropriate tool depending on the type of request.

---

## Technologies

* Python
* PostgreSQL
* psycopg
* LangChain Tools
* LangGraph

---

## Key Concepts

This level introduces several important backend concepts:

### Relational Database

PostgreSQL stores structured data in tables.

### Database Connection

Python establishes a connection with PostgreSQL using `psycopg`.

### Database Tool

Database operations are encapsulated inside a dedicated tool.

### Agent Routing

The Agent determines which tool should handle a request.

### Separation of Responsibilities

The project separates:

```text id="m8b4i0"
Agent
  ↓
Tools
  ↓
Database
```

This makes the application easier to maintain and extend.

---

## Example

A mathematical request:

```text id="e9s7k2"
User: What is 2 + 2?
             ↓
          AI Agent
             ↓
       Calculator Tool
             ↓
             4
```

A database request:

```text id="b8z1hx"
User: Show me the stored documents.
             ↓
          AI Agent
             ↓
       Database Tool
             ↓
         PostgreSQL
             ↓
          Documents
```

---

## Next Level

**Level 07 — Testing**

The next level introduces automated testing with **pytest** to verify:

* Calculator functionality
* PostgreSQL database operations
* AI Agent routing
