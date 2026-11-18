"""Relays Twitch chat into a Discord channel.

Settings come from environment variables (see .env.example):
  DISCORD_TOKEN        Discord bot token
  DISCORD_CHANNEL_ID   Discord channel to post into
  TWITCH_TOKEN         Twitch chat OAuth token
  TWITCH_CHANNELS      Twitch channels to read, comma-separated
"""
import asyncio
import os

import discord
from twitchio.ext import commands


def env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"missing environment variable {name}")
    return value


class Relay(commands.Bot):
    """Twitch bot that forwards every chat message to one Discord channel."""

    def __init__(self, discord_client, channel_id, token, channels):
        super().__init__(token=token, prefix="?", initial_channels=channels)
        self.discord = discord_client
        self.channel_id = channel_id

    async def event_ready(self):
        print(f"Twitch: logged in as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        channel = self.discord.get_channel(self.channel_id)
        if channel is not None:
            # Twitch chat must not be able to ping @everyone or roles.
            await channel.send(
                f"pjoc or bjoc: {message.content}",
                allowed_mentions=discord.AllowedMentions.none(),
            )
        await self.handle_commands(message)


async def main():
    client = discord.Client(intents=discord.Intents.default())
    channels = [c.strip() for c in env("TWITCH_CHANNELS").split(",") if c.strip()]
    relay = Relay(client, int(env("DISCORD_CHANNEL_ID")), env("TWITCH_TOKEN"), channels)

    @client.event
    async def on_ready():
        print(f"Discord: logged in as {client.user}")

    async with client:
        await asyncio.gather(client.start(env("DISCORD_TOKEN")), relay.start())


if __name__ == "__main__":
    asyncio.run(main())
