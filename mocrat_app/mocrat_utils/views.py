import json
import logging
import os
import requests

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

logger = logging.getLogger(__name__)

base_url = env("BASE_URL")
token = env('ADMIN_TOKEN')

class AsakatsuSchedule(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_utils AsakatsuSchedule")

        #Discord API 呼び出し
        mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")
        mocrat_asakatsu_webhook_url = env("MOCRAT_ASAKATSU_WEBHOOK")

        discord_post_url = env("DISCORD_POST_API")
        discord_payload = {
            "text": asakatsu_booking,
            "discord_webhook_url": mocrat_asakatsu_webhook_url
        }
        requests.post(base_url + discord_post_url, json=discord_payload, headers = {"Authorization": "JWT " + token})

        #Twitter API 呼び出し
        twitter_post_url = env("TWITTER_POST_API")
        twitter_payload = {
            "twitter_user": "chiba_moku2",
            "text": twitter_asakatsu_notice,
        }

        requests.post(base_url + twitter_post_url, json=twitter_payload, headers = {"Authorization": "JWT " + token})
        return Response(status=200)

class AsakatsuClosing(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_utils AsakatsuClosing")

        #Discord API 呼び出し
        mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")
        mocrat_asakatsu_webhook_url = env("MOCRAT_ASAKATSU_WEBHOOK")

        discord_post_url = env("DISCORD_POST_API")
        discord_payload = {
            "text": asakatsu_closing,
            "discord_webhook_url": mocrat_asakatsu_webhook_url
        }
        requests.post(base_url + discord_post_url, json=discord_payload, headers = {"Authorization": "JWT " + token})

        return Response(status=200)


# class HatebuItBot(APIView):
#     def get(self, request, format=None):
#         logger.info("Called mocrat_utils HatebuItBot")

#         #Discord API 呼び出し
#         mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")
#         mocrat_info_webhook_url = env("MOCRAT_INFO_WEBHOOK")

#         hatebu_top_itposts = hatebu_utils.return_tophatebu_itposts()

#         discord_post_url = env("DISCORD_POST_API")
#         discord_payload = {
#             "text": hatebu_top_itposts[0][0] + "\n" + hatebu_top_itposts[0][1],
#             "discord_webhook_url": mocrat_info_webhook_url
#         }
#         requests.post(base_url + discord_post_url, json=discord_payload,
#                       headers={"Authorization": "JWT " + token})

#         #Twitter API 呼び出し
#         twitter_post_url = env("TWITTER_POST_API")
#         twitter_payload = {
#             "twitter_user": "chiba_moku2",
#             "text": hatebu_top_itposts[0][0] + "\n" + hatebu_top_itposts[0][1],
#         }

#         requests.post(base_url + twitter_post_url, json=twitter_payload,
#                       headers={"Authorization": "JWT " + token})
#         return Response(status=200)
