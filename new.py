# Imports
from discord.ext import commands as dcommands
import random, json, requests, discord, logging
import commands as cmds
import config
from cmd import *
bot = dcommands.Bot()
import test_command

print(commands)
test_command.init(bot)

bot.run(config.token)

