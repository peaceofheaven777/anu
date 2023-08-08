import discord
import random
import string
import asyncio
import datetime
import requests
import os
import json
import pyfiglet
from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)

with open('messages.txt', 'r') as f:
    messages = f.readlines()

token = config.get("token")

def scale(time):
    defined = 60
    for unit in ["m", "h"]:
        if time < defined:
            return f"{time:.2f}{unit}"
        time /= defined

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()

def rnd1(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def rnd2(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def get_reply():
    return random.choice(messages).strip()

os.system('cls')
result = pyfiglet.figlet_format("""Discord Tools""", font = "graceful"  )
print (colored(result, 'blue'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now()
print (colored('''Created by: YSA DEV - YSA DEV - YSA DEV - YSA DEV - YSA DEV''', 'cyan', attrs=['bold']))
print (colored('••••', 'green', attrs=['bold']))
print (colored(f"Ξ Follow myGithub : https://github.com/yudhasaputra \nΞ START           : {x} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('••••••• \n', 'green', attrs=['bold']))
print (colored('Write ON DISCORD: \n!levelup to Start Replying', 'cyan', attrs=['bold']))

@client.event
async def on_ready():
    print(f'{Fore.WHITE}[ {Fore.YELLOW}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Bot is ready!')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Type !levelup to start replying')

async def levelup(ctx):
    await ctx.message.delete()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Waiting for command to start replying...")

    def check(message):
        return message.content.startswith("!Levelup") and message.channel == ctx.channel and message.author == ctx.author

    try:
        msg = await client.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}No command entered within 30 seconds.")
    else:
        print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Starting to reply to messages...")
        while True:
            async for message in ctx.channel.history(limit=None):
                if message.author != client.user:
                    try:
                        reply = get_reply()
                        await message.reply(reply)
                    except Exception as e:
                        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Error: {e}")

