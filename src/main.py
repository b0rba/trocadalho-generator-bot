import discord
import os

from dotenv import load_dotenv

from service.trocadalho_generator import TrocadalhoGeneratorService

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_keyword):
        question: str = message.content.strip(bot_keyword).strip()
        answer = trocadalho_generator_service.get_answer(question)
        if answer is None:
            await message.channel.send('Bot Offline, sry')

        await message.channel.send(answer)


trocadalho_generator_service = TrocadalhoGeneratorService(os.environ['GENERATOR_API_PATH'])
bot_keyword = os.environ['BOT_KEYWORD']

client.run(os.environ['DISCORD_TOKEN'])
