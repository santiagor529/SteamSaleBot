from Web_Server import Web_Server
from Requests import response
import discord
import os

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
  if message.content.lower().startswith('!hello'):
    await message.channel.send('Hello!')
  if message.content.lower().startswith('!test'):
    await message.channel.send(str(response()))

Web_Server()
client.run(os.getenv('token'))