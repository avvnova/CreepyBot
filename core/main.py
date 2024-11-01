
# ----------------------------------------------------------------- #
discord.utils.setup_logging()
TOKEN = os.environ['token']
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready() -> None:
    #await tree.sync(guild=discord.Object(id=CREEPER))
    bot.synced=True
    log.info(f"logged in as {bot.user}")
    print("Creepybot Online.")
    channel = bot.get_channel(TEST_CHANNEL_ID)
    await channel.send("Creepybot Online.")

@bot.command()
async def setup_hook(ctx) -> None:
    #cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}\cogs"
    for filename in os.listdir('./cogs'):
        print(f"Loading " + filename + ". . .")
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")    
    await bot.tree.sync()
    print("Cogs Loaded")

@bot.command()
async def creeper(ctx):
    await ctx.send(f"Awww man.\nLatency results: *leetcoce{round(bot.latency * 1000)}ms")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension()
    
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension()
#tree = discord.app_commands.CommandTree(bot)



#slash commands
#@tree.command(name="creeper", description="You already know", guild=discord.Object(id=CREEPER))
#async def bot(interaction:discord.Interaction):
#await interaction.response.send_message(f"Aww Man")