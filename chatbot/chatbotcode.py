import time

def get_current_time():
    return time.ctime()

def chatbot(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hi": "Hi there! I'm a chatbot here to assist you.",
        "hello": "Hi there! I'm a chatbot here to assist you.",
        "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me anything.",
        "where are you from": "I'm from the digital world, always ready to chat!",
        "how are you": "I'm fine.",
        "do you have any hobbies": "I'm always busy helping users, so my hobby is chatting with people like you!",
        "interests": "I'm always busy helping users, so my hobby is chatting with people like you!",
        "what did you eat today": "I don't eat, but I can help you find delicious recipes and food-related information.",
        "what do you like to eat": "I don't eat, but I can help you find delicious recipes and food-related information.",
        "favorite color": "I'm a chatbot, so I don't have personal preferences for colors.",
        "do you enjoy listening to music": "I can't listen to music, but I'm here to chat about it!",
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "another joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "tell me an interesting fact": "I don't have an interesting fact right now.",
        "weather in": "I'm sorry, I don't have real-time weather data.",
        "latest news": "I'm sorry, I don't have real-time news updates.",
        "translate": "I don't support real-time language translation.",
        "what is the time now": get_current_time(),
        "bye": "Goodbye! Take care and have a great day!"
    }

    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you please rephrase your sentence?")

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")

while True:
    user_input = input("Me: ").lower()
    if user_input == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break  
    
    response = chatbot(user_input)
    print("Chatbot:", response)