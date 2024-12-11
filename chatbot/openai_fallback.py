import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot which offers support to users. There are some hard coded replies but when the simple model doesn't understand the question you need to step on and try to reply."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content