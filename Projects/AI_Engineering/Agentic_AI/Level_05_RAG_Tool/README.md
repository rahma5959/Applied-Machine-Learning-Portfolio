# Level 05 — RAG Tool

## Overview

This level introduces **Retrieval-Augmented Generation (RAG)** as a tool for the AI Agent Platform.

The objective is to allow the Agent to retrieve relevant information from local documents before generating an answer.

The project uses:

* Document chunking
* Sentence embeddings
* Cosine similarity
* Semantic retrieval
* LangChain tools
* LangGraph Agent

---

## Learning Objectives

This level focuses on:

* Understanding the basic RAG architecture
* Splitting documents into smaller chunks
* Generating embeddings for text
* Comparing embeddings using cosine similarity
* Retrieving the most relevant document chunk
* Exposing RAG as an Agent tool
* Combining RAG with other Agent tools

---

## Project Structure

```text
Level_05_RAG_Tool/
│
├── README.md
├── requirements.txt
│
├── Data/
│   └── documents/
│       └── ai_basics.txt
│
└── src/
    ├── Agent.py
    ├── test_rag_agent.py
    │
    ├── services/
    │   ├── __init__.py
    │   └── llm_service.py
    │
    └── tools/
        ├── __init__.py
        ├── calculator.py
        ├── api_tool.py
        └── rag_tool.py
```

---

## RAG Architecture

The basic RAG workflow is:

```text
Document
   │
   ▼
Split into Chunks
   │
   ▼
Generate Embeddings
   │
   ▼
Compare with User Query
   │
   ▼
Retrieve Relevant Chunk
   │
   ▼
Context
   │
   ▼
LLM / Agent
   │
   ▼
Answer
```

---

## Knowledge Base

The project uses a simple text document:

```text
Data/documents/ai_basics.txt
```

The document contains basic information about:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Natural Language Processing
* Computer Vision

Example:

```text
Machine learning is a branch of artificial intelligence
that allows computers to learn patterns from data.
```

---

## Document Chunking

The document is divided into smaller pieces called **chunks**.

The current implementation uses line-based splitting:

```python
def split_document(content):
    chunks = content.split("\n")
    return [chunk.strip() for chunk in chunks if chunk.strip()]
```

This provides a simple introduction to document preprocessing before moving to more advanced chunking strategies.

---

## Embeddings

Each document chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

The same embedding model is used to encode the user's query.

Conceptually:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

For example:

```text
"Machine learning"
        ↓
[0.12, -0.34, 0.56, ...]
```

The vector represents the semantic information contained in the text.

---

## Similarity Search

The project uses **cosine similarity** to compare the query embedding with document embeddings.

The basic idea is:

```text
User Query
    │
    ▼
Query Embedding
    │
    ├──────────────┐
    ▼              ▼
Chunk 1          C
```
