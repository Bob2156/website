import discord
import requests

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.application_command and interaction.data["name"] == "ping":
        # Send a request to update the website
        try:
            requests.post("https://your-vercel-backend.vercel.app/api/update", json={"command": "/ping"})
            await interaction.response.send_message("!pong")
        except Exception as e:
            await interaction.response.send_message("Failed to update the website.")
            print(e)

client.run("YOUR_DISCORD_BOT_TOKEN")
