import discord
from discord import embeds
from discord import client
from discord.colour import Color
import aiohttp
import datetime
import asyncio
import json
import random
import os
from discord.embeds import Embed
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import has_permissions

token= "TokenGoesHere"
prefix= "!"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="Doin' your mom!!!"))
    print(f"The bot is online")

@bot.event
async def ping(ctx):
    await ctx.send(f":ping_pong: Pong!  {round(bot.latency*1000)}ms latency")


@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(899893382120366091)
    print(f"{member} has Joined")
    await welcome_channel.send(f"{member.mention} has joined the server")

@bot.event 
async def on_member_remove(member):
    print(f"{member} has left...")  
    welcome_channel = bot.get_channel(899893382120366091)
    await welcome_channel.send(f"{member.mention} has left the server")


@bot.command()
async def embed(ctx, ch:discord.TextChannel):
    a_color = discord.Colour.blue()
    myembed = discord.Embed(title="Rules for callimarie's basement", color = a_color).set_author(name="callimarie")
    myembed.add_field(name="Rules:", value="This is an anarchy server, so the only one is,", inline=False)
    myembed.add_field(name="rule 1", value="Dont Break tos.", inline=False)
    myembed.set_footer(text="Callimarie's basement")
    
    await ch.send(embed=myembed)   

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong :ping_pong:", description = f"My latency is: {round(bot.latency * 1000)}ms", color=0x10b9b1, inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895448744999391267/900777146350456912/duck_-_Copy.png')
    embed.set_footer(text= f'Requested By   {ctx.author}', icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed)



bot.run(token)
