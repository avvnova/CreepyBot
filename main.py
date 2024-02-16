from __future__ import annotations
import asyncio, discord
from core import Bot
from core.config import TOKEN
import os

async def load(b: Bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await b.load_extension(f'cogs.{filename[:-3]}')    

async def main():
    discord.utils.setup_logging()
    async with Bot() as bot:
        await load(bot)
        await bot.start(TOKEN, reconnect=True)
        

if __name__ == 'main__':
    asyncio.run(main())