print("===================================")
print("      SIMPLE CHATBOT PROJECT       ")
print("===================================")
print("Chatbot: Hello! I am SimpleBot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Chatbot: I am fine. How can I help you?")

    elif user == "what is your name":
        print("Chatbot: My name is SimpleBot.")

    elif user == "who created you":
        print("Chatbot: I was created by student's(SHUBHAM ,KARANVEER , SUJAL , BRAHMJOT , LOVEPREET) using Python.")

    elif user == "what can you do":
        print("Chatbot: I can answer simple questions.")

    elif user == "what is python":
        print("Chatbot: Python is a high-level programming language.")

    elif user == "what is a chatbot":
        print("Chatbot: A chatbot is a program that talks with users.")

    elif user == "what is your purpose":
        print("Chatbot: My purpose is to help users with simple queries.")

    elif user == "which language are you written in":
        print("Chatbot: I am written in Python.")

    elif user == "is python easy":
        print("Chatbot: Yes, Python is easy to learn for beginners.")

    elif user == "what is programming":
        print("Chatbot: Programming is writing instructions for computers.")

    elif user == "what is a computer":
        print("Chatbot: A computer is an electronic machine that processes data.")

    elif user == "what is software":
        print("Chatbot: Software is a set of programs used by a computer.")

    elif user == "what is hardware":
        print("Chatbot: Hardware refers to physical parts of a computer.")

    elif user == "what is an operating system":
        print("Chatbot: An operating system manages computer hardware and software.")

    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "do you use ai":
        print("Chatbot: No, I am a simple rule-based chatbot.")

    elif user == "what is your version":
        print("Chatbot: I am SimpleBot version 1.0.")

    elif user == "can you learn":
        print("Chatbot: No, I cannot learn new things.")

    elif user == "are you human":
        print("Chatbot: No, I am a computer program.")

    elif user == "tell me a fact":
        print("Chatbot: Python was created by Guido van Rossum.")

    elif user == "who am i":
        print("Chatbot: You are a user interacting with me.")

    elif user == "thank you":
        print("Chatbot: You're welcome!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")