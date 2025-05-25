from fastapi import APIRouter, Request
import json
import ollama
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OLLAMA_HOST'] = os.getenv('HOST_NAME')
router = APIRouter(
            tags=['Ollama-service']
         )

@router.post("/service/chat/")
async def chat(data : Request):
    request_info = await data.json()
    # Assignment
    ...
    return request_info

@router.post("/service/chat-image/")
async def chat_image_mock(data : Request):
    request_info = await data.json()
    # Assignment
    ...

    return request_info
