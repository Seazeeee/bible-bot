# imports

import discord
from discord.ext import commands
from cogs.DailyVerse import DailyVerse
from cogs.specificVerse import specificVerse
from cogs.env_vars import API_KEY
from typing import Optional

def Main():

    # Sets the bots commands to look at "."

    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())



    # logs when the bot is ready

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
    

    # Sync command to sync "/" commands
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

    @bot.tree.command(name="verse", description="A specified verse.")
    @commands.has_permissions(administrator=True)
    async def slash_command(interaction:discord.Interaction, book:str, chapter:int, verse:int, translation: Optional[str]):
        await interaction.response.send_message(':pray: ' + specificVerse(book, chapter, verse, translation).pullVerse())

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise await bot.interaction.response.send_message(f"only you, {bot.interaction.user}, can see this! Something went wrong with your command, please try again and verify the information", ephemeral=True)

    # run command

    bot.run(API_KEY)

if __name__ == "__main__":

    Main()