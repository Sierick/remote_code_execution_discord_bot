import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("rce.py Logged in as: " + client.user.name + "\n")

@client.event
async def on_message(message):
    valid_users = ["Nate#5359", "Nate's Bot#5352"]
    if message.author.bot:
        return
    if str(message.author) in valid_users:
        file = open("pythonoutput.txt", "w")
        file.write(str(message.content))
        file.close()
        time.sleep(0.2)
        file = open("bashoutput.txt", "r")
        content = file.read()
        file.close()
        if(len(str(content)) == 0):
            await message.channel.send("The command ran and had no output")
            return
        if(len(str(content)) > 2000):
            await message.channel.send("The command ran and had an output over 2000 characters")
            return
        await message.channel.send(content)
        return
    else:
        return

client.run("client_idNzQ5Mjk1MDM1MzI5MTUxMDA3.X0p5YQ.TsM15I92sJ44-t1QeeG-HKp2jQ")
