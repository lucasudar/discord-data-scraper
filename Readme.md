# Discord Bot for Counting User Messages and Tracking Invite Codes

This bot tracks the number of messages each user sends in your Discord server and records the invite code they used to join the server.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/discord-bot.git
    cd discord-bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv discord_bot
    source discord_bot/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables**:
    Create a `.env` file in the root of your project and add your Discord bot token:
    ```env
    TOKEN=your_discord_bot_token
    ```

5. **Run the bot**:
    ```bash
    ./discord_bot/bin/python3 discord_bot.py
    ```

## How It Works

- The bot logs in to your Discord server(s) and starts tracking user messages and invite codes.
- When a user sends a message, the bot logs the message details.
- When a user joins the server, the bot logs the invite code they used.
- The bot saves the collected data to CSV files (`user_message_counts.csv` and `user_invite_codes.csv`).
- The bot merges the message data with invite code data and saves the combined data to `user_combined_data.csv`.

## Notes

- Make sure your bot has the necessary permissions to read messages and access invite information.