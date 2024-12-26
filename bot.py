import discord
import requests
import os

# Load the Discord bot token from environment variables
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# URL to update the JSON file hosted on Vercel
API_URL = "https://your-vercel-domain.vercel.app/data/message.json"

# Initialize the bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@tree.command(name="ping", description="Responds with Pong!")
async def ping(interaction: discord.Interaction):
    try:
        # Send a PUT request to update the JSON file
        response = requests.put(API_URL, json={"message": "!pong"})
        if response.status_code == 200:
            await interaction.response.send_message("!pong")
        else:
            await interaction.response.send_message("Failed to update the website.")
    except Exception as e:
        print(e)
        await interaction.response.send_message("An error occurred.")

@bot.event
async def on_ready():
    await tree.sync()  # Sync slash commands
    print(f"Bot logged in as {bot.user}")

bot.run(TOKEN)
