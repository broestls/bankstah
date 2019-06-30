import discord
import config
import datetime

client = discord.Client()
lastconnectf = open("state/last.txt","w+")



cookies = []

def cookie_offer(user):
    print("caught cookie_offer")
    if user not in cookies:
        cookies.append(user)
        return user + " has a cookie to give away!"
    else:
        return user + "! You already told me you have a cookie to give away!"

def cookie_query(user):
    print("caught cookie_query")
    return "There are " + len(cookies) + " cookies posted!"

def cookie_beg(user):
    print("caught cookie_beg")
    return user + "is begging for your cookie!"

commands = {
    "cookie offer": cookie_offer,
    "cookie query": cookie_query,
    "cookie beg": cookie_beg,
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        for channel in guild.channels:
            print('Joining '+guild.name+"/"+channel.name)

    for com in commands:
        print('Loaded command: ' + com)

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
