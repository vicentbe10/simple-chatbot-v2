from chatbot import detect_keywords, generate_response, get_openai_response, responses

def chat_loop():
    print("Hello! I'm here to chat with you. Type 'exit' to end the chat.")
    last_intent = None # Track the last recognized intent
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
                # Check for intent
                intent = detect_keywords(user_input)

                if intent == "unknown":
                    print("Bot: Let me think about that...")
                    response = get_openai_response(user_input)

                # if intent == "unknown" and last_intent:
                #     print(f"Bot: I'm assuming you are still asking about {last_intent}.")
                #     intent = last_intent
                else:
                    #Generate and display response
                    response = generate_response(intent)
                    last_intent = intent
                    
                print(f"Bot: {response}")

        except Exception as err:
            print(f"Bot: Oops, something went wrong! ({err})") 

# Start the chat loop
if __name__ == "__main__":
    chat_loop()