import discord
import asyncio
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(1088152096550948905)  # replace with your channel ID
        await channel.send("Hello you need to update your backloge <@&1090682271494852609> :skull:")  # replace with your reminder message
        await asyncio.sleep(86400)  # 24 hours in seconds


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(my_background_task())


@client.event
async def on_message(message):
    if message.content.startswith('!setreminder'):
        # parse the reminder message from the user's command
        reminder_message = message.content[len('!setreminder'):].strip()
        # store the reminder message somewhere (e.g. a database)
        await message.channel.send(f"Reminder set: {reminder_message}")


Token = os.environ.get("KEY")
keep_alive()
client.run(Token)
