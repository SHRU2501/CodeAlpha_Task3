import random
responses = {
    "how are you": "I'm doing great, thanks for asking! ",
    "what's your name": "I'm your friendly chatbot. You can call me Copilot!",
    "what can you do": "I can chat with you, answer simple questions, and keep you company!",
    "what's the weather": "I can't check live weather yet, but it's always sunny in code land! ",
    "who created you": "I was created by a brilliant developer Miss.shruti Wadettiwar from India.",
    "bye": "Goodbye! Have a great day! "
}
greetings = ["hello", "hi", "hey"]
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
