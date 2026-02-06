import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


openai = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def prompt_to_ai(prompt: str, max_tries: int = 3) -> str | None:
    completion = openai.chat.completions.create(
        model=os.getenv("OPENROUTER_AI_MODEL"),
        messages=[
            {
                "role": "system",
                "content": ""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        top_p=0.95,
        max_tokens=1000,

    )
    result = completion.choices[0].message.content

    if not result:
        if max_tries > 0:
            return prompt_to_ai(prompt, max_tries - 1)
        else:
            print("Error")
            return None

    return result


while True:
    prompt = input("> ")
    print(prompt_to_ai(prompt))


