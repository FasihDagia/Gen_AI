from sqlalchemy import Column, String, Integer
from src.utils.db import base

class userModel(base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_name = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)

    