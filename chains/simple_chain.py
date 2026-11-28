from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm=HuggingFaceEndpoint(repo_id='', task='' )

model=ChatHuggingFace(llm)

prompt= PromptTemplate(
    template='generate 5 interseting facts about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

chain= prompt | model | parser

result=chain.invoke({'topic':'cricket'})

print(result)