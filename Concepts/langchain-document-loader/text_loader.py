from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()

def doc_load(path):
    with open(path["path"], "r", encoding="utf-8") as file:
        text = file.read()

    docs = [Document(
        page_content=text
    )]
    
    return docs[0].page_content

prompt = PromptTemplate.from_template(
    template="Explain the following poem in 5 lines \n {poem}"
)

path = "E:/GEN AI/Concepts/langchain-document-loader/cricket.txt"

chain = RunnableSequence(RunnableLambda(doc_load), prompt, model, parser)
print(chain.invoke({"path":path}))


