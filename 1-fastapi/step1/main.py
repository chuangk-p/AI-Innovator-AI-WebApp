from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def index():

    return 'Hello World!'

@app.get('/get/{item_id}')
async def get_api(item_id):

    return {'items' : item_id}

@app.get('/get-query/')
async def get_api(item_id):

    return {'items' : item_id}

@app.post('/post')
async def post_api(data: Request):
    request_info = await data.json()
    
    return request_info

