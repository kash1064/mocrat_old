import ast
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

        elif self.message_first_query == "ステータス":
            self.check_status()

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

        try:
            app_logger.info("POST : {}".format(chibamoku_user_api))
            response = requests.post(chibamoku_user_api, data=chibamoku_user_data)

            if response.status_code == 201:
                self.post_items_arr = ["ちばもく会へようこそ！\n新規ユーザー登録が完了しました！"]

            else:
                """
                > response.text
                '{"discord_id":["この discord id を持った chiba moku user が既に存在します。"]}'
                """
                self.post_items_arr = ast.literal_eval(response.text)["discord_id"]
        
        except Exception as e:
            #TODO: discord 側にも、エラーをDiscord通知する機能を実装する
            # error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}\n {}".format(sys.exc_info()[0], e.args))

        return

    def check_status(self):
        app_logger.info("CALL : check_status()")
        base_url = env("MOCRAT_APP_URL")
        user_id = self.message.author.id
        chibamoku_user_api = base_url + env("CHIBAMOKU_USER_API") + str(user_id) + "/"

        try:
            app_logger.info("GET : {}".format(chibamoku_user_api))
            response = requests.get(chibamoku_user_api)

            if response.status_code == 200:
                status_data = ast.literal_eval(response.text)
                user_name = status_data["display_name"]
                level = status_data["level"]
                total_exp = status_data["total_exp"]

                self.post_items_arr = [
                    self.message.author.mention + " さんのステータスを表示します。" + "\n" \
                    + "現在のレベル ： " + str(level) + "\n" \
                    + "総獲得経験値 : " + str(total_exp) + "\n" \
                    + "この調子で頑張りましょう！"
                ]

            else:
                self.post_items_arr = [ast.literal_eval(response.text)["detail"]]

        except Exception as e:
            # error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}\n {}".format(sys.exc_info()[0], e.args))

        return
    
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