import os
import streamlit as st
from langchain_openai import OpenAI

# Input for API key
apikey = st.text_input("Enter your OpenAI API key:", type="password", key="api_key_input")

# Set the API key environment variable
if apikey:
    os.environ['OPENAI_API_KEY'] = apikey

# Display media files
st.audio("Lofi hiphop.mp3")
st.image("girl.gif")

st.title(" 🦜️🔗Ask your Homework problem 🧟‍♂️")
prompt = st.text_input("Type your homework question below", key="homework_prompt_input")

# LLMs
if apikey and prompt:
    llm = OpenAI(temperature=0.9)
    response = llm(prompt)
    st.write(response)
elif not apikey:
    st.warning("Please enter your OpenAI API key to proceed.")

with st.sidebar:
    st.write("About me")
    st.image("cutie-cat.gif")
