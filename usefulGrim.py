    #Imports all necessary libraries
import discord
from discord.ext import commands
from discord.utils import get
import asyncio

    #Token to log in to bot
TOKEN = '<insert token here>'

    #Setting up for commands
prefix = '.'
grim = commands.Bot(command_prefix = prefix)

    #Login
@grim.event
async def on_ready():
    print('Logged in as...')
    print(grim.user.name)
    print(grim.user.id)
    print('-----')

    #At event
@grim.event
async def on_message(message):
    splitlist = message.content.split(' ')

        #test command to test command
    if message.content.startswith(prefix + 'test'):
        await grim.send_message(message.channel,'I am here now')

        #nap command to check splitlist
    elif message.content.startswith(prefix + 'nap'):
        if (type(splitlist[1]) != int):
            await grim.send_message(message.channel, 'The parameters you entered were incorrect. Refer to the .help command')
        sleeptime = int(splitlist[1])
        await grim.send_message(message.channel, 'Naptime for ' + splitlist[1] + ' seconds')
        for counter in range(sleeptime - 1):
            await asyncio.sleep(1)
            await grim.send_message(message.channel, 'Zzzz...')
        await asyncio.sleep(1)
        await grim.send_message(message.channel, 'Good Morning!')

        #solo command. mutes all in a role except the solist
    elif message.content.startswith(prefix+'solo'):
        soloist = message.mentions[0]
        role = message.role_mentions[0]
        membersmuted = list()
        for x in message.server.members:
            for y in x.roles:
                if y == role and x != soloist:
                    x.voice.mute = 1
                    membersmuted.append(x)
                    soloist.voice.mute = 0
        mutestring = ''
        for x in membersmuted:
            mutestring = mutestring + "-" + x.mention + '-'
        await grim.send_message(message.channel, 'I have muted ' + mutestring + ' and have solo\'d ' + soloist.mention)

        #For undoing the solo command
    elif message.content.startswith(prefix+'unsolo'):
        role = message.roles_mentions[0]
        for x in message.server.members:
            for y in x.roles:
                if y == role:
                    x.voice.mute = 0
        await grim.send_message(message.channel, 'Everyone in the ' + role.mention + ' role is unmuted')

        #silence command
    elif message.content.startswith(prefix+'silence'):
        if (type(splitlist[1]) != int):
            await grim.send_message(message.channel, 'The parameters you entered were incorrect. Refer to the .help command')
            return

            count = 1
            for x in message.mentions:
                await create_role(ctx.author.server,name('DUNCE'+num),permissions(send_messages = False))
                role = discord.utils.get(ctx.author.server.roles, name = 'DUNCE'+count)
                await bot.add_roles(dunce,role)
            
            timer = 0
            while timer < splitlist[1]*60:
                 timer+= 1
            count = 1
            for x in message.mentions:
            	await delete_role(message.author.server,discord.utils.get(message.author.server.roles, name = 'DUNCE'+count))
            	count += 1

        else:
            await grim.send_message(ctx.channel, 'I\'m sorry, but you don\'t have the permissions to do that')
        

        #help command
    elif message.content.startswith(prefix+'help'):
        file = open('help.txt','r')
        await grim.send_message(message.channel,file.read())

grim.run(TOKEN)
