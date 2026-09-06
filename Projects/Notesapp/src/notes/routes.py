from fastapi import APIRouter,Depends
from src.notes import controllers
from src.notes.dtos import noteSchema, updateNoteSchema
from src.utils.db import get_session

notesRoutes = APIRouter(prefix="/notes")

@notesRoutes.post("/create")
def createNote(body:noteSchema,db = Depends(get_session)):
    return controllers.createNote(body, db)

@notesRoutes.get("/")
def getNotes(db = Depends(get_session)):
    return controllers.getNotes(db)

@notesRoutes.get("/onenote/{id}")
def getOnenote(id: int, db=Depends(get_session)):
    return controllers.getOnenote(id,db)

@notesRoutes.put("/updatenote/{id}")
def updateNote(body:updateNoteSchema, id:int, db = Depends(get_session)):
    return controllers.updateNote(body, id, db)