#  router.py

from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from app.repository.task import TaskRepository
from app.schemas.task import STask, STaskId, STaskAdd


router = APIRouter(prefix="/tasks", tags=["Таски"])


@router.post("")
async def add_tasks(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> STask:
    tasks = await TaskRepository.find_all()
    return tasks
