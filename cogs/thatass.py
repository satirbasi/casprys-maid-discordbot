import disnake
from disnake.ext import commands

class ThatAss(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="thatass")
    async def that_ass(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message("https://cdn.discordapp.com/attachments/985237232539566090/1010434319694712882/unknown.png")

def setup(bot: commands.Bot):
    bot.add_cog(ThatAss(bot))