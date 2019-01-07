import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random

    #Token to log in to bot
TOKEN = 'NDI1MzMxNDMzODA1MTg1MDI0.Dp1y8Q.EI17fEk53nP_4ThPBv8ibiIsqRA'

    #Setting up for commands
prefix = '.'
grim = commands.Bot(command_prefix = prefix)

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
    for v in splitlist:
            if ( v == 'grim'):
                if message.author.id == '212257792722075650':
                    await grim.send_message(message.channel, 'hi')
                else:
                    string = insults[random.randint(0,len(insults)-1)]
                    await grim.send_message(message.channel, string)
                    
    if message.author.id != '212257792722075650' and message.content.startswith(prefix):
        string = insults[random.randint(0,len(insults)-1)]
        await grim.send_message(message.channel,string)
    else:
        
        if message.content.startswith(prefix+'help'):
            await grim.send_message(message.channel,'just read my pages master, they tell all they need to know')

        if (message.content=='Zad, koga naj-riuk drepa'):
            await grim.send_message(message.channel,'*My pages spring open, leaving through, with a ghastly smoke rising. A wolf\'s head is shaped for my body and I lunge at the rope. It is cut between my jaws. I spare the Marquis from his fate* Jiak okja zot-kri' )
            await grim.delete_message(message)

        if message.content.startswith(prefix+'echo'):
            ekko = message.content.replace(prefix+'echo','')
            await grim.send_message(message.channel,ekko)
            await grim.delete_message(message)

grim.run(TOKEN)
