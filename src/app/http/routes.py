import logging
from typing import Text

from src.app.containers import ServiceContainer
from fastapi import APIRouter, Depends

from src.app.db.repository import TortoiseRepository
from src.app.http.dtos.sw import PersonResponse

router = APIRouter()

service_container: ServiceContainer = ServiceContainer(repository=TortoiseRepository())

logger = logging.getLogger("Router")


@router.on_event("shutdown")
async def shutdown() -> None:
    logger.info("Closing services client sessions.")
    await service_container.sw_client.close_client()


@router.get("/character/{name}", response_model=PersonResponse)
async def images(
    name: Text, container: ServiceContainer = Depends(service_container),
) -> PersonResponse:
    return await container.sw_client.get_person_by_id(name)
