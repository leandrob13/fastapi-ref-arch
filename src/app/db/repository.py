from typing import Text
from src.app.db import BaseRepository, mappers
from src.app.http.dtos.sw import PersonResponse


class TortoiseRepository(BaseRepository):
    async def insert_person(self, person_response: PersonResponse) -> Text:
        record = mappers.response_to_person(person_response)
        await record.save()
        return str(record.id)
