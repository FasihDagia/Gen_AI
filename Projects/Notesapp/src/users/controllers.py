from src.users.dtos import userSchema
from src.users.models import userModel
from sqlalchemy.orm import Session

def register(body:userSchema, db:Session):
    print(body)
    return {"msg":"User Registered"}
