import discord
from .owner import owner

class Owner(owner):
    """Owner Commands"""

async def setup(bot):
    await bot.add_cog(Owner(bot))