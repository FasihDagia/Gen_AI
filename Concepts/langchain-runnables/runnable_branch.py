from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel,RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")

def wordcount(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = "write a report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="summerize the given report to make it under 500 words \n {report}",
    input_variables=["report"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, RunnableParallel({
    "report": RunnablePassthrough(),
    "length": RunnableLambda(wordcount)
}),RunnableBranch(
    (lambda x:x["length"]>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
))

print(chain.invoke({"topic":"Ukrain vs Russia"}))