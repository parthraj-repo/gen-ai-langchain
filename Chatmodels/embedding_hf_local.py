from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="")

text="query"

vector=embedding.embed_query(text)

print(str(vector))