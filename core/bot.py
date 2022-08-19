import logging
import pathlib
import discord
from discord.ext import commands

LOGGER = logging.getLogger(__name__)

class callimarie(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=">", intents=discord.Intents.all(), activity=discord.Activity(type=discord.ActivityType.playing, name="Revamped and better than ever!"))

    async def on_ready(self):
        for extension in self.cogs:
            LOGGER.info(f" - Loaded cogs.{extension.lower()}")

    async def run(self, token):
        await self.start(token)