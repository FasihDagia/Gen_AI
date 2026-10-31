from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke: {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, RunnableParallel({
    "joke": RunnablePassthrough(),
    "explain": RunnableSequence(prompt2, model, parser) 
    }))

print(chain.invoke({"topic":"cricket"}))