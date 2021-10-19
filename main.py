import discord
from discord.ext import commands

token= "Token"
prefix= "Prefix"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Looking over callimaries basement'))
    print("The bot is online")


@bot.command()
async def embed(ctx, ch:discord.TextChannel):
    a_color = discord.Colour.blue()
    myembed = discord.Embed(title="Rules for callimarie's basement", color = a_color).set_author(name="callimarie")
    myembed.add_field(name="Rules:", value="This is an anarchy server, so the only one is,", inline=False)
    myembed.add_field(name="rule 1", value="Dont Break tos.", inline=False)
    myembed.set_footer(text="Callimarie's basement")
    
    await ch.send(embed=myembed)   


bot.run(token)
