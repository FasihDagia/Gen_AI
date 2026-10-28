from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

template = PromptTemplate(
    template="List 5 intresting facts about {topic}",
    input_variables=['topic']
)

str_parser = StrOutputParser()

chain = template | model | str_parser
result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()
