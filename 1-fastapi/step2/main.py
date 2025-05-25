from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
import step2.service as service
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

app = FastAPI(
    title='AI-Innovator',
    description='AI-Innovator - AI Web AI / Cloud',
    version='0.0.1'
    )

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
    return 'AI-Innovator - AI Web AI / Cloud'

@app.on_event('startup')
def start_event():
    load_dotenv()

    logger.info(f'Service started')

@app.on_event('shutdown')
def shutdown_event():
    logger.info('Service stopped')

