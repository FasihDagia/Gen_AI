from google.genai import Client, types
from dotenv import load_dotenv
from pathlib import Path
from asyncio import run
import requests
import os

BASE_DIR = Path(__file__).resolve().parents[3]
load_dotenv(BASE_DIR/".env")

WEATHER_API = os.getenv("WEATHER_API_KEY")

client = Client()

def get_weather(location:str):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q":location.lower(),
        "appid":WEATHER_API,
        "units":"metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error":"Couldnt fetch weather"}

    data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }


GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

async def chat_bot(question: str) -> str:
    default_instruction = "Respond to the users question in a short, concise manner (one short sentence)"
    config = types.GenerateContentConfig(
        tools=[get_weather],
        system_instruction= default_instruction,
        temperature=0
    )

    chat = client.aio.chats.create(
        model="gemini-3.5-flash-lite",
        config=config
    )

    response = await chat.send_message_stream(question)

    answer = []

    async for chunk in response:
        if chunk.text:
            answer.append(chunk.text)

    return "".join(answer)

    

