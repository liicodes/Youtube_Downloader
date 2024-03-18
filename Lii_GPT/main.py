import discord
from discord.ext import commands
import requests

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Creates a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to fetch a random quote from ZenQuotes.io
def get_quote():
    quote_response = requests.get('https://zenquotes.io/api/random')
    data = quote_response.json()
    quote = data[0]['q'] + " -" + data[0]['a']  # Extracting the quote and author
    return quote

# Function to fetch a joke from JokeAPI
def get_joke():
    joke_response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=religious,political,racist,sexist,explicit")
    data = joke_response.json()
    joke = data["setup"] + " -" + data["delivery"]
    return joke

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your not so friendly Discord bot.")

# Command: !quote
@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

# Command: !joke
@bot.command()
async def joke(ctx):
    joke = get_joke()
    await ctx.send(joke)

# Run the bot
if __name__ == '__main__':
    bot.run("Enter Your BOT API KEY")
