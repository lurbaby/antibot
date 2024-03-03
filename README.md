# ANTIBOT ![image](https://github.com/lurbaby/antibot/assets/120603922/c74a92fe-489d-477e-8933-acf1517c47f8)


## Description

ANTI bot is a tool designed to combat automated bots in Telegram messanger. What is the purpouse, if you have Telegram group and want prevent spam, you add this bot and when user join to chat bot restrict user permissions and send simple captcha, if user answer right - he become all permissions in group and message will be automaticaly delete, if user don`t answer, the message will automaticaly deleted after 60 seconds.

## Technology Stack
- **Python**
- **Pyrogram**
- **Docker**
- **Docker Compose**
  
## Prerequisites
**You need to create file config.py after clonning and add variables this variables**
**api_id=YOUR_API_ID**
**api_hash=YOUR_API_ID**
**bot_token=YOUR_BOT_TOKEN**


## Installation and Running

1. **Clone the Repository**
# clone the repo
$ git clone https://github.com/lurbaby/antibot.git

# change the working directory to sherlock
$ cd antibot

# install the requirements
$ python3 -m pip install -r requirements.txt


## Installation Docker & Docker-compose
**docker build -t anti-bot:latest .**
**docker-compose up -d**


