import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    server_id =  data["server_id"]
    test_channel_id=["test_channel_id"]
    prefix = data["prefix"]
    owner_id = data["owner_id"]

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.all()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}. Creepybot Online.\n")
    print(discord.__version__)
    channel = bot.get_channel(test_channel_id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
    await channel.send("Creepybot Online.")
bot.run(token)

@bot.command()
async def creeper(ctx):
    await ctx.send(f"Awww man.\nLatency results: *leetcoce{round(bot.latency * 1000)}ms")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension()
    
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension()