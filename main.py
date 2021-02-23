import discord
import os
from discord.ext import commands
import youtube_dl

client = commands.Bot(command_prefix="!")
@client.command()
async def play(ctx, url : str):
  song_there = os.path.isfile('song.mp3')
  try:
    if song_there:
      os.remove('song.mp3')
  except PermissionError:
    await ctx.send("Wait for the current playing music to end or use the 'stop' command")
    return

  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Songs')
  await voiceChannel.connect()
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

  
  ydl_opts={
    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'prefferedcodec': 'mp3',
      'prefferedquality': '192',
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file, "song.mp3")
  voice.play(discord.FFmpegPCMAudio("song.mp3"))
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