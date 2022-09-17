from __future__ import annotations
import logging
import os
from typing import TYPE_CHECKING
from core.bot import CallimarieBot
from config import token
import asyncio
import discord
import pathlib 
import aiohttp
from utils.context import Context

LOGGER = logging.getLogger(__name__)

discord.utils.setup_logging()

async def main():
    async with aiohttp.ClientSession() as session, CallimarieBot(session=session) as bot:

        await bot.load_extension("jishaku")
        exts = [
            f"cogs.{ext if not ext.endswith('.py') else ext[:-3]}"
            for ext in os.listdir("cogs")
            if not ext.startswith("_")
        ]
        for ext in exts:
            await bot.load_extension(ext)
    
        await bot.run(token)

asyncio.run(main())