import os
from dotenv import load_dotenv
from openai import OpenAI
from app.prompts import SYSTEM_PROMPT

# 加载 .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def run_agent(user_message: str) -> str:
    """
    真正调用 ChatGPT
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
