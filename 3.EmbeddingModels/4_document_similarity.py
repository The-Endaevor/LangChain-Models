from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
    "Cricket is a popular team sport played with a bat and ball on a large field.",
    "The game involves two teams, with one batting and the other bowling and fielding.",
    "A typical cricket match can last from a few hours to several days depending on the format.",
    "Famous international tournaments include the ICC Cricket World Cup and the Ashes series.",
    "Cricket requires strategic thinking, physical skill, and teamwork to succeed."
]

query = 'tell me about the ashes'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is:",score)