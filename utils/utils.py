import json
import os
from openai import OpenAI
from cogs.env_vars import OPENAI_KEY

def openai_call(input: str):
    client = OpenAI(api_key = OPENAI_KEY)

    response = client.responses.create(
    model="gpt-4.1-nano",
    input=input,
    text={
        "format": {
            "type": "json_schema",
            "name": "bible_verse",
            "schema": {
                "type": "object",
                "properties": {
                    "Book": { "type": "string" },
                    "Chapter": { "type": "integer" },
                    "Verse": { "type": "integer" }
                },
                "required": ["Book", "Chapter", "Verse"],
                "additionalProperties": False
                }
            }
        }
    )

    return response.output_text


def json_writer(path: str, data: dict):
    # Validate input
    if "guild_id" not in data or "channel_id" not in data or "name" not in data:
        print("[json_writer] Invalid data format passed. Skipping write.")
        return

    read_data = json_reader(path)

    guild_id = str(data["guild_id"])

    # Update or insert the new data for this guild
    read_data[guild_id] = {
        "name": data["name"],
        "channel_id": data["channel_id"]
    }

    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(read_data, json_file, indent=4)

def json_reader(path: str):
    # Check file
    if not os.path.exists(path):
        write_json_barebone(path)

    with open(path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def write_json_barebone(path: str):
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump({}, json_file, indent=4)
