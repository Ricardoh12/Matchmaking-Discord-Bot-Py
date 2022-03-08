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



    @commands.command(name="addwin",
                      usage="addwin",
                      description="adiciona uma vitória")
    async def addwin(self, ctx, user):

        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            userp = user.upper()
            for Player in playerstats:
                if (Player["playername"].upper()) == userp:
                    Player["Rankinfo"]["wins"] = Player["Rankinfo"]["wins"] + 1
                    with open("database/playerstats.json", "w") as save:
                        json.dump(playerstats, save, indent=4)
                    await ctx.send("vitória adicionada")



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
        print(", ".join(Players))
        await ctx.send(", ".join(Players))

    @commands.command(name="sttdef",
                      usage="sttdef",
                      description="definir o stts de todos como false")
    async def sttdef(self, ctx, ):
        with open("database/playerstats.json", "r") as data:
            playerstats = json.load(data)
            for Player in playerstats:
                if Player["status"] is True:
                    Player["status"] = False
        with open("database/playerstats.json", "w") as save:
            json.dump(playerstats, save, indent=4)

    @commands.command(name="profile",
                      usage="profile",
                      description="mostra o perdil do jogador")
    async def profile(self, ctx, user):

        userp = user.upper()
        with open("database/playerstats.json", "r") as data:

            playerstats = json.load(data)

            Wins = 0
            Pontos = 0

            for Player in playerstats:



                if (Player["playername"].upper()) == userp:



                    Wins = Wins + Player["Rankinfo"]["wins"]
                    Pontos = Pontos + Player["Rankinfo"]["elo"]

                    await ctx.send(content=f"Player: {userp}\n"
                                           f"Vitórias: {Wins}\n"
                                           f"Pontos: {Pontos}\n")








def setup(client:commands.Bot):
    client.add_cog(tier(client))

