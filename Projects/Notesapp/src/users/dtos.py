from pydantic import BaseModel

class userSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str

class userResponseschema(BaseModel):
    name: str
    user_name: str
    email: str
    id: int