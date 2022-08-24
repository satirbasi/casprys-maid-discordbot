from lib2to3.pgen2.token import EQUAL
import disnake
from typing import Optional
from disnake.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: Optional[str] = "nothing", delete_message_days: Optional[int] = 0):
        """Bans the given user."""
        if delete_message_days > 7:
            await inter.response.send_message(f"Day is too long max is 7 days")
        await member.ban(reason=reason, delete_message_days=delete_message_days)
        await inter.response.send_message(f'i\'ve banned {member.name}#{member.discriminator} and the reason is "{reason}"')

def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))