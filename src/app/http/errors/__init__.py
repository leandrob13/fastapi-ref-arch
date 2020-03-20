from __future__ import annotations

from typing import Text, Dict, Any, List
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError


class DtoValidationError(BaseModel):
    path: Text
    message: Text

    @staticmethod
    def from_request_validation_error_dict(
        error: Dict[Text, Any]
    ) -> DtoValidationError:
        return DtoValidationError(
            path=".".join(error.get("loc", [])),
            message=error.get("msg", "validation error"),
        )


class DtoValidationErrors(BaseModel):
    errors: List[DtoValidationError]

    @staticmethod
    def from_request_validation_error(
        exc: RequestValidationError,
    ) -> DtoValidationErrors:
        return DtoValidationErrors(
            errors=[
                DtoValidationError.from_request_validation_error_dict(error)
                for error in exc.errors()
            ]
        )
