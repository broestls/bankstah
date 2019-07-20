import datetime
import discord
import config

from base import Session
from user import User
from transaction import Transaction
from util import snowflake_to_ts

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
    print(message)
    if message.author == client.user:
        return

    if message.author.name == 'DiscordRPG':
        if 'deposited' in message.content.lower():
            msg_split = message.content.split(" ")
            print(msg_split[0] + ' gave ' + str(msg_split[3]) + ' to their guild.')
            await message.channel.send('Logged that ' + msg_split[0] + ' gave ' + str(msg_split[3]) + ' to their guild.')

            session = Session()
            exists = session.query(User).filter(User.id == message.author.id)
            print(exists)
            session.close()
        elif 'withdrew' in message.content.lower():
            msg_split = message.content.split(" ")
            print(msg_split[0] + ' withdrew ' + str(msg_split[3]) + ' to their guild.')
            await message.channel.send('Logged that ' + msg_split[0] + ' withdrew ' + str(msg_split[3]) + ' to their guild.')

    if message.content.startswith('$$$'):
        msg = message.content.strip('$$$').split(" ")
        if " ".join(msg[0:2]) in commands.keys():
            print('got inside the if for commands')
            await message.channel.send(commands[" ".join(msg[0:2])](message.author.name))

client.run(config.discord_bot_token)
