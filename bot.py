import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    try:
        # Send a POST request to update the website
        response = requests.post("https://your-vercel-backend.vercel.app/api/update", json={"command": "/ping"})
        if response.status_code == 200:
            await ctx.send("!pong")
        else:
            await ctx.send("Failed to update the website.")
    except Exception as e:
        await ctx.send("An error occurred.")
        print(e)

bot.run("YOUR_DISCORD_BOT_TOKEN")
