# Level 07 — Testing

## Overview

This level introduces automated testing for the AI Agent Platform using **pytest**.

The objective is to verify that the main components of the application work correctly and that future changes do not break existing functionality.

The tests cover:

* Calculator tool
* PostgreSQL database tool
* AI Agent routing

---

## Learning Objectives

This level focuses on:

* Understanding automated testing in Python
* Writing tests with `pytest`
* Testing individual tools
* Testing database interactions
* Testing AI Agent behavior
* Using assertions to verify expected results
* Organizing tests in a dedicated `tests/` directory
* Running the complete test suite with a single command

---

## Project Structure

```text
Level_07_Testing/
│
├── README.md
├── requirements.txt
├── pytest.ini
│
└── src/
    ├── Agent.py
    │
    ├── database/
    │   ├── __init__.py
    │   └── connection.py
    │
    ├── tools/
    │   ├── __init__.py
    │   ├── calculate_tool.py
    │   └── database_tool.py
    │
    └── tests/
        ├── test_calculator.py
        ├── test_database.py
        └── test_agent.py
```

---

## Testing Architecture

```text
                    ┌─────────────────┐
                    │   pytest suite  │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       Calculator Test   Database Test   Agent Test
              │              │              │
              ▼              ▼              ▼
         Calculator      PostgreSQL       AI Agent
                           Database        Routing
```

---

## Tests

### 1. Calculator Test

`test_calculator.py` verifies that the calculator tool returns the expected result.

Example:

```python
result = calculate.invoke({
    "a": 2,
    "b": 3
})

assert result == 5
```

This test checks the basic functionality of the calculator tool.

---

### 2. Database Test

`test_database.py` verifies that the database tool can retrieve documents stored in PostgreSQL.

Example:

```python
result = get_documents.invoke({})

assert len(result) > 0
```

This confirms that:

* The PostgreSQL connection works
* The database tool works
* Documents can be retrieved successfully

---

### 3. Agent Test

`test_agent.py` verifies that the Agent correctly routes a mathematical question to the calculator.

Example:

```python
result = graph.invoke({
    "message": "what is 2+2"
})

assert result["action"] == "calculator"
assert result["result"] == 4
```

This validates the Agent's routing behavior.

---

## Pytest Configuration

The project uses a `pytest.ini` file:

```ini
[pytest]
pythonpath = src
```

This tells pytest to include the `src` directory in the Python path.

It allows imports such as:

```python
from tools.calculate_tool import calculate
```

instead of requiring longer relative paths.

---

## Running the Tests

From the `Level_07_Testing` directory:

```bash
pytest
```

Expected result:

```text
3 passed
```

---

## Technologies

* Python
* pytest
* LangGraph
* LangChain Tools
* PostgreSQL

---

## Key Concepts

This level demonstrates the transition from manually testing code to using **automated tests**.

Instead of manually checking whether each component works, pytest automatically verifies expected behavior.

```text
Code
  ↓
Automated Tests
  ↓
Assertions
  ↓
Pass / Fail
```

Th
