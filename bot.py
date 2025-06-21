#!/usr/bin/env python3

import argparse
import discord
from discord.ext import commands
from channels import CHANNELS

### FUNCTIONS ##################################################################

def get_arguments():
    parser = argparse.ArgumentParser(description="A Discord bot that sends a message to a specified channel.")
    parser.add_argument('-m', '--message', required=True, help='Message to send')
    parser.add_argument('-c', '--channel', required=True, help='Target channel name (e.g., general, dev, server-status)')
    return parser.parse_args()

def read_token():
    with open('token.txt', 'r') as token_file:
        return token_file.read().strip()

def create_bot():
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    # Optional: intents.message_content = True if needed for reading messages
    return commands.Bot(command_prefix='!', description='Simple message-sending bot', intents=intents)

async def send_message(bot, channel_id, message):
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
        print(f'Message "{message}" successfully sent to channel: {channel.name}')
    else:
        print(f"Error: Channel with ID {channel_id} not found or not accessible.")
    await bot.close()

### MAIN #######################################################################

def main():
    args = get_arguments()
    message = args.message
    channel_name = args.channel

    if channel_name not in CHANNELS:
        print(f"Error: Channel \"{channel_name}\" does not exist. Available channels: {', '.join(CHANNELS.keys())}")
        exit(1)

    channel_id = CHANNELS[channel_name]
    token = read_token()
    bot = create_bot()

    @bot.event
    async def on_ready():
        await send_message(bot, channel_id, message)

    bot.run(token)

if __name__ == "__main__":
    main()
