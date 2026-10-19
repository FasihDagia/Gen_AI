from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview", output_dimensionality=32)

result = embedding.embed_query("Islamabad is the Capital of Pakistan")

print(str(result))