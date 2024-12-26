import discord
import requests
import os

# Load environment variables
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
GUILD_ID = os.environ.get("GUILD_ID")  # Your Discord server (guild) ID

# URL to update the JSON file hosted on Vercel
API_URL = "https://your-vercel-domain.vercel.app/data/message.json"

# Initialize the bot and command tree
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@tree.command(name="ping", description="Responds with Pong!")
async def ping(interaction: discord.Interaction):
    """Handles the /ping command."""
    try:
        # Update the JSON file on Vercel
        response = requests.put(API_URL, json={"message": "!pong"})
        if response.status_code == 200:
            await interaction.response.send_message("!pong")
        else:
            await interaction.response.send_message("Failed to update the website.")
    except Exception as e:
        print(f"Error: {e}")
        await interaction.response.send_message("An error occurred.")

@bot.event
async def on_ready():
    """Sync slash commands to the guild."""
    try:
        guild = discord.Object(id=int(GUILD_ID))  # Specify the target guild
        synced = await tree.sync(guild=guild)  # Sync commands for a specific guild
        print(f"Slash commands synced to guild {GUILD_ID}: {synced}")
        print(f"Bot logged in as {bot.user}")
    except Exception as e:
        print(f"Error during sync: {e}")

bot.run(TOKEN)
