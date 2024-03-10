# imports

import discord
from discord.ext import commands
from cogs.DailyVerse import DailyVerse
from cogs.env_vars import API_KEY

def Main():

    # Sets the bots commands to look at "."

    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())



    # logs when the bot is ready

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
    # Command that runs the bible versus

    """ @bot.command()
    async def pray(ctx):
        await ctx.send(':pray:')
        await ctx.send(DailyVerse()) """
    
    # Sync command to force the "/" commands 

    @bot.command()
    @commands.is_owner()
    async def sync(ctx: commands.Context):
        try:
            fmt = await bot.tree.sync()
            print(f"Sync'd {len(fmt)} commands to the current server")
        except discord.Forbidden:
            await ctx.send("Unexpected forbidden from application scope.")

    # Slash command for random verse

    @bot.tree.command(name="random", description="A random verse from the Bible (ESV).")
    @commands.has_permissions(administrator=True)
    async def slash_command(interaction:discord.Interaction):
        await interaction.response.send_message(':pray: ' + DailyVerse())

    # run command

    bot.run(API_KEY)

if __name__ == "__main__":

    Main()