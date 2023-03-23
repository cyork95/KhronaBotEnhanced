import discord
import datetime
import aiosqlite
from easy_pil import Editor, load_image_async, Font, Canvas
from discord.ext import commands
from discord import app_commands


class leveling(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot

  @app_commands.command(name="level",
                    description="Check your current level!")
  async def level(self,interaction: discord.Interaction):
      author = interaction.user
      guild = interaction.guild
      async with aiosqlite.connect('databases/level.db') as db:
        async with db.execute("SELECT xp, level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id)) as cursor:
          result = await cursor.fetchone()
        try:
          xp = result[0]
          level = result[1]
        except TypeError:
          xp = 0
          level = 0

        user_data = {
          "name": f'{author}',
          "xp": xp,
          "level": level,
          "to_next_level": 100,
          "percentage": xp
        }

        background = Editor(Canvas((900, 300), color="#141414"))
        profile_picture = await load_image_async(str(author.avatar.url))
        profile = Editor(profile_picture).resize((150,150)).circle_image()

        montserrat = Font.montserrat(size=40)
        montserrat_small = Font.montserrat(size=30)

        light_grey_color = "#777777"
        gold_color = "#d4af37"
        darker_grey_color = "#5a6064"
        off_white_color = "#FAF9F6"
        medium_blue_color = "#006EB6"

        card_right_shape = [(600, 0), (750, 300), (900, 300), (900, 0)]

        background.polygon(card_right_shape, color=medium_blue_color)
        background.paste(profile, (30, 30))
        background.rectangle((30, 220), width=650, height=40, color=darker_grey_color)
        background.bar((30, 220), max_width=650, height=40, percentage=user_data["percentage"], color=gold_color)
        background.text((200, 40), user_data["name"], font=montserrat, color=off_white_color)
        background.rectangle((200, 100), width=350, height=5, fill=gold_color)
        background.text(
          (200, 130), 
          f"Level - {user_data['level']} | XP - {user_data['xp']}/{user_data['to_next_level']}",
          font = montserrat_small,
          color = off_white_color
        )
        file = discord.File(fp=background.image_bytes, filename="levelcard.png")
        await interaction.response.send_message(file=file)     
    
async def setup(bot: commands.Bot):
  await bot.add_cog(leveling(bot))

