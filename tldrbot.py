import os

import discord
from discord import app_commands
from discord.utils import find


# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # Need this for slash commands.
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to the my own test server only.
        MY_GUILD = discord.Object(id=os.environ["DEV_GUILD_ID"])
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


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
    user_id = interaction.user.id

    if not isinstance(channel, discord.TextChannel):
        await interaction.response.send_message("Unsupported channel type")
        return

    messages = channel.history(limit=None)
    last_message = await find(lambda m: m.author.id == user_id, messages)

    if last_message is None:
        await interaction.response.send_message("No message found")
        return

    # AI Prompt

    # Reply

    await interaction.response.send_message(
        f"Your last message was:\n>>> {last_message.content}"
    )


client.run(os.environ["TOKEN"])
