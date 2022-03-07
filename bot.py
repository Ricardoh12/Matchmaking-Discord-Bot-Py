
from discord.ext import commands
import os


TOKEN = "OTQzNTA1MDU4MTE1NTE4NTI0.Yg0Bjw.Ims8-eCv-vDvJJScTzUOq5RwN7k"

#---------------------------------------------------------------

client = commands.Bot(command_prefix = ">", case_insensitive=True)

for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        client.load_extension(f'cogs.{f[:-3]}')
        print(f'{f[:-3].title()} foi iniciado.')

#-------------------------------------------------------------#
@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))










client.run(TOKEN)
