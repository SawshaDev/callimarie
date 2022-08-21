import discord
from .fun import fun

class Fun(fun):
    """Everything fun!"""


async def setup(bot):
    await bot.add_cog(Fun(bot))