from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview", output_dimensionality=32)

documents = [
    "Islamabad is the capital of pakistan",
    "Paris is the capital of France",
    "What are you doing i am fine"
]

result = embedding.embed_documents(documents)

print(str(result))