from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google.genai import Client
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

app = FastAPI()
client = Client()

class chatRequest(BaseModel):
    prompt:str

def generateResponse(prompt: str):

    response = client.models.generate_content_stream(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    for chunk in response:
        if chunk.text:
            yield chunk.text

@app.post("/chat")
def generate(body:chatRequest):
    return StreamingResponse(
        generateResponse(body.prompt),
        media_type="text/plain"
    )