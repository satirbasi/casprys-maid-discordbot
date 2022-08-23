import disnake
from disnake.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome to the server {member.mention}")

def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))