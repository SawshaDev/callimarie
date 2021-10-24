from collections import UserList
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

token= "token"
prefix= ">"



bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="fuck you, cry"))
    print(f"The bot is online")


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
@has_permissions(kick_members=True)
async def kick(ctx, user:discord.Member,*, reason=None):
        await user.kick(reason=reason) 
        kick = discord.Embed(title=f'Kicked: {user.mention} for {reason}')
    
        if user == bot.user:
          await ctx.send(f"You can't kick me :sob:")
        
        elif user.top_role >= ctx.author.top_role:
            await ctx.send("this person has a higher role then yourself! :pensive:") 
        
        else:
            await user.kick(reason=reason)  
            await ctx.channel.send(embed=kick)
            await user.send(embed=kick)   
        

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send( "you don't have permission to kick this member :sunglasses:")


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
   embed = discord.Embed(title="unmuted", description=f" unmuted {member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands")
    embed.add_field(name="Ping", value="Gets the bot latency.", inline=False)
    embed.add_field(name="Ban", value="Bans a member.", inline=False)
    embed.add_field(name="Kick", value="kicks a member.", inline=False)
    embed.add_field(name="Mute", value="mutes member.", inline=False)
    embed.add_field(name="Unmute", value="unmutes member", inline=False)
    embed.add_field(name="Purge", value="Purges specified amount of messages", inline=False)
    embed.set_footer(text= f'Requested by {ctx.author}', icon_url = 'https://cdn.discordapp.com/attachments/895448744999391267/900840208579297300/duck.gif') 
    await ctx.send(embed=embed)    

@bot.command()
async def pinghelp(ctx):
    embed=discord.Embed(Title="Ping Usage")
    embed.add_field(name="Usage of ping", value=">ping", inline=False) 
    await ctx.send(embed=embed)


@bot.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")


@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f"succesfully banned {user.name} from this server", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'Cleared {limit} Messages')
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

bot.run(token)
