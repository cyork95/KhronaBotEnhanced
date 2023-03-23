import discord
import datetime
import os
from discord.ext import commands
from discord import app_commands

class info(commands.Cog):
  def __init__(self, bot: commands.bot):
    self.bot = bot


  @app_commands.command(name="userinfo",
                    description="Retrieve user info!")
  async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
      if member is None:
          member = interaction.user
      roles = [role for role in member.roles]
      embed = discord.Embed(title="User Info",
                            description=f'Here is the user info on the user {member.name}',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url=member.avatar)
      embed.add_field(name="ID", value=member.id)
      embed.add_field(name="Name", value=f'{member.name}#{member.discriminator}')
      embed.add_field(name="Nickname", value=member.display_name)
      embed.add_field(name="Status", value=member.status)
      embed.add_field(name="Created At", value=member.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
      embed.add_field(name="Joined At", value=member.joined_at.strftime("%m/%d/%Y, %H:%M:%S"))
      embed.add_field(name=f"Roles ({len(roles)})", value=' '.join([role.mention for role in roles]))
      embed.add_field(name="Top Role", value=member.top_role.mention)
      embed.add_field(name="Messages", value="0")
      embed.add_field(name="Bot?", value=member.bot)
      await interaction.response.send_message(embed=embed)


  @app_commands.command(name="serverinfo",
                    description="Retrieve user info!")
  async def serverinfo(self, interaction: discord.Interaction):
      embed = discord.Embed(title="Server Info",
                            description=f'Here is the server info on the server {interaction.guild.name}',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url=interaction.guild.icon)
      embed.add_field(name="Members", value=interaction.guild.member_count)
      embed.add_field(name="Channels",
                      value=f"{len(interaction.guild.text_channels)} text | {len(interaction.guild.voice_channels)} voice")
      embed.add_field(name="Owner", value=interaction.guild.owner.mention)
      embed.add_field(name="Description", value=interaction.guild.description)
      embed.add_field(name="Created At", value=interaction.guild.owner.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
      await interaction.response.send_message(embed=embed)

  @app_commands.command(name="botinfo",
                    description="Retrieve bot info!")
  async def botinfo(self, interaction: discord.Interaction):
      khrona = self.bot.get_user(int(os.getenv('KHRONA_ID')))
      embed = discord.Embed(title="Cephalon Khrona Information",
                            description='Hello! I am Khrona a bot created in Python and being hosted by Replit! I was built with love by CoYoFroYo!',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.now()
                            )
      embed.set_thumbnail(url=khrona.avatar)
      embed.add_field(name="Find my Code on Github: ", value="https://github.com/cyork95/KhronaBotEnhanced")
      embed.add_field(name="Find my Replit", value="https://replit.com/@CoYoFroYo/KhronaBot?v=1")
      embed.add_field(name="Bot Owner", value="@CoYoFroYo")
      embed.add_field(name="Created At", value=khrona.joined_at.strftime("%m/%d/%Y, %H:%M:%S"))
      await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
  await bot.add_cog(info(bot))