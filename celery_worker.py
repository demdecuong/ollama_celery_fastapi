import os
import time
import random
import requests

import pandas as pd
from celery import Celery
from celery.utils.log import get_task_logger
from celery.result import AsyncResult

celery_app = Celery('tasks',
                    broker=os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//"),
                    backend=os.environ.get("CELERY_RESULT_BACKEND")
                    )
celery_log = get_task_logger(__name__)


# celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
# celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery_app.task(name="Request Ollama API")
def request_ollama_api(payload, headers, OLLAMA_URL):
    response = requests.post(OLLAMA_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def get_task_info(task_id):
    """
    return task info for the given task_id
    """
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
