from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text="what is the capital of earth?" #Can do documents aswell

vector = embedding.embed_query(text) 

print(str(vector))