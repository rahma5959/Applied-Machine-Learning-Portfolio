# Level 03 — LangGraph Agent

## Overview

This level introduces **LangGraph** and the fundamental concepts required to build an AI Agent workflow.

The objective is to move from a simple LLM service to a structured Agent that can process information through a graph of connected nodes.

The project introduces:

* State
* Nodes
* Edges
* Conditional routing
* Graph compilation
* Graph execution
* LLM integration

---

## Learning Objectives

This level focuses on:

* Understanding the architecture of an AI Agent
* Understanding LangGraph fundamentals
* Creating a `StateGraph`
* Defining and updating Agent state
* Creating processing nodes
* Connecting nodes with edges
* Using conditional edges
* Compiling and executing a graph
* Integrating an LLM into a graph workflow

---

## Project Structure

```text id="x6s1w4"
Level_03_LangGraph_Agent/
│
├── README.md
├── requirements.txt
│
└── src/
    └── Agent.py
```

---

## What is LangGraph?

**LangGraph** is a framework for building stateful workflows and AI Agents.

Instead of executing a simple sequence of functions, LangGraph represents the application as a graph.

The graph contains:

* **State** — information carried through the workflow
* **Nodes** — functions that perform operations
* **Edges** — connections between nodes
* **Conditional edges** — connections selected according to the current state

A simplified representation is:

```text id="q5j4aa"
        START
          │
          ▼
       Node 1
          │
          ▼
       Node 2
          │
          ▼
        END
```

---

## Agent State

The state contains the information that the Agent needs during execution.

For example:

```python id="v8h2k1"
state = {
    "message": "Hello"
}
```

A node can read the state and return an updated state.

```text id="m9x3qf"
Initial State
     │
     ▼
   Node
     │
     ▼
Updated State
```

The state allows information to be passed between different parts of the Agent workflow.

---

## Nodes

A node is a Python function that performs an operation.

Example:

```python id="2y8h1k"
def process_message(state):
    message = state["message"]

    return {
        "message": message
    }
```

The node receives the current state and returns an updated state.

---

## Edges

Edges define the execution flow between nodes.

For example:

```python id="5r4d2a"
builder.add_edge("node_1", "node_2")
```

This means:

```text id="8h2m3v"
Node 1
  ↓
Node 2
```

The Agent therefore follows a defined workflow.

---

## Conditional Edges

LangGraph can also choose the next node depending on the current state.

For example:

```text id="2z7p8k"
                Analyze
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
      Calculator          LLM
```

The Agent can therefore follow different paths depending on the request.

This concept becomes particularly important in later levels when tools are introduced.

---

## Building the Graph

The project uses `StateGraph` to construct the Agent workflow.

Basic example:

```python id="c4m7w9"
from langgraph.graph import StateGraph, START, END

builder = StateGraph(dict)

builder.add_node("process", process_message)

builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()
```

The graph is compiled before execution.

---

## Executing the Agent

Once compiled, the graph can be executed with:

```python id="q8v5z2"
result = graph.invoke({
    "message": "Hello"
})
```

The input state is passed into the graph and processed by the defined nodes.

---

## Multiple Nodes

The project also demonstrates a workflow with multiple nodes.

Conceptually:

```text id="g5k3n1"
START
  │
  ▼
Node 1
  │
  ▼
Node 2
  │
  ▼
END
```

Each node performs a specific operation and can update the state.

This introduces the idea of decomposing an Agent into several specialized steps.

---

## LLM Integration

The Level 03 Agent is also connected to the LLM service created in Level 02.

The architecture becomes:

```text id="p3w9v6"
User Message
     │
     ▼
LangGraph Agent
     │
     ▼
Processing Node
     │
     ▼
LLM Service
```
