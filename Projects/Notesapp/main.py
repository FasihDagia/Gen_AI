from fastapi import FastAPI,status
from src.utils.db import base,engine
from src.notes.routes import notesRoutes
from src.users.routes import userRoutes

base.metadata.create_all(engine)


app = FastAPI()
app.include_router(notesRoutes)
app.include_router(userRoutes)

@app.get("/", status_code=status.HTTP_200_OK)
def read_item():
    return {"newDoc": "hello"}
        