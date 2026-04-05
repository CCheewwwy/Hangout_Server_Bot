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



@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author.bot:
        return

    # Check if the bot was pinged AND the message contains "prefix" (case-insensitive)
    if bot.user in message.mentions and message.content.lower().strip().endswith("prefix"):
        embed = discord.Embed(
            title="Bot Prefix",
            description='The prefix is "."',
            color=discord.Color.blue()
        )
        await message.channel.send(embed=embed)

    # Allow commands to still work
    await bot.process_commands(message)

## ======================

bot.run(token)
