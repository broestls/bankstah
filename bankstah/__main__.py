import datetime
import discord
import config

from base import Session
from models import User,Transaction
from util import snowflake_to_ts,get_channel_user
from itemhunt import ingest_brew

# Create an instance of the discord class
client = discord.Client()
lastconnectf = open("state/last.txt","w+")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        for channel in guild.channels:
            print('Joining '+guild.name+"/"+channel.name)

@client.event
async def on_disconnect():
    lastconnectf.write(datetime.datetime.now())

@client.event
async def on_message(message):
    print(snowflake_to_ts(message.id), end='')
    print(": ", end='')
    print(repr(message.content))
    if message.author == client.user:
        return

    if message.author.name == 'DiscordRPG':
        if 'stopped the brew' in message.content.lower():
            await message.channel.send(ingest_brew(message.content))

client.run(config.discord_bot_token)
