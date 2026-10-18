from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = GoogleGenerativeAI(model="gemini-3.5-flash-lite")
result = llm.invoke("what is the capital of pakistan")
print(result)