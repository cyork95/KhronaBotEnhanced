import discord
import requests
import datetime
import os
from discord.ext import commands, tasks
from discord import app_commands


class warframe_worldstate(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot
    self.alerts_channel = None
    self.error_channel = None
    #self.cambian_drift_task.start()
    #self.cetus_task.start()
    #self.vallis_task.start()
    #self.archon_task.start()
    #self.sortie_task.start()
    #self.invasion_task.start()

  @tasks.loop(hours=1)
  async def cambian_drift_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    base_url = "https://api.warframestat.us/xb1/cambionCycle/"
    response = requests.get(base_url)
    if response.status_code == 200:
      data = response.json()
      embed = discord.Embed(title="Cambion Drift State",
                            description='Here is the current Cambion Drift state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086932031260336178/Zw.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['timeLeft'])
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel = self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
    
  
  @cambian_drift_task.before_loop
  async def before_cambrion_drift(self):
    await self.bot.wait_until_ready()


  
  
  @tasks.loop(hours=1)
  async def cetus_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    base_url = "https://api.warframestat.us/xb1/cetusCycle/"
    response = requests.get(base_url)
    if response.status_code == 200:
      data = response.json()
      embed = discord.Embed(title="Cetus State",
                            description='Here is the current Cetus state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086943772761399356/aWRvbG9uLnBuZw.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['shortString'])
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel = self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
    
  
  @cetus_task.before_loop
  async def before_cetus(self):
    await self.bot.wait_until_ready()

 
  @tasks.loop(hours=1)
  async def vallis_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/vallisCycle/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      # do something with the data, for example print the results
      embed = discord.Embed(title="Orb Vallis State",
                            description='Here is the current Cetus state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086944840299855962/bA.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['shortString'])
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel =  self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
  
  vallis_task.before_loop
  async def before_vallis(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    await self.bot.wait_until_ready()

  @tasks.loop(hours=8)
  async def sortie_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    base_url = "https://api.warframestat.us/xb1/sortie/"
    response = requests.get(base_url)
    if response.status_code == 200:
      data = response.json()
      missions = [data['variants'][0], data['variants'][1], data['variants'][2]]
      embed = discord.Embed(title="Current Sortie",
                            description='Here is the current Sortie!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086946234297753660/LmpwZw.png')
      embed.add_field(name="Boss", value=data['boss'])
      embed.add_field(name="Faction", value=data['faction'])
      embed.add_field(name="Ending", value=data['eta'])
      embed.add_field(name="Mission 1", value=f"{missions[0]['missionType']} on {missions[0]['node']} with modifier: {missions[0]['modifierDescription']}", inline=False)
      embed.add_field(name="Mission 2", value=f"{missions[1]['missionType']} on {missions[1]['node']} with modifier: {missions[1]['modifierDescription']}", inline=False)
      embed.add_field(name="Mission 3", value=f"{missions[2]['missionType']} on {missions[2]['node']} with modifier: {missions[2]['modifierDescription']}", inline=False)
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel = self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
    
  
  @sortie_task.before_loop
  async def before_sortie(self):
    await self.bot.wait_until_ready()
  
  @tasks.loop(hours=8)
  async def archon_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    base_url = "https://api.warframestat.us/xb1/archonHunt/"
    response = requests.get(base_url)
    if response.status_code == 200:
      data = response.json()
      missions = [data['missions'][0], data['missions'][1], data['missions'][2]]
      embed = discord.Embed(title="Current Archon Hunt",
                            description='Here is the current Archon Hunt!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086954981187407882/LmpwZw.png')
      embed.add_field(name="Boss", value=data['boss'])
      embed.add_field(name="Faction", value=data['faction'])
      embed.add_field(name="Ending", value=data['eta'])
      embed.add_field(name="Mission 1", value=f"{missions[0]['typeKey']} on {missions[0]['nodeKey']}. Archwing? {missions[0]['archwingRequired']}", inline=False)
      embed.add_field(name="Mission 2", value=f"{missions[1]['typeKey']} on {missions[1]['nodeKey']}.  Archwing? {missions[1]['archwingRequired']}", inline=False)
      embed.add_field(name="Mission 3", value=f"{missions[2]['typeKey']} on {missions[2]['nodeKey']}. Archwing? {missions[2]['archwingRequired']}", inline=False)
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel = self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
    
 
  @archon_task.before_loop
  async def before_archon(self):
    await self.bot.wait_until_ready()

  
  @tasks.loop(hours=4)
  async def invasion_task(self):
    self.alerts_channel = self.bot.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    url = "https://api.warframestat.us/xb1/invasions"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      embed = discord.Embed(title="Current Invasions",
                            description='Here is the current Invasions!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
      )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087415596452425918/latest.png')
      for invasion in data:
          node = invasion["node"]
          desc = invasion["desc"]        
          attacker = invasion["attackingFaction"]
          attacker_reward = invasion["attackerReward"]["asString"]
          if attacker_reward == "" or attacker_reward == " ":
            attacker_reward = "NOTHING"
          defender = invasion["defendingFaction"]
          defender_reward = invasion["defenderReward"]["asString"]
          if defender_reward == "" or defender_reward == " ":
            defender_reward = "NOTHING"
          eta = invasion["eta"]
          embed.add_field(name=f"{attacker} vs {defender}", value=f"{node} - {attacker} are giving {attacker_reward} and {defender} are giving {defender_reward}\n{desc}\nETA: {eta}", inline=False)
      await self.alerts_channel.send(embed=embed)
    else:
      self.error_channel = self.bot.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
    
  
  @invasion_task.before_loop
  async def before_invasion(self):
    await self.bot.wait_until_ready()

  @app_commands.command(name="cambion",
                    description="Retrieve cambion drift state!")
  async def cambion(self, interaction: discord.Interaction):
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/cambionCycle/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      # do something with the data, for example print the results
      embed = discord.Embed(title="Cambion Drift state",
                            description='Here is the current Cambion Drift state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086932031260336178/Zw.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['timeLeft'])
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"State sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)
  
  
  @app_commands.command(name="cetus",
                    description="Retrieve Cetus state!")
  async def cetus(self, interaction: discord.Interaction):
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/cetusCycle/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      # do something with the data, for example print the results
      embed = discord.Embed(title="Cetus State",
                            description='Here is the current Cetus state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086943772761399356/aWRvbG9uLnBuZw.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['shortString'])
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"State sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)

  
  
  @app_commands.command(name="vallis",
                    description="Retrieve Orb Vallis state!")
  async def vallis(self, interaction: discord.Interaction):
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/vallisCycle/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      # do something with the data, for example print the results
      embed = discord.Embed(title="Orb Vallis State",
                            description='Here is the current Cetus state!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086944840299855962/bA.png')
      embed.add_field(name="Current State", value=data['state'])
      embed.add_field(name="Time Left", value=data['shortString'])
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"State sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)
  
 
  @app_commands.command(name="sortie",
                    description="Retrieve current Sortie details!")
  async def sortie(self, interaction: discord.Interaction):
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/sortie/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      missions = [data['variants'][0], data['variants'][1], data['variants'][2]]
      # do something with the data, for example print the results
      embed = discord.Embed(title="Current Sortie",
                            description='Here is the current Sortie!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086946234297753660/LmpwZw.png')
      embed.add_field(name="Boss", value=data['boss'])
      embed.add_field(name="Faction", value=data['faction'])
      embed.add_field(name="Ending", value=data['eta'])
      embed.add_field(name="Mission 1", value=f"{missions[0]['missionType']} on {missions[0]['node']} with modifier: {missions[0]['modifierDescription']}", inline=False)
      embed.add_field(name="Mission 2", value=f"{missions[1]['missionType']} on {missions[1]['node']} with modifier: {missions[1]['modifierDescription']}", inline=False)
      embed.add_field(name="Mission 3", value=f"{missions[2]['missionType']} on {missions[2]['node']} with modifier: {missions[2]['modifierDescription']}", inline=False)
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"Sortie sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)

 
  @app_commands.command(name="archon",
                    description="Retrieve current Archon details!")
  async def Archon(self, interaction: discord.Interaction):
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
     # define the base URL for the Warframe API
    base_url = "https://api.warframestat.us/xb1/archonHunt/"
    response = requests.get(base_url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
      # access the response data in JSON format
      data = response.json()
      missions = [data['missions'][0], data['missions'][1], data['missions'][2]]
      # do something with the data, for example print the results
      embed = discord.Embed(title="Current Archon Hunt",
                            description='Here is the current Archon Hunt!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1086954981187407882/LmpwZw.png')
      embed.add_field(name="Boss", value=data['boss'])
      embed.add_field(name="Faction", value=data['faction'])
      embed.add_field(name="Ending", value=data['eta'])
      embed.add_field(name="Mission 1", value=f"{missions[0]['typeKey']} on {missions[0]['nodeKey']}. Archwing? {missions[0]['archwingRequired']}", inline=False)
      embed.add_field(name="Mission 2", value=f"{missions[1]['typeKey']} on {missions[1]['nodeKey']}.  Archwing? {missions[1]['archwingRequired']}", inline=False)
      embed.add_field(name="Mission 3", value=f"{missions[2]['typeKey']} on {missions[2]['nodeKey']}. Archwing? {missions[2]['archwingRequired']}", inline=False)
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"Sortie sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)

 
  @app_commands.command(name="invasion",
                    description="Retrieve current Invasion details!")
  async def invasion(self, interaction: discord.Interaction):
    """Gets the current invasions data from the Warframe API and sends it as an embed."""
    self.alerts_channel = interaction.guild.get_channel(int(os.getenv("WARFRAME_ALERTS_CHANNEL")))
    url = "https://api.warframestat.us/xb1/invasions"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      embed = discord.Embed(title="Current Invasions",
                            description='Here is the current Invasions!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
      )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087415596452425918/latest.png')
      for invasion in data:
          node = invasion["node"]
          desc = invasion["desc"]        
          attacker = invasion["attackingFaction"]
          attacker_reward = invasion["attackerReward"]["asString"]
          if attacker_reward == "" or attacker_reward == " ":
            attacker_reward = "NOTHING"
          defender = invasion["defendingFaction"]
          defender_reward = invasion["defenderReward"]["asString"]
          if defender_reward == "" or defender_reward == " ":
            defender_reward = "NOTHING"
          eta = invasion["eta"]
          embed.add_field(name=f"{attacker} vs {defender}", value=f"{node} - {attacker} are giving {attacker_reward} and {defender} are giving {defender_reward}\n{desc}\nETA: {eta}", inline=False)
      await self.alerts_channel.send(embed=embed)
      await interaction.response.send_message(f"Invasions sent to {self.alerts_channel.mention}", ephemeral=True)
    else:
      self.error_channel = interaction.guild.get_channel(int(os.getenv("BOT_WORK_CHANNEL")))
      await self.error_channel.send(f"Error: {response.status_code}, {response.reason}")
      await interaction.response.send_message("Oops something went wrong let CoYoFroYo know!", ephemeral=True)

async def setup(bot: commands.Bot):
  await bot.add_cog(warframe_worldstate(bot))
