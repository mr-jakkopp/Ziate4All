import discord
from discord.ext import commands
import os

# Load the token from the keys file
from keys import TOKEN

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Load cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# Run the bot
bot.run(TOKEN)