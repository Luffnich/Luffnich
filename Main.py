import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} sudah ON!')

@bot.event
async def on_member_join(member):
    # Bot akan cari channel bernama 'selamat-datang'
    channel = discord.utils.get(member.guild.text_channels, name='selamat-datang')
    if channel:
        await channel.send(f"Halo {member.mention}, selamat datang! 🎉")

bot.run(os.getenv('DISCORD_TOKEN'))
