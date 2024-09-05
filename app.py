from fastapi import FastAPI, WebSocket
from celery_worker import add, celery_app
from celery.result import AsyncResult
import asyncio
import time
import uvicorn

from pydantic import BaseModel
from router import file_router

app = FastAPI()
app.include_router(file_router)

# class TaskOut(BaseModel):
#     id: str
#     status: str


# @app.get("/process")
# async def process_endpoint(a: int, b: int) -> TaskOut:
#     result = add.delay(a, b)
#     return _to_task_out(result)
#
#
# def _to_task_out(r: AsyncResult) -> TaskOut:
#     return TaskOut(id=r.task_id, status=r.status)


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8888)
