import os
import disnake
import requests
import random
from py_dotenv import read_dotenv
from disnake.ext import commands

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
read_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("TOKEN")

intents = disnake.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(intents=intents, reload=True)

@bot.event
async def on_ready():
    print("Ready!!")
        
@bot.listen("on_message")
async def askim_bebeim(message):
    if message.content == "<@1010921624012333197> u good?":
        if message.author.id == 370253988806918155:
            await message.reply("ye")
        else:
            await message.reply(". . .")

@bot.listen("on_message")
async def waifu(message):
    if message.content == "waifu":
        url = 'https://api.waifu.im/search'

        params = {
            'included_tags': [random.choice(['maid', 'waifu', 'selfies', 'uniform', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai'])],
            'height': '>=2000'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if 'images' in data:
                if 'url' in data['images'][0]:
                    await message.reply(data['images'][0]['url'])
            else:
                print('Key "url" not found in data')
        else:
            print('Request failed with status code:', response.status_code)


bot.load_extensions("cogs/")
bot.load_extensions("cogs/events/")
bot.load_extensions("cogs/general/")
bot.load_extensions("cogs/moderation/")
bot.load_extensions("cogs/nsfw/")

bot.run(BOT_TOKEN)