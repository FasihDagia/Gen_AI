from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

chat_history = [SystemMessage(content = "You are a helpful ai asistant"),
                HumanMessage(content="What is the capital of pakistan.")]

result = model.invoke(chat_history)
chat_history.append(AIMessage(content=result.text))
print(result.text)

print(chat_history)