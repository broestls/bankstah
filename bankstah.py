import discord
import config
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an instance of the discord class
client = discord.Client()
lastconnectf = open("state/last.txt","w+")

engine = create_engine(config.DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

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
    if message.author == client.user:
        return

    if message.author.name == 'DiscordRPG':
        if 'deposited' in message.content.lower():
            msg_split = message.content.split(" ")
            print(msg_split[0] + ' gave ' + str(msg_split[3]) + ' to their guild.')
            await message.channel.send('Logged that ' + msg_split[0] + ' gave ' + str(msg_split[3]) + ' to their guild.')

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
