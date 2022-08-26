from twitchio.ext import commands
import threading
import asyncio
import discord
import main


# main.on_message()
class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='o15e3ka0oovmbs4iaehr4rumgghcv0', prefix='?', initial_channels=['bjoc_bot'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        print(main.message_content)

        # Print the contents of our message to console...
        print(message.content)
        print(main.on_message(main.message_content))

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')


def thread_function(name):
    asyncio.set_event_loop(asyncio.new_event_loop())
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    #x.join()
    main.client.run('ODk1MjcwMzEyOTczODI4MTE2.YV2Hcw.7LzNgqs7GEgjcyiWsNHus0M0dBA')

