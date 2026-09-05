from fastapi import APIRouter,Depends
from src.notes import controllers
from src.notes.dtos import noteSchema
from src.utils.db import get_session

notesRoutes = APIRouter(prefix="/notes")

@notesRoutes.post("/create")
def createNote(body:noteSchema,db = Depends(get_session)):
    return controllers.createNote(body, db)