import json
import discord
import os
from .env_vars import JSON_PATH
from discord import app_commands
from discord.ext import commands


class select_channel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def json_writer(self, path: str, data: dict):
        # Validate input
        if "guild_id" not in data or "channel_id" not in data or "name" not in data:
            print("[json_writer] Invalid data format passed. Skipping write.")
            return

        read_data = self.json_reader(path)

        guild_id = str(data["guild_id"])

        # Update or insert the new data for this guild
        read_data[guild_id] = {
            "name": data["name"],
            "channel_id": data["channel_id"]
        }

        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(read_data, json_file, indent=4)

    def json_reader(self, path: str):
        # Check file
        if not os.path.exists(path):
            self.write_json_barebone(path)

        with open(path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def write_json_barebone(self, path: str):
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump({}, json_file, indent=4)


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
        ]

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

            # Grab IDs for JSON
            g_id = interaction.guild.id
            channel_id = int(channel)

            # Create JSON Formated Data var.
            data = {
                    "guild_id": g_id,
                    "name": interaction.guild.name,
                    "channel_id": channel_id,
            }

            # Call json_writer
            self.json_writer(JSON_PATH, data)
            await interaction.response.send_message(f"You selected <#{channel}>")


# Setup function for loading the cog
async def setup(bot):
    await bot.add_cog(select_channel(bot))
