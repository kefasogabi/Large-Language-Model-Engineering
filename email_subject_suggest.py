import os
from openai import OpenAI
from dotenv import load_dotenv


def load_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def suggest_subject(email_body):
    """Generates a concise subject line for an email based on its content."""
    client = OpenAI(api_key=load_api_key())
    
    messages = [
        {"role": "system", "content": "You are an AI assistant that generates concise and clear subject lines for emails."},
        {"role": "user", "content": f"Generate a short and relevant subject line for the following email:\n{email_body}"}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    return response.choices[0].message.content.strip()


email_text = "Dear team, just a quick reminder that the quarterly reports are due by Friday. Please ensure all data is updated before submission. Let me know if you have any questions. Thanks!"
    
subject = suggest_subject(email_text)
print("Suggested Subject:", subject)

