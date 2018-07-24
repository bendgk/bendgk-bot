import discord
from discord.ext import commands
import random, os, requests, pprint, collections

class Server:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        #run server

description = "made by bendgk"
bot = commands.Bot(command_prefix='ben ', description=description)
server = Server()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('=' * len(str(bot.user.id)))

@bot.command()
async def server_status(ctx):
    r = requests.get("https://use.gameapis.net/mc/query/info/108.29.35.195").json()
    try:
        assert r["status"]
        data = {"online": r["status"],
                "players": str(r["players"]["online"])+ "/" + str(r["players"]["max"]),
                "motd": r["motds"]["clean"]}
    except AssertionError:
        data = {"online": r["status"]}

    await ctx.send("```python\n" + pprint.pformat(data, indent=0, width=20)[1:-1] + "\n```")

async def start_server(ctx):
    server.start()

bot.run(os.environ['BENDGK_BOT_TOKEN'])
