from logging import disable
import os
import sys
from constants import main_channel
import discord
from discord import embeds
from discord import channel
from discord.ext import commands
from discord.flags import Intents
import datetime
from math import ceil

# Adding commands dir
sys.path.insert(0, './commands')

# importing commands in main
from ques import ans
from joke import joke_res
from weather import weather_response
from anime import current
from github import git
with open("token.txt", "r") as f:
  token = f.read()

# Set up the bot
client = commands.Bot(command_prefix=".", intents=Intents.all())


# Define the command to send a message
@client.command()
async def ping(ctx):
  await ctx.send(f'yay! {round(client.latency*1000)}ms')


#  Removing default help command
client.remove_command("help")


# Embeded help command
@client.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(color=discord.Color.red())
  embed.set_author(name="Help : list of commands available")
  embed.add_field(name=".ping",
                  value="Returns bot respond time in seconds",
                  inline=False)
  embed.add_field(name=".joke", value="Returns a Joke", inline=False)
  embed.add_field(name=".qna <Question>",
                  value="Ask any Question",
                  inline=False)
  embed.add_field(name=".weather <city>",
                  value="Know about weather",
                  inline=False)
  embed.add_field(name=".ongoing",
                  value="returns top animes of current season",
                  inline=False)

  await ctx.send(embed=embed)


# QNA commands ->
@client.command()
async def qna(ctx, *, question):
  res = ans(question)
  if len(res) > 1950:
    for i in range(ceil(len(res) / 1950)):
      await ctx.send(res[i * 1950:1950 * (i + 1)])
  else:
    await ctx.send(res)


# Jokes commands ->
@client.command()
async def joke(ctx):
  res = joke_res()
  await ctx.send(res[0] + " ....XD")


#weather command->
@client.command()
async def weather(ctx, city):
  res = weather_response(city)
  embed = discord.Embed(title=f"Weather of {res['name']}", color=0x109319)

  embed.add_field(name="Condition",
                  value=f"Current Weather :{res['weather'][0]['description']}",
                  inline=False)
  embed.add_field(
      name="Temperature",
      value=
      f"Current temperature is {str(((res['main']['temp']-32)*5)/9)[:4]} °C",
      inline=True)
  embed.add_field(name="Humidity",
                  value=f"{res['main']['humidity']} g/m^3",
                  inline=True)
  embed.add_field(name="Country",
                  value=f"{res['sys']['country']}",
                  inline=False)
  embed.set_footer(
      text=f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}")
  await ctx.send(embed=embed)


# Github query command ->
@client.command()
async def github(ctx, owner: str):
  repo_data = git(owner)
  if repo_data:
    embed = discord.Embed(
        title=repo_data['login'],
        url=repo_data['html_url'],
        description=f"GitHub Profile of {repo_data['login']}",
        color=discord.Color.green())

    embed.add_field(name="Name",
                    value=repo_data.get('name', 'N/A'),
                    inline=True)
    embed.add_field(name="Public Repos",
                    value=repo_data['public_repos'],
                    inline=True)
    embed.add_field(name="Followers",
                    value=repo_data['followers'],
                    inline=True)
    embed.add_field(name="Following",
                    value=repo_data['following'],
                    inline=True)
    embed.add_field(name="Location",
                    value=repo_data.get('location' or 'N/A'),
                    inline=False)

    embed.set_thumbnail(url=repo_data['avatar_url'])

    # Send the embed to the channel
    await ctx.send(embed=embed)
  else:
    await ctx.send("User not found!")


# Anime ongoing command ->
@client.command()
async def ongoing(ctx):
  res = current()
  embed = discord.Embed(title="Ongoing Animes =>", color=0x109319)
  for x in res:
    name, date = x.split("_")
    embed.add_field(name=name, value=date, inline=False)
  await ctx.send(embed=embed)


# Anime search command ->


# join the voice channel
@client.command(pass_context=True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in a voice channel")


@client.command(pass_context=True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I left the voice channel")
  else:
    await ctx.send("I am not in a voice channel")


# Events


# when bot is ready
@client.event
async def on_ready():
  print("Bot is online")


# Member joining the server
@client.event
async def on_member_join(member):
  channel = client.get_channel(main_channel)
  await channel.send(f"Welcome to the server {member.mention}")


# Member leaving the server
@client.event
async def on_member_remove(member):
  channel = client.get_channel(main_channel)
  await channel.send(f"Goodbye {member.mention}")


# Making bot react on a msg using emoji
# @client.event
# async def on_message(ctx):
#   emoji='\N{EYES}'
#   await ctx.add_reaction(emoji)


#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
  await ctx.send(f'Error. Try .help ({error})')


# NEXT FEATURES
"""
- News 
- Reminders
- Music
- Image Generation
- Anime (almost done)


"""

# To run the bot
client.run(token)
