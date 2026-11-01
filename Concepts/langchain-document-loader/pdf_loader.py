from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()

def doc_load(data):
    loader = PyMuPDF4LLMLoader(data["path"])
    docs = loader.load()
    return docs[data["page"]-1].page_content

prompt = PromptTemplate.from_template(
    template="Explain in one line each topic mentioned: \n {page}"
)

path = "E:/GEN AI/Concepts/langchain-document-loader/dl-curriculum.pdf"

chain = RunnableSequence(RunnableLambda(doc_load), prompt, model, parser)
print(chain.invoke({"path":path,"page":2}))


