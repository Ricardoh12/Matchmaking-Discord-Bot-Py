
from discord.ext import commands
import os
from tokencode import tokencode


TOKEN = tokencode

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
