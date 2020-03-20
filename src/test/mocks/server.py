from typing import Text

from fastapi import FastAPI

from src.app.http.dtos.sw import PersonResponse

test_app = FastAPI()


@test_app.get("/person")
def persons(name: Text) -> PersonResponse:
    return PersonResponse(name=name)
