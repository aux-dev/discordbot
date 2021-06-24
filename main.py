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

# !help
@bot.command()
async def help(ctx):
    help=discord.Embed(title="Bot Commands", url="https://github.com/aux-dev/discordbot", color=0xF5F5FF)
    help.add_field(name="Moderation", value="~~`mute`, `kick`, `ban`~~")
    help.add_field(name="Miscellaneous", value="`help`, `invite`")
    help.set_footer(text="v0.0.2 beta")
    
bot.run(TOKEN)
