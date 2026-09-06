from src.notes.dtos import noteSchema
from src.notes.models import NotesModel
from sqlalchemy.orm import Session
from fastapi import HTTPException

def createNote(body:noteSchema, db:Session):

    data = body.model_dump()
    newData = NotesModel(title=data["title"],
                          note=data["note"])

    db.add(newData)
    db.commit()
    db.refresh(newData)

    return {"status":"Note Created successfully!","data":newData}

def getNotes(db:Session):
    notes = db.query(NotesModel).all()
    return {"Status":"All Notes","notes":notes}

def getOnenote(note_id:int,db:Session):
    oneNote = db.query(NotesModel).get(note_id)

    if not oneNote:
        raise HTTPException(404,detail="No Note with such ID")

    return {"Status":"Note Fetched","Data":oneNote}