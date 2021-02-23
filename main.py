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

@client.command()
async def leave(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if voice.is_connected():
    await voice.disconnect()
  else:
    await ctx.send('The bot is not connected to a voice channel.')

@client.command()
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send('Currently no audio is playing.')

@client.command()
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send('The audio is already playing.')

@client.command()
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  voice.stop()
client.run(os.getenv('TOKEN')) #run the bot