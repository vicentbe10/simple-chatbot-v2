import requests
import os
from flask import Flask, request, jsonify
from chatbot import detect_keywords, generate_response, get_openai_response, responses

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

LINE_API_URL="https://api.line.me/v2/bot/message/reply"
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_TOKEN = os.getenv("LINE_CHANNEL_TOKEN")


@app.route("/")
def hello_world():
    return "<h2>Hello, World!!!</h2>"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    # Basic keyword detection
    intent = detect_keywords(user_input)
    if intent == "unknown":
        response = get_openai_response(user_input)  # OpenAI fallback
    else:
        response = generate_response(intent)

    return jsonify({"response": response})

@app.route("/webhook/telegram", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    user_input = data["message"]["text"]

    intent = detect_keywords(user_input)
    if intent == "unknown":
        response = get_openai_response(user_input)  # OpenAI fallback
    else:
        response = generate_response(intent)

    # Send the response back to the user on Telegram
    requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text":response})
    return "ok"

@app.route("/webhook/line", methods=["POST"])
def line_webhook():
    data = request.get_json()
    events = data.get("events", [])
    if events:
        event = events[0]
        user_input = event.get("message", {}).get("text")
        reply_token = event.get("replyToken")

        intent = detect_keywords(user_input)
        if intent == "unknown":
            response = get_openai_response(user_input)  # OpenAI fallback
        else:
            response = generate_response(intent)

        # Send the response back to the user on Telegram
        requests.post(LINE_API_URL, json={"replyToken": reply_token, "messages": [{"type": "text", "text":response}]}, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {LINE_CHANNEL_TOKEN}'})
        return "ok"
    return "ok"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
