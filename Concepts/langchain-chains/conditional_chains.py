from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-20b")

class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description="Sentiment of the feedback")

pyd_parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()

template1 = PromptTemplate(
    template="Classify the sentiment of the given feedback into positive of negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":pyd_parser.get_format_instructions()}
)

classifier_chain = template1 | model | pyd_parser

template2 = PromptTemplate(
    template="Write an appropriate response for this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

template3 = PromptTemplate(
    template="Write an appropriate response for this negative feedback \n {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", template2 | model | str_parser ),
    (lambda x:x.sentiment == "negative", template3 | model | str_parser ),
    RunnableLambda(lambda x: "could not find sentiment")
)

feedback = "the food was good"
chain = classifier_chain | branch_chain 
result = chain.invoke({"feedback":feedback})
print(result)

chain.get_graph().print_ascii()

