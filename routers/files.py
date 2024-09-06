import asyncio
import time
from fastapi import APIRouter, status
from fastapi import APIRouter, File, UploadFile
from typing import List
from controller import FileUpload
from schemas import OkResponse, CreatedResponse, AcceptedResponse
import requests

router = APIRouter(
    prefix="/file",
    tags=["file"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/ping",
    status_code=status.HTTP_201_CREATED,  # default status code
    description="Description of the well documented endpoint",
    tags=["Endpoint Category"],
    summary="Summary of the Endpoint",
    responses={
        status.HTTP_200_OK: {
            "model": OkResponse,  # custom pydantic model for 200 response
            "description": "Ok Response",
        },
        status.HTTP_201_CREATED: {
            "model": CreatedResponse,  # custom pydantic model for 201 response
            "description": "Creates something from user request ",
        },
        status.HTTP_202_ACCEPTED: {
            "model": AcceptedResponse,  # custom pydantic model for 202 response
            "description": "Accepts request and handles it later",
        },
    },
)
async def ping():
    return {"status": True}


@router.post("/upload_files")
async def upload_file_queue(files_list: List[UploadFile] = File(...)):
    files_number = FileUpload.upload_files(files_list)
    return {"Number of files will be processed": files_number}
