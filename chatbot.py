import nltk
from nltk.tokenize import word_tokenize
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "hi": "Hello!",
    "how are you": "I'm good, how are you?",
    "bye": "Goodbye!",
    "what is your name": "I'm Chatbot, your friendly assistant.",
    "who created you": "I was created by charan.",
    "what's up": "Not much, just here to chat with you!",
    "how's the weather": "I don't have weather data, but I hope it's nice where you are.",
    "can you help me": "Sure, I'm here to help. What do you need?",
    "i need assistance": "I'm here to assist you. What can I do for you?",
    "default": "I don't understand.can you rephrase the sentence"
    }

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Function to process input with spaCy
def process_input_spacy(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    return ' '.join(tokens)

# Main loop for conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Bot: Goodbye!")
        break
    processed_input = process_input_spacy(user_input)
    response = get_response(processed_input)
    print(f"Bot: {response}")
