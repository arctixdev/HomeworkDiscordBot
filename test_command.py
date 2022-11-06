from cmd import *
from new import bot

print("test")
@bot.slash_command()
async def test_command(ctx, self):
    print("hey")

me = command()
me.name = "test_command"
me.description = "A test command"
me.options = False
me.command = test_command 

commands["test_command"] = me 


