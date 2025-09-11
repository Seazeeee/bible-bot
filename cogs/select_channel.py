import json
import discord
from discord import app_commands
from discord.ext import commands


class select_channel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def json_reader(self, path: str):
        pass

    def json_writer(self, path: str):
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        print("Select_Channel cog Loaded!")

    # Autocomplete function
    async def autofill_channel_choices(
        self, interaction: discord.Interaction, current: str
    ):
        if not interaction.guild:
            return []

        return [
            app_commands.Choice(name=channel.name, value=str(channel.id))
            for channel in interaction.guild.text_channels
            if current.lower() in channel.name.lower()
        ][
            :25
        ]  # Limit to 25 suggestions

    # Slash command
    @app_commands.command(
        name="select_channel", description="Set the Channel for the Daily Verse."
    )
    @app_commands.autocomplete(channel=autofill_channel_choices)
    async def select_channel(self, interaction: discord.Interaction, channel: str):
        if not await self.bot.is_owner(interaction.user):
            await interaction.response.send_message(
                "You are not the owner of this bot.", ephemeral=True
            )
            return
        else:
            await interaction.response.send_message(f"You selected <#{channel}>")


# Setup function for loading the cog
async def setup(bot):
    await bot.add_cog(select_channel(bot))
