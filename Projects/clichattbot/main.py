from google.genai import Client, types
from dotenv import load_dotenv
from pathlib import Path
from asyncio import run

BASE_DIR = Path(__file__).resolve().parents[3]
load_dotenv(BASE_DIR/".env")

client = Client()

def getWeather():
    pass

config = types.GenerateContentConfig(
    tools= [getWeather]
)

chat = client.aio.chats.create(
    model="gemini-3.5-flash-lite",
    config=config
)

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

async def main():

    prompt = " "
    while prompt:
        if prompt:
            prompt = input(f"{GREEN}Human:")
            print(RESET)

            response = await chat.send_message_stream(prompt)
            print(f"{BLUE}AI:")
            async for chunk in response:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print(RESET)
        
        print()
run(main())