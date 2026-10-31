from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")

def wordcounter(text):
    return len(text.split())


prompt1 = PromptTemplate(
    template="write a joke on {topic}",
    input_variables=["topic"]
) 

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser,RunnableParallel({
    "joke":RunnablePassthrough(),
    "length": RunnableLambda(wordcounter)
}))

print(chain.invoke({"topic":"Cricket"}))
