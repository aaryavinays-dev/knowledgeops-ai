from fastapi import FastAPI
from app.schemas.query import TestQueryRequest, TestQueryResponse

app = FastAPI(
    title="KnowledgeOps AI Backend",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "KnowledgeOps AI Backend",
        "version": "0.1.0",
        "environment": "development"
    }

@app.post(
    "/test-query",
    response_model=TestQueryResponse,
    status_code=200,
)
def test_query(request: TestQueryRequest):
    return {
        "received_question": request.question,
        "document_id": request.document_id,
        "status": "accepted",
        "message": "Query received successfully",
    }