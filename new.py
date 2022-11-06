# Imports
from discord.ext import commands as dcommands
import random, json, requests, discord, logging
import commands as cmds
import config
from cmd import *
import test_command

bot = dcommands.Bot()

print(commands)

bot.run(config.token)

