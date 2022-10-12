import disnake
from disnake.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = disnake.Embed()

            embed.color=disnake.Color.dark_purple()
            embed.title="Welcome to the server!"
            embed.description=f'There is only 1 rule and that is **rule 263**'
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="That aside always have some common sense or you'll get your ass cheeks clapped.")

            await channel.send(embed=embed)
            await member.add_roles(member.guild.get_role(845949403024982047), member.guild.get_role(927221688603643924), member.guild.get_role(927221571590971403))

def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))