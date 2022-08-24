import disnake
import requests
from disnake.ext import commands

class Fourk(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="4k")
    @commands.is_nsfw()
    async def fourk(self, inter: disnake.ApplicationCommandInteraction):
        """Sends a random 4k real life shit"""
        r = requests.get("http://api.nekos.fun:8080/api/4k")
        res = r.json()
        embd = disnake.Embed()
        embd.set_image(url=res['image'])
        await inter.response.send_message(embed=embd)


def setup(bot: commands.Bot):
    bot.add_cog(Fourk(bot))