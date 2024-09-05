import os
import pandas as pd
from celery import Celery

celery_app = Celery('tasks', broker='redis://redis/0', backend='redis://redis/0')


@celery_app.task()
def add(a, b):
    for i in range(a, b):
        print(i)
    return {"number": a + b}


celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


# Celery periodic tasks
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs) -> None:
    # Example of periodic task (will be executed every 10 seconds)
    sender.add_periodic_task(10, periodic_task.s(), name='Periodic task example')


@celery_app.task(name="Periodic Task (every 10 seconds)")
def periodic_task() -> None:
    print("Example of periodic task executed!")


@celery_app.task(name="File Processing Task")
def file_handler_task(file: str):
    df = pd.read_excel(file)
    print(f"{df.head()}")
    print(f"file processed {file}")
    os.remove(file)
