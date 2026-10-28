from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
str_parser = StrOutputParser()

template1 = PromptTemplate(
    template="Give a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Generate a 5 pointer summary of the given text \n {text}",
    input_variables=["text"]
)

chain = template1 | model | str_parser | template2 | model | str_parser
result = chain.invoke({"topic": "Cricket"})

print(result)

chain.get_graph().print_ascii()