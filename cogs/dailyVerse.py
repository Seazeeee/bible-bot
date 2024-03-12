
import random
import discord
import pytz
import datetime
from discord.ext import commands, tasks
from .random import randomVerse

# Define UTC timezone
utc = datetime.timezone.utc

# Create a time object representing 8:30 AM EST (UTC)
time = datetime.time(hour=12, minute=30)

class dailyScripture(commands.Cog):

    # Reference: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()


    def dailyVerse():
        

        # Pull in our dailyVerse selected at random
        verse = randomVerse()

        # Split the verse on the spaces
        splitVerse = verse.split(" ")

        # Grab the chapter:verse 
        chapterVerse = splitVerse[1]

        #Split the chapter and verse
        chapter_verse_split = chapterVerse.split(":")

        # Grab the first 3 letters. EXCEPTIONS: John = JHN
        grabChapterName = splitVerse[0]


        exceptionList = {"John": "JHN"}

        if grabChapterName[len(grabChapterName)-1].strip() in exceptionList:
            grabChapterName = exceptionList.get(grabChapterName[len(grabChapterName)].strip())

        # https://bible.com/bible/59/{3 letter book name}.{chapter}.{verse}.ESV
        # Format the url to use when returning the verse

        verseURL = "https://bible.com/bible/59/" + grabChapterName[:3] + "." + chapter_verse_split[0] + "." + chapter_verse_split[1] + "." + "ESV/"
        

        return  verse, verseURL

    # Loop to send on each day at the given time
    @tasks.loop(time=time)
    async def my_task(self):
            await self.bot.wait_until_ready()

            verse_text, verse_link = dailyScripture.dailyVerse()

            while True:

                try:
                    

                    embed = discord.Embed(
                        color = discord.Color.blue(),
                        title="Daily Verse",
                        description= verse_text,
                        type="rich",
                        url=verse_link,
                    )
                    
                    embed.set_footer(text="*Watching Oppenheimer*")

                    remind_channel = self.bot.get_channel(1215738402260127784)   

                    await remind_channel.send(embed=embed)

                except IndexError:
                    
                    continue

                break

async def setup(bot):
    await bot.add_cog(dailyScripture(bot))


    
