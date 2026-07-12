import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_event(event_description):

    prompt = f"""
You are an AI Networking Assistant.

Analyze the following networking event.

Event:
{event_description}

Return your response in this exact format:

Summary:
(2-3 sentences)

Themes:
- Theme 1
- Theme 2
- Theme 3
- Theme 4
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content