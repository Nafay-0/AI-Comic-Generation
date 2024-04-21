import os
from together import Together

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": "What are some fun things to do in New York"}],
)
print(response.choices[0].message.content)