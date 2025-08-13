# CodeAlpha_Task3

This is a simple rule-based chatbot built using Python. It interacts with users through predefined responses, offering greetings, jokes, and answers to basic questions. The chatbot also logs conversations for reference.


## Features
Responds to common greetings like “hi”, “hello”, and “hey”

Answers basic questions (e.g., “how are you?”, “who created you?”)

Tells random jokes on request

Logs chat history to a text file


## Technologies Used
Python (Standard Library)

File handling for chat logging

Random module for joke selection
Easy to run and extend



import random
responses = {

    "how are you": "I'm doing great, thanks for asking! ",
    "what is your name": "I'm your friendly chatbot. You can call me Copilot!",
    "what can you do": "I can chat with you, answer simple questions, and keep you company!",
    "what's the weather": "I can't check live weather yet, but it's always sunny in code land! ",
    "who created you": "I was created by a brilliant developer Miss.shruti Wadettiwar from India.",
    "bye": "Goodbye! Have a great day! "
}

greetings = [
    "hello", "hi","hey" 
    ]
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to therapy? It had too many issues.",
    "Why was the math book sad? It had too many problems."
    
]

def basic_chatbot():
    print("Welcome to the Enhanced Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input in greetings:
            response = "Hello there! How can I assist you today?"
        elif user_input == "tell me a joke":
            response = random.choice(jokes)
        elif user_input in responses:
            response = responses[user_input]
        else:
            response = "Hmm... I didn't understand that. Can you try something else?"

        print(f"Bot: {response}")
        with open("chat_log.txt", "a") as log:
            log.write(f"You: {user_input}\nBot: {response}\n")
        if user_input == "bye":
            break

if __name__ == "__main__":
    basic_chatbot()

## OUTPUT 
    
You: hi

Bot: Hello there! How can I assist you today?

You: hey

Bot: Hello there! How can I assist you today?

You: hello

Bot: Hello there! How can I assist you today?

You: how are you

Bot: I'm doing great, thanks for asking! 

You: what is your name

Bot: Hmm... I didn't understand that. Can you try something else?

You: hi

Bot: Hello there! How can I assist you today?

You: who created you

Bot: I was created by a brilliant developer Miss.shruti Wadettiwar from India.


## How to Run
Just execute chatbot.py in your Python environment. Type “bye” to exit the chat.


basic-chatbot/
│
├── chatbot.py         # Main chatbot script
├── chat_log.txt       # Chat history (auto-generated)
└── README.md          # Project documentation
