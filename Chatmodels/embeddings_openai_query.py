from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(
    model="embedding model name",
    dimensions=32

)

result=model.embed_query("query")

print(str(result))