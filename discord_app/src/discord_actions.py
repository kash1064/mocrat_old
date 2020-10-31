import discord
import requests

from config.common_logger import *
from config.environ_config import env

from hatena import hatebu_utils
from a3rt import talk_api


class GenericRoomAction(object):
    def __init__(self, message):
        app_logger.info("GenericRoomAction object has created")
        self.message = message
        self.message_first_query = self.message.content.split(" ")[1]
        self.post_items_arr = []

    def return_generic_post_items(self):
        if self.message_first_query == "登録":
            self.create_chibamoku_user()

        elif self.message_first_query == "hatebu":
            self.hatebu()
        
        else:
            self.talk_reply()

        return self.post_items_arr

    def create_chibamoku_user(self):
        app_logger.info("CALL : create_chibamoku_user()")
        base_url = env("MOCRAT_APP_URL")
        chibamoku_user_api = base_url + env("CHIBAMOKU_USER_API")

        chibamoku_user_data = {
            "discord_id" : self.message.author.id,
            "display_name" : self.message.author.display_name
        }

        response = requests.post(chibamoku_user_api, data=chibamoku_user_data)
        print(response)
        res = ["hello"]
        return res
    
    def talk_reply(self):
        app_logger.info("CALL : talk_reply()")
        query = self.message_first_query
        reply = talk_api.call_talk_api(query)

        self.post_items_arr.append(reply)
        return

    def hatebu(self):
        app_logger.info("CALL : hatebu()")
        items = hatebu_utils.return_tophatebu_itposts()

        self.post_items_arr = [item[0] + ":" + item[1] for item in items]
        return

class Moku2RoomAction(GenericRoomAction):
    def return_moku2_post_items(self):
        if self.message_first_query == "プロパティ":
            self.post_items_arr = ["ここはもくもく会の部屋です！\nもくもく会に参加すると手に入る経験値は 100 EXP です！"]
        
        else:
            self.return_generic_post_items()

        return self.post_items_arr

class Asakatsu2RoomAction(Moku2RoomAction):
    def return_post_items(self):
        if self.message_first_query == "プロパティ":
            self.post_items_arr = ["ここは朝活もくもく会の部屋です！\n朝活もくもく会に参加すると手に入る経験値は 50 EXP です！"]
        
        else:
            self.return_moku2_post_items()

        return self.post_items_arr

if __name__ == "__main__":
    pass