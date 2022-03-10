import json
from discord.ext import commands


class tier(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command(name="profile",
                      usage="profile",
                      description="definir o stts de todos como false")

    async def profile(self, ctx, user):
        userp = user.upper()
        with open("database/playerstats.json", "r") as data:

            playerstats = json.load(data)

            Wins = 0
            Pontos = 0
            Loses = 0

            for Player in playerstats:



                if (Player["playername"].upper()) == userp:



                    r1 = sorted(Player['history'].values(), reverse=True)

                    for item in Player['history'].items():
                        if r1[0] == 0:
                            top1 = "Sem agentes adicionados"
                        else:
                            if item[1] == r1[0]:
                                top1 = item[0]
                            if item[1] == r1[1]:
                                top2 = item
                            if item[1] == r1[2]:
                                top3 = item

                    Wins = Wins + Player["Rankinfo"]["wins"]
                    Pontos = Pontos + Player["Rankinfo"]["elo"]
                    Loses = Loses + Player["Rankinfo"]["loses"]
                    Jogost = Wins + Loses
                    if Jogost == 0:
                        Winrate = "Sem jogos suficientes"
                        Winratep = "Sem jogos suficientes"
                    else:
                        Winrate = Wins/Jogost
                        Winratep = Winrate*100

                    await ctx.send(content=f"Player: {userp}\n"
                                           f"Vitórias: {Wins}\n"
                                           f"Derrotas: {Loses}\n"
                                           f"Jogos totais: {Jogost}\n"
                                           f"Pontos: {Pontos}\n"
                                           f"Winrate: {Winratep}\n"
                                           f"Mais jogado: {top1}")









def setup(client:commands.Bot):
    client.add_cog(tier(client))

