import os
import disnake
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
    await bot.change_presence(status=disnake.Status.offline)
    print("Ready!!")
        
@bot.listen("on_message")
async def askim_bebeim(message):
    if message.content == "<@1010921624012333197> u good?":
        if message.author.id == 370253988806918155:
            await message.reply("ye")
        else:
            await message.reply(". . .")

@bot.listen("on_message")
async def shutit(message):
    if message.content == "<@1010921624012333197> shut it.":
        if message.author.id == 370253988806918155:
            os.system("shutdown /s /t 1")
        else:
            await message.reply("no shut it for u >:|")

@bot.listen("on_message")
async def send_screeny(message):
    if message.content == "<@1010921624012333197> send screeny.":
        if message.author.id == 370253988806918155:
            os.popen(r'nircmd.exe savescreenshot "C:\Users\Caspry\Desktop\disc-bot\screen.png"')
            await message.reply(file=disnake.File("./screen.png"))
        else:
            os.popen(r'nircmd.exe savescreenshot "C:\Users\Caspry\Desktop\disc-bot\screen.png"')
            await message.reply(file=disnake.File("./screen.png")) 

bot.load_extensions("cogs/")
bot.load_extensions("cogs/events/")
bot.load_extensions("cogs/general/")
bot.load_extensions("cogs/moderation/")
bot.load_extensions("cogs/nsfw/")

bot.run(BOT_TOKEN)