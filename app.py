from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##setup steamlit
st.set_page_config(page_title="Lalith ChatGPT")
st.header("Geminu LLM app")
input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

#when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)