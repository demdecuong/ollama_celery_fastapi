import time
import os
from celery.result import AsyncResult
from celery_worker import celery_app


def is_running_in_docker():
    # Check for the existence of .dockerenv
    if os.path.exists('/.dockerenv'):
        return True

        # Check for cgroup information
    with open('/proc/self/cgroup', 'r') as f:
        for line in f:
            if 'docker' in line:
                return True

    return False


def monitor_task(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    while not task_result.ready():
        time.sleep(1)
    print(f"Task {task_id} completed with result: {task_result.result}")
