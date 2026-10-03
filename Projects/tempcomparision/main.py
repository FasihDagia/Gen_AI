import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")
app = FastAPI(title="AI Temp API")
client = genai.Client()

class aiRequest(BaseModel):
    prompt:str = Field(...,min_length=1, max_length=8000)
    temperature:float = Field(default=0.7,ge=0.0,le=2.0)

class aiResponse(BaseModel):
    responseText:str
    temperature: float

@app.post("/generate", response_model=aiResponse)
async def generateText(request:aiRequest):
    try:
        config = types.GenerateContentConfig(
            temperature=request.temperature,
        )

        chat = client.aio.chats.create(
            model='gemini-3.5-flash-lite',
            config=config
        )
        
        response = await chat.send_message(request.prompt)
        
        if not response.text:
            raise HTTPException(status_code=500, detail="Gemini returned an empty response.")
            
        return aiResponse(
            responseText=response.text, 
            temperature=request.temperature
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))