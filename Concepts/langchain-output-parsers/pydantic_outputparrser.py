from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

class Person(BaseModel):

    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    background: str = Field(description="Little background of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Give the name, age and a little background of a fictional character from {country} \n {format_instruction}',
    input_variables=['country'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'country':'Paksitan'})
print(result)