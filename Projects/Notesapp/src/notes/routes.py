from fastapi import APIRouter, Depends, status
from src.notes import controllers
from src.notes.dtos import noteSchema, updateNoteSchema, noteResposeschema
from src.utils.db import get_session
from typing import List
from src.utils.helpers import is_auth
from src.users.models import userModel

notesRoutes = APIRouter(prefix="/notes")

@notesRoutes.post("/create", response_model=noteResposeschema, status_code=status.HTTP_201_CREATED)
def createNote(body:noteSchema, db = Depends(get_session), user:userModel = Depends(is_auth)):
    return controllers.createNote(body, db, user)

@notesRoutes.get("/", response_model=List[noteResposeschema], status_code=status.HTTP_200_OK)
def getNotes(db = Depends(get_session), user:userModel = Depends(is_auth)):
    return controllers.getNotes(db, user)

@notesRoutes.get("/onenote/{id}", response_model=noteResposeschema, status_code=status.HTTP_200_OK)
def getOnenote(id:int, db=Depends(get_session), user:userModel = Depends(is_auth)):
    return controllers.getOnenote(id, db, user)

@notesRoutes.put("/update/{id}", response_model=noteResposeschema, status_code=status.HTTP_201_CREATED)
def updateNote(body:updateNoteSchema, id:int, db = Depends(get_session), user:userModel = Depends(is_auth)):
    return controllers.updateNote(body, id, db, user)

@notesRoutes.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteNote(id:int, db = Depends(get_session), user:userModel = Depends(is_auth)):
    return controllers.deleteNote(id, db, user)