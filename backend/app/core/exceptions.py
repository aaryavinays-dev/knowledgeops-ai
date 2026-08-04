class AppException(Exception):
    def __init__(
        self,
        *,
        code: str,
        message: str,
        status_code: int,
    ) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class DocumentNotFoundException(AppException):
    def __init__(
        self,
        *,
        document_id: int,
    ) -> None:

        super().__init__(
            code="DOCUMENT_NOT_FOUND",
            message=f"Document '{document_id}' was not found.",
            status_code=404,
        )