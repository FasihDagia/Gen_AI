import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

url = "https://www.python.org/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

content = soup.get_text(separator=" ", strip=True)

document = Document(
    page_content=content,
    metadata = {"source":url}
)

print(document)