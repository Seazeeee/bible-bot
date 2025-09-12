import os

from dotenv import find_dotenv, load_dotenv

# Find the .env file

dotenvPath = find_dotenv()


# Load env variables

load_dotenv(dotenvPath)

API_KEY = os.getenv("API_KEY")
JSON_PATH = os.getenv("JSON_PATH")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
