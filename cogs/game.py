import discord
import random
import os
import asyncio
from discord.ext import commands
from discord import app_commands


class game(commands.Cog):

  def __init__(self, bot: commands.bot):
    self.bot = bot

  @app_commands.command(name="roll", description="Roll Dice")
  async def roll(self, interaction: discord.Interaction, num_dice: int,
                 num_sides: int):
    dice = [random.randint(1, num_sides) for i in range(num_dice)]
    total = sum(dice)
    await interaction.response.send_message(
      f"Rolling {num_dice}d{num_sides}: {dice}\nTotal: {total}")

  @app_commands.command(
    name="guess", description="Play guess the number! Say 'quit' to stop!")
  async def guess(self, interaction: discord.Interaction, max: int = 10):
    MAX_GUESSES = int(os.getenv('MAX_GUESSES'))
    secret_number = random.randint(1, max)

    await interaction.response.send_message(
      f"I'm thinking of a number between 1 and {max}. Can you guess what it is?"
    )

    def check(m):
      return m.author == interaction.user and m.channel == interaction.channel

    for i in range(MAX_GUESSES):
      try:
        guess_message = await self.bot.wait_for('message',
                                                    check=check,
                                                    timeout=10.0)
        if guess_message.content.lower() == 'quit':
          await interaction.channel.send("Okay, stopping!")
          return
        try:
          guess_content = int(guess_message.content)
          if str(guess_content) == str(secret_number):
            await interaction.channel.send(
              f'Congratulations, you guessed it! The number was {secret_number}. It took you {i + 1} trys!'
            )
            return
          elif guess_content < secret_number:
            await interaction.channel.send("Higher!")
          else:
            await interaction.channel.send("Lower!")
        except Exception as e:
          await interaction.channel.send("Please send a number!")
          print(e)
      except Exception as e:
        await interaction.channel.send("Timed out!")
        print(e)
        return
    await interaction.channel.send(
      f"You ran out of trys! The number was {secret_number}!")

  @app_commands.command(
    name="choose",
    description="Let the bot pick between thoughts! Put a ',' between choices!"
  )
  async def choose(self, interaction: discord.Interaction, args: str):
    arguments = args.split(",")
    choice = random.choice(arguments)
    thinking = await interaction.channel.send(":clock1: Thinking...")
    for i in range(4):
      await thinking.edit(content=f':clock{i + 1}: Thinking...')
      await asyncio.sleep(0.2)
    await interaction.response.send_message(choice)


  @app_commands.command(name="coinflip", description="Flip a coin!")
  @app_commands.choices(choices=[
  app_commands.Choice(name="Heads", value="heads"),
  app_commands.Choice(name="Tails", value="tails")
  ])
  async def coinflip(self, interaction: discord.Interaction,
                    choices: app_commands.Choice[str]):
    values = ['heads', 'tails']
    bot_choice = random.choice(values)
    if bot_choice == choices.value:
      await interaction.response.send_message(
        f'You guessed correctly! It was {choices.value}!')
    else:
      await interaction.response.send_message(
        f'You guessed incorrectly! It was {bot_choice}!')

  @app_commands.command(
    name="secret",
    description="..."
  )
  async def secret(self, interaction: discord.Interaction):
    secret_role = interaction.guild.get_role(int(os.getenv("SECRET_ROLE")))
    await interaction.user.add_roles(secret_role)
    await interaction.response.send_message('...Secret Activated...', ephemeral=True)

async def setup(bot: commands.Bot):
  await bot.add_cog(game(bot))
