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
