from dis import dis
from operator import truediv
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

# @bot.listen("on_message")
# async def whatever_you_want_to_call_it(message):
#     print(message.content)

bot.load_extensions("cogs/")
bot.run(BOT_TOKEN)