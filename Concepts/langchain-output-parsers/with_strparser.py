from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)