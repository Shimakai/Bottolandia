import asyncio
import discord
from discord.ext.commands import Bot
import os
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = 'NTUxNzMwODE0MzU0ODQ5ODAz.D11QnQ.hUOzavvJ7onAAK7GDiDEUudZYjU'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send("ZA WARUDO")

bot.run(TOKEN)
