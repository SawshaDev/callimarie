import textwrap
import typing
import discord
from discord.ext import commands
from core.bot import CallimarieBot
from utils.context import Context

class InfoSelect(discord.ui.Select):
    def __init__(self, og_embed: typing.Optional[discord.Embed]=None):
        self.og_embed = og_embed
        options = [
            discord.SelectOption(label="Info", description="Server Info"),
            discord.SelectOption(label="a")
        ]

        super().__init__(options=options, min_values=1, max_values=1)

    async def callback(self, itr: discord.Interaction):
        await itr.response.defer()

        if self.values[0] == "Info":
            if self.og_embed:
                return await itr.message.edit(embed=self.og_embed)

        if self.values[0] == 'a':
            return await itr.followup.send(f"{itr.guild}")



class InfoView(discord.ui.View):
    def __init__(self, embed):
        super().__init__(timeout=None)
        self.add_item(InfoSelect(embed))

class Info(commands.Cog):
    def __init__(self, bot: CallimarieBot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx: Context):
        embed = discord.Embed(title=f"Info about {ctx.guild.name}")
        await ctx.send(embed=embed,view=InfoView(embed))
