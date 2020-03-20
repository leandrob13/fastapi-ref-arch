from fastapi import FastAPI
from httpx import AsyncClient

from src.app.http.clients import StarWarsClient


class StarWarsClientMock(StarWarsClient):
    def __init__(self, test_app: FastAPI):
        self.sw_client = AsyncClient(
            app=test_app, verify=False, base_url="http://testserver"
        )
