import json
import random
from discord.ext import commands

class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client


    @commands.command(name = "tier",
                    usage="<tier>",
                    description = "")
    async def tier(self, ctx, elo):


        Players = []
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            for Player in playerstats:
                if Player["Rankinfo"]["elo"] == int(elo):
                    Players.append(Player["playername"])
                    print(", ".join(Players))
                    await ctx.send(", ".join(Players))




    @commands.command(name="status",
                      usage="status",
                      description="definir status do player")
    async def status(self, ctx, user):
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)

            for Player in playerstats:
                userp = user.upper()
                if (Player["playername"].upper()) == userp:
                    if Player["status"]:
                        Player["status"] = False
                        await ctx.reply("Offline e broxa", delete_after=10)
                    else:
                        Player["status"] = True
                        await ctx.reply("Online e metendo", delete_after = 10)

            with open("database/playerstats.json", "w") as save:
                json.dump(playerstats, save, indent=4)


    @commands.command(name="poi",
                      usage="poi",
                      description="Par ou impar")
    async def poi(self, ctx):
        x = random.randint(1,10)
        await ctx.send(x)


    @commands.command(name="online",
                      usage="online",
                      description="mostrar quem tá on")
    async def online(self, ctx,):
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            Players = []

            for Player in playerstats:
                if Player["status"] is True:
                    Players.append(Player["playername"])

            await ctx.send(content=f"Jogadores online:{Players} são {len(Players)} online ")

    @commands.command(name="addwin1",
                      usage="addwin1",
                      description="adiciona uma vitória ao time")

    async def addwin1(self, ctx):
        reply = await ctx.send("Carregando...")
        with open("database/playerstats.json", "r") as data:
            with open("database/globalstats.json", "r") as datag:
                playerstats = json.load(data)
                globalstats = json.load(datag)
                for time in globalstats:
                    for Player in playerstats:

                        if time["mc"] > 0:
                            if Player["playername"] in (time["time1"]):
                                    print("ok")
                                    Player["Rankinfo"]["wins"] = Player["Rankinfo"]["wins"] + 1
                                    Player["Rankinfo"]["elo"] = Player["Rankinfo"]["elo"] + 0
                                    time["mc"] = time["mc"] - 1
                                    await reply.edit(content=f"Partida computada")






                    with open("database/globalstats.json", "w") as save:
                        json.dump(globalstats, save, indent=4)

                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)

    @commands.command(name="addwin2",
                      usage="addwin2",
                      description="adiciona uma vitória ao time")
    async def addwin2(self, ctx):
        reply = await ctx.send("Carregando...")
        with open("database/playerstats.json", "r") as data:
            with open("database/globalstats.json", "r") as datag:
                playerstats = json.load(data)
                globalstats = json.load(datag)
                for time in globalstats:
                    for Player in playerstats:

                        if time["mc"] > 0:
                            if Player["playername"] in (time["time2"]):
                                print("ok")
                                Player["Rankinfo"]["wins"] = Player["Rankinfo"]["wins"] + 1
                                Player["Rankinfo"]["elo"] = Player["Rankinfo"]["elo"] + 0
                                time["mc"] = time["mc"] - 1
                                await reply.edit(content=f"Partida computada")

                    with open("database/globalstats.json", "w") as save:
                        json.dump(globalstats, save, indent=4)

                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)

'''''    @commands.command(name="rank",
                      usage="rank",
                      description="mostrar o top 10 players")
    async def rank(self, ctx):
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)

            for Player in playerstats:

                r1 = sorted(Player["Rankinfo"]["wins"], reverse=True)

                for item in Player['Rankinfo']["wins"].items():
                    if item[1] == r1[0]:
                        top1 = item[0]
                    if item[1] == r1[1]:
                        top2 = item
                    if item[1] == r1[2]:
                        top3 = item

                Wins = Wins + Player["Rankinfo"]["wins"]
                Pontos = Pontos + Player["Rankinfo"]["elo"]

                print("top1")

    @commands.command(name="addhistory",
                      usage="addhistory",
                      description="adiciona uma vitória ao time")
    async def addhistory(self, ctx, user, boneco):
        userp = user.upper()
        bonecop = boneco.upper()
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            for Player in playerstats:
                if (Player["playername"].upper()) == userp:
                    if bonecop in (Player["history"].upper()):
                        Player["history"] = Player["history"][bonecop] + '''''















def setup(client:commands.Bot):
    client.add_cog(tier(client))

