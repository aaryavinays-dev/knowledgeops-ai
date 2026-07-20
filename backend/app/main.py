import logging
from time import perf_counter
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.schemas.query import TestQueryRequest, TestQueryResponse


configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

logger.info("KnowledgeOps AI backend initialized")
@app.middleware("http")
async def request_tracking_middleware(request: Request, call_next):
    request_id = str(uuid4())
    request.state.request_id = request_id

    start_time = perf_counter()

    logger.info(
        "Request started | request_id=%s | method=%s | path=%s",
        request_id,
        request.method,
        request.url.path,
    )

    try:
        response = await call_next(request)
    except Exception:
        logger.exception(
            "Request failed | request_id=%s | method=%s | path=%s",
            request_id,
            request.method,
            request.url.path,
        )
        raise

    duration_ms = (perf_counter() - start_time) * 1000

    response.headers["X-Request-ID"] = request_id

    logger.info(
        "Request completed | request_id=%s | status_code=%s | duration_ms=%.2f",
        request_id,
        response.status_code,
        duration_ms,
    )

    return response

@app.get("/health")
def health_check():
    logger.info("Health check requested")
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
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