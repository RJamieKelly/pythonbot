import discord
from twitchio.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # string = ""

    global message_content
    if message.author == client.user:
        message_content = message.content
        return

    if message.content is not None:
        message_content = message.content

    await message.channel.send(message_content)
    print(message_content)
    return message_content

# twitch.bot(commands.bot)
