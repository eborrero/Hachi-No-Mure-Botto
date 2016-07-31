import discord
from discord.ext import commands
import random
import asyncio

client = discord.Client()


#THIS IS FROM THE MEMBER JOIN EXAMPLE
#This is an automatically triggered message welcoming a new new member join
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



#THIS IS FROM THE GUESSING GAME EXAMPLE
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')

    if message.content.startswith('$guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')


    if message.content.startswith('?help'):
        await client.send_message(message.channel, '__***HELP MENU***__'
                                             '\n**NOTE:** Currently, all commands ARE CASE SENSITIVE. will fix later.'
                                             '\nThis is the command list currently supported:'
                                             '\n**?help**: Brings this back'
                                             '\n**!overwatch**: Information on Overwatch commands')


    if message.content.startswith('!overwatch'):
        await client.send_message(message.channel, '__***OVERWATCH COMMANDS***__'
                                             '\nTo learn more about a character, type ?[characters name]'
                                             '\nBelow is a list of the current characters in Overwatch:'
                                             '\n__**Offensive Heroes**__'
                                             '\n'
                                             '\n__**Defensive Heroes**__'
                                             '\n**?Bastion**'
                                             '\n_**Tank Heroes**__'
                                             '\n__**Support Heroes**__'
                                             '\n')

    if message.content.startswith('?Bastion'):
        await client.send_message(message.channel, '__***BASTION***__'
                                             '\nBastion is a powerful turret. However, due to immobility, can be countered by long ranged heroes and flankers. Pair him with a shield for the best results.'
                                             '\nBasion is best played on defense. He can be effective on attack, but only when positioned well with a good team.'
                                             '\n__**E-Key Ability:**__ Self-Repair: Cannot move or firing while repairing, but can be used at any time'
                                             '\n__**Shift Ability:**__ Reconfigure: Changes into a non-moving turret. Takes ~2 seconds to do.'
                                             '\n__**Ultimate:**__ Configuration Tank: Turns into a tank firing cannon shells that do huge damage. Extra health is gained. Form only lasts for a bit.'
                                             '\n__**Effective Against:**__ Reaper, Mercy, Lucio, D.Va, Winston'
                                             '\n__**Countered By:**__ Widowmaker, Hanzo, Pharah, Tracer, Junkrat, Genji')

    if message.content.startswith('?D.Va'):
        await client.send_message(message.channel, '__***D.VA***__'
                                             '\nD.Va is an offensive tank specialized in assualtin the enemy team on the objective.'
                                             '\nD.Va is best played on attack and has very little in terms of defensive abilities. Should always be paired with another tank.'
                                             '\n__**E-Key Ability:**__ '
                                             '\n__**Shift Ability:**__ '
                                             '\n__**Ultimate:**__ '
                                             '\n__**Get Up Close To:**__ Widowmaker, Hanzo, Torbjorn, Soldier 76'
                                             '\n__**Countered By:**__ Junkrat, Roadhog, Zarya, Zenyatta, Mei')





        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


#An attempt at a poll

#for i in input:
#options[i] = 0
#direct messaging is just like. function changes
#with options being a dictionary
#{'maybe': 0, 'yes': 0, 'no': 0}
#and then whenever you get a response
#you just do
#options[response] += 1
#you could do custom answers that way too
#because if response isn't in the dictionary, it'll just add it


#THIS IS FROM THE BASIC BOT EXAMPLE
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Trigger command that adds two numbers. I'm not sure how to trigger the commands yet
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

#Command that rolls a die
@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

#Command that picks a random choice when given choices...useful for random choice
@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

#Command that repeats a message a certain amount of times...useful for for loop
@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

#Command that announces when a member joins
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

#This is a command that is a check for subcommands
@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')


#User Information goes here for login: client.run('email','password')
client.run('','')
