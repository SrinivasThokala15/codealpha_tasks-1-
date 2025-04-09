import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Define chatbot responses using predefined patterns
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing great! How about you?"]],
    [r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
    [r"(.*) your name?", ["I'm ChatBot, your virtual assistant."]],
    [r"(.) help (.)", ["Sure! What do you need help with?"]],
    [r"who created you?", ["I was created by a Python developer using NLTK."]],
    [r"(.*)", ["I'm not sure how to respond to that. Can you ask something else?"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Function to start chatbot interaction
def start_chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run chatbot
if _name_ == "_main_":
    start_chat()