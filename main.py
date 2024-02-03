from __future__ import annotations
import asyncio, discord
from core import Bot
from core.config import TOKEN

async def main():
    discord.utils.setup_logging()
    async with Bot() as bot:
        await bot.start(TOKEN, reconnect=True)
        

if __name__ == 'main__':
    asyncio.run(main())