from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm=HuggingFaceEndpoint(repo_id='', task='text gneration')

model=ChatHuggingFace(llm)


class person(BaseModel):
     name: str=Field(description='name of the person')
     age: int=Field(description='age of the person')
     city: str=Field(description='name of the city person belongs to')


parser=PydanticOutputParser(pydantic_object=person)

template=PromptTemplate(
     template='Genearte the name , age , and city of a fiction {place} person\n{format_instructions}',
     input_variables=['place'],
     partial_variables={'format_instruction':parser.get_format_instructions}

)

prompt=template.invoke({'place': 'indian'})
result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)


