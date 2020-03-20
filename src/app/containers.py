from __future__ import annotations

from src.app.db import BaseRepository
from src.app.http.clients import StarWarsClient


class ServiceContainer:
    sw_client: StarWarsClient
    repository: BaseRepository

    def __init__(
        self, repository: BaseRepository, sw_client: StarWarsClient = StarWarsClient(),
    ) -> None:
        self.sw_client = sw_client
        self.repository = repository

    def __call__(self) -> ServiceContainer:
        return self
