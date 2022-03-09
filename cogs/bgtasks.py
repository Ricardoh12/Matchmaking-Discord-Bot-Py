import json
from discord.ext import commands, tasks
import datetime
import pytz


class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client
        self.afkcheker.start()

    @tasks.loop(seconds=10, reconnect=True)
    async def afkcheker(self):
        fuso = pytz.timezone('Etc/GMT+3')
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
        for Player in playerstats:
            if "lastmatch" in Player:
                if Player["lastmatch"] < str(datetime.datetime.now(fuso)):
                    Player["status"] = False
                    Player.pop("lastmatch")
            else:
                if Player["status"] is True:
                    if "count" not in Player:
                        Player["count"] = 0
                    else:
                        if Player["count"] >= 10000:
                            Player.pop("count")
                            Player["status"] = False
                        else:
                            Player["count"] += 10

        with open("database/playerstats.json", "w") as save:
            json.dump(playerstats, save, indent=4)








def setup(client:commands.Bot):
    client.add_cog(tier(client))