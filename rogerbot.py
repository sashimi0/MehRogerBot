import discord
import random

intents = discord.Intents.default()
intents.message_content = True  # Important: enables reading messages
bot = discord.Client(intents=intents)

roger_lines = [
    "Grok is better than ChatGPT. Blah blah blah. Elon booty mmm <3",
    "Listen to Roger Radio. I command you.",
    ":penis:",
    "CultCouture.co eventually"
]

@bot.event
async def on_ready():
    print(f'RogerBot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == '/roger':
        response = random.choice(roger_lines)
        await message.channel.send(response)

bot.run("YOUR_BOT_TOKEN_HERE")
