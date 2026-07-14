from fastapi import FastAPI
from app.core.config import settings
from app.schemas.query import TestQueryRequest, TestQueryResponse

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
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