from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app: FastAPI = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'message': f'Hello {name}'}

@app.post('/hello')
async def say_hello_post(name: str):
    return {'message': f'Hello {name}'}