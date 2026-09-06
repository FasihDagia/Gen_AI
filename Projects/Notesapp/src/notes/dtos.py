from pydantic import BaseModel
from typing import Optional

class noteSchema(BaseModel):
    title: str 
    note: str 

class updateNoteSchema(BaseModel):
    title: Optional[str] = None
    note: Optional[str] = None
    