import discord
from .info import Info

class Info(Info):
    pass

async def setup(bot) -> None:
    await bot.add_cog(Info(bot))