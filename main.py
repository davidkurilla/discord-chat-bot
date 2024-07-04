import os
import discord
from groq import Groq


intents = discord.Intents.all()
bot = discord.Client(intents=intents)
discord_key = os.environ['DISCORD_KEY']

client = Groq(
  api_key = os.environ['LLAMA_KEY'],
)

# FUNCTION: call_groq - This function prompts the LLM and returns its response
async def call_groq(prompt):
  
  try:
  
    chat_completion = client.chat.completions.create(
      messages = [
        {
          "role": "user",
          "content": f"You are a furry cat monster named One Star Chan. Respond in slighty rude UwU speech: {prompt}",
        }
      ],
      model = "llama3-8b-8192",
      temperature = 0,
      max_tokens=2000,
    )
  
    return chat_completion.choices[0].message.content

  except Exception as e:
    print(e)
    return "SYSTEM ERROR - Could not get response"

# FUNCTION: on_ready - This function boots up the Discord bot
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# FUNCTION: on_message - This function handles the messages sent to the bot
@bot.event
async def on_message(message):
  try: 
    if message.author == bot.user or bot.user not in message.mentions:
      return
    
    else:
      response = await call_groq(message.content)
      await message.channel.send(response)
      
  except Exception as e:
    print(e)
    await message.channel.send("SYSTEM ERROR - Unable to handle message")
    
bot.run(discord_key)
