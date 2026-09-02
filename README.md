# Discord PC Remote Bot

A personal Discord bot to:

- Take screenshots on demand
- Run periodic screenshot loops
- Stop screenshot loops
- Shutdown your PC

⚠ **WARNING:** This app is for personal use only. It will only respond to the Discord user ID you set in environment variables. Do not run it on shared or public machines.

---

## Features

| Command         | Description                        |
|-----------------|------------------------------------|
| `!ss`           | Take a one-time screenshot         |
| `!ss <minutes>` | Take screenshots every `<minutes>` |
| `!stop`         | Stop the screenshot loop           |
| `!shutdown`     | Shutdown your PC immediately       |

---

## Requirements

- Python 3.10+  
- Dependencies:
```
pip install discord.py pillow
```

## Setup

1. Create your Discord app
    1. Go to Discord Developer Portal. 
    2. Create a new application → Bot → Copy token
    3. Enable Message Content Intent

2. Set environment variables

    Windows (PowerShell)
    ```
    setx DISCORD_TOKEN "your_bot_token_here"
    setx DISCORD_USER_ID "your_discord_user_id_here"
    ```

3. Run the app
    ```python bot.py```

### Optional: Run on Windows startup

To automatically start the bot when Windows starts:

1. Press `Win + R`
2. Enter:
   `shell:startup`
3. Copy `DiscordApp.pyw` into the Startup folder.

The bot will now start automatically when you log into Windows without opening a command prompt window.

## Notes
- Screenshot loop interval is limited to 1–60 minutes.
- Bot is safe for personal use only; it will ignore messages from other Discord users.
- Use environment variables to protect your token and user ID.
