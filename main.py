from Web_Server import Web_Server
import Requests
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
    #Top 100 Games
  if message.content.lower().startswith('!steam100'):
    await message.channel.send('The top 100 Steam games right now are: \n'+ '```'+ '\n'.join(map(str, Requests.list))+'```')
    #Top 10 Games
  if message.content.lower().startswith('!top10'):
    await message.channel.send('The top 10 Steam games right now are: \n'+ '```'+ '\n'.join(map(str, Requests.list[0:10]))+'```')
    #Top 50 Games
  if message.content.lower().startswith('!top50'):
    await message.channel.send('The top 50 Steam games right now are: \n'+ '```'+ '\n'.join(map(str, Requests.list[0:50]))+'```')
    #Bottom 50
  if message.content.lower().startswith('!bot50'):
    await message.channel.send('The bottom 50 of the top 100 Steam games are: \n'+ '```'+ '\n'.join(map(str, Requests.list[50:100]))+'```')
    #Bottom 10
  if message.content.lower().startswith('!bot10'):
    await message.channel.send('The Bottom 10 of the top 100 Steam games are: \n'+ '```'+ '\n'.join(map(str, Requests.list[90:100]))+'```')

Web_Server()
client.run(os.getenv('token'))