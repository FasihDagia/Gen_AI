from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='write a 5 line summary on given text: \n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.text})

result1 = model.invoke(prompt2)

print(result1.text)