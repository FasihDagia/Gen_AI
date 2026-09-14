from src.notes.dtos import noteSchema, updateNoteSchema
from src.notes.models import NotesModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.users.models import userModel

def createNote(body:noteSchema, db:Session, user:userModel):

    data = body.model_dump()
    newData = NotesModel(user_id = user.id,
                        title=data["title"],
                        note=data["note"])

    db.add(newData)
    db.commit()
    db.refresh(newData)

    return newData

def getNotes(db:Session, user:userModel):

    notes = db.query(NotesModel).filter(NotesModel.user_id == user.id).all()
    if not notes:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No notes for particular user")
    return notes

def getOnenote(noteId:int, db:Session, user:userModel):

    oneNote = (
        db.query(NotesModel)
        .filter(
            NotesModel.id == noteId,
            NotesModel.user_id == user.id
        ).first())

    if not oneNote:
        raise HTTPException(404,detail="No Note with such ID")

    return oneNote

def updateNote(body:updateNoteSchema, noteId:int, db:Session, user:userModel):

    oneNote = db.query(NotesModel).get(noteId)
    if not oneNote:
        raise HTTPException(404,detail="No Note with such ID")

    if oneNote.user_id != user.id:
        raise HTTPException(401,detail="you are not authorized to update")

    bodyd = body.model_dump(exclude_unset=True)
    for field, value in bodyd.items():
        setattr(oneNote, field, value)

    db.add(oneNote)
    db.commit()
    db.refresh(oneNote)

    return oneNote

def deleteNote(noteId:int, db:Session, user:userModel):

    oneNote = db.query(NotesModel).get(noteId)
    if not oneNote:
        raise HTTPException(404,detail="No Note with such ID")

    if oneNote.user_id != user.id:
        raise HTTPException(401,detail="you are not authorized to delete")

    db.delete(oneNote)
    db.commit()

    return None

