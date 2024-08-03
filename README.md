

---

# Faster Chatbot

Welcome to the Faster Chatbot project! This application provides a seamless and interactive chatbot experience, built with modern technologies to ensure efficiency and speed.

## Technologies Used

- **Streamlit**: For building an interactive web application.
- **Python**: The primary programming language used.
- **Groq API**: For natural language processing and generating chatbot responses.
- **JSON**: For configuration management.

## Features

- **User-friendly Interface**: Streamlit provides an intuitive and responsive interface for interacting with the chatbot.
- **Real-time Interaction**: The chatbot provides immediate responses, making the conversation feel natural.
- **Persistent Chat History**: The chat history is maintained throughout the session for continuity.

## Usage

To experience the Faster Chatbot, visit our live application:

[**Faster Chatbot**](https://llama-chatbot-6stp5hsnwxbwkipakfccnf.streamlit.app/)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/faster-chatbot.git
cd faster-chatbot
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Create a `config.json` file in the root directory with your Groq API key:

```json
{
    "GROQ_API_KEY": "your_groq_api_key_here"
}
```

## Running the Application

1. Start the Streamlit application:

```sh
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Contributing

We welcome contributions! Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.

---


