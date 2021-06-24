import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot('!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# BOT COMMANDS
# !test
@bot.command()
async def test(ctx):
    await ctx.send("test")
    
bot.run("TOKEN")
