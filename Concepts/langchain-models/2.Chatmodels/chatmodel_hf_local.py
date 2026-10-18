from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "E:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task= "text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("who is the primeminister of pakistan")
print(result.content)