from logging import getLogger; logging = getLogger(__name__)
from discord.ext import commands
from discord import Member
from discord import Embed

#Status changing class


class People(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"{member.mention} has entered Creeper. *SSSSSSS*")
    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"{member.mention} has left Creeper. *BOOM*")
    @commands.command()
    async def whois(self, ctx, member:Member = None):
        if member == None:
            member == ctx.author
            
        name = member.display_name
        pfp = member.display_avatar
        
        dox = Embed(title="Information about User {name}", description="Disclaimer: Creeper is a pro-doxxing server. >:)", colour=Member.accent_color)
        dox.set_author(name=f"{name}", url="https://www.youtube.com/watch?v=cPJUBQd-PNM&ab_channel=CaptainSparklez", icon_url="https://img.icons8.com/bot")
        dox.set_set_thumbnail(url=f"{pfp}")
        dox.add_field(name="Created:", value=member.created_at)
        dox.add_field(name="Joined:", value=member.joined_at,inline=True)
        dox.add_field(name="Status:", value=member.status, inline=False)
        dox.set_footer(text="Icons provided by Icons8")
        
        await ctx.send(embed=dox)