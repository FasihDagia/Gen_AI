from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Write a tweet on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a linkedin post on {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({"topic":"AI"})
print(result)