import discord

from config.common_logger import *
from config.environ_config import env

from hatena import hatebu_utils
from a3rt import talk_api


DISCORD_TOKEN = env("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    app_logger.info("mocrat is loggin")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    # TODO: ちゃんとキレイにする
    try:
        if message.mentions[0].display_name == "mocrat":

            if message.content.split(" ")[1] == "hatebu":
                items = hatebu_utils.return_tophatebu_itposts()
                for item in items:
                    await message.channel.send(item[0] + ": " + item[1])

            else:
                query = message.content.split(" ")[1]
                reply = talk_api.call_talk_api(query)
                await message.channel.send(reply)

    except:
        pass

client.run(DISCORD_TOKEN)