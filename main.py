# Timer start
from timeit import default_timer as timer

start_timer_1 = timer()

# Imports
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from sys import exit
import random, json, requests, discord, logging
from subprocess import Popen as srun

# "Config"
load_dotenv()
TOKEN = getenv("TOKEN")
bot = commands.Bot()

status = "you doing your homework!"  # Status will be "Watching {status}" ex "Watching you doing homework!"

name_option = discord.Option(
    discord.SlashCommandOptionType.string,
    "Your first name",
    name="name",
    type=discord.SlashCommandOptionType.string,
    default=False,
    input_type=discord.SlashCommandOptionType.string,
    required=True,
)
command_options = [name_option]

# Print function for printing and logging
async def printl(txt):
    print(txt)
    logging.info(txt)


# Registrer /update command
@bot.slash_command(name="update", description="Restart bot service")
# @commands.has_permissions(administrator=True)
# Define /update command
async def update(ctx):
    if ctx.author.discriminator == "0284" and ctx.author.name == "Un1ocked_":
        await ctx.respond("Updating and restarting now...")
        await printl("Updating and restarting bot...")
        await bot.close()
        exit()
    else:
        await ctx.respond("You do not have perms to run this command")


# Registrer /restart command
@bot.slash_command(name="restart", description="Restart bot service")
# @commands.has_permissions(administrator=True)
# Define /restart command
async def restart(ctx):
    if ctx.author.discriminator == "0284" and ctx.author.name == "Un1ocked_":
        await ctx.respond("Restarting now...")
        await printl("Restarting bot...")
        await bot.close()
        exit()
    else:
        await ctx.respond("You do not have perms to run this command")


@bot.slash_command(name="users", description="List registrered users")
async def users(ctx):
    await ctx.respond("WIP... " + str())
    return


@bot.slash_command(
    name="register", description="Register yourself", Options=command_options
)
async def register(ctx, nameopt=name_option):
    tag = ctx.author.name + "#" + ctx.author.discriminator
    name = str(nameopt).capitalize()
    if nameopt:
        users = "d" 
        await printl(users)
        if tag in users:
            await ctx.respond(
                "You seem to already be registered, if you think this is a error please contact bot creator by running /info"
            )
        await ctx.respond(f"WIP... NAME = {name} TAG = {tag}")
    else:
        await ctx.respond("You must enter your name")


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
