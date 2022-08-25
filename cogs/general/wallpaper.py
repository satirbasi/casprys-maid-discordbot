import disnake
import requests
from disnake.ext import commands

class Wallpaper(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def wallpaper(self, inter: disnake.ApplicationCommandInteraction):
        """Sends a random wallpaper"""
        r = requests.get("http://api.nekos.fun:8080/api/wallpapers")
        res = r.json()
        embd = disnake.Embed()
        embd.set_image(url=res['image'])
        await inter.response.send_message(embed=embd)


def setup(bot: commands.Bot):
    bot.add_cog(Wallpaper(bot))