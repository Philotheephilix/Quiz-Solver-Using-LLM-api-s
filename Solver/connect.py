import openai
import anthropic

from .seggregate import trim_response_claude
from .config import API_KEY,API_BASE


openai.api_key = API_KEY
openai.api_base =API_BASE


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=API_KEY,
)

# change engine and remove api_base if using official openai api

#   increase max_tokens to get a long response

def chatgpt(prompt):
    response = openai.Completion.create(
        engine="pai-001",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def claude(prompt):
    message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
        ]
    )
    response=message.content[0].text
    seggregated_output=trim_response_claude(response)
    return seggregated_output

