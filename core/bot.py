
from __future__ import annotations
from typing import Optional
from logging import getLogger; log = getLogger(__name__)
from core.config import TOKEN, TEST_CHANNEL_ID, CREEPER
import discord
from discord.ext import commands
from discord import app_commands

# ----------------------------------------------------------------- #

__all__ = (
    "Bot",
)

#replace commands.Bot with commands.AutoShardedBot if and when this bot becomes large enough to warrant sharding (~1000+ guilds, unlikely)
#or class Bot(commands.Bot)
class Bot(discord.Client):
    def __init__(self):
        super().__init__(

            command_prefix=".",
            intents=discord.Intents.all(),
            chunk_guild_at_startup=False,  
        )
        self.synced=False  

    async def on_ready(self)-> None:
        await tree.sync(guild=discord.Object(id=CREEPER))
        self.synced=True
        log.info(f"logged in as {self.user}")
        print("Creepybot Online.")
        channel = bot.get_channel(TEST_CHANNEL_ID)
        await channel.send("Creepybot Online.")
        
    async def creeper(self, ctx):
        await ctx.send(f"Awww man.\nLatency results: *{round(self.latency * 1000)}ms")
        
    async def success(self, content: str, interaction: discord.Interaction, ephemerral: Optional[bool]):
        """""Sending success message"""
        pass

    async def error(self, content: str, interaction: discord.Interaction, ephemerral: Optional[bool]):
        """""Sending error message"""
        pass           
    ### Events. These will be organized into cogs eventually.

bot = Bot()
tree = app_commands.CommandTree(bot)

#slash commands
@tree.command(name="Creeper", description="You already know", guild=discord.Object(id=CREEPER))
async def self(interaction:discord.Interaction):
    await interaction.response.send_message(f"Aww Man")

#load cogs  

bot.run(TOKEN)
