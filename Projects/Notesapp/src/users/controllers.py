from fastapi import HTTPException
from src.users.dtos import userSchema
from src.users.models import userModel
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def getPasswordhash(password):
    return password_hash.hash(password)

def register(body:userSchema, db:Session):

    is_username = db.query(userModel).filter(userModel.user_name == body.username).first()
    if is_username:
        raise HTTPException(400, detail="Username already exists!")

    is_email = db.query(userModel).filter(userModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail="User with this email already exists!")

    hashedPassword = getPasswordhash(body.password)

    newUser = userModel(
            name = body.name,
            user_name = body.username,
            hash_password = hashedPassword,
            email = body.email
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser