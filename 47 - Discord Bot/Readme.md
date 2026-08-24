# Discord Bot

A simple **Discord Bot** built with Python and `discord.py`.

The bot can respond to commands, check its latency, greet users, and provide information about its available commands.

## Features

- Discord bot integration
- Custom command prefix
- `!hello` command
- `!ping` command
- `!about` command
- Command list
- Bot latency detection
- Command error handling
- Secure bot token handling
- Asynchronous event handling

## Requirements

Install `discord.py`:

```bash
python -m pip install discord.py
```

## Discord Bot Setup

Before running the program, you need to create a Discord application and bot through the **Discord Developer Portal**.

Create a bot application and obtain its bot token.

The token should **never** be placed directly inside the Python source code.

## API Key / Token Setup

Set the bot token as an environment variable.

### Windows PowerShell

```powershell
$env:DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN" #Not inside the python code, but in terminal
```

Verify that the environment variable exists:

```powershell
python -c "import os; print(bool(os.getenv('DISCORD_BOT_TOKEN')))"
```

Expected output:

```text
True
```

## Important Security Rule

Never write your Discord bot token directly in your Python program.

### Do not do this:

```python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

### Do this instead:

```python
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
```

If your bot token is accidentally exposed, regenerate it immediately through the Discord Developer Portal.

## Message Content Intent

This bot uses:

```python
intents.message_content = True
```

The **Message Content Intent** must also be enabled for the bot in the Discord Developer Portal.

Without it, the bot may connect successfully but fail to respond to message commands.

## Run the Project

Start the bot:

```bash
python Discord_Bot.py
```

If everything works correctly:

```text
==================================================
              DISCORD BOT
==================================================
Logged in as: MyPythonBot
Bot is online!
```

## Commands

The bot supports the following commands:

```text
!hello
!ping
!about
!commands_list
```

### Hello

```text
!hello
```

Example response:

```text
Hello @User! 👋
```

### Ping

```text
!ping
```

Example response:

```text
Pong! 🏓 42ms
```

The latency is measured in milliseconds.

### About

```text
!about
```

Example response:

```text
I am a Python Discord bot built using discord.py! 🤖
```

### Commands

```text
!commands_list
```

Displays the available commands.

## How It Works

```text
Discord Server
      ↓
Discord Gateway
      ↓
Python Bot
      ↓
discord.py
      ↓
Command Detection
      ↓
Command Function
      ↓
Response
      ↓
Discord Channel
```

## Bot Events

The project uses Discord events such as:

```python
@bot.event
async def on_ready():
```

The `on_ready()` event runs when the bot successfully connects to Discord.

## Bot Commands

Commands are created using:

```python
@bot.command()
async def hello(ctx):
```

The `ctx` object contains information about the command context, including the user and channel where the command was executed.

## Modules Used

- Python 3
- discord.py
- os
- asyncio
- Discord API

## What i learned

- Discord Bot Development
- Discord API
- discord.py
- Event-driven programming
- Asynchronous programming
- Bot commands
- Environment variables
- API authentication
- Error handling
- HTTP/WebSocket-based services

---

⭐ Part of my **#50DaysOfPython** challenge.