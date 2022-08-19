import discord
from discord.ext import commands
from config import token

class Callimarie(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=">", intents=discord.Intents.all())

        
    async def run(self):
        await self.start(token)