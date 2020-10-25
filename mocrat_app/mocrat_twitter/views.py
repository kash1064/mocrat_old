import json
import logging
import os
import requests
import sys
import time

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from mocrat_config.admin_utils import error_notify
from mocrat_user.models import User
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp, SocialAccount

from .twitter_func import *

logger = logging.getLogger(__name__)

#TODO ユーザ認証が必要＆内部呼び出しのみ実行可能にしたい
def get_twitter_tokens(username):
    try:
        #TODO:Serializer使ったほうがいいのでは？
        user = User.objects.get(username=username)
        account = SocialAccount.objects.get(user=user)
        token_obj = SocialToken.objects.get(account=account)

        access_token = token_obj.token
        access_token_secret = token_obj.token_secret
        logger.info("access_token and access_token_secret is got")
        return access_token, access_token_secret

    except Exception as e:
        error_notify.error_notifier(sys.exc_info()[0], e.args)
        logger.error("Unexpected error {}".format(sys.exc_info()[0]))
        return Response(status=500)


# 多重継承をした際、initが衝突するので、メソッド名を指定
def get_tweepy_api(twitter_user):
    logger.info("Called mocrat_twitter TwitterAuth")
    access_token, access_token_secret = get_twitter_tokens(twitter_user)
    tweepy_api = get_auth_api(access_token, access_token_secret)
    return tweepy_api


# TODO:なぜかPOSTで送ってるのにGETは許可されてませんってはじかれる問題
class CreateFav(APIView):
    def post(self, request):
        logger.info("Called mocrat_twitter CreateFav")
        logger.debug(request.POST)

        twitter_user = request.data["twitter_user"]
        self.tweepy_api = get_tweepy_api(twitter_user)

        try:
            #TODO：タイムアウト問題
            #TODO：リプライにふぁぼしない
            for tweet_id in request.POST.getlist("tweet_ids"):
                #Heroku の仕様で30秒以上でワーカーがタイムアウトする
                try:
                    create_fav(self.tweepy_api, int(tweet_id))
                    time.sleep(1)

                except Exception as e:
                    #TODO: {'code': 139, 'message': 'You have already favorited this status.'} ならスキップする
                    logger.error("Unexpected error {}".format(sys.exc_info()[0]))

            return Response(status=200)

        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)

#Todo: 
class GetProfile(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_twitter GetProfile")

        twitter_user = request.GET.get(key="twitter_user", default="")
        self.tweepy_api = get_tweepy_api(twitter_user)

        try:
            profile = get_profile(self.tweepy_api)
            logger.debug("User profile: {}".format(profile))
            return Response(status=200)

        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)


#/timeline/home
class GetTimelineHome(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_twitter GetTimelineHome")

        twitter_user = request.GET.get(key="twitter_user", default="")
        self.tweepy_api = get_tweepy_api(twitter_user)

        since_id = request.GET.get(key="since_id", default="")
        max_id = request.GET.get(key="max_id", default="")
        count = request.GET.get(key="count", default="")
        page = request.GET.get(key="page", default="")

        try:
            timeline_posts = get_timeline_home(self.tweepy_api)
            return Response(status=200)

        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)


class SearchQueryTweets(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_twitter SearchQueryTweets")

        query = request.GET.get(key="query", default="")
        count = request.GET.get(key="count", default="20")

        twitter_user = request.GET.get(key="twitter_user", default="")
        self.tweepy_api = get_tweepy_api(twitter_user)

        try:
            searched_posts = search_query_strings(self.tweepy_api, query, int(count))
            search_results = []

            for s in searched_posts:
                search_result_dic = {"id":s.id, "text":s.text}
                search_results.append(search_result_dic)


            return Response(search_results, status=200)

        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)


class GetUserTweets(APIView):
    def get(self, request, format=None):
        logger.info("Called mocrat_twitter GetUserTweets")
        twitter_user = request.GET.get(key="twitter_user", default="")
        self.tweepy_api = get_tweepy_api(twitter_user)

        twitter_user = "yuki_kashiwaba"
        max_id = request.GET.get(key="max_id", default="")
        count = request.GET.get(key="count", default="")
        page = request.GET.get(key="page", default="")

        try:
            timeline_posts = get_user_tweets(self.tweepy_api, user_id)
            return Response(status=200)

        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)


class PostText(APIView):
    def post(self, request):
        logger.info("Called mocrat_twitter PostText")
        twitter_user = request.data["twitter_user"]
        text = request.data["text"]

        self.tweepy_api = get_tweepy_api(twitter_user)
        
        try:
            post_twitter(self.tweepy_api, text)
            return Response(status=200)
            
        except Exception as e:
            error_notify.error_notifier(sys.exc_info()[0], e.args)
            logger.error("Unexpected error {}".format(sys.exc_info()[0]))
            return Response(status=500)

