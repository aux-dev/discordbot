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

if message.author == client.user:
    return

# BOT COMMANDS
# !test
@client.event
async def on_message(message):
    if message.content.startsWith(prefix + "test"):
        await ctx.send("test")
client.run(TOKEN)