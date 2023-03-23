import discord
import requests
from discord.ext import commands
from discord import app_commands


class apis(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot

  @app_commands.command(name="affirmation",
                    description="Retrieve an affirmation!")
  async def affirmation(self, interaction: discord.Interaction):
    try:
        response = requests.get('https://www.affirmations.dev/')
        data = response.json()
        embed = discord.Embed(title="Affirmation", description=data['affirmation'], color=discord.Color.gold())
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
        await self.error_channel.send(f"Error: {e}")
        await interaction.response.send_message("I tried to search but found nothing :(")  

  @app_commands.command(name="advice",
                    description="Recieve advice!")
  async def advice(self, interaction: discord.Interaction):
    try:
        response = requests.get('https://api.adviceslip.com/advice')
        data = response.json()
        embed = discord.Embed(title="Advice", description=data['slip']['advice'], color=discord.Color.gold())
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
        await self.error_channel.send(f"Error: {e}")
        await interaction.response.send_message("I tried to search but found nothing :(")  

async def setup(bot: commands.Bot):
  await bot.add_cog(apis(bot))
