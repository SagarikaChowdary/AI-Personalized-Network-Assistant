import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def fact_check(topic):

    prompt = f"""
You are an AI Fact Checker.

Check the following statement carefully.

Statement:
{topic}

Return the answer in the EXACT format below.

✅ Verdict
(True / False / Partially True)

📖 Explanation
- Point 1
- Point 2
- Point 3

🎯 Confidence
(High / Medium / Low)

Rules:
- Give only the requested format.
- Use simple English.
- Keep the explanation concise.
- Do not add introductions or conclusions.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
