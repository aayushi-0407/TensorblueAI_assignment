# file_reader/gpt3.py

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from django.conf import settings

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def generate_code(prompt):
    full_prompt = f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}"
    response = client.completions.create(
        model="claude-v1",  # Specify the correct model
        prompt=full_prompt,
        max_tokens_to_sample=400,
    )
    return response.completion.lstrip()
