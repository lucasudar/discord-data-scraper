# Discord Data Scraper

This project is a Discord bot that scrapes user activity data from Discord servers and saves it to a CSV file. The bot logs in using a provided token, fetches user activity data, and stores the information in a CSV file called `user_message_counts.csv`.

## Setup and Running Instructions

### 1. Create a Virtual Environment

To keep dependencies isolated, it's recommended to create a virtual environment.

```sh
# Create a virtual environment
python3 -m venv discord_bot

# Activate the virtual environment
source discord_bot/bin/activate
```

### 2. Set your token

Copy your token from admin panel

```sh
cp .env.example .env
```

### 3. RUN script

```sh
./discord_bot/bin/python3 discord_bot.py
```

### Enjoy your statistics!