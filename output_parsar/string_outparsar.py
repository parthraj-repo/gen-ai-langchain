from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    task="text-generation",
    max_new_tokens=150,
    temperature=0.7)

model=ChatHuggingFace(llm)

# 1st temlate ----> detailed report

template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']

)

# 2nd template -----> summary

template2=PromptTemplate(
    template='give me 5 line summary on following text. /n {text}'
)

parsar=StrOutputParser()

chain = template1 | model | parsar | template2 | model | parsar

result=chain.invoke({'topic': 'black hole'})
print(result)