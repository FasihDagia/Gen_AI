from fastapi import APIRouter, status, Depends
from src.users import controllers
from src.users.dtos import userSchema, userResponseschema, userLoginschema
from src.utils.db import get_session
from sqlalchemy.orm import Session

userRoutes = APIRouter(prefix="/user")

@userRoutes.post("/register", response_model=userResponseschema, status_code=status.HTTP_201_CREATED)
def registerUser(body:userSchema, db:Session = Depends(get_session)):
    return controllers.register(body,db)

@userRoutes.post("/login",status_code=status.HTTP_200_OK)
def loginUser(body:userLoginschema, db:Session = Depends(get_session)):
    return controllers.login(body,db)