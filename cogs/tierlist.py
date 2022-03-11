import json
import random
from discord.ext import commands

class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

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


            await ctx.send(content=f"Jogadores online:{Players}\n"
                                   f"{len(Players)} online ")

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
                                    Player["Rankinfo"]["elo"] = Player["Rankinfo"]["elo"] + 15
                                    time["mc"] = time["mc"] - 1
                            if Player["playername"] in (time["time2"]):
                                    print("ok2")
                                    Player["Rankinfo"]["loses"] = Player["Rankinfo"]["loses"] + 1
                                    Player["Rankinfo"]["elo"] = Player["Rankinfo"]["elo"] - 10
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
                            if Player["playername"] in (time["time1"]):
                                    print("ok2")
                                    Player["Rankinfo"]["loses"] = Player["Rankinfo"]["loses"] + 1
                                    Player["Rankinfo"]["elo"] = Player["Rankinfo"]["elo"] - 10
                                    time["mc"] = time["mc"] - 1
                                    await reply.edit(content=f"Partida computada")

                    with open("database/globalstats.json", "w") as save:
                        json.dump(globalstats, save, indent=4)

                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)

    @commands.command(name="addhist",
                      usage="addhist",
                      description="Adicionar agente ao histórico")
    async def profile(self, ctx, user, agente):
        userp = user.upper()
        agentep = agente.upper()
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            for Player in playerstats:
                if (Player["playername"].upper()) == userp:
                    if agentep == "ASTRA":
                        Player["history"]["Astra"] = Player["history"]["Astra"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "BREACH":
                        Player["history"]["Breach"] = Player["history"]["Breach"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "BRIMSTONE":
                        Player["history"]["Brimstone"] = Player["history"]["Brimstone"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "CHAMBER":
                        Player["history"]["Chamber"] = Player["history"]["Chamber"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "CYPHER":
                        Player["history"]["Cypher"] = Player["history"]["Chyper"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "JETT":
                        Player["history"]["Jett"] = Player["history"]["Jett"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "KAY0":
                        Player["history"]["Kay/0"] = Player["history"]["Kay/0"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "KILLJOY":
                        Player["history"]["Killjoy"] = Player["history"]["Killjoy"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "NEON":
                        Player["history"]["Neon"] = Player["history"]["Neon"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "OMEN":
                        Player["history"]["Omen"] = Player["history"]["Omen"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "PHOENIX":
                        Player["history"]["Phoenix"] = Player["history"]["Phoenix"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "RAZE":
                        Player["history"]["Raze"] = Player["history"]["Raze"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "REYNA":
                        Player["history"]["Reyna"] = Player["history"]["Reyna"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "SAGE":
                        Player["history"]["Sage"] = Player["history"]["Sage"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "SKYE":
                        Player["history"]["Skye"] = Player["history"]["Skye"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "SOVA":
                        Player["history"]["Sova"] = Player["history"]["Sova"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "VIPER":
                        Player["history"]["Viper"] = Player["history"]["Viper"] + 1
                        await ctx.send("Agente adicionado")
                    if agentep == "YORU":
                        Player["history"]["Yoru"] = Player["history"]["Yoru"] + 1
                        await ctx.send("Agente adicionado")
                    else:
                        await ctx.send("Agente inválido")

                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)














def setup(client:commands.Bot):
    client.add_cog(tier(client))

