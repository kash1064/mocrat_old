import ast
import discord
import re
import requests

from discord_user import *

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
        self.get_exp = 0

        self.discord_user = GenericDiscordUser(self.message)

        self.set_generic_option_regex()
    
    def set_generic_option_regex(self):
        self.user_register_regex = r"^登録"
        self.user_status_regex = r"^ステータス|^\\s"

        self.room_property_regex = r"^プロパティ|^\\p"
        
        self.commands_list_regex = r"^コマンドリスト|^\\c"

        self.hatebu_top5_regex = r"^はてぶ|^\\ht"

        self.commands_list = {
            "ユーザ登録" : "登録",
            "ステータスチェック" : "ステータス (\\s)",
            "コマンドリストを表示" : "コマンドリスト (\\c)",
            "ルームの情報を表示" : "プロパティ (\\p)",
            "はてぶ上位記事を取得" : "はてぶ (\\ht)",
        }

    def return_generic_post_items(self):
        if re.match(self.user_register_regex, self.message_first_query):
            self.create_chibamoku_user()

        elif re.match(self.user_status_regex, self.message_first_query):
            self.check_status()

        elif re.match(self.commands_list_regex, self.message_first_query):
            self.show_commands()

        elif re.match(self.hatebu_top5_regex, self.message_first_query):
            self.hatebu()
        
        else:
            self.talk_reply()

        return self.post_items_arr

    # actions
    def check_status(self):
        app_logger.info("CALL : check_status()")

        response = self.discord_user.get_own_userdata()

        if response.status_code == 200:
            self.post_items_arr = [
                self.message.author.mention + " さんのステータスを表示します。" + "\n" \
                + "現在のレベル ： " + str(self.discord_user.level) + "\n" \
                + "総獲得経験値 : " + str(self.discord_user.total_exp) + "\n" \
                + "次のレベルまで : " + str(self.discord_user.next_level_exp - self.discord_user.total_exp) + "\n" \
                + "この調子で頑張りましょう！"
            ]

        else:
            self.post_items_arr = [ast.literal_eval(response.text)["detail"]]

        # except Exception as e:
        #     # error_notify.error_notifier(sys.exc_info()[0], e.args)
        #     logger.error("Unexpected error {}\n {}".format(sys.exc_info()[0], e.args))

        return


    def create_chibamoku_user(self):
        app_logger.info("CALL : create_chibamoku_user()")

        response = self.discord_user.create_new_discord_user()

        if response.status_code == 201:
            self.post_items_arr = ["ちばもく会へようこそ！\n新規ユーザー登録が完了しました！"]

        else:
            """
            > response.text
            '{"discord_id":["この discord id を持った chiba moku user が既に存在します。"]}'
            """
            self.post_items_arr = ast.literal_eval(response.text)["discord_id"]
    
        # except Exception as e:
        #     #TODO: discord 側にも、エラーをDiscord通知する機能を実装する
        #     # error_notify.error_notifier(sys.exc_info()[0], e.args)
        #     logger.error("Unexpected error {}\n {}".format(sys.exc_info()[0], e.args))

        return


    def hatebu(self):
        app_logger.info("CALL : hatebu()")
        items = hatebu_utils.return_tophatebu_itposts()

        self.post_items_arr = [item[0] + ":" + item[1] for item in items]
        return

    
    def show_commands(self):
        reply = "このルームで使えるコマンド一覧を表示します\n※ ()の中はショートカットコマンド\n\n"
        for command in self.commands_list:
            reply += command + " :  "
            reply += self.commands_list[command] + "\n"

        self.post_items_arr.append(reply)
        return


    def talk_reply(self):
        app_logger.info("CALL : talk_reply()")
        query = self.message_first_query
        reply = talk_api.call_talk_api(query)

        self.post_items_arr.append(reply)
        return


    def update_userdata(self):
        app_logger.info("CALL : update_userdata()")
    
        # レベルアップ判定
        if self.discord_user.is_level_up(self.get_exp):
            self.post_items_arr = [
                self.message.author.mention + " さんがレベルアップしました！" + "\n" \
                + "現在のレベル ： " + str(self.discord_user.level) + "\n" \
                + "総獲得経験値 : " + str(self.discord_user.total_exp) + "\n" \
                + "次のレベルまで : " + str(self.discord_user.next_level_exp - self.discord_user.total_exp) + "\n" \
                + "この調子で頑張りましょう！"
            ]

        else:
            self.check_status()
       
        return


    def __del__(self):
        app_logger.info("CALL : Destructor")
        pass
        

class Moku2RoomAction(GenericRoomAction):
    def return_moku2_post_items(self):
        if self.message_first_query == "プロパティ":
            self.post_items_arr = ["ここはもくもく会の部屋です！\nもくもく会に参加すると手に入る経験値は 100 EXP です！"]
        
        # elif self.message_first_query == "成果報告":

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

class FurikaeriRoomAction(GenericRoomAction):
    def __init__(self, message):
        super().__init__(message)

        self.add_furikaeri_option_regex()

    def add_furikaeri_option_regex(self):
        self.furikaeri_regex = r"^振り返り|^\\f"

        self.commands_list["振り返りを宣言"] = "振り返り (\\f)"

        return

    def return_post_items(self):
        if re.match(self.room_property_regex, self.message_first_query):
            self.post_items_arr = ["ここは振り返りの部屋です！\n振り返りをすると手に入る経験値は 100 EXP です！"]
        
        elif re.match(self.furikaeri_regex, self.message_first_query):
            self.get_exp = 100
            self.update_userdata()

        else:
            self.return_generic_post_items()

        return self.post_items_arr


if __name__ == "__main__":
    pass