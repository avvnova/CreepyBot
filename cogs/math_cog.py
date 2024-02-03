from logging import getLogger; logging = getLogger(__name__)
from discord.ext import commands
import math

class Math(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def add(ctx, *arr):
        result = 0
        for i in arr:
            result += int(i)
        await ctx.send(f"*BEEP BOOP*\nThe Creepy Calculator says the result is ...\n{result}")
        
def setup(bot):
    bot.add_cog(Math(bot))