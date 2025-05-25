from fastapi import APIRouter, Request
from step2.logging_config import logger
import os
from aift import setting
from aift.multimodal import textqa
from dotenv import load_dotenv

load_dotenv()

setting.set_api_key(os.getenv('API_KEY'))
router = APIRouter(
            tags=['service']
         )

@router.get('/get/{item_id}')
async def get_api(item_id):
    logger.info(f"/get : '{item_id}'")
    return {'items' : item_id}

@router.get('/get-query/')
async def get_api(item_id):

    return {'items' : item_id}

@router.post('/post')
async def post_api(data: Request):
    request_info = await data.json()
    
    return request_info


