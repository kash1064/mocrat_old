import logging
import requests

from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

logger = logging.getLogger(__name__)

base_url = env("BASE_URL")
token = env('ADMIN_TOKEN')

class UserRequests(object):
    pass


class MainRequests(object):
    pass


class TwitterRequests(object):
    def __init__(self, twitter_user):
        self.twitter_user = twitter_user

        print("Called mocrat_requests_classes TwitterRequests")
        print("Twitter user is : " + self.twitter_user)

    #get info
    def get_tweet(self, query, count):
        twitter_search_query_url = env("TWITTER_SERCH_QUERY_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "query": query,
            "count": count
        }
        search_results = requests.get(base_url + twitter_search_query_url,
                                      params=twitter_payload, headers={"Authorization": "JWT " + token})
        search_results = search_results.json()
        return search_results


    #actions
    def twitter_post(self, text):
        '''
        curl - X POST - H "Content-Type: application/json" - d '{ "text":"投稿" }' chiba-moku2.herokuapp.com/mocrat_twitter/api/v1/post_text/ -H "Authorization: JWT <TOKEN>"
        '''
        logger.info("Called mocrat_requests_classes TwitterRequests.twitter_post")
        twitter_post_url = env("TWITTER_POST_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "text": text,
        }
        results = requests.post(base_url + twitter_post_url, data=twitter_payload, headers = {"Authorization": "JWT " + token})
        return results
    

    def twiter_fav(self, tweet_ids):
        logger.info("Called mocrat_requests_classes TwitterRequests.twitter_post")
        twitter_create_fav_url = env("TWITTER_CREATE_FAV_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "tweet_ids": tweet_ids,
        }
        results = requests.post(base_url + twitter_create_fav_url, data=twitter_payload, headers = {"Authorization": "JWT " + token})
        return results
        


class DiscordRequests(object):
    def __init__(self):
        mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")
        mocrat_asakatsu_webhook_url = env("MOCRAT_ASAKATSU_WEBHOOK")
        discord_post_url = env("DISCORD_POST_API")


class TodoistRequests(object):
    pass


class GoogleRequests(object):
    pass


class RssRequests(object):
    pass



if __name__ == "__main__":
    pass
