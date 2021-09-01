import discord
import json

client = discord.Client()

@client.event
async def on_ready():
    print("We logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.channel.name == "trening":
        results = []
        messages = await message.channel.history().flatten()
        for message in messages:
            items = message.content.split()
            target = items[0].split("x")
            result = {
                "sets": int(target[0]),
                "reps": int(target[1]),
                "weight": float(items[1].replace("kg", "")),
                "achieved": int(items[2].replace("reps", "")),
                "date": str(message.created_at)
            }
            results.append(result)
        data = json.dumps(results)
        with open("results.json", "w") as file:
            file.write(data)

with open("token.txt") as file:
    token = file.read()

client.run(token)