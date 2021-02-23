import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")
@client.command()
async def play(ctx, url : str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Songs')
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if not voice.is_connected():
    await voiceChannel.connect()

client.run(os.getenv('TOKEN')) #run the bot