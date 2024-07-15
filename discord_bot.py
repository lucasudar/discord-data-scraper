import os
import discord
import pandas as pd
intents = discord.Intents.all()
client = discord.Client(intents=intents)

token = os.getenv('token')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await fetch_user_activity()
    await client.close()


async def fetch_user_activity():
    all_user_data = []

    for guild in client.guilds:
        print(f'Fetching data for guild: {guild.name}')
        for channel in guild.text_channels:
            print(f'Fetching data for channel: {channel.name}')
            try:
                async for message in channel.history(limit=None):
                    if message.author.bot:
                        continue
                    user_data = {
                        'guild_name': guild.name,
                        'channel_name': channel.name,
                        'user_id': message.author.id,
                        'name': message.author.global_name,
                        'nickname': message.author.name,
                        'discriminator': message.author.discriminator,
                        'message_count': 1
                    }
                    all_user_data.append(user_data)
            except discord.Forbidden:
                print(f"Cannot access channel: {channel.name}")

    df = pd.DataFrame(all_user_data)
    df.to_csv('user_message_counts.csv', index=False)
    print("User message counts saved to user_message_counts.csv")

client.run(token)
