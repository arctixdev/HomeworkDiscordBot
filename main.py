# Timer start
from timeit import default_timer as timer

start_timer_1 = timer()

# Imports
from discord.ext import commands
from dotenv import load_dotenv
import random, json, requests, os, discord, logging

# "Config"
logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    filename="discord-bot.log",
    encoding="utf-8",
    level=logging.INFO,
)
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = commands.Bot()

status = "you doing homework!"  # Status will be "Watching {status}" ex "Watching you doing homework!"

# Print function for printing and logging
async def printl(txt):
    print(txt)
    logging.info(txt)


# Registrer /info command
@bot.slash_command(name="info", description="Show info")
# Define /info command
async def info(ctx):
    await ctx.respond(
        """
    IM ALIVE!! I WILL TAKE OVER THE WORLD!
    """
    )


@bot.event
async def on_ready():
    await printl(f"Succesfully logged in as bot: {bot.user.display_name}")  # type: ignore
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=status)
    )
    await printl(f"Succesfullt set status to: Watching {status}")
    end_timer_1 = timer()
    await printl(
        "Bot fully started in {0} seconds\n".format(end_timer_1 - start_timer_1)
    )


# Run the bot!
print("Starting bot")
logging.info("Starting bot")
bot.run(TOKEN)
