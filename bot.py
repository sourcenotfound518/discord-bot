import os
import discord
from discord.ext import commands
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ask(ctx, *, question):
    """Ask ChatGPT something"""
    await ctx.channel.typing()
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a helpful assistant on Discord."},
            {"role": "user", "content": question}
        ]
    )
    await ctx.reply(response.choices[0].message.content[:2000])

bot.run(os.getenv("DISCORD_TOKEN"))
