from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.schemas.error import ErrorDetails, ErrorResponse


async def app_exception_handler(
    request: Request,
    exc: AppException,
) -> JSONResponse:
    request_id = request.state.request_id

    error_details = ErrorDetails(
        code=exc.code,
        message=exc.message,
        request_id=request_id,
    )

    error_response = ErrorResponse(
        error=error_details,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump(),
    )