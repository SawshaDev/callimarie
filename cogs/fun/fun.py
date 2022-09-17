from io import BytesIO
import logging
import discord
from discord.ext import commands
from core.bot import CallimarieBot
from utils import Context

logger = logging.getLogger(__name__)

class fun(commands.Cog):
    def __init__(self, bot: CallimarieBot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def emoji(self, ctx):
        pass
        
    @emoji.command()
    @commands.has_permissions(manage_emojis=True)
    async def add(self, ctx: Context, emoji: discord.PartialEmoji):
        emote = await emoji.read()
        
        if not ctx.author.guild_permissions.manage_emojis or not ctx.guild.me.guild_permissions.manage_emojis:
            return await ctx.send("Either i or the author does not have the needed permissions to add this emoji!")
        new = await ctx.guild.create_custom_emoji(name=emoji.name, image=emote)
            
        
        mention = f"<:{new.name}:{new.id}>"
        if new.animated:
            mention =  f"<a:{new.name}:{new.id}>"
        return await ctx.send(f"Succesfully stole **{new.name} {mention}**")
        
    