import os
from openai import OpenAI

def generate_response(instructions="you are a helpful assistant that acts as human as possible",user_input="",debug_feedback= [False,""]) -> str:
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key = os.getenv("OPEN_AI_API_KEY")
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": user_input
            },
            {
                "role":"developer",
                "content": debug_feedback[1]
            }],
        model="openai/gpt-4o",
        temperature=0.8,
        max_tokens=100,
        top_p=1
    )

    return str(response.choices[0].message.content)