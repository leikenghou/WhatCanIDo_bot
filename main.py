# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:11:56 2023

@author: li102
"""

# This example requires the 'message_content' intent.
import discord
import requests
import json
import random

#open 'Token.json'file
with open('Token.json','r') as token_file:
    file = json.load(token_file)
    Token = file['Token']


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if message.content.startswith('$hello'):
        await message.channel.send('hello!')
        
    if message.content.startswith('$inspire'):
        quoto = get_quote()
        await message.channel.send(quoto)
        
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run(Token)