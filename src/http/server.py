import asyncio
import logging
import signal
from asyncio import AbstractEventLoop, Event
from typing import Any, Optional
from fastapi import FastAPI, APIRouter
from fastapi.exceptions import RequestValidationError
from hypercorn.asyncio import serve
from hypercorn.config import Config
from tortoise.contrib.starlette import register_tortoise
import uvloop
from src.app.config import DATABASE_URL, APP_PORT
from src.app.http.errors.handlers import validation_exception_handler


class Server:
    app: FastAPI = FastAPI()

    shutdown_event: Event = Event()

    logger = logging.getLogger("Server")

    loop: AbstractEventLoop

    def __init__(self, r: APIRouter, loop: Optional[AbstractEventLoop] = None) -> None:
        self.loop = loop if loop is not None else Server.create_loop()
        self.loop.add_signal_handler(signal.SIGTERM, self.signal_handler)
        self.loop.add_signal_handler(signal.SIGINT, self.signal_handler)
        self.app.include_router(r)
        self.app.add_exception_handler(
            RequestValidationError, validation_exception_handler
        )
        register_tortoise(
            self.app,
            db_url=DATABASE_URL,
            modules={"models": ["src.app.db.models"]},
            generate_schemas=True,
        )

    @staticmethod
    def create_loop() -> AbstractEventLoop:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

    def signal_handler(self, *_: Any) -> None:
        self.logger.info("Handling termination signal, terminating loop.")
        self.shutdown_event.set()

    async def shut_down_awaitable(self) -> None:
        await self.shutdown_event.wait()

    def run(self) -> None:
        config = Config()
        config.bind = [f"0.0.0.0:{APP_PORT}"]
        self.logger.info("Starting server.")
        self.loop.run_until_complete(
            serve(self.app, config, shutdown_trigger=self.shut_down_awaitable)
        )

    def shutdown(self) -> None:
        self.loop.stop()
        self.loop.run_until_complete(self.loop.shutdown_asyncgens())
        self.loop.close()
