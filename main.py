import discord
import self as self
from twitchio.ext import commands
import threading
import asyncio
import datetime

client = discord.Client()
global discord_message
global twitch_message
global posted_message
posted_message = "not_test"
twitch_message = "test"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # await test_function()
    await twitch_to_discord()
    await asyncio.sleep(1)


@client.event
async def on_message(message):
    # string = ""
    import twitch_client
    global discord_message
    a = True;
    if message.author == client.user:
        discord_message = message.content
        return

    if a:
        discord_message = message.content


#  print(discord_message)
# print(twitch_client.twitch_message)
# return discord_message

# twitch.bot(commands.bot)
# TWITCH CLIENT V


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='o15e3ka0oovmbs4iaehr4rumgghcv0', prefix='?',
                         initial_channels=['pokegaard', 'reckful', 'bjoc_bot'])

    async def test_function(self):
        print("hello")
        await self.client.wait_until_ready()
        print("hello")
        channel = client.get_channel(895284133520097314)
        await channel.send('hello')

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # returns the twitch message in a variable
    async def event_message(self, message):
        global twitch_message

        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        # print(discord_message)

        # Print the contents of our message to console...
        twitch_message = message.content
        print(twitch_message)
        # print(main.on_message(main.message_content))

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)
        return twitch_message


async def twitch_to_discord():
    print("hello")
    bot = Bot()
    time = datetime.datetime.now
    global posted_message
    global twitch_message
    channel = client.get_channel(1004070964105056338)  # replace with channel ID that you want to send to
    msg_sent = False
    while not msg_sent:
        while posted_message != twitch_message:
            print("hello")
            if True:
                await channel.send("pjoc or bjoc: " + twitch_message)
                twitch_message = posted_message
                print(posted_message + "posted \n")
                print(twitch_message + "twitch \n")
                await twitch_to_discord()
    else:
        msg_sent = True
    await asyncio.sleep(1)


def thread_function(name):
    asyncio.set_event_loop(asyncio.new_event_loop())
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    # x.join()
    client.run('ODk1MjcwMzEyOTczODI4MTE2.YV2Hcw.7LzNgqs7GEgjcyiWsNHus0M0dBA')
