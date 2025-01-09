import os

import discord
from discord import app_commands


# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # Need this for slash commands.
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        if dev_guild_id := os.environ.get("DEV_GUILD_ID"):
            dev_guild = discord.Object(id=dev_guild_id)

            # This copies the global commands over the test servers only
            self.tree.copy_global_to(guild=dev_guild)
            await self.tree.sync(guild=dev_guild)
        else:
            await self.tree.sync()


intents = discord.Intents.default()
client = Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.tree.command()
async def tldr(interaction: discord.Interaction):
    """Summarize all messages in this channel since your last message."""

    # Fetch messages

    channel = interaction.channel

    if not isinstance(channel, discord.TextChannel):
        await interaction.response.send_message("Unsupported channel type")
        return

    history = channel.history(limit=None)
    to_summarize: list[discord.Message] = []

    async for message in history:
        if message.author.id == interaction.user.id:
            break
        to_summarize.insert(0, message)

    # AI Prompt

    # Reply

    await interaction.response.send_message(
        f"Generating TL;DR for {len(to_summarize)} messages..."
    )


client.run(os.environ["TOKEN"])
