import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    messages = await message.channel.history().flatten()
    for message in messages:
        print(message.content)

with open("botToken.txt") as file:
    myToken = file.read()
client.run(myToken)