import disnake
import os
import logging
from disnake.ext import commands
import sys
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix='!',
    test_guilds=[545669263994650625],
    intents=intents,
)

client = bot # just in case as it is also commonly used

@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")

@bot.slash_command(description="Multiplies the number by the multiplier")
async def multiply(inter, number: int, multiplier: int):
    await inter.response.send_message(number * multiplier)

@bot.event
async def on_ready():
    print(f"------\nLogged in as {bot.user} (ID: {bot.user.id})\n------")

class Website(str, Enum):
    DovydasTEDS = 'https://dovydasteds.tk'
    TEDS = 'https://teamtedps.tk'
    wilam = 'https://tedps.tk/wilam'

class DovydasTEDSSocials(str, Enum):
    Website = 'https://dovydasteds.tk'
    Partners = 'https://teamtedps.tk'
    Discord = 'https://tedps.tk/discord'
    Reddit = 'https://reddit.com/u/DovydasTEDS'
    Twitter = 'https://twitter.com/DovydasTEDS'
    Github = 'https://github.com/DovydasTEDS'
    Steam = 'https://steamcommunity.com/id/dovydasteds'
    Itch = 'https://dovydasteds.itch.io/'
    Xbox = 'https://live.xbox.com/Profile?Gamertag=DovydasTEDS'
    Twitch = 'https://twitch.tv/DovydasTEDS'

class TEDSSocials(str, Enum):
    Website = 'https://teamtedps.tk'
    Discord = 'https://tedps.tk/discord'
    Github = 'https://github.com/TeamTEDS'


class DovydasTEDSSubcommands(str, Enum):
    socials = 'socials'

@bot.slash_command()
async def website(inter: disnake.ApplicationCommandInteraction, website: Website):
    await inter.response.send_message(website)

@bot.user_command(name="Avatar")  # name is optional
async def avatar(inter: disnake.UserCommandInteraction, user: disnake.User):
    embed = disnake.Embed(title=f"{user}'s avatar")
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)

@bot.slash_command()
async def dovydasteds(inter):
    print("DovydasTEDS ran")


@dovydasteds.sub_command()
async def socials(inter: disnake.ApplicationCommandInteraction, socials: DovydasTEDSSocials):
    await inter.response.send_message(socials)

@bot.slash_command()
async def teamteds(inter):
    print("TeamTEDS ran")


@teamteds.sub_command()
async def socials(inter: disnake.ApplicationCommandInteraction, socials: TEDSSocials):
    await inter.response.send_message(socials)

bot.run(os.getenv("DISCORD_TOKEN"))