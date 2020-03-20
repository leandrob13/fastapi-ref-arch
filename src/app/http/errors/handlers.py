import logging

from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError

from src.app.http.errors import DtoValidationErrors

_logger = logging.getLogger("Server")


def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    _logger.error(f"Bad Request for {request.url}: {exc}")
    return JSONResponse(
        status_code=400,
        content=DtoValidationErrors.from_request_validation_error(exc).dict(),
    )
