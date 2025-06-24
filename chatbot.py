def chatbot():
    print("Hi! I'm Chatbot, How can I help you?.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['hi', 'hello', 'hey','greetings']:
            print("ChatPy: Hello there!")
        elif 'how are you' in user_input:
            print("ChatPy: I'm doing well. How about you?")
        elif 'your name' in user_input:
            print("ChatPy: I'm your friendly chatbot!")
        elif 'have a nice day' in user_input:
            print("Chatpy: Thanks!")
        elif 'bye' in user_input:
            print("ChatPy: Goodbye! Have a great day.")
            break
        else:
            print("ChatPy: I'm not sure how to respond to that.")
chatbot()
