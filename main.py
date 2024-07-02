import os
import discord
from groq import Groq


intents = discord.Intents.all()
bot = discord.Client(intents=intents)
discord_key = os.environ['DISCORD_KEY']

client = Groq(
  api_key = os.environ['LLAMA_KEY'],
)

async def callGroq(prompt):
  
  try:
  
    chat_completion = client.chat.completions.create(
      messages = [
        {
          "role": "user",
          "content": f"Respondin under 2000 characters in slighty rude UwU speech: {prompt}",
        }
      ],
      model = "llama3-8b-8192",
    )
  
    return chat_completion.choices[0].message.content

  except Exception as e:
    print(e)
    return "Error"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
  try: 
    if message.author == bot.user or bot.user not in message.mentions:
      return
    
    else:
      response = await callGroq(message.content)
      await message.channel.send(response)
      
  except Exception as e:
    print(e)
    await message.channel.send("Error")

bot.run(discord_key)
