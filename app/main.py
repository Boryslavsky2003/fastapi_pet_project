#  main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger

from app.routers.task import router as tasks_router
from app.database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    logger.info("БД очищенна")

    await create_tables()
    logger.info("БД готова")

    yield

    logger.info("Вимкнення")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
