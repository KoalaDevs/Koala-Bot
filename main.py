import discord
import random
import os
import requests
import aiohttp
import box
import datetime
import platform

from dadjokes import *
from discord.ext import commands
from datetime import datetime
from keep_alive import keep_alive


#Core Bot
client = commands.Bot(description = "Koala Bot", command_prefix = "!")
client.remove_command('help')
client.launch_time = datetime.utcnow()

#Starting Bot
@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game(name = 'with your mom'))
print("#################\n# Bot is online #\n#################")

#Join Logs
@client.event
async def on_member_join(member):
  welcomechannel = client.get_channel(759864899706290187)
  staffwelcomechannel = client.get_channel(759914456859279360)
  jl = [f"We've got cookies {member.mention}!",
    f"Isn't there a discord server for memes like {member.mention}?",
    f"I hope {member.mention} likes Sodium?",
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
  await staffwelcomechannel.send(f"{member.mention} Joined. Account created on {member.created_at}")

@client.event
async def on_member_remove(member):
  channel = client.get_channel(759864899706290187)
  staff_channel = client.get_channel(759914456859279360)
  await channel.send(f"{member.mention} was blown up by a Creeper")
  await staff_channel.send(f"{member.mention} left")



#Suggestions
@client.event
async def on_message(message):
  if message.channel.id == 759913865848553513:
    await message.add_reaction('👍')
    await message.add_reaction('👎')
  await client.process_commands(message)

#Help Command
@client.command()
async def help(ctx):
  author = ctx.message.author
  embed = discord.Embed(color = discord.Color.orange())
  embed.set_author(name="Commands:")

  #General Comamnds
  embed.add_field(name="General", value="!help - Shows This Message\n\n!ping - Says Pong Back To You\n\n!uptime - Bot Uptime Counter\n\n!server - Shows Server Info", inline=False)

  #Fun Comamnds
  embed.add_field(name="Fun", value="!toss - Coin Flip\n\n!dadjoke - Give a Dad Joke\n\n!dice - Roll 1-6\n\n!reverse - Reverses the given text\n\n!meme - Gives a random meme\n\n!r/feedthebeast - shows a random post from this subreddit.\n\n!drama - Some random Minecraft Related Drama thing.\n\n\!fdrama - Some random Minecraft Fabric related drama thing.", inline=False)

  #Launcher Specific
  embed.add_field(name="Launcher", value="!java - Explain how to install Java\n\n!javainfo - Access info about what Java is\n\n!log - Explain how to read the launchers log", inline=False)
  await ctx.send(author, embed=embed)

#Info Command
@client.command("server")
async def s_info(ctx):
    server = ctx.guild
    #icon = server.icon_url_as(size=256)
    #icon = ("\uFEFF")
    embed = discord.Embed(title=f"Server info for {server.name}", description=None, colour=0x98FB98)
    #embed.set_thumbnail(url=icon)
    # Basic info -- Name, Region, ID, Owner (USER+descrim, ID), Creation date, member count
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Owner", value=f"{server.owner.name}**-**{server.owner.id}", inline=True)
    embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
    #embed.add_field(name="Server Icon Url", value=server.icon_url, inline=False)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    await ctx.send(content=None, embed=embed)

#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')

#Roll Dice Command
@client.command()
async def dice(ctx):
  """Rolls the dice"""
  cont = random.randint(1, 6)
  await ctx.send("You Rolled **{}**".format(cont))

#Coin Flip Command
@client.command()
async def toss(ctx):
  """Put the toss"""
  ch = ["Heads", "Tails"]
  rch = random.choice(ch)
  await ctx.send(f"You got **{rch}**")

#Reverse Text Command
@client.command()
async def reverse(ctx, *, text):
  """Reverse the given text"""
  await ctx.send("".join(list(reversed(str(text)))))

#Meme Command
@client.command()
async def meme(ctx):
  """Sends you random meme"""
  r = await aiohttp.ClientSession().get(
    "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100"
    )
  r = await r.json()
  r = box.Box(r) 
  data = random.choice(r.data.children).data
  img = data.url
  title =  data.title
  url_base = data.permalink
  url = "https://reddit.com" + url_base
  embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
  embed.set_image(url=img)
  await ctx.send(embed=embed)

#Meme Search Command
@client.command()
async def memesearch(ctx, meme_term):
    """Sends you random meme"""
    url_comb = "https://www.reddit.com/r/dankmemes/search.json?sort=new&limit=100&q=www.reddit.com/r/dankmemes&q=" + meme_term
    r = await aiohttp.ClientSession().get(url_comb)
    r = await r.json()
    r = box.Box(r) 
    data = random.choice(r.data.children).data
    img = data.url
    title =  data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)


