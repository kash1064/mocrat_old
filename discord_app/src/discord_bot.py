import discord

from config.common_logger import *
from config.environ_config import env

from discord_actions import *
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
        app_logger.debug("Talk from {} : / Talk User : {} / Talk User Id : {}".format(message.channel.name, message.author.display_name, message.author.id))
        
        if message.mentions[0].display_name == "mocrat":
            if message.channel.name == "朝活もくもく会" or message.channel.name == "もくもく会":
                pass

            elif message.channel.name == "振り返り部屋":
                pass
            
            elif message.channel.name == "資格勉強の部屋":
                pass

            else:
                mocrat_actions = GenericRoomAction(message)
                post_item_arr = mocrat_actions.return_post_items()

            for post in post_item_arr:
                await message.channel.send(post)

    except:
        pass

client.run(DISCORD_TOKEN)