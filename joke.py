import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

system_message = "You are an assistant that is great at telling jokes"
user_prompt = "Tell a light-hearted joke for an audience of Data Scientists"


prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]


# GPT-4o

completion = openai.chat.completions.create(
    model='gpt-4o',
    messages=prompts,
    temperature=0.4
)

stream = openai.chat.completions.create(
            model='gpt-4o',
            messages=prompts,
            temperature=0.7,
            stream=True
        )

response = ""
for chunk in stream:
    text = chunk.choices[0].delta.content or ''
    text = text.replace("```", "").replace("markdown", "")
    response += text
    print(text, end="", flush=True)  # Print each chunk immediately

print("\n")  # Add a newline at the end for better formatting
