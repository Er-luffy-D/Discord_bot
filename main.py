from logging import disable
import os
import discord
from discord.ext import commands
from discord.flags import Intents
# Set up the bot
with open('token.txt', "r") as f:
  Token = f.readline()
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


# Define the command to send a message
@client.command()
async def ping(ctx):
  await ctx.send(f'yay! {round(client.latency*1000)}ms')


client.remove_command("help")
# Embeded help command (working rn..........)



#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

client.run(Token)
