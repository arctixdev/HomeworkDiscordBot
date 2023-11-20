from cmd import *

me = command()
me.name = "test_command"
me.description = "A test command"
me.options = False
#me.command = test_command 

commands["test_command"] = me 

def init(bot):
    print("test")
    @bot.slash_command()
    async def test_command(ctx):
        print("hey")
