from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import ollama

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# set up environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)




system_prompt = "You are an assistant that analyzes code and explain the the functionality and outcome of the code. \
Respond to code questions breaking down in steps the functionality of the provided code"

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

messagesReq=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
        ]



# Get gpt-4o-mini to answer, with streaming
# stream = openai.chat.completions.create(
#             model=MODEL_GPT,
#             messages=messagesReq,
#             stream=True
#         )
      

# response = ""
# display_handle = display(Markdown(""), display_id=True)
# for chunk in stream:
#     response += chunk.choices[0].delta.content or ''
#     response = response.replace("```","").replace("markdown", "")
#     update_display(Markdown(response), display_id=display_handle.display_id)

# response = ""
# for chunk in stream:
#     text = chunk.choices[0].delta.content or ''
#     text = text.replace("```", "").replace("markdown", "")
#     response += text
#     print(text, end="", flush=True)  # Print each chunk immediately

# print("\n")  # Add a newline at the end for better formatting



# Get Llama 3.2 to answer
stream = ollama.chat(model=MODEL_LLAMA, messages=messagesReq, stream=True)

# response = ""
# display_handle = display(Markdown(""), display_id=True)

# for chunk in stream:
#     if "message" in chunk:
#         response += chunk["message"]["content"] or ''
#         response = response.replace("```", "").replace("markdown", "")
#         update_display(Markdown(response), display_id=display_handle.display_id)


response = ""
for chunk in stream:
    if "message" in chunk and "content" in chunk["message"]:
        text = chunk["message"]["content"] or ''
        text = text.replace("```", "").replace("markdown", "")
        response += text
        print(text, end="", flush=True)  # Print each chunk immediately

print("\n")  # Add a newline at the end for better formatting