#RFTB Command
@client.command(aliases=['r/ftb', 'r/feedthebeast', "rfeedthebeast"])
async def rftb(ctx):
  """Sends you a random post from r/feedthebeast"""
  r = await aiohttp.ClientSession().get(
    "https://www.reddit.com/r/feedthebeast/top.json?sort=new&t=day&limit=100"
    )
  r = await r.json()
  r = box.Box(r) 
  data = random.choice(r.data.children).data
  img = data.url
  title =  data.title
  url_base = data.permalink
  url = "https://reddit.com" + url_base
  embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
  embed.set_image(url=img)
  await ctx.send(embed=embed)

#Reddit Wide Search Command
@client.command()
async def reddit(ctx, meme_term):
    url_comb = "https://www.reddit.com/search.json?sort=new&limit=100&q=" + meme_term
    r = await aiohttp.ClientSession().get(url_comb)
    r = await r.json()
    r = box.Box(r) 
    data = random.choice(r.data.children).data
    img = data.url
    title =  data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)

#Dadjoke Command
@client.command()
async def dadjoke(ctx):
  """Sends the dadjokes"""
  async with ctx.typing():
      await ctx.send(Dadjoke().joke)

#Log Command
@client.command(aliases=['logs'])
async def log(ctx):
  await ctx.send('To View your Log click **>_** near the Top Left of the Launcher and then go to console. If you are further having issues feel free to upload the log to a paste site.\nHeres a list of some paste sites:\n      - <https://gist.github.com/>\n      - <https://pastebin.com/>\n      - <https://hastebin.com/>\n      - <https://paste.feed-the-beast.com/>\n      - <https://paste.dimdev.org/>')

#Java Command
@client.command()
async def java(ctx):
  await ctx.send('**Koala Launcher Requires a 64-bit version of Java 8.**\n\n**Windows:**\n<https://adoptopenjdk.net> Grab the `x64 JRE` with a `.msi` extension.\n\n**MacOS**\n<https://adoptopenjdk.net> Grab the `x64` bit `.pkg`\n\n**Arch Linux / Manjaro**\n`sudo pacman -S jre8-openjdk`  **or**  `yay -S jdk8-openjdk`\n\n**Debian / Ubuntu**\n`sudo apt-get install openjdk-8-jre`\n\n**RHEL / Fedora**\n`sudo dnf install java-1.8.0-openjdk`\n\n\nFor more info type `!javainfo`')

#Java Info Command
@client.command()
async def javainfo(ctx):
  await ctx.send('- **Java Virtual Machine (JVM)** - The core part that turns java code into native code for your specific operation system (OS).\n- **Java Runtime Enviroment (JRE)** - The part of Java that allows java applications to work. In turn it bundles the **JVM**\n- **Java Development Kit (JDK)** - The part of java that allows developers like Mojang to make Java based applications. Also includes the **JRE** and **JVM**\n\n**Java SE** is a closed source piece of software by **Oracle** that is different from the open source **OpenJDK** project. Either version works for **Minecraft**')

#drama command
@client.group()
async def drama(ctx):
    drama = requests.get('https://mc-drama.herokuapp.com/raw')
    await ctx.send(drama.text)

#fabric_drama command
@client.group()
async def fdrama(ctx):
    fdrama = requests.get('https://fabric-drama.herokuapp.com/txt')
    await ctx.send(fdrama.text)

#Stats Command
@client.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(title=f'{client.user.name} Stats',
                          description='\uFEFF',
                          colour=ctx.author.colour,
                          timestamp=ctx.message.created_at)

    embed.add_field(name='Python Version:', value=f"{pythonVersion}", inline=False)
    embed.add_field(name='Discord.PY Version', value=f"{dpyVersion}", inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developers:', value="<@543576276108181506>")

    embed.set_footer(text=f"Yours truly, | {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#Poll Command
@client.command(pass_context=True)
async def poll(ctx, *args):
	mesg = ' '.join(args)
	await ctx.message.delete()
	embed = discord.Embed(title='A Poll has Started !',
			      description='{0}'.format(mesg),
			      color=0x00FF00)
	
	embed.set_footer(text='Poll created by: {0} • React to vote!'.format(ctx.message.author))
	
	embed_message = await ctx.send(embed=embed)
	
	await embed_message.add_reaction( '👍')
	await embed_message.add_reaction('👎')
	await embed_message.add_reaction('🤷')


#Run Bot
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
