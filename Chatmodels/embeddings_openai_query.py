
# query ---> embeddings    [ using openai model]

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(
    model="embedding model name",
    dimensions=32 # size of gnerated embedding

)

result=model.embed_query("query")

print(str(result))