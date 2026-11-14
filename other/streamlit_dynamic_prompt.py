import load_dotenv
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(repo_id="xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic", task="text-generation")
model=ChatHuggingFace(llm=llm)

st.header("RESEARCH ABOUT")

selected_paper = st.selectbox(
    "Select a research paper:",
     [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "Language Models are Few-Shot Learners"]
)

style_input = st.selectbox(
    "Select style:",
     ["begginer friendly", "techincal view", " heavy maths view"]
)

length_input = st.selectbox(
    "Select explaination length:",
     ["short(1-2 paragraphs)","medium(3-5 paragraphs)","long(8-9paragraphs)"]
)
template=PromptTemplate(template="""Please summarize the research paper titled \"{selected_paper}\" with the following specifications:Explanation Style: {style_input} Explanation Length: {length_input}  1. Mathematical Details:
- Include relevant mathematical equations if present in the paper. 
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies: 
- Use relatable analogies to simplify complex ideas. If certain information is not available in the paper, respond with:Insufficient information available instead of guessing. Ensure the summary is clear, accurate, and aligned with the provided style and length
    """)


user_input=st.text_input("enter your prompt")

if st.button("summarize"):
    result=model.invoke(user_input)
    st.write(result.content)





