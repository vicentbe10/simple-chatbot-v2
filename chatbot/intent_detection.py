import spacy

nlp = spacy.load("en_core_web_lg")

# Each key in this dictionary is an "intent" (ex. weather, news, etc.)
keywords = {
    "weather": ["weather", "outside", "rain", "forecast", "temperature"],
    "news": ["news", "headlines", "current events", "update"],
    "time": ["time", "clock", "hour"],
    "date": ["date", "day", "today"],
    "greeting": ["hello", "hi", "hey", "greetings", "what's up"],
    "joke": ["joke", "funny", "laugh", "humor"],
    "python_help": ["python", "code", "programming", "help", "syntax", "debug"],
    "project_idea": ["project", "idea", "build", "create", "suggestion"],
}

def detect_keywords(text):
    doc = nlp(text)
    # The next for loops through each key-value pair in the keywords dictionary
    # Intent will be the key (e.g., "weather"), and words will be the list of associated keywords (e.g., ["weather", "forecast", "temperature", "rain"]).
    for intent, words in keywords.items():
        for word in words:
            keyword_token = nlp(word)[0] #Convert keyword to spaCy token
            for token in doc:
                # User similarity method to get a score (tweak the 0.7 as needed)
                if token.similarity(keyword_token) > 0.8:
                    return intent
    return "unknown" #Return "unknown" if no intent is found

