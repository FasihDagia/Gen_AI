print("kia haal hai")
from pathlib import Path
from langchain_core.documents import Document

directory = Path("E:/GEN AI/Concepts/langchain-document-loader/books")

documents = []
supported_extensions = [".pdf"]

print(directory)
for file_path in directory.rglob("*"):
    if file_path.is_file() and file_path.suffix in supported_extensions:
        content = file_path.read_text(encoding="utf-8")

        document = Document(
            page_content=content,
            metadata = {"source":str(file_path)}
        )
        documents.append(document)
print(len(documents))

for document in documents:
    print("content")
    print(document.page_content)