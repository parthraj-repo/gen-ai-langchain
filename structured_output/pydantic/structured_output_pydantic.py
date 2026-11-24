from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field 

load_dotenv()

user_review=input('write a review')

class review(BaseModel):
    key_themes: list[str]=Field(description="write all the keys ")
    summary: str=Field(description="write the breif summary of the review")
    sentiment: Literal['pos','neg']=Field(default=None,description="give a positive sen or neg sent")
    pros: Optional[list[str]]=Field(default=None,description="give all the pros of the review")
    cons: Optional[list[str]]=Field(default=None,description="give all the cons of the review")
    


model=ChatOpenAI()
structured_model=model.with_structured_output(review)

result=structured_model.invoke(user_review)

print(result) #it will be a pydantic obj, so to fetch something particular use print(result.feature)

