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
        await message.reply("evet aşkımm ❤")

bot.load_extensions("cogs/")
bot.load_extensions("cogs/nsfw/")
bot.run(BOT_TOKEN)