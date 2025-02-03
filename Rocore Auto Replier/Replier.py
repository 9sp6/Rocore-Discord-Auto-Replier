import discord
import asyncio
import time
from rich.console import Console
from rich.prompt import Prompt

# Create an instance of Console for enhanced visuals
console = Console()

# Function to display a fancy welcome banner using Rich
def print_welcome_banner():
    console.rule("[bold blue]Welcome to Spooky's Auto-Reply Bot[/bold blue]", style="bright_yellow")
    console.print("[bold magenta]The Ultimate Discord Auto-Reply Tool[/bold magenta]", justify="center")
    console.rule(style="bright_yellow")

# Prompt the user to input the Discord token
TOKEN = Prompt.ask("\n> Enter your Discord User Token")

# Initialize the client with the user token and without bot mode (user account)
client = discord.Client()

# Your custom auto-reply message
AUTO_REPLY_MESSAGE = "Wsp bro, its me spooky, if you're seeing this, this is my auto-replier I made. Please be patient and wait for me to reply, thank you!"

# Function to handle incoming messages
@client.event
async def on_ready():
    print_welcome_banner()
    print(f"Logged in as {client.user.name} ({client.user.id})")
    console.print("[green]Bot is now online! Listening for mentions...[/green]", style="bold")

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message mentions the bot (user) by its ID
    if f"<@{client.user.id}>" in message.content:
        # Send the auto-reply to the same channel where the message came from
        await message.channel.send(AUTO_REPLY_MESSAGE)
        console.print(f"[blue]Auto-replied to message in: {message.guild.name} - {message.channel.name}[/blue]")

# Run the bot using the user token (not bot mode)
try:
    client.run(TOKEN, bot=False)
except Exception as e:
    print(f"[red]Error: {e}[/red]")
    console.print("[bold red]Failed to login! Please check your token and try again.[/bold red]")
