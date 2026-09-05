from sqlalchemy import Column, Integer, String
from src.utils.db import base

class NotesModel(base):
    __tablename__ = "user_notes"

    id = Column(Integer, primary_key=True)
    title = Column(String, default=None)
    note = Column(String, default=None)