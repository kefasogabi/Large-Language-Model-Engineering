import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
import ollama

MODEL = "llama3"  # Ensure this model exists
# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)

class Website:
    def __init__(self, url):
        self.url = url
        self.title, self.text = self.scrape()

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No Title Found"
            text = " ".join(p.get_text() for p in soup.find_all("p"))
            return title, text
        return "Failed to retrieve page", ""

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related."

def user_prompt_for(website):
    return f"You are looking at a website titled {website.title}.\n\
    The contents of this website are as follows:\n{website.text}\n\n\
    Please summarize the website concisely."

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarize(url):
    website = Website(url)
    # response = openai.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=messages_for(website)
    # )
    response = ollama.chat(model=MODEL, messages=messages_for(website))
    return response['message']['content']

def display_summary(url):
    summary = summarize(url)
    print(summary)  # Use print instead of display(Markdown(summary))

display_summary("https://anthropic.com")




