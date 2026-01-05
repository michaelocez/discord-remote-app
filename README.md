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
You can add a shortcut in your Shell:Startup folder to start the bot automatically when your PC boots.

For example: 

``` "C:\Program Files\Python313\pythonw.exe" "C:\Users\YourUsername\Path\To\DiscordApp.py" ```

Replace the path with the location of your bot on your PC.

## Notes
- Screenshot loop interval is limited to 1–60 minutes.
- Bot is safe for personal use only; it will ignore messages from other Discord users.
- Use environment variables to protect your token and user ID.
