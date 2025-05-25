from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

from step2.logging_config import logger
import step2.service as service

from dotenv import load_dotenv
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(service.router)

@app.get('/')
async def index():
    return 'Hello World!'

@app.on_event('startup')
def start_event():
    load_dotenv()

    logger.info(f'Service started')

@app.on_event('shutdown')
def shutdown_event():
    logger.info('Service stopped')

