import pytest
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from httpx import AsyncClient, Response

from src.app.containers import ServiceContainer
from src.app.http.dtos.sw import PersonResponse
from src.app.http.errors.handlers import validation_exception_handler
from src.app.http.routes import router, service_container

from src.test.mocks.clients import StarWarsClientMock
from src.test.mocks.repository import RepositoryMock
from src.test.mocks.server import test_app

base_url = "http://testserver"


@pytest.fixture
def tapp() -> FastAPI:
    fa_app = FastAPI()
    fa_app.include_router(router)
    fa_app.add_exception_handler(RequestValidationError, validation_exception_handler)
    test_container = ServiceContainer(
        sw_client=StarWarsClientMock(test_app), repository=RepositoryMock(),
    )
    fa_app.dependency_overrides.update({service_container: test_container})
    return fa_app


@pytest.mark.asyncio
async def test_get_person(tapp: FastAPI) -> None:
    async with AsyncClient(app=tapp, base_url=base_url) as client:
        name = "Leia"
        response: Response = await client.get(f"/character/{name}")
        person_response = PersonResponse.parse_obj(response.json())
        assert response.status_code == 200
        assert person_response.name == name
