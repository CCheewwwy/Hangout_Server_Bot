import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents, case_insensitive=True)

## ======================

@bot.command()
async def hi(ctx):
    await ctx.reply("Hello, and welcome to Hangout Server!")


## ======================

bot.run(token)
