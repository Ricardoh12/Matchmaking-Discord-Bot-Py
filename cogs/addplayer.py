import json
from discord.ext import commands
class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client




    @commands.command(name="addplayer",
                      usage="addplayer",
                      description="adicionar player ao json")
    async def addplayer(self, ctx, Player):

        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)

            if Player not in playerstats:
                if any(Player == unit["playername"] for unit in playerstats):
                    for unit in playerstats:
                        if Player == unit["playername"]:
                            if unit["status"]:
                                continue
                            else:
                                pass
                else:
                    stats = {
                        "playername": Player,
                        "status": False,
                        "Rankinfo": {
                            "wins": 0,
                            "elo": 1
                        }
                    }
                    playerstats.append(stats)
                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)



def setup(client:commands.Bot):
    client.add_cog(tier(client))