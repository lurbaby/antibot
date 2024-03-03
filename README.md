<div align="center">

# ANTIBOT ![image](https://github.com/lurbaby/antibot/assets/120603922/c74a92fe-489d-477e-8933-acf1517c47f8)

## Description

ANTI bot is a tool designed to combat automated bots in Telegram Messenger. If you have a Telegram group and want to prevent spam, you can add this bot. When a user joins the chat, the bot restricts user permissions and sends a simple captcha. If the user answers correctly, they regain all permissions in the group, and the message will be automatically deleted. If the user doesn't answer, the message will automatically be deleted after 60 seconds.

## Technology Stack

- **Python**
- **Pyrogram**
- **Docker**
- **Docker Compose**

</div>

## Prerequisites


**You need to create file config.py after clonning and add variables this variables**
``` python
**api_id=YOUR_API_ID**
**api_hash=YOUR_API_ID**
**bot_token=YOUR_BOT_TOKEN**
```
## Installation and Running


``` python
# Clone the repo
git clone https://github.com/lurbaby/antibot.git

# Change the working directory to antibot
cd antibot

# Install the requirements
python3 -m pip install -r requirements.txt
```

# Docker & Docker-compose
``` 
docker build -t anti-bot:latest .
docker-compose up -d
```

