import os

from dotenv import find_dotenv, load_dotenv

# Find the .env file

dotenvPath = find_dotenv()


# Load env variables

load_dotenv(dotenvPath)

API_KEY = os.getenv("API_KEY")

GUILD_ID = os.getenv("GUILD_ID")

VERSE_URL = os.getenv("VERSE_URL")
