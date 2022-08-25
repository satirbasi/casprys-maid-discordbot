import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]

intents = disnake.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Ready!!")
        
@bot.listen("on_message")
async def askim_bebeim(message):
    if message.content == "<@1010921624012333197> dimi":
        if message.author.id == 370253988806918155:
            await message.reply("evet aşkımm ❤")
        else:
            await message.reply("nahhh man stfu 💀💀💀")

bot.load_extensions("cogs/")
bot.load_extensions("cogs/events/")
bot.load_extensions("cogs/general/")
bot.load_extensions("cogs/moderation/")
bot.load_extensions("cogs/nsfw/")

bot.run(BOT_TOKEN)