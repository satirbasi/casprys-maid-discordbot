import os
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = commands.Bot()

@bot.event
async def on_ready():
    print("Ready!!")
    
bot.load_extension("cogs.ping")

bot.run(BOT_TOKEN)