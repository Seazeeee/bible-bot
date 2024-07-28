# #Bible-bot

A discord bot that allows for a daily verse to be sent. Currently, the verse is set to be sent at 8:30 AM EST. This will later be changed to a command that will
allow you to schedule the time. I have implemented a /verse and /random. /verse lets you specify the book, chapter, and verse that would like to see. Optional you can
provide a translation that is checked and used. /random send and completely random verse from the bible. This is a passion project that I will develop over time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things do you need to install the software and how to install them

```
python: https://www.python.org/downloads/

Discord-app API Key: Private https://discord.com/developers/docs/intro

discord.py

pytz

dotenv

```

### Installing

```
Python: Standard .exe installation
```

```
Following given prompts at https://discord.com/developers/docs/intro to create a discord application
```

```python
pip3 install discord.py
```

```python
pip3 install python-dotenv
```

```python
pip3 install pytz
```

You would then invite the bot to your server and you would have access to the given commands.

## Deployment

Currently, the bot is deployed on my local network via a Raspberry PI to run 24/7.

I have had great success with this and you can easily move the working directory onto the
pi and start it up by following the above prompts.

However, if the internet drops or cuts out the bot will not start automatically.

You can configure the bot to run on Pi startup. Something simple like this would
suffice.

First, create a bot.sh (script) that runs the bot

```bash
cd /path/to/bot

nohup .venv/bin/python3 bot.py
```

Second, make the file executable

```bash
chmod +x bot.sh
```

Lastly, configure a way to run bot.sh on startup. I chose to use Cron

```bash
sudo crontab -e
```

```bash
@reboot /path/to/bot.sh
```

Save and you should be all set! This doesn't fix the necessary issue that is prompted
when the internet drops. I have found that you can easily SSH back into the Pi and run
the bot.sh script

```bash
bash path/to/bot.sh
```

## Built With

- [Discord.py](https://discordpy.readthedocs.io/en/stable/) - The bot framework

## Authors

- **Matthew Thompson** - _Initial work_ - [Seazeeee](https://github.com/Seazeeee)

## License

This project is licensed under the MIT License - see LICENSE.md for details

```

```

```

```

```

```
