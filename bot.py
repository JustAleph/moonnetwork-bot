import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time

import os

client = commands.Bot(command_prefix= "!")
client.remove_command('help')

chat_filter = ["!ip", "!ip",]
bypass_list = []

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Nu actief in " + str(len(client.servers)) + " server(s)."))
    await asyncio.sleep(20)
    await client.change_presence(game=discord.Game(name="!help"))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
        if message.content.startswith('!help'):
            embed=discord.Embed(title="Dit zijn mijn commando's", url="", color=0x3498db)
            embed.set_author(name="MoonNetwork", icon_url="https://cdn.discordapp.com/icons/536582250721181737/a0595aceb96d5883aa08b338c787f8b0.png")
            embed.add_field(name="!ip", value="krijg het IP van de server", inline=False)
            embed.add_field(name="test", value="test", inline=False)
            embed.add_field(name="!help", value="krijg dit bericht", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/426246972853190657.gif?v=1")
            embed.set_footer(text="MoonNetwork bot © 2018 | gemaakt door @JustAleph#0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)
 
        elif message.content.startswith('!ip'):
            embed=discord.Embed(title="dit is het IP van de server!", url="", color=0x3498db)
            embed.set_author(name="MoonNetwork", icon_url="https://cdn.discordapp.com/icons/536582250721181737/a0595aceb96d5883aa08b338c787f8b0.png")
            embed.add_field(name="hier onder staat het ip", value="ip nog niet beschikbaar. de server gaat binnenkort open!", inline=False)
            embed.add_field(name="test", value="test", inline=False)
            embed.add_field(name="!help", value="krijg meer informatie over deze bot", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/426246972853190657.gif?v=1")
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph#0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)

        elif message.content.startswith('!test'):
            embed=discord.Embed(title="test", url="https://cdn.discordapp.com/icons/536582250721181737/a0595aceb96d5883aa08b338c787f8b0.png", color=0x3498db)
            embed.set_author(name="MoonNetwork", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            embed.add_field(name="test", value="test", inline=False)
            embed.add_field(name="test", value="test", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/426246972853190657.gif?v=1")
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph#0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            sent = await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)

client.run(os.environ["BOT_TOKEN"])
