import logging

from src.app.http.routes import router
from src.http.server import Server

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)s [%(levelname)s] %(message)s"
)

server: Server = Server(router)


if __name__ == "__main__":
    try:
        server.run()
    finally:
        server.shutdown()
