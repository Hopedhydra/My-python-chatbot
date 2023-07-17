import random
import json

class ChatBot:
    def __init__(self):
        self.bot_responses = {}
        self.load_responses()

    def load_responses(self):
        try:
            with open("chatbot_responses.json", "r") as f:
                self.bot_responses = json.load(f)
        except FileNotFoundError:
            self.bot_responses = {
                "how are you": ["I'm good, thank you!", "I'm doing great!", "All good here!"],
                "what's your name": ["I'm ChatBot.", "You can call me ChatBot.", "I go by the name ChatBot."],
                "hello": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
                "bye": ["Goodbye!", "See you later!", "Farewell!"],
                "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"],
                "tell me a fact": ["The Earth has more than 80,000 species of edible plants.", "A group of flamingos is called a 'flamboyance'."],
                "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "Sorry, I don't understand."],
            }

    def save_responses(self):
        with open("chatbot_responses.json", "w") as f:
            json.dump(self.bot_responses, f, indent=4)

    def get_bot_response(self, user_input):
        user_input = user_input.lower()

        for question, responses in self.bot_responses.items():
            if question in user_input:
                return random.choice(responses)

        return self.learn_response(user_input)

    def learn_response(self, user_input):
        new_response = input("ChatBot: I'm not familiar with that. How should I respond? ")
        self.bot_responses[user_input] = [new_response]
        self.save_responses()
        return "Thank you! I'll remember that for next time."

def main():
    chat_bot = ChatBot()
    print("ChatBot: Hello! How can I assist you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day.")
            break

        response = chat_bot.get_bot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
