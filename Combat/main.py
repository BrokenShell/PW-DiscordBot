""" RPG-lite Discord Bot """
import os

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Test Active'))


@bot.command()
@commands.bot_has_permissions(manage_messages=True)
async def clear(ctx, amount=999):
    await ctx.channel.purge(limit=amount+1)


bot.load_extension('cogs.character_ops')
bot.run(os.getenv('TOKEN'))
