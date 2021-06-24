import os
import json
import discord
import dotenv
from dotenv import load_dotenv
from discord import commands
from discord import get_prefix

# Prefix
client = commands.Bot(
    command_prefix=(get_prefix),
    )
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# BOT COMMANDS
# !test
@client.command
async def test(message):
    await message.send("test")


client.run(TOKEN)
