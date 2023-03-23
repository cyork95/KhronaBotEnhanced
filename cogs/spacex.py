import discord
import requests
import os
from discord.ext import commands
from discord import app_commands


class api(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot
    self.error_channel = None

  @app_commands.command(name="spacex_launch",
                    description="Retrieve spacex most recent launch info!")
  async def spacex_launch(self, interaction: discord.Interaction):
    try:
        response = requests.get('https://api.spacexdata.com/v4/launches/latest')
        data = response.json()
        embed = discord.Embed(title=data['name'], description=data['details'], color=discord.Color.gold())
        embed.add_field(name='Flight Number', value=data['flight_number'], inline=True)
        embed.add_field(name='Launch Date', value=data['date_utc'], inline=True)
        embed.add_field(name='Was it successful?', value=data['success'], inline=True)
        embed.add_field(name='Reddit', value=data['links']['reddit']['launch'], inline=False)
        embed.add_field(name='Press Kit', value=data['links']['presskit'], inline=False)
        embed.add_field(name='Webcast', value=data['links']['webcast'], inline=False)
        embed.add_field(name='Article', value=data['links']['article'], inline=False)
        embed.add_field(name='Wikipedia', value=data['links']['wikipedia'], inline=False)
        embed.set_thumbnail(url=data['links']['patch']['small'])
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
        await self.error_channel.send(f"Error: {e}")
        await interaction.response.send_message("I tried to search but found nothing :(")     
        return

  @app_commands.command(name="spacex_roadster",
                    description="Retrieve spacex roadster in space info!")
  async def spacex_roadster(self, interaction: discord.Interaction):
    try:
        response = requests.get('https://api.spacexdata.com/v4/roadster/')
        data = response.json()
        embed = discord.Embed(title=data['name'], description=data['details'], color=discord.Color.gold())
        embed.add_field(name='Orbit Type', value=data['orbit_type'], inline=True)
        embed.add_field(name='Apoapsis', value=data['apoapsis_au'], inline=True)
        embed.add_field(name='Periapsis', value=data['periapsis_au'], inline=True)
        embed.add_field(name='Semi Major Axis', value=data['semi_major_axis_au'], inline=True)
        embed.add_field(name='Eccentricity', value=data['eccentricity'], inline=True)
        embed.add_field(name='Inclination', value=data['inclination'], inline=True)
        embed.add_field(name='Longitude', value=data['longitude'], inline=True)
        embed.add_field(name='Days in Space', value=data['period_days'], inline=True)
        embed.add_field(name='Speed', value=f"{data['speed_kph']} kph, {data['speed_mph']} mph", inline=False)
        embed.add_field(name='Distance form Earth', value=f"{data['earth_distance_km']} km, {data['earth_distance_mi']} mi", inline=False)
        embed.add_field(name='Distance form Mars', value=f"{data['mars_distance_km']} km, {data['mars_distance_mi']} mi", inline=False)
        embed.add_field(name='Launch Date', value=data['launch_date_utc'], inline=False)
        embed.add_field(name='Wikipedia', value=data['wikipedia'], inline=False)
        embed.add_field(name='Video', value=data['video'], inline=False)
        embed.set_thumbnail(url=data['flickr_images'][0])
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
        await self.error_channel.send(f"Error: {e}")
        await interaction.response.send_message("I tried to search but found nothing :(")     
        return

async def setup(bot: commands.Bot):
  await bot.add_cog(api(bot))
