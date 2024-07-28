# Simple Chatbot Project

## Overview
This project involves the development of a simple conversational chatbot using Python and Natural Language Processing (NLP) libraries such as NLTK and spaCy. The chatbot can engage in basic conversations with users, providing predefined responses to various queries. This project serves as an introduction to natural language processing and chatbot development.

## Features
- Greets users
- Responds to simple questions about time, date, preferences, knowledge, and trivia
- Provides motivational quotes and fun facts
- Performs basic math operations
- Easy to extend with additional responses

## Technologies Used
- **Python**: The primary programming language used for developing the chatbot.
- **NLTK**: Natural Language Toolkit, used for processing textual data.
- **spaCy**: An open-source software library for advanced natural language processing in Python.

## Theory

### Natural Language Processing (NLP)
Natural Language Processing is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The goal is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful.

### Chatbots
Chatbots are AI-based software applications that simulate human conversation. They are used in a variety of applications, such as customer service, information retrieval, and entertainment. Chatbots can be rule-based, providing predefined responses to specific inputs, or more advanced, using machine learning to generate responses.

### How It Works
1. **User Input**: The user inputs a text query.
2. **Text Processing**: The input text is processed using NLP techniques. This can include tokenization, lemmatization, and other text preprocessing steps.
3. **Response Generation**: The processed text is matched against predefined responses, and the appropriate response is returned to the user.
4. **Output**: The chatbot outputs the response to the user.

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/chatbot-project.git
    cd chatbot-project
    ```

2. **Create and Activate a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the Required Libraries**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download spaCy Model**
    ```sh
    python -m spacy download en_core_web_sm
    ```

## Usage

1. **Run the Chatbot**
    ```sh
    python chatbot.py
    ```

2. **Interact with the Chatbot**
    - Type in your queries and press Enter.
    - To exit, type "exit", "bye", or "quit".

## Adding More Responses
To add more responses, update the `responses` dictionary in the `chatbot.py` file with new key-value pairs. The key is the user's query, and the value is the chatbot's response.

Example:
```python
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "what is your name": "I'm Chatbot, your friendly assistant.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "default": "I don't understand. Can you rephrase?"
}
 ```
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

Acknowledgments
NLTK
spaCy
