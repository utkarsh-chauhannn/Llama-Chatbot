# Faster Chatbot

This project is a faster chatbot application built using Streamlit and Groq's API. It allows users to interact with a chatbot and displays the chat history.

## Features

- User-friendly interface with Streamlit
- Chatbot interaction with Groq API
- Persistent chat history within the session

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/faster-chatbot.git
cd faster-chatbot

## Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Create a config.json file in the root directory with your Groq API key:
{
    "GROQ_API_KEY": "your_groq_api_key_here"
}
