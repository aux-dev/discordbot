import os

import discord
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# BOT COMMANDS
# !test
@bot.command
async def test(message):
        await message.send("test")


client.run(TOKEN)
