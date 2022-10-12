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

        embed = disnake.Embed()

        embed.color=disnake.Color.dark_purple()
        embed.title="Banned"
        embed.description=f'i\'ve banned ```{member.name}#{member.discriminator}``` and the reason is: ```{reason}```'
        embed.set_thumbnail(url=member.avatar.url)

        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Kick(bot))