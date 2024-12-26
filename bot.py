import discord
import requests
import os

# Load the Discord bot token from environment variables
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# URL to the JSON file hosted on Vercel
API_URL = "https://your-vercel-domain.vercel.app/data/message.json"

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.content == "/ping":
        try:
            # Send a PUT request to update the JSON file
            response = requests.put(API_URL, json={"message": "!pong"})
            if response.status_code == 200:
                await message.channel.send("!pong")
            else:
                await message.channel.send("Failed to update the website.")
        except Exception as e:
            print(e)
            await message.channel.send("An error occurred.")

bot.run(TOKEN)
