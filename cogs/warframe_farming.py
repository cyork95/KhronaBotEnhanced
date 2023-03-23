import discord
import datetime
from discord.ext import commands
from discord import app_commands


class farming(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot

  @app_commands.command(name="farm",
                    description="Retrieve farming info for a resource!")
  async def calc(self, interaction: discord.Interaction, *, resource: str):
    embed = discord.Embed(title=f"Farming Details for {resource}",
                          color=discord.Color.gold(),
                          timestamp=datetime.datetime.now()
                          )
    if resource.lower() == "nano spores" or resource.lower() == "nano spore" or resource.lower() == "nano":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087511081930473502/latest.png')
      embed.add_field(name="Best Place to Farm", value="Eris (Akkad) a Defense Mission with level 35-45 infested.")
      embed.add_field(name="Other Places to Farm", value="Saturn (Piscinas), Deimos (Hyf), Deimos (Terrorem).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "credits" or resource.lower() == "credit" or resource.lower() == "money":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087515240192807072/latest.png')
      embed.add_field(name="Best Place to Farm", value="The Index on Neptune.")
      embed.add_field(name="Other Places to Farm", value="The Index on Neptune.")
      embed.add_field(name="Recommended Farming Method", value="Any Index Built Frame (think low energy but high survivability).")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "affinity" or resource.lower() == "xp" or resource.lower() == "exp":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087516232326074419/latest.png')
      embed.add_field(name="Best Place to Farm", value="Sedna (Hydron) a defense mission with level 30-40 enemies.")
      embed.add_field(name="Other Places to Farm", value="Sedna (Hydron).")
      embed.add_field(name="Recommended Farming Method", value="Whatever needs experience.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "axi" or resource.lower() == "axi relic" or resource.lower() == "axi relics":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087517816225275995/350.png')
      embed.add_field(name="Best Place to Farm", value="Sedna (Hydron) a defense mission with level 30-40 enemies. Rotation B and C meaning every 15 and 20 rounds.")
      embed.add_field(name="Other Places to Farm", value="Pluto (Hieracon) an excavation mission with level 35-45. Rotation B has Neo Relics and Rotation C has Axi Relics meaning every third an fourth excavator completion you can get a relic.")
      embed.add_field(name="Recommended Farming Method", value="Anything that completes the mission.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "neo" or resource.lower() == "neo relic" or resource.lower() == "neo relics":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087518434620878929/350.png')
      embed.add_field(name="Best Place to Farm", value="Sedna (Hydron) a defense mission with level 30-40 enemies. Rotation A meaning every 5 and 10 rounds.")
      embed.add_field(name="Other Places to Farm", value="Pluto (Hieracon) an excavation mission with level 35-45. Rotation B has Neo Relics and Rotation C has Axi Relics meaning every third an fourth excavator completion you can get a relic.")
      embed.add_field(name="Recommended Farming Method", value="Anything that completes the mission.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "meso" or resource.lower() == "meso relic" or resource.lower() == "meso relics":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087518894849273886/350.png')
      embed.add_field(name="Best Place to Farm", value="Jupiter (IO) a defense mission with level 15-20 enemies. Rotation A meaning every 5 and 10 rounds.")
      embed.add_field(name="Other Places to Farm", value="Jupiter (IO) a defense mission with level 15-20 enemies. Rotation A meaning every 5 and 10 rounds.")
      embed.add_field(name="Recommended Farming Method", value="Anything that completes the mission.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "lith" or resource.lower() == "lith relic" or resource.lower() == "lith relics":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087519393082253352/350.png')
      embed.add_field(name="Best Place to Farm", value="Mars (Spear) a defense mission with level 8-13 enemies. Rotation A meaning every 5 and 10 rounds.")
      embed.add_field(name="Other Places to Farm", value="Mars (Spear) a defense mission with level 8-13 enemies. Rotation A meaning every 5 and 10 rounds.")
      embed.add_field(name="Recommended Farming Method", value="Anything that completes the mission.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "req" or resource.lower() == "req relic" or resource.lower() == "req relics" or resource.lower() == "requiem" or resource.lower() == "requiem relic" or resource.lower() == "requiem relics":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087520206961774602/350.png')
      embed.add_field(name="Best Place to Farm", value="Completing Kuva Flood, Kuva Siphons, Killing a Lich Thralls, or Sister Hounds.")
      embed.add_field(name="Other Places to Farm", value="Completing Kuva Siphons, Killing a Lich Thralls, or Sister Hounds.")
      embed.add_field(name="Recommended Farming Method", value="Anything that completes the mission.")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "alloy plate" or resource.lower() == "alloy plates" or resource.lower() == "alloy":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087522405028741200/350.png')
      embed.add_field(name="Best Place to Farm", value="Ceres (Gabii) a Survival mission with level 15-25 grineer.")
      embed.add_field(name="Other Places to Farm", value="Ceres (Draco), Venus (Tessera), Sedna (Berehynia).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "salvage":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087523445140631593/350.png')
      embed.add_field(name="Best Place to Farm", value="Jupiter (Cameria) a Survival mission with level 20-30 corpus.")
      embed.add_field(name="Other Places to Farm", value="Mars (Wahiba).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "rubedo":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087523856941592596/350.png')
      embed.add_field(name="Best Place to Farm", value="Phobos (Zeugma) a Survival mission with level 15-25 grineer.")
      embed.add_field(name="Other Places to Farm", value="Phobos (Stickney).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "plastid" or resource.lower() == "plastids":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087524304343802048/350.png')
      embed.add_field(name="Best Place to Farm", value="Uranus (Stephano) a Defense mission with level 24-29 grineer.")
      embed.add_field(name="Other Places to Farm", value="Saturn (Piscinas), Eris (Akkad), Uranus (Ophelia).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "circuit" or resource.lower() == "circuits":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087525133935186011/350.png')
      embed.add_field(name="Best Place to Farm", value="Ceres (Seimeni) a Defense mission with level 15-25 grineer.")
      embed.add_field(name="Other Places to Farm", value="Venus (Tessara), Ceres (Gabii), Venus (Romula).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "orokin cell" or resource.lower() == "orokin cells" or resource.lower() == "orokin":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087525737403252736/350.png')
      embed.add_field(name="Best Place to Farm", value="Ceres (Lex) a Capture mission with level 14-16 grineer. Make sure to look for the cell arrays before leaving the mission.")
      embed.add_field(name="Other Places to Farm", value="Ceres (Exta), Ceres (Gabii), Saturn (Piscinas).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    elif resource.lower() == "argon crstals" or resource.lower() == "argon crystal" or resource.lower() == "argon" or resource.lower() == "argons":
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/993002350790840410/1087527502165057697/350.png')
      embed.add_field(name="Best Place to Farm", value="Void (Teshub) an Exterminate mission with level 1o-15 corrupted. Make sure to look for the argon crstals on the map before leaving the mission.")
      embed.add_field(name="Other Places to Farm", value="Void (Ani), Void (Stribog), Void (Oxomoco).")
      embed.add_field(name="Recommended Farming Method", value="Nekros Despoil Desicrate, Hydroid Pilfering Swarm, Khora Pilfering Stangledome,  Atlas Ore Gaze Petrify")
      await interaction.response.send_message(embed=embed)
    else:
      await interaction.response.send_message(f"Sorry I cant find the resource {resource}. Can you try again with a different name?")


async def setup(bot: commands.Bot):
  await bot.add_cog(farming(bot))
