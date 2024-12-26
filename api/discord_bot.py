import discord
import requests
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
API_URL = "https://your-vercel-deployment.vercel.app/api/update"

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.content == "/ping":
        # Send POST request to update the website
        response = requests.post(API_URL, json={"command": "/ping"})
        if response.status_code == 200:
            await message.channel.send("!pong")
        else:
            await message.channel.send("Failed to update the website.")

bot.run(TOKEN)
