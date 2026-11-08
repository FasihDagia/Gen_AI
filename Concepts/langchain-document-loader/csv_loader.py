import csv
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
str_parser = StrOutputParser()
csv_path = "E:/Gen_AI/Concepts/langchain-document-loader/Social_Network_Ads.csv"

prompt = PromptTemplate.from_template(
    template="This the data of some users give the whole information of user with heighest estimated salary and also give the averagee of the estimated salary \n {data} "
)

documents = []

with open(csv_path, "r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        documents.append(
            Document(
                page_content= str(row),
                metadata = {"source":csv_path}
            )
        )

chain = RunnableSequence(prompt, model, str_parser)
result = chain.invoke({"data":documents})
print(result)

