from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='model-name')

result=llm.invoke("prompt sent to model")

print(result)