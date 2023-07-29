import disnake
from disnake.ext import commands

class ServerIcon(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def servericon(self, inter: disnake.ApplicationCommandInteraction):
        """Get that juicy profile picture of a server"""
        embed1 = disnake.Embed()
        embed1.set_image(inter.guild.icon.url)
        await inter.response.send_message(embed=embed1)

def setup(bot: commands.Bot):
    bot.add_cog(ServerIcon(bot))