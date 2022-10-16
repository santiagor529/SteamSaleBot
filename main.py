from Web_Server import Web_Server
import discord
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('$sale'):
    await message.channel.send('Not ready yet.')

Web_Server()
client.run(os.getenv('token'))