#!/usr/bin/env python3

import sys
import discord
from discord.ext import commands

### CONSTANTS ##################################################################

CHANNEL_ID = # Posa aquí el teu Channel ID

### FUNCTIONS ##################################################################

def read_token():
    # Llegix el token des d'un fitxer
    with open('token.txt', 'r') as token_file:
        return token_file.read().strip()

def create_bot():
    # Configurar el bot amb intents i configuracions
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False

    return commands.Bot(command_prefix='!', description='A bot that sends messages from a command parameter', intents=intents)

async def send_message(bot, message):
    # Enviar el missatge al canal fixat
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)  # Utilitza la constant CHANNEL_ID
    if channel:
        await channel.send(message)
        print(f"Missatge {message} enviat al canal {channel}")
    else:
        print("Error: No s'ha trobat el canal.")

    await bot.close()

### MAIN #######################################################################

def main():

    # Comprovar que s'ha passat un missatge com a paràmetre

    if len(sys.argv) < 2:
        print("Ús: python3 bot.py \"Missatge\"")
        sys.exit(1)

    message = sys.argv[1]   # S'agafa el missatge
    token = read_token()    # Llegir el token

    bot = create_bot()

    @bot.event
    async def on_ready():
        await send_message(bot, message)

    bot.run(token)

if __name__ == "__main__":
    main()