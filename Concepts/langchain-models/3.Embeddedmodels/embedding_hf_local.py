from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Islamabad is the capital of pakistan",
    "Paris is the capital of France",
    "What are you doing i am fine"
]

result = embedding.embed_documents(documents)
print(str(result))