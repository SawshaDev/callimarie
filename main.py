import discord
from discord import embeds
from discord import client
from discord import colour
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
from discord.ext.commands import has_permissions, MissingPermissions

token= "tokengoeshere"
prefix= ">"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')





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
    embed = discord.Embed(title="Pong :ping_pong:", description = f"My latency is: {round(bot.latency * 1000)}ms", color=0x5d63c0, inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895448744999391267/900777146350456912/duck_-_Copy.png')
    embed.set_footer(text= f'Requested By {ctx.author}', icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed)

@bot.command()
@has_permissions(ban_members=True)
async def ban(message, ban_member:discord.Member,*, reason=None):
    if ban_member == bot.user:
       await message.send(f"You can't ban me :sob:")
    
    elif ban_member.top_role >= message.author.top_role:
        await message.send("this person has a higher role then yourself! :pensive:") 

    else:
        await ban_member.ban(reason=reason)      


@ban.error
async def ban_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send(f"you don't have permission to ban this member :sunglasses:")
 

@bot.command()
@has_permissions(kick_members=True)
async def kick(message, kick_member:discord.Member,*, reason=None):
    if kick_member == bot.user:
       await message.send(f"You can't kick me :sob:")
    
    elif kick_member.top_role >= message.author.top_role:
        await message.send("this person has a higher role then yourself! :pensive:") 

    else:
        await kick_member.kick(reason=reason)      

@kick.error
async def kick_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send( "you don't have permission to kick this member :sunglasses:")


@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   guild = ctx.guild
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
   
   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted {member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands")
    embed.add_field(name="ping", value="Gets the bot latency.", inline=False)
    embed.add_field(name="ban", value="Bans a member.", inline=False)
    embed.add_field(name="kick", value="kicks a member.", inline=False)
    embed.add_field(name="mute", value="mutes member.", inline=False)
    embed.add_field(name="unmute", value="unmutes member", inline=False)
    embed.set_footer(text= f'Help commands.', icon_url = 'https://cdn.discordapp.com/attachments/895448744999391267/900840208579297300/duck.gif ') 
    await ctx.send(embed=embed)    



bot.run(token)
