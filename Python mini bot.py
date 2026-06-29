print("Simple Chat bot")
print("Type 'quit' to exit")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chat bot: Goodbye!")
        break
    elif user_input.lower() == 'hello':
        print("Chat bot: Hello! How can I help you today?")
    elif user_input.lower() =="how are you":
        print("Chat bot: I'm just a bot, but I'm doing great! How about you?")
    elif user_input.lower() == 'what is your name':
        print("Chat bot: I'm a simple chat bot created to assist you.")
    elif user_input.lower() == 'what is python':
        print("Chat bot: Python is a high-level, interpreted programming language known for its simplicity and readability.")
    elif user_input.lower() == 'what is AI':
        print("Chat bot: AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.")
    elif user_input.lower() == 'what is machine learning':
        print("Chat bot: Machine learning is a subset of AI that involves training algorithms to learn patterns from data and make predictions or decisions without being explicitly programmed.")
    else:
        print("Chat bot: I'm sorry, I don't understand that. Can you please rephrase?")
        