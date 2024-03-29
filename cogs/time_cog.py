from logging import getLogger; logging = getLogger(__name__)
from discord.ext import commands, tasks
import datetime
from datetime import timedelta
from dataclasses import dataclass

from core.config import TEST_CHANNEL_ID
MAX_SESSION_TIME_MINUTES = 45

@dataclass
class Timer():
    is_active: bool = False
    start_time: int = 0

class TimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.on_message_send(bot)
        session = self.bot.get_cog('Timer')
    
    @tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
    async def break_reminder(self, ctx):
        
        if self.break_reminder.current_loop == 0:
            return
        
        channel = ctx.get_channel(TEST_CHANNEL_ID)
        await channel.send(f"***BREAK TIME***!\n You've been studying for {MAX_SESSION_TIME_MINUTES} minutes. Go touch grass.")

    
    @commands.command
    async def start(self, ctx):
        if self.session.is_active:
            await ctx.send("Session is already active! I can't multitask, but you're more than welcome to. :)")
            return

        self.session.is_active = True
        self.session.start_time = ctx.message.created_at.timestamp()
        human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
        self.break_reminder.start()
        await ctx.send(f"Study session started at {human_readable_time}!\nHave fun. (or don't idfk)")

    async def end(self, ctx):
        if not self.session.is_active:
            await ctx.send("No session is active!")
            return
        
        self.session.is_active = False
        end_time = ctx.message.created_at.timestamp()
        duration = end_time - self.session.start_time
        self.break_reminder.stop()
        human_readable_duration = str(datetime.timedelta(seconds=duration)).split(".")[0]
        await ctx.send(f"Session ended after {human_readable_duration}.")

def setup(bot):
    bot.add_cog(TimeCog(bot))