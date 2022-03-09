
import random
import json
from discord.ext import commands
import datetime
import pytz


class Match(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client


    @commands.command(name = "match",
                    usage="<match>",
                    description = "Gerar partida com os players do json")
    async def match(self, ctx):
        reply = await ctx.send("Gerando time...")

        Tentativas = 0
        with open("database/playerstats.json", "r") as data:
            with open("database/globalstats.json", "r") as datag:


                playerstats = json.load(data)
                globalstats = json.load(datag)

                Players = []

                for Player in playerstats:
                    if Player["status"] is True:
                        Players.append(Player["playername"])

                if len(Players) >= 10:
                    while True:
                        Time1 = []
                        Time2 = []
                        count = 0
                        print("koe1")
                        while True:
                            Player = random.choice(Players)
                            if Player not in Time1:
                                Time1.append(Player)
                                count += 1
                            if count == 5:
                                count = 0
                                break
                        print("koe2")
                        while True:
                            Player = random.choice(Players)
                            if Player not in Time1:
                                if Player not in Time2:
                                    Time2.append(Player)
                                    count += 1
                            if count == 5:
                                count = 0
                                break
                        print("koe3")
                        #Pareamento_dos_times
                        Pontostime1 = 0
                        for Player in Time1:
                            for unit in playerstats:
                                if Player == unit["playername"]:
                                   Pontostime1 += unit["Rankinfo"]["elo"]
                        print("koe4")

                        Pontostime2 = 0
                        print("koe5")
                        for Player in Time2:
                            for unit in playerstats:
                                if Player == unit["playername"]:
                                    Pontostime2 += unit["Rankinfo"]["elo"]
                        print("koe6")

                        print(Time1)
                        print(Time2)
                        Match = Pontostime1 - Pontostime2
                        print(Match)
                        if Match <= 2:
                            if Match >= -2:
                                print(Match)
                                break
                        else:
                            print("koe7")
                            continue

                    await reply.edit(content=f"O time 1 é:{Time1} e o time 2 será:{Time2}. ")

                    fuso = pytz.timezone('Etc/GMT+3')
                    hora = (datetime.datetime.now(fuso) + datetime.timedelta(hours=2))

                    for PlayerTime in Time1:
                        for Player in playerstats:
                            if Player["playername"] == str(PlayerTime):
                                Player["lastmatch"] = str(hora)
                                Player["lasteam"] = Time1
                                try:
                                    Player.pop("count")
                                except KeyError:
                                    continue

                    for PlayerTime in Time2:
                        for Player in playerstats:
                            if Player["playername"] == str(PlayerTime):
                                Player["lastmatch"] = str(hora)
                                Player["lasteam"] = Time2
                                try:
                                    Player.pop("count")
                                except KeyError:
                                    continue
                    for Times in globalstats:
                        Times["time1"] = Time1
                        Times["time2"] = Time2
                        Times["mc"] = 5

                    with open("database/globalstats.json", "w") as save:
                        json.dump(globalstats, save, indent=4)

                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)




                    print(Pontostime1)
                    print(Pontostime2)
                    print(Match)
                    print(Time1)
                    print(Time2)
                    print(Tentativas)
                else:
                    await reply.edit(content=f"Não possuem jogadores suficientes")






def setup(client:commands.Bot):
    client.add_cog(Match(client))




