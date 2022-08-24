import disnake
import requests
from disnake.ext import commands

class Feet(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    @commands.is_nsfw()
    async def feet(self, inter: disnake.ApplicationCommandInteraction):
        """Sends a random feet :face_with_raised_eyebrows:"""
        r = requests.get("http://api.nekos.fun:8080/api/feet")
        res = r.json()
        embd = disnake.Embed()
        embd.set_image(url=res['image'])
        await inter.response.send_message(embed=embd)


def setup(bot: commands.Bot):
    bot.add_cog(Feet(bot))