# ────────────────────imports────────────────────
import discord
from discord.ext import commands
import random
import time
import sys
import os

# ────────────────────token et autres trucs────────────────────
TOKEN = ''
client = commands.Bot(command_prefix='r!')
date = time.strftime("%A %d %B %Y %H:%M:%S")
client.remove_command('help')

random.seed(2)


def generateXP():
    random.randint(2, 100)


# ────────────────────Message de démarrage du bot────────────────────

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Radiant Bot", url='https://www.twitch.tv/'))
    print('Je suis OK!')
    embed = discord.Embed(title="『:white_check_mark:』Je suis allumé!", color=0xf0f4f6)
    embed.set_footer(text=date)
    channel = client.get_channel(id=695918330338607104)
    await channel.send(embed=embed)


# ────────────────────cogs────────────────────

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# ────────────────────dodo────────────────────


@client.command
@commands.has_permissions(administrator=True)
async def dodo(ctx):
    embed = discord.Embed(title="Bonne nuit!", description='je vé dormir UwU')
    await ctx.send(embed=embed)
    await client.logout


# ────────────────────erreurs────────────────────

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        date = time.strftime("%A %d %B %Y %H:%M:%S")
        embed = discord.Embed(title="『:warning:』Erreur! Vérifiez les arguments requis!", color=0xfe0b00)
        embed.set_footer(text=date)
        await ctx.send(embed=embed)


@client.event
async def on_MissingPermissions(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        date = time.strftime("%A %d %B %Y %H:%M:%S")
        embed = discord.Embed(title="『:warning:』Erreur! Vous n'avez pas les perms!", color=0xfe0b00)
        embed.set_footer(text=date)
        await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        date = time.strftime("%A %d %B %Y %H:%M:%S")
        embed = discord.Embed(title="『:warning:』Erreur! Mauvaise commande!!", color=0xfe0b00)
        embed.set_footer(text=date)
        await ctx.send(embed=embed)


# ────────────────────ping/pong────────────────────

@client.command()
async def ping(ctx):
    embed = discord.Embed(title="『:ping_pong:』 Pong!",
                          description=f"{round(client.latency * 1000)}ms")
    await ctx.send(embed=embed)
