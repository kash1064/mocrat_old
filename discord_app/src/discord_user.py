import ast
import discord
import requests

from config.common_logger import *
from config.environ_config import env

class GenericDiscordUser(object):
    def __init__(self, message):
        app_logger.info("GenericDiscordUser object has creating")
        self.message = message

        self.base_url = env("MOCRAT_APP_URL")
        self.chibamoku_user_api = self.base_url + env("CHIBAMOKU_USER_API")

        self.discord_id =  self.message.author.id
        self.display_name = self.message.author.display_name
        app_logger.info("GenericDiscordUser object has created")


    def get_own_userdata(self):
        app_logger.info("CALL : get_own_userdata()")

        chibamoku_user_api_url = self.chibamoku_user_api + str(self.discord_id) + "/"

        app_logger.info("GET : {}".format(chibamoku_user_api_url))
        response = requests.get(chibamoku_user_api_url)

        if response.status_code == 200:
            status_data = ast.literal_eval(response.text)
            self.level = status_data["level"]
            self.total_exp = status_data["total_exp"]
            self.next_level_exp = self.level * 100 + (self.level - 1) * 100
        
        app_logger.debug("get_own_userdata response : {}".format(response.text))

        return response

    def create_new_discord_user(self):
        app_logger.info("CALL : create_new_discord_user()")
        app_logger.info("POST : {}".format(self.chibamoku_user_api))

        chibamoku_user_data = {
            "discord_id" : self.discord_id,
            "display_name" : self.display_name
        }

        response = requests.post(self.chibamoku_user_api, data=chibamoku_user_data)

        return response


    def update_own_userdata(self):
        app_logger.info("CALL : update_own_userdata()")

        chibamoku_user_api_url = self.chibamoku_user_api + str(self.discord_id) + "/"

        chibamoku_user_data = {
            "discord_id" : self.discord_id,
            "display_name" : self.display_name,
            "level" : self.level,
            "total_exp" : self.total_exp
        }

        app_logger.info("PUT : {}".format(chibamoku_user_api_url))
        app_logger.debug("update chibamoku_user_data is : {}".format(str(chibamoku_user_data)))

        response = requests.put(chibamoku_user_api_url, data=chibamoku_user_data)
        app_logger.debug("update_own_userdata response : {}".format(response.text))

        response = self.get_own_userdata()

        return response


    def is_level_up(self, get_exp):
        app_logger.debug("CALL : is_level_up() / get_exp {}".format(get_exp))

        self.get_own_userdata()
        self.total_exp += get_exp

        if self.total_exp >= self.next_level_exp:
            app_logger.info("level is up")
            self.level = round(self.total_exp / 150)

            is_level_up = True

        else:
            app_logger.debug("level is not up")
            is_level_up = False

        self.update_own_userdata()
        return is_level_up