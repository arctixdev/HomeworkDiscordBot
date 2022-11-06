

async def update(ctx):
    if ctx.author.discriminator == "0284" and ctx.author.name == "Un1ocked_":
        await ctx.respond("Updating and restarting now...")
    else:
        await ctx.respond("You do not have the right perms to execute this command")
