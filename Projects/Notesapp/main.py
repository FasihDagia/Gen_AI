from fastapi import FastAPI,status
from dotenv import load_dotenv
from pymongo import MongoClient
import os

env_path = "E:/GEN AI/.env"
load_dotenv(env_path)

app = FastAPI()
db_conn = MongoClient(os.getenv("MONGODB_URI"))

@app.get("/notes", status_code=status.HTTP_200_OK)
def read_item():
    docs = db_conn.notes.notes.find({})
    new_doc = []
    for doc in docs:
        new_doc.append(
            {
                "_id":str(doc["_id"]),
                "note":doc["note"]
            }
        )
    return {"newDoc": new_doc}
        

@app.get("/dummy")
def dummy_data():
    db = db_conn.sample_mflix.users
    detail = db.find_one({"name": "Ned Stark"}, {"_id": 0})
    return detail