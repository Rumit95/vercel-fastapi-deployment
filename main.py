from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"yes":"its working"}

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}