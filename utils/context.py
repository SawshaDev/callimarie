from __future__ import annotations
from copy import deepcopy

import discord
from discord.ext import commands

from typing import TYPE_CHECKING,Union, Any, Optional, cast

from core.bot import CallimarieBot


if TYPE_CHECKING:
    from core.bot import SkyeBot
    from asyncpg import Pool, Connection
    from aiohttp import ClientSession
    
class Context(commands.Context):    
    channel: Union[discord.VoiceChannel, discord.TextChannel, discord.Thread, discord.DMChannel]
    prefix: str
    command: commands.Command[Any, ..., Any]
    bot: SkyeBot

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pool = self.bot.pool
        self._db: Optional[Union[Pool, Connection]]

    def __repr__(self) -> str:
        return '<Context>'

    @property
    def session(self) -> ClientSession:
        return self.bot.session

    @property
    def db(self) -> Union[Pool, Connection]:
        return self._db if self._db else self.pool

    @property
    def bot(self) -> CallimarieBot:
        return cast(CallimarieBot, self.bot)


    async def reply(self,*args, **kwargs):
        if not kwargs.get("mention_author"):
            kwargs["mention_author"] = False
        
        return await super().reply(*args, **kwargs)
