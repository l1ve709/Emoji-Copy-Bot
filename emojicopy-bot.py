########################################
##                                    ##
##   Support:                         ## 
##   Instagram :l1ve709               ##
##   Discord : unk709/l1ve709.com     ##
##                                    ##
##                                    ##
##     --Made By Ediz SÖNMEZ--        ##  
##                                    ##  
########################################
#  Emoji Copy Bot
#  Type "*start" to start
#  Bot must be on both servers

import discord
from discord.ext import commands
import aiohttp
import asyncio

intents = discord.Intents.all()   # "*" prefix
l1ve709 = commands.Bot(command_prefix='*', intents=intents)
l1ve709.run("YOUR_TOKEN") # DISCORD BOT TOKEN
sourceguild = 1259842026443112529  # SOURCE SERVER
copiedguild = 1269380269744459786  # COPIED SERVER

@l1ve709.event
async def on_ready():
    print(f'Bot : {l1ve709.user.name} is ready.')

@l1ve709.command()
@commands.has_permissions(administrator=True)
async def start(ctx):
    source_guild = l1ve709.get_guild(sourceguild)
    target_guild = l1ve709.get_guild(copiedguild)

    if source_guild is None or target_guild is None:
        await ctx.send("Source or target server not found.")
        return

    async with aiohttp.ClientSession() as session:
        for emoji in source_guild.emojis:
            try:
                async with session.get(emoji.url) as response:
                    image_data = await response.read()
                    await target_guild.create_custom_emoji(name=emoji.name, image=image_data)
                    await ctx.send(f"{emoji.name} emoji copied successfully.")
                    print(f"{emoji.name} emoji copied.")
                    await asyncio.sleep(1.5)  # wait 1.5 second to avoid rate ( optional )
            except Exception as e:
                await ctx.send(f"{emoji.name} An error occurred while copying the emoji: {e}")

    await ctx.send("All emojis copied successfully.")
