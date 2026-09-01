from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from pymongo import MongoClient
import os

env_path = "E:/GEN AI/.env"
load_dotenv(env_path)

app = FastAPI()
db_conn = MongoClient(os.getenv("MONGODB_URI"))

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )

@app.get("/dummy")
def dummy_data():
    db = db_conn["sample_mflix"]["users"]
    detail = db.find_one({"name": "Ned Stark"}, {"_id": 0})
    return detail