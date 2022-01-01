import discord
import os

client = discord.Client()

#Event that triggers on startup.
@client.event
async def on_ready():
  print("Start up successful. Logged in as: {0.user}".format(client))

#event that triggers when bot recieves a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('botHello'):
    await message.channel.send("Hello!")
  elif message.content.startswith('bothello'):
    await message.channel.send("Hello!")


client.run(DISCORD TOKEN HERE)
