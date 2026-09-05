from pydantic import BaseModel

class noteSchema(BaseModel):

    title: str = "" 
    note: str = ""