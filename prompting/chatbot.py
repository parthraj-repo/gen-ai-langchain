from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm= HuggingFaceEndpoint(repo_id="",
                         temperature="")

model= ChatHuggingFace(llm)

chat_history=[]

while True:
    user_input=input("you: ")
    chat_history.append(user_input)
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)

    print("AI: ",result.content)

print(chat_history)