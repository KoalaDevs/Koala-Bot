import aiohttp
import asyncio
import box
import config
import datetime
import discord
import jishaku
import json
import nekos
import os
import platform
import random
import requests
import re
import typing
from dadjokes import *
from datetime import datetime
from discord.ext import commands
from webserver import keepalive

client = commands.Bot(description = "Rob Bot", command_prefix = "!")
#client.remove_command('help')
client.remove_command('frizzy')
client.launch_time = datetime.utcnow()
EQUAL_REGEX = re.compile(r"""(\w+)\s*=\s*["'](.+?)["']""")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='A Netplay Game'))
    print("#################\n# Bot is online #\n#################")
    print("Running as: " + client.user.name)
    print("Discord.py: " + discord.__version__)
    print("Created by Cranky Supertoon#7376")

@client.event
async def on_member_join(member):
  welcomechannel = client.get_channel(684180084307001423)
  staffwelcomechannel = client.get_channel(691010936500256859)
  jl = [f"We've got cookies {member.mention}!",
    f"Isn't there a discord server for memes like {member.mention}?",
    f"October 31st, Halloween, November 1st, beginning of Hanukkah and Christmas, what is this {member.mention}!",
    f"{member.mention}, Do you like spooky? I like spooky, SPOOOOOKY!!!",
    f"The cake is a lie, or is it {member.mention}?",
    f"There’s a fire burning {member.mention}! Anybody got marshmallows?",
    f"Minecraft 1.13 is here {member.mention}! It took a long time for you guys to add water animals Mojang!",
    f"You like games {member.mention}? Hopefully!",
    f"Once you get here {member.mention}, you just keep going and going and going...!",
    f"Every {member.mention} is like a bird, they just fly in out of nowhere and poop on your head! Not really though!",
    f"Never enough {member.mention}'s, or maybe too many I don’t know!",
    f"Free Advice From Phantom_storm {member.mention} don't eat your mic, it's too...salty.",
    f"I see a message in the sky it says, “welcome {member.mention}!",
    f":notes:I see trees of green, {member.mention}  too:notes: and i think to myself what a wonderful sever!:notes:",
    f"{member.mention} came prepared, with absolutely nothing!",
    f"A new player has entered the ring, {member.mention} , show us what you can do!",
    f"We have free icecream {member.mention}! But it may melt, so hurry fast!",
    f"It’s time to do do do do do do do do do do do do DOOO ITTTT {member.mention}!!!!",
    f"Made with 100% dank memes {member.mention}!",
    f"This match will get red hot {member.mention}!",
    f"Wonder what this button does {member.mention}, oh, another member, amazing!!!",
    f"A brawl is surely brewing {member.mention}!",
    f"The Man, The Myth, The Legend, {member.mention} has entered the building!",
    f"Do you knew the wae {member.mention}? We do know the wae!",
    f"Old friends new friends like {member.mention} they’re all my friends!",
    f"We were expecting you {member.mention} ( ͡° ͜ʖ ͡°)",
    f"We count by friends not members {member.mention}!:grin:",
    f"I wonder how many people are on the server? Oh wait, here comes {member.mention}!",
    f"Obviously {member.mention} is not an alt account, am I right or am I right! :sunglasses:"
    ]
  jlrandom = random.choice(jl)
  await welcomechannel.send(f"{jlrandom}")
  await staffwelcomechannel.send(f"{member} Joined. Account created on {member.created_at}")

@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

@client.command()
async def dice(ctx):
  """Rolls the dice"""
  cont = random.randint(1, 6)
  await ctx.send("You Rolled **{}**".format(cont))

@client.command()
async def toss(ctx):
  """Put the toss"""
  ch = ["Heads", "Tails"]
  rch = random.choice(ch)
  await ctx.send(f"You got **{rch}**")

@client.command()
async def dadjoke(ctx):
  """Sends the dadjokes"""
  async with ctx.typing():
      await ctx.send(Dadjoke().joke)

@client.command("info")
async def s_info(ctx):
    server = ctx.guild
    try:
        icon = server.icon_url_as(size=256)
    except Exception as e:
        icon = ("\uFEFF")
    embed = discord.Embed(title=f"Server info for {server.name}", description=None, colour=0x98FB98)
    embed.set_thumbnail(url=icon)
    # Basic info -- Name, Region, ID, Owner (USER+descrim, ID), Creation date, member count
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Owner", value=f"{server.owner.name}**-**{server.owner.id}", inline=True)
    embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
    embed.add_field(name="Server Icon Url", value=server.icon_url, inline=False)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    await ctx.send(content=None, embed=embed)

keepalive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)