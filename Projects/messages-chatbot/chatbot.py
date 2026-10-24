from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from google.genai.types import AutomaticFunctionCallingConfig
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite").bind(
    automatic_function_calling=AutomaticFunctionCallingConfig(
        disable=True
    )
)

chat_history = [
    SystemMessage(content="You are a smart ai asistant")

]

while True:
    user_input = input("Human:")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print("Ai:",result.text)

print(chat_history)
