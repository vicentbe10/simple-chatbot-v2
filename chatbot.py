import spacy

nlp = spacy.load("en_core_web_sm")
responses = {
    "tell": "I'm cheating the intent with a fake keyword before the actual one",
    "weather": "I'm not a weather app, but I can tell you it's always sunny in the code!",
    "time": "I'm not a clock, but I know it's coding o'clock!",
    "news": "I can’t provide live news yet, but I can tell you I’m here to help!",
    "date": "Every day is a good day to learn Python!"
}
chat_history = []

def analyze_intent(text):
    doc = nlp(text)
    for token in doc:
        print(f"Text: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}")

def detect_keywords(text):
    doc = nlp(text)
    keywords = ["weather", "time", "date", "news"]
    for token in doc:
        if token.text.lower() in keywords:
            print(f"Detected keyword '{token.text}' indicating intent.")

def respond_to_intent(text):
    doc = nlp(text)
    for token in doc:
        keyword = token.text.lower()
        if keyword in responses:
            print(f"Response: {responses[keyword]}")
            return keyword
    print("Response: Sorry, I didn't understand that.")

def chat_loop():
    print("Hello! I'm here to chat with you. Type 'exit' to end the chat.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Bot: Goodbye!")
                break
            elif user_input.lower() == "help":
                print("Bot: Here are the available keywords:")
                for keyword in responses:
                    print(f"> {keyword}")
            else:
                response = respond_to_intent(user_input)
                chat_history.append({"User": user_input, "Bot": response})
                print(f"Bot: {response}")
        except Exception as err:
            print(f"Bot: Oops, something went wrong! ({err})")
    
    print("\nChat History:")
    for message in chat_history:
        print(f"You: {message['User']}")
        print(f"Bot: {message['Bot']}")

chat_loop()


# user_question = "Can you tell me the weather?"
# analyze_intent(user_question)
# detect_keywords(user_question)

# respond_to_intent("Can you tell me the time?")
# respond_to_intent("What's the latest news?")
# respond_to_intent("Can I get a weather update?")
# respond_to_intent("What's your name?")