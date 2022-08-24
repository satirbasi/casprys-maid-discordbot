import disnake
from typing import Optional
from disnake.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: Optional[str] = "nothing"):
        """Kicks the given user."""
        await member.kick(reason=reason)
        await inter.response.send_message(f'i\'ve kicked {member.name}#{member.discriminator} and the reason is "{reason}"')

def setup(bot: commands.Bot):
    bot.add_cog(Kick(bot))