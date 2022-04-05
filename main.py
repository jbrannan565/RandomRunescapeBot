import os
from discord.ext import commands
from dotenv import load_dotenv

from cogs.fetcher import Fetcher


# setup logging
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# load dot env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')

# make the bot
bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.add_cog(Fetcher(bot))
bot.run(TOKEN)