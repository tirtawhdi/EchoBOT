import openai  # Import openai
import discord  # Import discord
import os  # Import os for environment variables
from dotenv import load_dotenv  # Import load_dotenv for loading environment variables from .env file
from openai import OpenAI

# load env from .env file
load_dotenv()

# API-TOKEN: 
OPENAI_API_KEY = os.getenv('OPENAI_API')  
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Initialize the OpenAI 
openai = OpenAI(api_key=OPENAI_API_KEY)

# Initialize Discord Bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ask'):
        user_input = message.content[5:]

        response = openai.chat.completions.create(
            model="davinci-002",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response['choices'][0]['message']['content']
        
        await message.channel.send(answer)

client.run(DISCORD_BOT_TOKEN)