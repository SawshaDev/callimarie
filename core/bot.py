import logging
import pathlib
import discord
from discord.ext import commands
import aiohttp
import os

LOGGER = logging.getLogger(__name__)

class CallimarieBot(commands.Bot):
    def __init__(
        self,*,
        session: aiohttp.ClientSession, 
    ):
        self.session: aiohttp.ClientSession = session
        os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
        os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 

        super().__init__(command_prefix=">", intents=discord.Intents.all(), activity=discord.Activity(type=discord.ActivityType.playing, name="Revamped and better than ever!"), chunk_guilds_on_startup = False)

    async def on_ready(self):
        for extension in self.cogs:
            LOGGER.info(f" - Loaded cogs.{extension.lower()}")

    async def run(self, token):
        await self.start(token)