import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
        """Deletes the amount of messages you give"""
        await inter.channel.purge(limit=amount)
        await inter.response.send_message(f"Deleted {amount} messages!", ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))