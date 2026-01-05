import discord, os, io, asyncio
from PIL import ImageGrab

# Set up environment variables in powershell, see README for more details
TOKEN = os.getenv("DISCORD_TOKEN")
USER_ID = int(os.getenv("DISCORD_USER_ID"))

# Discord client setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

screenshot_task = None
MIN_INTERVAL = 1  # minutes
MAX_INTERVAL = 60

# Take one screenshot
async def screenshot_once(channel):
    screenshot = ImageGrab.grab()
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)
    await channel.send(file=discord.File(buffer, "screenshot.png"))

# Loop screenshots
async def screenshot_loop(channel, interval):
    try:
        while True:
            await screenshot_once(channel)
            await asyncio.sleep(interval * 60)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        await channel.send(f"Screenshot loop error: {e}")

@client.event
async def on_message(message):
    global screenshot_task

    # Ignore messages from others
    if message.author.id != USER_ID:
        return

    command = message.content.strip().split()
    if not command:
        return

    # One-time screenshot
    if command[0] == "!ss" and len(command) == 1:
        await screenshot_once(message.channel)

    # Start screenshot loop
    elif command[0] == "!ss" and len(command) == 2 and command[1].isdigit():
        interval = int(command[1])
        if not (MIN_INTERVAL <= interval <= MAX_INTERVAL):
            await message.channel.send("Interval must be 1–60 minutes.")
            return
        
        screenshot_task = asyncio.create_task(
            screenshot_loop(message.channel, interval)
        )
        await message.channel.send(f"Started screenshots every {interval} minute(s).")

    # Stop screenshot loop
    elif command[0] == "!stop":
        if screenshot_task and not screenshot_task.done():
            screenshot_task.cancel()
            screenshot_task = None
            await message.channel.send("Stopped screenshots.")
        else:
            await message.channel.send("No screenshot task running.")

    # Shutdown PC immediately
    elif command[0] == "!shutdown":
        await message.channel.send("Shutting down PC...")
        os.system("shutdown /s /t 1")

@client.event
async def on_ready():
    print(f"Bot ready. Logged in as {client.user}")

client.run(TOKEN)
