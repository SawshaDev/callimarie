from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from core.bot import callimarie
from config import token
import asyncio
import discord
import pathlib 

LOGGER = logging.getLogger(__name__)

discord.utils.setup_logging()

async def main():
    async with callimarie() as bot:
        await bot.load_extension("jishaku")
        for file in sorted(pathlib.Path("cogs").glob("**/[!_]*.py")):
            ext = ".".join(file.parts).removesuffix(".py")
            try:
                await bot.load_extension(ext)
            except Exception as error:
                LOGGER.exception("Failed to load extension: %s\n\n%s", ext, error)
        await bot.run(token)

asyncio.run(main())