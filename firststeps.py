import discord
from discord.ext import commands
import logging

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf=8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)



# bot =command.Bot(".")
# @bot.listen()


client = discord.Client()

@client.event
async def on_ready():
    print("We logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$input"):
        await message.channel.send("hei buddy")






with open("botToken.txt") as f:
    myToken = f.read()
client.run(myToken)