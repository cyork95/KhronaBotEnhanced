import discord
from discord.ext import commands
from discord import app_commands


class calculate(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot

  @app_commands.command(name="calc",
                    description="Retrieve user info!")
  async def calc(self, interaction: discord.Interaction, *, expression: str):
    try:
        result = eval(expression)
    except Exception as e:
        await interaction.response.send_message(f"Error evaluating expression: {str(e)}")
        return
    await interaction.response.send_message(f"{expression} = {result}")

async def setup(bot: commands.Bot):
  await bot.add_cog(calculate(bot))
