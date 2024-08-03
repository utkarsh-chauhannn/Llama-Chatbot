import os
import json
import streamlit as st
from groq import Groq

# Streamlit page configuration
st.set_page_config(
    page_title="Faster Chatbot",
    page_icon="🦙",
    layout="centered"
)

# Load configuration
working_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{working_dir}/config.json") as config_file:
    config_data = json.load(config_file)

GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Faster Chatbot")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Prompt
user_prompt = st.chat_input("Ask Chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})  # Corrected the variable name

    messages = [
        {"role": "system", "content": "Helpful Chatbot"},
        *st.session_state.chat_history
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    assistant_response = response.choices[0].message.content  # Corrected access to the response content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
