import discord
from discord import Emoji, app_commands
from discord.ext import commands

class Select(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Prayer Cog Loaded")

    @app_commands.command(name="prayer", description="A list of a few different prayers.")
    @app_commands.describe(prayers = "Prayers to choose from.")
    @app_commands.choices(prayers = [
            discord.app_commands.Choice(name="Our Father 🙏", value=1,),
            discord.app_commands.Choice(name="Hail Mary 📿", value=2),
            discord.app_commands.Choice(name="Apostles' Creed 😇", value=3)
            
    ])
    async def choosePrayer(self, interaction: discord.Interaction, prayers: discord.app_commands.Choice[int]):
        if prayers.value == 1:
            embed = discord.Embed (
                                    color = discord.Color.blue(),
                                    title="Prayer",
                                    type="rich",
                                    description= "Our Father, Who art in heaven, Hallowed be Thy Name. Thy Kingdom come, Thy Will be done, On earth as it is in Heaven. Give us this day, our daily bread, And forgive us our trespasses, as we forgive those who trespass against us. And lead us not into temptation, but deliver us from evil. Amen."
                                    )
            
            await interaction.response.send_message(embed=embed)
            
        elif prayers.value == 2:

            embed = discord.Embed (
                                    color = discord.Color.blue(),
                                    title="Prayer",
                                    type="rich",
                                    description= "Hail Mary, full of grace. The Lord is with thee. Blessed art thou amongst women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death, Amen."
                                    )
            
            await interaction.response.send_message(embed=embed)

        elif prayers.value == 3:

            embed = discord.Embed (
                                    color = discord.Color.blue(),
                                    title="Prayer",
                                    type="rich",
                                    description = "I believe in God, the Father almighty, Creator of heaven and earth, and in Jesus Christ, his only Son, our Lord, who was conceived by the Holy Spirit, born of the Virgin Mary, suffered under Pontius Pilate, was crucified, died and was buried; he descended into hell; on the third day he rose again from the dead; he ascended into heaven, and is seated at the right hand of God the Father almighty; from there he will come to judge the living and the dead. I believe in the Holy Spirit, the holy catholic Church, the communion of saints, the forgiveness of sins, the resurrection of the body, and life everlasting. Amen."
                                    )
            
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Select(bot))
    