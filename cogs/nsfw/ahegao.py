import disnake
import requests
from disnake.ext import commands

class Ahegao(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    @commands.is_nsfw()
    async def ahegao(self, inter: disnake.ApplicationCommandInteraction):
        """Sends a random ahegao"""
        r = requests.get("http://api.nekos.fun:8080/api/gasm")
        res = r.json()
        embd = disnake.Embed()
        embd.set_image(url=res['image'])
        await inter.response.send_message(embed=embd)


def setup(bot: commands.Bot):
    bot.add_cog(Ahegao(bot))