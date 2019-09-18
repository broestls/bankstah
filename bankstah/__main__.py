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
        if 'deposited' in message.content.lower():
            msg_split = message.content.split(" ")
            bankuser = get_channel_user(msg_split[0], client.get_channel(message.channel.id).members)
            await message.channel.send('Logged that ' + msg_split[0] + ' gave ' + str(msg_split[3]) + ' to their guild.')
            session = Session()
            exists = session.query(User).filter(User.id == bankuser.id)
            if exists is None:
                newuser = User(discord_id=bankuser.id, name=bankuser.name,lastseen=datetime.datetime.utcnow())
                session.add(newuser)
                print("added a new user to the db!")
            else:
                exists.update_lastseen(datetime.datetime.utcnow())
                print("Saw an existing user and updated their info!")
            session.commit()
        elif 'withdrew' in message.content.lower():
            msg_split = message.content.split(" ")
            print(msg_split[0] + ' withdrew ' + str(msg_split[3]) + ' to their guild.')
            await message.channel.send('Logged that ' + msg_split[0] + ' withdrew ' + str(msg_split[3]) + ' to their guild.')
        elif 'stopped the brew' in message.content.lower():
            await message.channel.send("Logged a brew: " + ingest_brew(message.content))


    if message.content.startswith('$$$'):
        msg = message.content.strip('$$$').split(" ")
        if " ".join(msg[0:2]) in commands.keys():
            print('got inside the if for commands')
            await message.channel.send(commands[" ".join(msg[0:2])](message.author.name))

client.run(config.discord_bot_token)
