# document(contains many query) ----> embeddings

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(
    model="embedding model name",
    dimensions=32 # size of generated embedding

)

document=[
    "query1",
    "query2",
    "query3"
]

result=model.embed_documents(document)

print(str(result))