
from dotenv import load_dotenv
import os
import discord
import requests
import json


load_dotenv()


my_secret = os.environ['TOKEN']

client = discord.Client()

def getQuote():
  response = requests.get('https://zenquotes.io/api/random')
  jsonData = json.loads(response.text) 

  quote = jsonData[0]['q'] + ' ~' + jsonData[0]['a']
  return quote


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$plsinspire'):
    quote = getQuote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))