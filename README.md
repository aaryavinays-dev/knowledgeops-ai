
## Architecture

Frontend (React)
        │
        ▼
FastAPI Backend
        │
        ▼
PostgreSQL + pgvector
        │
        ▼
OpenAI Embeddings
        │
        ▼
Claude (Answer Generation)

# KnowledgeOps AI

KnowledgeOps AI is an Enterprise Knowledge Intelligence Platform that enables employees to retrieve trusted information from organizational documents using Retrieval-Augmented Generation (RAG).

---

# Problem

Enterprise knowledge is scattered across multiple systems such as:

- SharePoint
- Confluence
- PDFs
- SOPs
- Emails
- Policies
- Contracts
- Reports

Finding reliable information is often slow, inconsistent, and time-consuming.

---

# Solution

KnowledgeOps AI provides a single AI-powered search interface where employees can ask questions in natural language and receive:

- Grounded AI-generated answers
- Source citations
- Page references
- Related documents
- Confidence scores

---

# Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

## AI

- Anthropic Claude (Answer Generation)
- OpenAI Embeddings (Vector Embeddings)
- Retrieval-Augmented Generation (RAG)

---

# Backend Progress

## Phase 1 — Backend Foundation

### ✅ Completed

- Created FastAPI application
- Configured Uvicorn development server
- Implemented `GET /health`
- Verified backend runs locally
- Verified Swagger API documentation
- Added Pydantic request models
- Added Pydantic response models
- Implemented `POST /test-query`
- Added request validation using `Field`
- Added optional request fields
- Tested validation using Swagger
- Verified automatic `422 Unprocessable Entity` responses for invalid requests
- Learned HTTP methods and REST API fundamentals

---

# Run Backend

```bash
cd backend
uvicorn app.main:app --reload
```

---

# API Endpoints

## Health Check

```
GET /health
```

Returns the backend health status.

---

## Test Query

```
POST /test-query
```

Example Request

```json
{
  "question": "What is the leave policy?",
  "document_id": 1
}
```

Example Response

```json
{
  "received_question": "What is the leave policy?",
  "document_id": 1,
  "status": "accepted",
  "message": "Query received successfully"
}
```

---

# Local URLs

### Health Endpoint

```
http://127.0.0.1:8000/health
```

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Current Status

🚧 Phase 1 Backend Foundation is currently in progress.

Completed

- FastAPI Fundamentals
- Uvicorn
- Swagger
- Pydantic
- Request Validation
- Basic REST API Design
- Added centralized configuration using `pydantic-settings`
- Created reusable `Settings` configuration object
- Moved app name, version, and environment out of `main.py`
- Added safe configuration placeholders to `.env.example`

Upcoming

- Configuration Management
- Environment Variables
- Logging
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- Error Handling