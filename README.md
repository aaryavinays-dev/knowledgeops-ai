# KnowledgeOps AI

KnowledgeOps AI is an Enterprise Knowledge Intelligence Platform that enables employees to retrieve trusted information from organizational documents using Retrieval-Augmented Generation (RAG).

## Problem

Enterprise knowledge is scattered across multiple systems such as SharePoint, Confluence, PDFs, SOPs, emails, policies, contracts, and reports. Finding reliable information is often slow and inefficient.

## Solution

KnowledgeOps AI provides a single search interface where users can ask questions in natural language and receive:

- Grounded AI-generated answers
- Source citations
- Page references
- Related documents
- Confidence scores

## Tech Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

### AI
- OpenAI
- Embeddings
- Retrieval-Augmented Generation (RAG)

## Status

## Backend Progress

### Phase 1 — Backend Foundation

Completed:
- Created FastAPI application entry point
- Added `/health` endpoint
- Verified backend runs locally with Uvicorn
- Verified Swagger API docs at `/docs`

Run backend locally:

```bash
cd backend
uvicorn app.main:app --reload

Health check:

http://127.0.0.1:8000/health

Swagger docs:

http://127.0.0.1:8000/docs