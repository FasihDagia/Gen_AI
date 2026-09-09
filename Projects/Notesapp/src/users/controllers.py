from fastapi import HTTPException, status, Request
from src.users.dtos import userSchema, userLoginschema
from src.users.models import userModel
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError

password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def getPasswordhash(password):
    return password_hash.hash(password)

def register(body:userSchema, db:Session):

    is_username = db.query(userModel).filter(userModel.user_name == body.username).first()
    if is_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists!")

    is_email = db.query(userModel).filter(userModel.email == body.email).first()
    if is_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists!")

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

def login(body:userLoginschema,db:Session):

    user = db.query(userModel).filter(userModel.user_name == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No User with such username exists!")

    if not verify_password(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")

    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode({"_id":user.id,"exp":exp_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)

    return token

def is_auth(body:Request,db:Session):
    try:
        token = body.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")

        user = db.query(userModel).filter(userModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorize")

        return user

    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorize")
