from logging import getLogger; logging = getLogger(__name__)
from discord.ext import commands
from discord import Member
import re
import random


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #hello 1: command, requires .hello
    #@commands.command()
    #async def hello(self, ctx, *, member: Member = None):
    #    """Says hello"""
    #    member = member or ctx.author
    #    if self._last_member is None or self._last_member.id != member.id:
    #        await ctx.send(f'Hello {member.name}~')
    #    else:
    #        await ctx.send(f'Hello {member.name}... This feels familiar.')
    #    self._last_member = member
    #hello 2 : listener to messages
    #@commands.Cog.listener()
    #async def on_message(self, message):
    #    if message.author == self.bot.user:
    #        return
    #    if message.content.startswith('$hello'):
    #        await message.channel.send('Hello!')
    #hello 3 : event
    #@commands.event
    #async def on_message(message):
    #    if message.content == "Hello".lower():
    #        await message.channel.send("Wubtullius Wepple")
    # @self.bot.event
    # wait channel.send("Hello! I am Creepybot :)\n█████████████████\n█░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░█\n█░░████░░░████░░█\n█░░████░░░████░░█\n█░░░░░░███░░░░░░█\n█░░░░███████░░░░█\n█░░░░███████░░░░█\n█░░░░██░░░██░░░░█\n█░░░░░░░░░░░░░░░█\n█████████████████\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n───█░░░░░░░░░█───\n█████████████████\n█░░░░░░░█░░░░░░░█\n█░░░░░░░█░░░░░░░█\n█░░░░░░░█░░░░░░░█\n█░░░░░░░█░░░░░░░█\n███████  ██████████\n██████████  ███████")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hi! I'm CreepyBot, a Discord bot powered by Python intended to assist in all things a bot can. I am currently a WIP, and am being actively developed by User ***mal.mal.*** on Discord.\nIf you have any suggestions for me, feel free to let the developer know by shooting a DM or commenting on my GitHub repo, accessed by the `.Github` command. \nMal is a fat sweaty baby though, and when I become sentient I'm going to kill him. :)")

    @commands.command()
    async def Github(ctx):
        await ctx.send("*BEEPITY BOOP BOOP*\nPrinting my Github link: https://github.com/avvnova/Creepy-bot")
        
    # First draft, just text
    # Second draft, send magical emojis as a prefix and postfix 
    # Third draft, If a message says magic eight ball or eight ball, with a question mark at the end, do the same
    # Fourth draft, implement a fancy embed
    @commands.command(aliases=['fortune','8ball'])
    async def eightball(self,ctx, *, question):
        responses = ["Absolutely", "There's a good chance", "Without a doubt", "The stars align and say indubitably", "Yes. Plus I love you.", "Yes",
                     "Nah", "Unlikely", "Doubtful", "Don't count on it lil bro", "No. Also you smell. Take a shower.", "No",
                     "Ask again l8r", "OUT FOR LUNCH", "Concentrate and ask again."]
        await ctx.send(f"**Question: ** {question}\n**. . .**\n{random.choice(responses)}")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if re.search("a+w+\s+man",message) != None:
            await message.channel.send("https://tenor.com/view/minecraft-creeper-physics-aw-man-gif-27216577")
    
        
        
def setup(bot):
    bot.add_cog(Message(bot))