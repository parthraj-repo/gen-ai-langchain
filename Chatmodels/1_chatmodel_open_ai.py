from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='model-name')

result=model.invoke("prompt sent to model")
print(result.content) # the result contains content(actual answer) and many kwargs 