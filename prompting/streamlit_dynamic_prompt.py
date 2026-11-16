from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate, load_prompt

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
template=load_prompt('template.json')


prompt=template.invoke(
    {
     'selected_paper':selected_paper,
     'style_input':style_input,
     'length_input':length_input

    }
)






if st.button("summarize"):
    result=model.invoke(prompt)
    st.write(result.content)





