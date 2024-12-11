import random

responses = {
    "weather": [
        "Let me check... ah, seems like a great day to stay indoors and code! (HC)",
        "I can’t tell if it's raining, but it's always a good time to work on your project! (HC)",
        "Weather's unpredictable, but you can count on me being here to help! (HC)",
    ],
    "news": [
        "I’m here to deliver the latest in coding news: Python is awesome! (HC)",
        "Breaking news! You're about to learn something new. (HC)",
        "I don’t have the headlines, but I can answer your coding questions! (HC)",
    ],
    "time": [
        "Right now, it's code o'clock! (HC)",
        "Time flies when you're coding! (HC)",
        "You’ve got the time. Let’s make the most of it! (HC)",
    ],
    "date": [
        "It’s always a great day to write some code. (HC)",
        "Today’s the perfect day to make progress on your chatbot! (HC)",
        "Not sure about the date, but I’m sure it's a great day to learn something new! (HC)",
    ],
    "greeting": [
        "Hello there! How can I assist you with your coding journey? (HC)",
        "Hi! Ready to dive into some Python magic? (HC)",
        "Hey! I’m here to help you with all things code. What do you need? (HC)",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because the light attracts bugs! (HC)",
        "Why do Java developers wear glasses? Because they don’t see sharp! (HC)",
        "Why was the developer unhappy at their job? They wanted arrays. (HC)",
    ],
    "python_help": [
        "Need help with Python? I'm here to guide you! (HC)",
        "Python tip: Remember to stay indented! Need more advice? (HC)",
        "Let's dive into Python! Tell me what you’re stuck on. (HC)",
    ],
    "project_idea": [
        "How about building a simple to-do list app to track your goals? (HC)",
        "Why not create a chatbot that answers questions? Oh wait, you already did! (HC)",
        "Try a web scraper to collect interesting data. It’s a fun project! (HC)",
    ],
    "unknown": [
        "Hmm, I didn’t catch that. Can you rephrase? (HC)",
        "Not sure I understand. Want to try saying it a different way? (HC)",
        "Sorry, I’m still learning. Could you clarify? (HC)",
    ]
}

def generate_response(intent):
    return random.choice(responses.get(intent, responses["unknown"]))