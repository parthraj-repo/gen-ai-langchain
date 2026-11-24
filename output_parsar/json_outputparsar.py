from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="",
    task="text-generation")

model=ChatHuggingFace(llm)

parser=JsonOutputParser()



template = PromptTemplate(
    template="Give me the name, age and city of a fictional person.\n{format_instruction}",
    input_variables=[],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

prompt=template.format()

result=model.invoke(prompt)

final_result= parser.parse(result.content)

print(type(final_result))   ## python class obj