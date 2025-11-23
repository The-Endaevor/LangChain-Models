from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-1b-it",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("who invented electricity")

print(result.content)