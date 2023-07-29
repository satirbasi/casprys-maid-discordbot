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
        await member.ban(reason=reason, clean_history_duration=delete_message_days)

        embed = disnake.Embed()

        embed.color=disnake.Color.dark_purple()
        embed.title="Banned"
        embed.description=f'i\'ve banned ```{member.name}#{member.discriminator}``` and the reason is: ```{reason}```'
        embed.set_thumbnail(url=member.avatar.url)

        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))