import openai
from .config import API_KEY,API_BASE
openai.api_key = API_KEY
openai.api_base =API_BASE

# change engine and remove api_base if using official openai api

#   increase max_tokens to get a long response

def chat(prompt):
    response = openai.Completion.create(
        engine="pai-001",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
