import json
import os

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
