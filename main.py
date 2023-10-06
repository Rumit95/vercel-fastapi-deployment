from time import time
from fastapi import FastAPI, __version__

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"yes":"its working"}

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}