import discord
from discord.ext import commands

class ExampleCog(commands.Cog):
    """Example commands for your bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        """Replies with a friendly greeting."""
        await ctx.send(f"Hello, {ctx.author.mention}!")