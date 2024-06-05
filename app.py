import uvicorn

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# from app import app
if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=1919, reload=True, workers=10, reload_delay=10)
    # uvicorn.run("app:app", host="0.0.0.0", port=1919, reload=True)