# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# not using huggingFace open source LLMs due to issues
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.2-1B-Instruct",
#     task="text-generation"
# ) 

# model = ChatHuggingFace(llm=llm)

model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke(result1)

result2 = model.invoke(prompt2)

print(result2.content)