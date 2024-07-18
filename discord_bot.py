import os
import discord
import pandas as pd
import aiohttp
intents = discord.Intents.all()
client = discord.Client(intents=intents)

token = os.getenv('token')
guild_id = os.getenv('guild_id')
headers = {
    'Authorization': f'Bot {token}',
    'Content-Type': 'application/json'
}

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await fetch_user_activity()
    await fetch_user_invite_codes()
    await client.close()


async def fetch_user_invite_codes():
    url = f'https://discord.com/api/guilds/{guild_id}/members-search'
    all_invite_data = []
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json={'limit': 1000}) as response:
            if response.status == 200:
                data = await response.json()
                for member_info in data.get('members', []):
                    user_info = member_info['member']['user']
                    user_id = user_info['id']
                    invite_code = member_info.get('source_invite_code', 'N/A')
                    all_invite_data.append({
                        'user_id': user_id,
                        'source_invite_code': invite_code
                    })
            else:
                print(f'Error fetching invite data: {response.status}')

    df_invite = pd.DataFrame(all_invite_data)
    df_invite.to_csv('user_invite_codes.csv', index=False)
    print("User invite codes saved to user_invite_codes.csv")


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

    df_activity = pd.DataFrame(all_user_data)
    df_activity.to_csv('user_message_counts.csv', index=False)
    print("User message counts saved to user_message_counts.csv")

    # Merge user activity data with invite data
    try:
        df_invite = pd.read_csv('user_invite_codes.csv')
        df_merged = pd.merge(df_activity, df_invite, on='user_id', how='left')
        df_merged.to_csv('user_combined_data.csv', index=False)
        print("User combined data saved to user_combined_data.csv")
    except FileNotFoundError:
        print("Invite codes CSV not found. Make sure invite codes are fetched properly.")


client.run(token)
