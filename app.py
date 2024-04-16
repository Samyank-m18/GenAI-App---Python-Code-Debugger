from openai import OpenAI
import google.generativeai as genai

import streamlit as st

f = open("keys/.open-ai-key.txt")
key = f.read()
genai.configure(api_key=key)

model=genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="You are a helpful code assistant who helps to debug python code and give reviews on the code")

st.header("GenAI App : Python Code Debugger🤖")

st.text("")

st.subheader("Enter Your Python Code and Fix the Bugs🥳")



prompt = st.text_area("Enter your Python Code here :")


if st.button("DEBUG🐞") == True:
    

    response = model.generate_content(prompt)

    st.balloons();

    st.header("Review of Your Code🧐")

    st.write(response.text)