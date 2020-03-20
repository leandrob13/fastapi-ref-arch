import logging
from typing import Text

from fastapi import HTTPException
from httpx import AsyncClient

from src.app.http.dtos.sw import PersonResponse


class StarWarsClient:
    logger = logging.getLogger("StarWarsClient")

    host = "https://swapi.co/api"

    sw_client = AsyncClient(verify=False, base_url=host)

    async def close_client(self) -> None:
        await self.sw_client.aclose()

    async def get_person_by_id(self, name: Text) -> PersonResponse:
        params = {"name": name}
        response = await self.sw_client.get(f"/person", params=params)

        if response.status_code == 200:
            person_response = PersonResponse.parse_obj(response.json())
            return person_response
        else:
            self.logger.error(
                f"Error querying SW {response.status_code}, {response.text}"
            )
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Error querying SW {response.status_code}, {response.text}",
            )
