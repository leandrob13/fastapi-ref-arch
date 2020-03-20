from typing import *

from src.app.http.dtos.sw import PersonResponse


class BaseRepository:
    async def insert_person(self, person_response: PersonResponse) -> Text:
        ...
