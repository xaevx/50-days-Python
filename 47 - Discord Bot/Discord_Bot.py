import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

if not TOKEN:

    print("Discord bot token not found.")
    print("Please set the DISCORD_BOT_TOKEN environment variable.")
    exit()

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():

    print("=" * 50)
    print("              DISCORD BOT")
    print("=" * 50)

    print(f"Logged in as: {bot.user}")
    print("Bot is online!")
    print("")

@bot.command()
async def hello(ctx):

    await ctx.send(f"Hello {ctx.author.mention}! 👋")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! 🏓 {latency}ms")

@bot.command()
async def about(ctx):

    await ctx.send("I am a Python Discord bot built using discord.py! 🤖")


@bot.command()
async def commands_list(ctx):

    message = """
**Available Commands**

`!hello` - Say hello
`!ping` - Check bot latency
`!about` - About the bot
`!commands_list` - Show available commands
"""

    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command. Use `!commands_list` to see available commands.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument.")
        
    else:
        print(f"Error: {error}")

bot.run(TOKEN)