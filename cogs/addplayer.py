import json
from discord.ext import commands
class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client




    @commands.command(name="addplayer",
                      usage="addplayer",
                      description="adicionar player ao json")
    async def addplayer(self, ctx, Player, elo):

        with open("database/playerstats.json", "r") as data:
            with open("database/elos.json", "r") as datae:

                playerstats = json.load(data)

                Playerpoints = 0
                elop = elo.upper()
                if elop == "FERRO":
                    Playerpoints = 100
                if elop == "BRONZE":
                    Playerpoints = 200
                if elop == "PRATA":
                    Playerpoints = 300
                if elop == "OURO":
                    Playerpoints = 400
                if elop == "PLATINA":
                    Playerpoints = 600
                if elop == "DIAMANTE":
                    Playerpoints = 700
                if elop == "IMORTAL":
                    Playerpoints = 850
                if elop == "RADIANTE":
                    Playerpoints = 1000

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
                                "loses": 0,
                                "elo": Playerpoints,
                                        },
                            "history": {
                                "Astra": 0,
                                "Breach": 0,
                                "Brimstone": 0,
                                "Chamber": 0,
                                "Cypher": 0,
                                "Jett": 0,
                                "kay/0": 0,
                                "Killjoy": 0,
                                "Neon": 0,
                                "omen": 0,
                                "Phoenix": 0,
                                "Raze": 0,
                                "Reyna": 1,
                                "Sage": 0,
                                "Skye": 0,
                                "Sova:": 0,
                                "Viper": 0,
                                "Yoru": 0
                            }
                        }

                        playerstats.append(stats)
                        with open("database/playerstats.json", "w") as save:
                            json.dump(playerstats, save, indent=4)



def setup(client:commands.Bot):
    client.add_cog(tier(client))