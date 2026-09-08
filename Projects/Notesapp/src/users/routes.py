from fastapi import APIRouter, status, Depends
from src.users import controllers
from src.users.dtos import userSchema
from src.utils.db import get_session
from sqlalchemy.orm import Session

userRoutes = APIRouter(prefix="/user")

@userRoutes.post("/register", status_code=status.HTTP_201_CREATED)
def registerUser(body:userSchema, db:Session = Depends(get_session)):
    return controllers.register(body,db)
