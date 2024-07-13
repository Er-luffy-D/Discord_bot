from logging import disable
import os
import discord
from discord.ext import commands
from discord.flags import Intents
import sys

# Adding commands dir
sys.path.insert(0, './commands')

from ques import ans

with open("token.txt", "r") as f:
  token = f.read()

# Set up the bot
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


# Define the command to send a message
@client.command()
async def ping(ctx):
  await ctx.send(f'yay! {round(client.latency*1000)}ms')


client.remove_command("help")

# Embeded help command (working rn..........)


# Embeded help command
@client.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(color=discord.Color.purple())
  embed.set_author(name="Help : list of commands available")
  embed.add_field(name=".ping",
                  value="Returns bot respond time in seconds",
                  inline=False)
  embed.add_field(name=".qna", value="Ask any Question", inline=False)
  await ctx.send(embed=embed)


@client.command()
async def qna(ctx, *, question):
  res = ans(question)
  await ctx.send(res)


# Making bot react on a msg using emoji
# @client.event
# async def on_message(ctx):
#   emoji='\N{EYES}'
#   await ctx.add_reaction(emoji)


#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
  await ctx.send(f'Error. Try .help ({error})')


client.run(token)
