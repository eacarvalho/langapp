import streamlit as st
from langchain_openai import ChatOpenAI

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide Your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")
if not OPENAI_API_KEY:
    st.info("Enter your OpenAI API Key to Continue")
    st.stop()

llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14", api_key=OPENAI_API_KEY)

st.title("Ask Anything")

question = st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)