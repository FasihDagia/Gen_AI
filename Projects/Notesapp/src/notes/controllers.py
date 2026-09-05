from src.notes.dtos import noteSchema
from src.notes.models import NotesModel
from sqlalchemy.orm import Session

def createNote(body:noteSchema, db:Session):

    data = body.model_dump()
    newData = NotesModel(title=data["title"],
                          note=data["note"])

    db.add(newData)
    db.commit()
    db.refresh(newData)

    return {"status":"Note Created successfully!","data":newData}