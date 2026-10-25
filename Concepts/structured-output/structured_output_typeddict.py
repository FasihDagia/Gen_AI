from langchain_google_genai import ChatGoogleGenerativeAI
from google.genai.types import AutomaticFunctionCallingConfig
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite").bind(
    automatic_function_calling=AutomaticFunctionCallingConfig(
        disable=True
    )
)

class Review(TypedDict):

    summary: str
    sentiment: str


structured_output = model.with_structured_output(Review)

result = structured_output.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result["summary"])
print(result["sentiment"])