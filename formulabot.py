import discord

from discord.ext import commands

from database import short_team_name, short_driver_name_number

import requests
from typing import Mapping
from bs4 import BeautifulSoup

from os.path import join, dirname

with open(join(dirname(__file__), "token.txt"), "r") as f:
    token=f.read()

def scrape_info(f1_url: str) -> Mapping[str, str]:
    if not f1_url.startswith('https://www.formula1.com/en/'):
        return {}

    try:
        r = requests.get(f1_url, timeout=5)
    except requests.Timeout:
        return {}

    soup = BeautifulSoup(r.content, 'html.parser')

    field_tags = soup.find_all('dt') 
    value_tags = soup.find_all('dd') 
    info = {key.text: value.text for key, value in zip(field_tags, value_tags)}
    info['URL'] = f1_url

    string = " "

    for key, value in info.items():
        string += f"**{key}**: {value}\n"

    return string

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f"It's lights out and away {bot.user} goes!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if ('smooth') in message.content.lower():
        await message.reply('https://tenor.com/view/carlos-sainz-f1-wink-gif-25852406')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def driver(ctx, driver_name):
    retreive = short_driver_name_number(driver_name)
    await ctx.reply(scrape_info(retreive))

@bot.command()
async def team(ctx, team_name):
    retreive = short_team_name(team_name)
    await ctx.reply(scrape_info(retreive))

bot.run(token)


