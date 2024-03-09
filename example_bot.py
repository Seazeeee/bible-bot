# imports

import discord
from discord.ext import commands
from cogs.DailyVerse import DailyVerse
from cogs.env_vars import API_KEY, GUILD_ID

# Sets the bots commands to look at /

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())



# logs when the bot is ready

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command that runs the bible versus

@bot.command()
@commands.has_permissions(administrator=True)
async def pray(ctx):
    await ctx.send(':pray:')
    await ctx.send(DailyVerse())

# run command

bot.run(API_KEY)