import discord

from config.common_logger import *
from config.environ_config import env

from hatena import hatebu_utils
from a3rt import talk_api


class GenericRoomAction(object):
    def __init__(self, message):
        app_logger.info("GenericRoomAction object has created")
        self.message = message
        self.post_items_arr = []

    def return_post_items(self):
        if self.message.content.split(" ")[1] == "hatebu":
            self.hatebu()
        
        else:
            self.talk_reply()

        return self.post_items_arr
    
    def talk_reply(self):
        query = self.message.content.split(" ")[1]
        reply = talk_api.call_talk_api(query)

        self.post_items_arr.append(reply)
        return

    def hatebu(self):
        items = hatebu_utils.return_tophatebu_itposts()

        self.post_items_arr = [item[0] + ":" + item[1] for item in items]
        return



if __name__ == "__main__":
    pass