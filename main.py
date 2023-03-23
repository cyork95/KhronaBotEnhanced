import discord
import os
import logging
import datetime
import random
import aiosqlite
from itertools import cycle
from discord.ext import commands, tasks
from utils.keep_alive import keep_alive
from easy_pil import Editor, Canvas, Font, load_image_async

logger = logging.FileHandler(filename='logs/discord.log',
                             encoding='utf-8',
                             mode='w')

TOKEN = os.getenv('DISCORD_TOKEN')

bot_status = cycle(["Helping CoYoFroYo", "Playing Warframe", "Checking Elon Musk's Satellites", "Calculating formulas", "Speaking to Ordis", "Fighting with Simaris", "Data Collecting with Suda", "Going to war with Cy"])

class PersistentViewBot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.all()
    super().__init__(command_prefix=commands.when_mentioned_or('.'),
                     intents=intents)
    self.cogslist = ["cogs.admin", "cogs.apis", "cogs.calculate", "cogs.fun", "cogs.game", "cogs.image", "cogs.info", "cogs.leveling", "cogs.spacex", "cogs.tpb", "cogs.warframe_farming", "cogs.warframe_worldstate"]

  async def setup_hook(self) -> None:
    for ext in self.cogslist:
      await self.load_extension(ext)

bot = PersistentViewBot()

@tasks.loop(seconds=45)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
  await bot.tree.sync()
  change_status.start()
  async with aiosqlite.connect('databases/level.db') as db:
    await db.execute("CREATE TABLE IF NOT EXISTS levels (level INTEGER, xp INTEGER, user INTEGER, guild INTEGER)")
    await db.commit()

@bot.event
async def on_member_join(member):
    join_role = member.guild.get_role(int(os.getenv("JOIN_ROLE")))
    intro_channel = member.guild.get_channel(int(os.getenv("INTRODUCTIONS_CHANNEL")))
    roles_channel = member.guild.get_channel(int(os.getenv("ROLES_CHANNEL")))
    welcome_channel = member.guild.get_channel(int(os.getenv("WELCOME_CHANNEL")))
    rule_channel = member.guild.get_channel(int(os.getenv("RULES_CHANNEL")))
    gamertag_channel = member.guild.get_channel(int(os.getenv("GAMERTAGS_CHANNEL")))
    ticket_channel = member.guild.get_channel(int(os.getenv("TICKET_SUPPORT_CHANNEL")))
    
    embed = discord.Embed(title="Welcome to The Orokin Sentinels Alliance Discord!",
                          description=f'Hello, {member.mention}! Since you are new around here I would like give you a nice rundown on some important information!',
                          color=discord.Color.gold(),
                          timestamp=datetime.datetime.now()
                          )
    embed.set_thumbnail(url=member.guild.icon)
    embed.add_field(name="Rules", value=f'Please read the rules in {rule_channel.mention}', inline=False)
    embed.add_field(name="Introductions", value=f'Please add an introduction, if you like, in the {intro_channel.mention}', inline=False)
    embed.add_field(name="Gamertag", value=f'Please add your gamertags to {gamertag_channel.mention}', inline=False)
    embed.add_field(name="Roles", value=f'Please choose a timezone in {roles_channel.mention} to make matchmaking a little easier! We have many other fun roles you are welcome to look over as well!', inline=False)
    embed.add_field(name="Support", value=f'Feel free to look around the server and let us know if we can help! You can use the channel {ticket_channel.mention} if you need help! Just create a ticket and add as many details as you want!', inline=False)
    await welcome_channel.send(embed=embed)
    await member.add_roles(join_role)

@bot.event
async def on_member_remove(member):
    # Replace CHANNEL_ID with the ID of the channel where you want to send the message
    channel = member.guild.get_channel(int(os.getenv("RECRUITMENT_CHANNEL")))
    leave_message = f"{member.name} has left the server. You will be missed...maybe"
    await channel.send(leave_message)

@bot.event
async def on_message(message):
  if message.author.bot:
    return
  author = message.author
  guild = message.guild
  
  async with aiosqlite.connect('databases/level.db') as db:
    async with db.execute("SELECT xp, level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id)) as cursor:
      result = await cursor.fetchone()

    if result is None:
      await db.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?, ?, ?, ?)",(0, 0, author.id, guild.id))
      await db.commit()
      rank_channel = guild.get_channel(int(os.getenv("RANK_CHANNEL")))
      await rank_channel.send(f"{author} was added to the ranking system!")
    else:
      xp = result[0]
      level = result[1]
      if level < 5:
        xp += random.randint(1,10)
        await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
        await db.commit()
      else:
        chance = random.randint(1,level//4)
        if chance < 3:
          xp += random.randint(1,10)
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
        elif chance < 5:
          xp += random.randint(1,8)
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
        elif chance < 7:
          xp += random.randint(1,6)
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
        elif chance < 9:
          xp += random.randint(1,4)
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
        elif chance < 11:
          xp += random.randint(1,2)
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
        else:
          xp += 1
          await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
          await db.commit()
      if xp >= 100:
        level += 1
        await db.execute("UPDATE levels SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id))
        await db.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id))
        await db.commit()
        rank_channel = guild.get_channel(int(os.getenv("RANK_CHANNEL")))
        await rank_channel.send(f"{author} just leveled up to level **{level}**! Congratulations!!")
    
keep_alive()

try:
  bot.run(TOKEN, log_handler=logger)
except discord.errors.HTTPException:
  print(
    "-----\n-----\n-----\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n-----\n-----\n------"
  )
  os.system('kill 1')
  os.system("python utils/restarter.py")
