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
        app_logger.debug("Talk from {} : / Talk User : {} / Talk User Id : {} / Message : {}".format(message.channel.name, message.author.display_name, message.author.id, message.content.split(" ")[1]))
        
        if message.mentions[0].display_name == "mocrat":
            if message.channel.name == "朝活もくもく会":
                mocrat_actions = AsakatsuRoomAction(message)
                post_item_arr = mocrat_actions.return_post_items()

            elif  message.channel.name == "もくもく会":
                mocrat_actions = Moku2RoomAction(message)
                post_item_arr = mocrat_actions.return_moku2_post_items()

            elif message.channel.name == "振り返り部屋":
                mocrat_actions = FurikaeriRoomAction(message)
                post_item_arr = mocrat_actions.return_post_items()
            
            elif message.channel.name == "作業ログの部屋":
                mocrat_actions = LearningLogRoom(message)
                post_item_arr = mocrat_actions.return_generic_post_items()

            else:
                mocrat_actions = GenericRoomAction(message)
                post_item_arr = mocrat_actions.return_generic_post_items()

            for post in post_item_arr:
                await message.channel.send(post)

    except:
        pass

client.run(DISCORD_TOKEN)