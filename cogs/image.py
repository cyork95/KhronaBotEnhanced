import discord
import requests
import os
import datetime
from discord.ext import commands
from discord import app_commands


class image(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot
    self.error_channel = None
    
  @app_commands.command(name="cat", description="Displays a random image of a cat!")
  async def cat(self, interaction: discord.Interaction):
    url = 'https://api.unsplash.com/photos/random/?query=cat&orientation=landscape'
    headers = {'Authorization': 'Client-ID ' + os.getenv('UNSPLASH_ACCESS_KEY')}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    image_url = json_data['urls']['regular']
    image_description = json_data['description']
    image_photographer_name = json_data['user']['name']
    image_photographer_username = json_data['user']['username']
    image_photographer_link = json_data['user']['links']['html']
    embed = discord.Embed(title="Your image search for Cat!",
                            description=f'{image_description} \n By [{image_photographer_name} ({image_photographer_username})]({image_photographer_link}) on [Unsplash](https://unsplash.com/)',
                          color=discord.Color.gold(),
                          timestamp=datetime.datetime.now()
                          )
    embed.set_image(url=f'{image_url}')
    await interaction.response.send_message(embed=embed)

  @app_commands.command(name="dog", description="Displays a random image of a dog!")
  async def dog(self, interaction: discord.Interaction):
    url = 'https://api.unsplash.com/photos/random/?query=dog&orientation=landscape'
    headers = {'Authorization': 'Client-ID ' + os.getenv('UNSPLASH_ACCESS_KEY')}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    image_url = json_data['urls']['regular']
    image_description = json_data['description']
    image_photographer_name = json_data['user']['name']
    image_photographer_username = json_data['user']['username']
    image_photographer_link = json_data['user']['links']['html']
    embed = discord.Embed(title="Your image search for Dog!",
                            description=f'{image_description} \n By [{image_photographer_name} ({image_photographer_username})]({image_photographer_link}) on [Unsplash](https://unsplash.com/)',
                          color=discord.Color.gold(),
                          timestamp=datetime.datetime.now()
                          )
    embed.set_image(url=f'{image_url}')
    await interaction.response.send_message(embed=embed)

  @app_commands.command(name="image", description="Displays a random image of your search!")
  async def image(self, interaction: discord.Interaction, image: str):
    try:
      cleaned_image = image.replace(" ", "-")
      cleaned_image = cleaned_image.replace("'", "")
      url = f'https://api.unsplash.com/photos/random/?query={cleaned_image}&orientation=landscape'
      headers = {'Authorization': 'Client-ID ' + os.getenv('UNSPLASH_ACCESS_KEY')}
      response = requests.get(url, headers=headers)
      json_data = response.json()
      image_url = json_data['urls']['regular']
      image_description = json_data['description']
      image_photographer_name = json_data['user']['name']
      image_photographer_username = json_data['user']['username']
      image_photographer_link = json_data['user']['links']['html']
      embed = discord.Embed(title=f"Your image search for {image}!",
                            description=f'{image_description} \n By [{image_photographer_name} ({image_photographer_username})]({image_photographer_link}) on [Unsplash](https://unsplash.com/)',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_image(url=f'{image_url}')
      await interaction.response.send_message(embed=embed)
    except Exception as e:
        self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
        await self.error_channel.send(f"Error: {e}")
        await interaction.channel.send("I tried to search but found nothing :(")        

async def setup(bot: commands.Bot):
  await bot.add_cog(image(bot))
