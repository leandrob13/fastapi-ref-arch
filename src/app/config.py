import os
import logging

logging.getLogger("tortoise").setLevel(logging.ERROR)

APP_PORT = os.getenv("APP_PORT", "8081")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://sw.db")
