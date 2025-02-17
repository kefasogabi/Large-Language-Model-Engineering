import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
from IPython.display import Markdown, display, update_display

load_dotenv(override=True)

# lOAD GEMINI API KEY
google_api_key = os.getenv('GOOGLE_API_KEY')
google.generativeai.configure()

# lOAD CHATGPT API KEY
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

gpt_model = "gpt-4o-mini"
gemini_model = "gemini-2.0-flash-exp"

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

gemini_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

gpt_messages = ["Hi there"]
gemini_messages = ["Hi"]

def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, gemini in zip(gpt_messages, gemini_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": gemini})
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content


print(call_gpt())