from typing import Optional

from pydantic import BaseModel, Field

class TestQueryRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500)
    document_id: Optional[int] = None

class TestQueryResponse(BaseModel):
    received_question: str
    document_id: Optional[int] = None
    status: str
    message: str