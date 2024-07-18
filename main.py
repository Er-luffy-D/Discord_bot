from logging import disable
import os
import sys
import discord
from discord import embeds
from discord.ext import commands
from discord.flags import Intents
from math import ceil

# Adding commands dir
sys.path.insert(0, './commands')

# importing commands in main
from ques import ans
from joke import joke_res
from weather import weather_response

with open("token.txt", "r") as f:
  token = f.read()

# Set up the bot
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


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
  embed.add_field(name=".joke", value="Returns a Daddy Joke", inline=False)
  embed.add_field(name=".qna", value="Ask any Question", inline=False)
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
  embed = discord.Embed(color=discord.Color.orange())
  embed.add_field(name=res[0], value=res[1], inline=False)
  await ctx.send(embed=embed)


#weather command->
@client.command()
async def weather(ctx, city):
  res = weather_response(city)
  embed = discord.Embed(title="Weather", color=0x109319)
  # Adding details from response
  embed.set_author(name=ctx.author.display.name,
                   icon_url=ctx.author.avatar_url)

  embed.add_field(name="Temperature",
                  value=f"Current temperature is {res['main']['temp']} °C",
                  inline=True)
  embed.add_field(name="Field 2 Title",
                  value="It is inline with Field 3",
                  inline=True)
  embed.add_field(name="Field 3 Title",
                  value="It is inline with Field 2",
                  inline=True)
  embed.set_footer(
      # not working rn
      text="Information requested by: {}".format(ctx.author.display_name))
  await ctx.send(embed=embed)

  # embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")


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
- Weather
- News
- Jokes
- Reminders
- Music
- Image Generation
- Anime


"""

# To run the bot
client.run(token)
