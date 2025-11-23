from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions=32)

documents = [
    "There are 7 wonders in the world",
    "There are 7 continents in the world",
    "There is 7 after 6"
]

result = embedding.embed_documents(documents)

print(str(result))