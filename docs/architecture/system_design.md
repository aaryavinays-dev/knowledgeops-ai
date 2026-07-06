# KnowledgeOps AI System Design

## Query Flow

User types question
→ React sends question to FastAPI endpoint
→ FastAPI creates embedding for the question
→ FastAPI searches pgvector for similar document chunks
→ pgvector returns relevant chunks + similarity scores
→ FastAPI builds context from those chunks
→ FastAPI sends question + context to Claude
→ Claude generates grounded answer
→ FastAPI returns JSON response with answer + citations to React
→ React displays the answer

## Initial Database Design
users - stores the people who use the platform.

documents - stores metadata about uploaded documents such as filename, file type, upload status, and uploaded user.

chunks - stores small text sections extracted from documents, along with their embeddings for retrieval.

queries - stores the user question, AI answer, model used, response time, tokens, and cost.

citations - stores which chunks/documents were used to support each AI answer.

feedback - stores user rating or comments on the AI response.

usage_logs - stores system-level usage data like API calls, latency, token usage, and errors.

### users
Stores the people who use the platform.

Columns:
- id
- name
- email
- password_hash
- role
- created_at
- updated_at

### documents
Stores metadata about uploaded documents.

Columns:
- id
- filename
- file_type
- file_size
- description
- storage_path
- status
- uploaded_by
- created_at
- updated_at

### chunks
Stores small text sections extracted from documents, along with embeddings for retrieval.

Columns:
- id
- document_id
- chunk_index
- content
- page_number
- embedding
- created_at

### queries
Stores user questions, AI answers, and response metadata.

Columns:
- id
- user_id
- question
- answer
- model_name
- latency_ms
- prompt_tokens
- completion_tokens
- total_tokens
- estimated_cost
- created_at

### citations
Stores which chunks/documents supported each AI answer.

Columns:
- id
- query_id
- document_id
- chunk_id
- page_number
- similarity_score
- created_at

### feedback
Stores user feedback on AI responses.

Columns:
- id
- query_id
- user_id
- rating
- comment
- created_at

### usage_logs = deferred to Phase 7 Observability
Stores system-level usage data, API activity, latency, token usage, cost, and errors.

Columns:
- id
- user_id
- event_type
- endpoint
- model_name
- latency_ms
- prompt_tokens
- completion_tokens
- total_tokens
- estimated_cost
- error_message
- created_at
```
### Authentication

#### POST /auth/register
React sends:
- name
- email
- password

FastAPI returns:
- user_id
- email
- role
- message

#### POST /auth/login
React sends:
- email
- password

FastAPI returns:
- access_token
- token_type
- user_id
- role

---

### Documents

#### POST /documents/upload
React sends:
- uploaded PDF/DOCX file
- optional description

FastAPI returns:
- document_id
- filename
- status
- message

#### GET /documents
React sends:
- auth token

FastAPI returns:
- list of uploaded document metadata

#### DELETE /documents/{document_id}
React sends:
- document_id in URL
- auth token

FastAPI returns:
- deleted document_id
- status
- message

Note:
- Only Admin users can delete documents.

---

### Query

#### POST /query
React sends:
- user question
- optional document filters

FastAPI returns:
- grounded answer
- citations
- confidence_score
- related documents/chunks

#### GET /query/history
React sends:
- auth token

FastAPI returns:
- previous questions
- answers
- timestamps
- model used
- citation summaries

---

### Feedback

#### POST /feedback
React sends:
- query_id
- rating
- optional comment

FastAPI returns:
- feedback_id
- status
- message