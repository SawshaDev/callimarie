import traceback
from typing import Optional
import discord
from discord.ext import commands
from core.bot import CallimarieBot

class owner(commands.Cog):
    def __init__(self, bot: CallimarieBot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog: Optional[str]=None):
        if cog is None:
            return await ctx.send("Please specify a cog to reload!")

        try: 
            await self.bot.reload_extension(cog)
            await ctx.send(f":repeat: Succesfully reloaded: ``{cog}``!")
        except Exception as e:
            _traceback = ''.join(traceback.format_tb(e.__traceback__))
            error = '```py\n{1}{0}: {2}\n```'.format(type(e).__name__, _traceback, e)
            return await ctx.send(f"\N{WARNING SIGN} Oh No! there was an error\nError Class: **{e.__class__.__name__}**\n{error}")
