#             +-----> MODEL 1 ----> NOTES -------+
# DOCUMENT----|                                  |----> MODEL 3(MERGER)---> FINAL OUTPUT(NOTES + QUIZ)
#             +-----> MODEL 2 ----> QUIZ --------+
# -----------------------------------------------------------------------------------------------------
                     
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
llm1=HuggingFaceEndpoint(repo_id="",task="text generation")

llm2=HuggingFaceEndpoint(repo_id='',task="text generation")

model1=ChatHuggingFace(llm1)
                       
model2=ChatHuggingFace(llm2)

prompt1= PromptTemplate(
    template='Genearte short and simple notes from the given text \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Genearte 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='merge the provided notes and the quiz into a single document \n {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel()


