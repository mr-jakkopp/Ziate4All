import discord
from discord.ext import commands

from keys import ADMIN_ID  # Import your admin ID

def is_admin():
    async def predicate(ctx):
        return ctx.author.id == ADMIN_ID
    return commands.check(predicate)

class SanityCheck(commands.Cog):
    """Example commands for your bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    @is_admin()
    async def sanity(self, ctx):
        """Base admin command."""
        await ctx.send("Available subcommands: ping, echo")

    @sanity.command()
    async def ping(self, ctx):
        """Replies with 'Pong!'."""
        await ctx.send("Pong!")

    @sanity.command()
    async def echo(self, ctx, *, message: str):
        """Echoes the user's message."""
        await ctx.send(message)

def setup(bot):
    bot.add_cog(SanityCheck(bot))