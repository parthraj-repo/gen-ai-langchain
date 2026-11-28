## OVERVIEW OF THE CONTROL FLOW

#                                               (+ve)--> MODEL 1 ---->reply ----+
#                                               |                               |
# feedback ----> model(recognizes sentiment)----|                               |----------> reply
#                     (condition)               |                               |
#                                               (-ve)--> MODEL 2 ---->reply ----+  #                               


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal

load_dotenv()
llm=HuggingFaceEndpoint()

model=ChatHuggingFace(llm)
parser1=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=Review)


class Review(BaseModel):
    sentiment: Literal['postive','negative']=Field(description='Give the sentiment of the feedback')

prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback into positive or negative \n{feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions}
    
)

prompt2=PromptTemplate(
    template='write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment =='positive', prompt2 | model | parser1),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser1),
    lambda x: 'could not find the sentiment'
)

chain = classifier_chain | branch_chain

feedback=input('enter your feedabck')


chain.invoke({'feedback': feedback})