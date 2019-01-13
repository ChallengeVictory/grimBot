import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import pickle

TOKEN = 'NDI1MzMxNDMzODA1MTg1MDI0.Dp1y8Q.EI17fEk53nP_4ThPBv8ibiIsqRA'
    #Setting up for commands
prefix = '.'
grim = commands.Bot(command_prefix = prefix)
filename = 'responses'
try:
    infile = open(filename, 'rb')
    responses = pickle.load(infile)
    infile.close()
except:
    responses = []
    responses.append(0)

insults = ['What is that horrid beast that speaks? Oh, its you','Villain, I have done thy mother',
            'It appears to be shown a pig has learned to speak. How amusing',
           'With profound confidence, I concurr you are the rankest compound of villainous smell that ever offended any nostril',
           'How peculiar? Thou hast no more brain than I have in mine elbows, and mine elbows are not real',
           'Do not touch me. Methinks infection',
           'Such a vile offence to life',
           'What? An egg?',
           'Ah, a face that is not worth sunburning',
           'Was the Duchess a flesh-monger, a fool and a coward?',
           'Hmm... Like the toad; ugly and venomous',
           'Get thee to a nunnery. Thou needst god',
           '*I scoff in your general direciton*',
           'How did you even get a coconut here? Oh, sorry, that\'s your brain']

    
@grim.event
async def on_ready():
    print('Logged in as...')
    print(grim.user.name)
    print(grim.user.id)
    print('-----')

    
chapter = 1
@grim.event
async def on_message(message):
    global chapter
    if (message.author.id != 425331433805185024):
        
        #To determine random message storage
        if(random.randint(1,100) == 69 and message.content.count('grim') == 0):
            responses.insert(responses[0],message.content)
            if len(responses )== 1000:
                await grim.send_message(message.channel,'boop')
            with open(filename,'wb') as file:
                pickle.dump(responses,file)
    
        chapter
        if chapter == 1:

            #splits text to its different groups
            splitlist = message.content.split(' ')
            for v in splitlist:

                    #was he mentioned
                    if ( v == 'grim'):
                        if message.author.id == '212257792722075650':
                            await grim.send_message(message.channel, 'hi')
                        else:
                            string = insults[random.randint(0,len(insults)-1)]
                            await grim.send_message(message.channel, string)
    
            #did someone try to use his thing
            if message.author.id != '212257792722075650' and message.content.startswith(prefix):
                string = insults[random.randint(0,len(insults)-1)]
                await grim.send_message(message.channel,string)
            else:
            
                #help command
                if message.content.startswith(prefix+'help'):
                    file = open('help1.txt','r')
                    await grim.send_message(message.channel,file.read())
                    file.close()

                #echo command
                elif message.content.startswith(prefix+'echo'):
                    ekko = message.content.replace(prefix+'echo','')
                    await grim.send_message(message.channel,ekko)
                    await grim.delete_message(message)

                #change utility of bot
                elif message.content.startswith(prefix+'chapter'):
                    chapter = splitlist[1]
                    await grim.send_message(message.channel,'Flipping to chapter ' + str(chapter))

        if chapter == 2:
            print('chap 2 recognized')
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
                    await grim.send_message(ctx.channel, 'Do you seriously think someone like you, illiterate, could command a book? How idiotic')
        

                #help command
            elif message.content.startswith(prefix+'help'):
                print('help recognized')
                file = open('help2.txt','r')
                await grim.send_message(message.channel,file.read())
                file.close()

                #change utility of bot
            elif message.content.startswith(prefix+'chapter'):
                chapter = splitlist[1]
                await grim.send_message(message.channel,'Got it. Chapter ' + str(chapter) + ' here we come!')

        if chapter == 3:
            splitlist = message.content.split(' ')
            #gives count of recorded responses
            if message.content.startswith(prefix+'count'):
                await grim.send_message(message.channel, 'There are ' + str(len(responses) - 1) + 'responses kept in my pages')
            #changes utility of bot
            elif message.content.startswith(prefix+'chapter'):
                chapter = splitlist[1]
                await grim.send_message(message.channel,'As you wish... although, I always hated chapter ' + str(chapter))
            #help command
            elif message.content.startswith(prefix+'help'):
                file = open('help3.txt','r')
                await grim.send_message(message.channel,file.read())
                file.close()




grim.run(TOKEN)
