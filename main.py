import os
from groq import Groq

client = Groq(
  api_key = os.environ['LLAMA_KEY'],
)

prompt = input("Enter a prompt: ")

while prompt != "quit":
  
  chat_completion = client.chat.completions.create(
    messages = [
      {
        "role": "user",
        "content": f"{prompt}",
      }
    ],
    model = "llama3-8b-8192",
  )

  print(chat_completion.choices[0].message.content)

  prompt = input("Enter a prompt: ")
