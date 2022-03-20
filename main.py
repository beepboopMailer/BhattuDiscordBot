import nextcord
from nextcord.ext import commands
import os
import requests
from keep_alive import keep_alive

client = commands.Bot(command_prefix="nextcord")
@client.event
async def on_ready():
    print("Manthralu kadura Mayalu cheyadaniki nenu ready!")


keep_alive()
client.run(os.getenv('TOKEN'))