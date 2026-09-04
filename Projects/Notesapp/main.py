from fastapi import FastAPI,status
from src.utils.db import base,engine



base.metadata.create_all(engine)


app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def read_item():
    return {"newDoc": "hello"}
        