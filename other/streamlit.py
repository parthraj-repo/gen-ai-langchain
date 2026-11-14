from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm=HuggingFaceEndpoint(repo_id="xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic", task="text-generation")
model=ChatHuggingFace(llm=llm)

st.header("RESEARCH ABOUT")

user_input=st.text_input("enter your prompt")

if st.button("summarize"):
    result=model.invoke(user_input)
    st.write(result.content)





