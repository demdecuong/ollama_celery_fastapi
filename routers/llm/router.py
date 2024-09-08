import os
import requests
from fastapi import APIRouter, HTTPException, BackgroundTasks
from celery_worker import request_ollama_api, get_task_info
from routers.llm.utils import monitor_task, is_running_in_docker
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/llm",
    tags=["llm"],
    responses={404: {"description": "Not found"}},
)
if is_running_in_docker:
    OLLAMA_URL = "http://host.docker.internal:11434"
else:
    OLLAMA_URL = "http://localhost:11434"

OLLAMA_URL = OLLAMA_URL + "/api/generate"
OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL')


@router.post("/generate")
async def generate_text(prompt: str, background_tasks: BackgroundTasks):  # sourcery skip: raise-from-previous-error
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_keep": 5,
            "seed": 42,
            "num_predict": 100,
            "top_k": 20,
            "top_p": 0.9,
            "tfs_z": 0.5,
            "typical_p": 0.7,
            "repeat_last_n": 33,
            "temperature": 0.8,
            "repeat_penalty": 1.2,
            "presence_penalty": 1.5,
            "frequency_penalty": 1.0,
            "mirostat": 1,
            "mirostat_tau": 0.8,
            "mirostat_eta": 0.6,
            "penalize_newline": True,
            "numa": False,
            "num_ctx": 1024,
            "num_batch": 2,
            "num_gpu": 1,
            "main_gpu": 0,
            "low_vram": False,
            "f16_kv": True,
            "vocab_only": False,
            "use_mmap": True,
            "use_mlock": False,
            "num_thread": 8,
        },
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(OLLAMA_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

        # TODO: FIX HERE
        # task = request_ollama_api.delay(
        #     OLLAMA_URL=OLLAMA_URL,
        #     payload=payload,
        #     headers=headers
        # )
        #
        # background_tasks.add_task(monitor_task, task.id)
        # return JSONResponse({"task_id": task.id})
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Error communicating with Ollama: {str(e)}"
        )


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)
