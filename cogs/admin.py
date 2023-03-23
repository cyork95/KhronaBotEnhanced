import discord
import datetime
import os
from discord.ext import commands
from discord import app_commands


class admin(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot
    self.mute_role = None

  @app_commands.command(name="kick",
                        description="Kick someone from the server")
  @app_commands.checks.has_permissions(kick_members=True)
  async def kick(self, interaction: discord.Interaction,
                 member: discord.Member, reason: str):
    await member.kick()
    await interaction.response.send_message(f'{member} has been kicked at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')

  @app_commands.command(name="ban", 
                        description="Ban someone from the server")
  @app_commands.checks.has_permissions(ban_members=True)
  async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    await member.ban()
    await interaction.response.send_message(f'{member} has been banned at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')

  @app_commands.command(name="unban", 
                        description="Unban someone from the server")
  @app_commands.checks.has_permissions(ban_members=True)
  async def unban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    await member.unban()
    await interaction.response.send_message(f'{member} has been unbanned at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')

  @app_commands.command(name="mute", 
                        description="Mute someone in the server")
  @app_commands.checks.has_permissions(kick_members=True)
  async def mute(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    self.mute_role = member.guild.get_role(int(os.getenv("MUTE_ROLE")))
    await member.add_roles(self.mute_role, reason=reason)
    await interaction.response.send_message(f'{member} has been muted at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')  

  @app_commands.command(name="unmute", 
                        description="Unmute someone in the server")
  @app_commands.checks.has_permissions(kick_members=True)
  async def unmute(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    self.mute_role = member.guild.get_role(int(os.getenv("MUTE_ROLE")))
    await member.remove_roles(self.mute_role, reason=reason)
    await interaction.response.send_message(f'{member} has been unmuted at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')  

  @app_commands.command(name="slowmode", 
                        description="Start slowmode for a channel!")
  @app_commands.checks.has_permissions(manage_messages=True)
  async def unmute(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    self.mute_role = member.guild.get_role(int(os.getenv("MUTE_ROLE")))
    await member.remove_roles(self.mute_role, reason=reason)
    await interaction.response.send_message(f'{member} has been unmuted at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} for {reason}!')  

  @app_commands.command(name="clear", 
                        description="Clear some messages!")
  @app_commands.checks.has_permissions(manage_messages=True)
  async def clear(self, interaction: discord.Interaction, count: int):
    await interaction.response.send_message(f'{count} message(s) have/has been removed!')
    await interaction.channel.purge(limit=count)

async def setup(bot: commands.Bot):
  await bot.add_cog(admin(bot))
