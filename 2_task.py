import spacy
from spacy.matcher import Matcher
from nltk.chat.util import Chat, reflections
import random
import tkinter as tk
from tkinter import scrolledtext

# Load the English language model for SpaCy
nlp = spacy.load("en_core_web_sm")

# Define the FAQ pairs
faq_pairs = [
    (
        r"What is your name?",
        ["I am a chatbot designed to answer FAQs.",]
    ),
    (
        r"What can you do?",
        ["I can answer questions about a specific topic or product.",]
    ),
    (
        r"How do I contact support?",
        ["You can contact support at support@example.com.",]
    ),
    (
        r"What are your working hours?",
        ["I am available 24/7 to answer your questions.",]
    ),
    (
        r"Where can I find more information?",
        ["You can visit our website at www.example.com for more information.",]
    ),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(faq_pairs, reflections)

# Define a function to handle greetings
def handle_greetings(text):
    greetings = ["hello", "hi", "hey", "howdy"]
    if text.lower() in greetings:
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"])
    else:
        return None

# Define a function to handle unknown queries
def handle_unknown(text):
    return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Define a function to handle user input
def handle_user_input():
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)  # Clear the input field

    # Check for greetings
    greeting_response = handle_greetings(user_input)
    if greeting_response:
        add_message_to_chat("Chatbot", greeting_response)
        return

    # Process user input using SpaCy
    doc = nlp(user_input)
    # Extract entities, keywords, or any other NLP processing you want

    # Check if the input is a question and get a response from the FAQ chatbot
    if "?" in user_input:
        response = chatbot.respond(user_input)
        add_message_to_chat("Chatbot", response)
    else:
        # Handle unknown queries
        add_message_to_chat("Chatbot", handle_unknown(user_input))

# Define a function to add messages to the chat window
def add_message_to_chat(sender, message):
    chat_text.config(state=tk.NORMAL)  # Enable editing
    chat_text.insert(tk.END, f"{sender}: {message}\n")
    chat_text.config(state=tk.DISABLED)  # Disable editing
    chat_text.see(tk.END)  # Scroll to the bottom of the chat window

# Create the GUI
root = tk.Tk()
root.title("FAQ Chatbot")

# Create a chat window using a scrolled text widget
chat_text = scrolledtext.ScrolledText(root, width=50, height=20)
chat_text.pack(padx=10, pady=10)

# Create an input field for user queries
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(padx=10, pady=5)

# Create a send button to submit user queries
send_button = tk.Button(root, text="Send", command=handle_user_input)
send_button.pack(padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
