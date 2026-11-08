from dotenv import load_dotenv
import os

load_dotenv("E:/Gen_AI/.env")

print("API Key:", bool(os.getenv("GROQ_API_KEY")))