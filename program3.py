import os
from groq import Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
chat_completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain Artificial Intelligence."
        }
    ]
)
print(chat_completion.choices[0].message.content)